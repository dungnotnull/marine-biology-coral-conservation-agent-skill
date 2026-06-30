"""
knowledge_updater.py — Skill #238: Marine Biology Research & Coral Reef Conservation Support
crawl4ai knowledge pipeline for SECOND-KNOWLEDGE-BRAIN.md

Fetches latest oceanographic and marine science content from:
  1. NOAA Coral Reef Watch news & alerts
  2. AIMS research publications RSS
  3. Coral Triangle Initiative updates
  4. Marine Pollution Bulletin (ScienceDirect — abstract/metadata only)
  5. ReefBase news
  6. ArXiv q-bio.PE (population ecology preprints)

Schedule: Weekly (recommended: Sunday 02:00 UTC via cron or Windows Task Scheduler)

Usage:
  python knowledge_updater.py
  python knowledge_updater.py --dry-run      # fetch and score but do not append
  python knowledge_updater.py --source noaa  # run only one source
  python knowledge_updater.py --limit 10     # append maximum 10 new entries

Requirements:
  pip install crawl4ai feedparser requests beautifulsoup4 arxiv
"""

import argparse
import hashlib
import json
import logging
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# Third-party imports — install with pip if not present
try:
    import feedparser
except ImportError:
    feedparser = None

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    requests = None
    BeautifulSoup = None

try:
    import arxiv
except ImportError:
    arxiv = None

try:
    from crawl4ai import AsyncWebCrawler
    CRAWL4AI_AVAILABLE = True
except ImportError:
    CRAWL4AI_AVAILABLE = False

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SKILL_DIR = Path(__file__).parent.parent  # D:\Dungchan\skill_adv\238\
KNOWLEDGE_BRAIN_PATH = SKILL_DIR / "SECOND-KNOWLEDGE-BRAIN.md"
LOG_PATH = SKILL_DIR / "tools" / "knowledge_updater.log"

DOMAIN_KEYWORDS = [
    "coral reef", "coral bleaching", "reef restoration", "ocean acidification",
    "sea surface temperature", "degree heating weeks", "DHW", "coral cover",
    "Symbiodiniaceae", "Acropora", "Porites", "marine biodiversity",
    "reef monitoring", "GCRMN", "Reef Check", "reef health",
    "coral transplant", "coral nursery", "micro-fragmentation",
    "Crown of Thorns starfish", "COTS", "reef ecology",
    "climate change coral", "bleaching event", "thermal tolerance coral",
    "Great Barrier Reef", "Coral Triangle", "Caribbean reef",
    "aragonite saturation", "ocean warming"
]

REQUEST_DELAY_SECONDS = 2.0  # Rate limiting between requests

logging.basicConfig(
    filename=str(LOG_PATH),
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

class Entry:
    """Represents one knowledge entry to be appended to SECOND-KNOWLEDGE-BRAIN.md."""
    def __init__(
        self,
        source: str,
        title: str,
        authors: str,
        date: str,
        doi_or_url: str,
        abstract: str,
        key_finding: str,
        relevance_score: float
    ):
        self.source = source
        self.title = title
        self.authors = authors
        self.date = date
        self.doi_or_url = doi_or_url
        self.abstract = abstract
        self.key_finding = key_finding
        self.relevance_score = relevance_score
        self.fingerprint = self._compute_fingerprint()

    def _compute_fingerprint(self) -> str:
        """SHA-256 fingerprint for deduplication. Uses DOI if present, else URL."""
        canonical = self.doi_or_url.strip().lower()
        return hashlib.sha256(canonical.encode()).hexdigest()

    def to_markdown(self, fetch_date: str) -> str:
        return (
            f"\n## [{fetch_date}] {self.source} — {self.title}\n"
            f"**Authors:** {self.authors}\n"
            f"**Published:** {self.date}\n"
            f"**DOI/URL:** {self.doi_or_url}\n"
            f"**Abstract/Summary:** {self.abstract[:600]}{'...' if len(self.abstract) > 600 else ''}\n"
            f"**Relevance Score:** {self.relevance_score:.2f}\n"
            f"**Key Finding:** {self.key_finding}\n"
            "---\n"
        )


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def compute_recency_score(date_str: str) -> float:
    """Score 0–1 based on recency. Fully decays at 180 days."""
    try:
        if not date_str:
            return 0.3  # Unknown date gets partial score
        # Try common date formats
        for fmt in ("%Y-%m-%d", "%d %b %Y", "%B %d, %Y", "%Y/%m/%d"):
            try:
                pub_date = datetime.strptime(date_str.strip()[:20], fmt)
                break
            except ValueError:
                continue
        else:
            return 0.3
        days_since = (datetime.now() - pub_date).days
        return max(0.0, 1.0 - days_since / 180.0)
    except Exception:
        return 0.3


def compute_relevance_score(text: str) -> float:
    """Score 0–1 based on keyword match density."""
    text_lower = text.lower()
    matches = sum(1 for kw in DOMAIN_KEYWORDS if kw.lower() in text_lower)
    return min(1.0, matches / max(1, len(DOMAIN_KEYWORDS) * 0.3))


def compute_combined_score(date_str: str, text: str) -> float:
    """Weighted combination: 60% recency, 40% relevance."""
    recency = compute_recency_score(date_str)
    relevance = compute_relevance_score(text)
    return 0.6 * recency + 0.4 * relevance


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def load_existing_fingerprints(brain_path: Path) -> set:
    """Extract all DOI/URL fingerprints from existing SECOND-KNOWLEDGE-BRAIN.md."""
    fingerprints = set()
    if not brain_path.exists():
        return fingerprints
    content = brain_path.read_text(encoding="utf-8", errors="replace")
    # Match DOI/URL lines in knowledge update log sections
    doi_url_pattern = re.compile(r"\*\*DOI/URL:\*\*\s*(\S+)")
    for match in doi_url_pattern.finditer(content):
        raw = match.group(1).strip().lower()
        fingerprints.add(hashlib.sha256(raw.encode()).hexdigest())
    return fingerprints


# ---------------------------------------------------------------------------
# Source 1: NOAA Coral Reef Watch News
# ---------------------------------------------------------------------------

def fetch_noaa_crw_news() -> list[Entry]:
    """Scrape NOAA Coral Reef Watch news page for recent alerts and articles."""
    entries = []
    if not requests or not BeautifulSoup:
        logger.warning("requests or BeautifulSoup not installed — skipping NOAA CRW")
        return entries

    url = "https://coralreefwatch.noaa.gov/news/index.php"
    try:
        time.sleep(REQUEST_DELAY_SECONDS)
        resp = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Parse news items — structure may vary; adapt as needed
        news_items = soup.find_all("div", class_=re.compile(r"news|article|post", re.I))
        if not news_items:
            # Fallback: look for any <h2> or <h3> within main content
            news_items = soup.select("main h2, main h3, #content h2, #content h3")

        for item in news_items[:10]:  # Limit to 10 most recent
            title = item.get_text(strip=True)
            if not title or len(title) < 10:
                continue
            # Try to find associated link and date
            parent = item.parent if item.parent else item
            link_tag = parent.find("a", href=True)
            date_tag = parent.find(class_=re.compile(r"date|time", re.I))
            article_url = link_tag["href"] if link_tag else url
            if article_url.startswith("/"):
                article_url = "https://coralreefwatch.noaa.gov" + article_url
            date_str = date_tag.get_text(strip=True) if date_tag else datetime.now().strftime("%Y-%m-%d")
            abstract = parent.get_text(strip=True)[:400]
            score = compute_combined_score(date_str, title + " " + abstract)

            entries.append(Entry(
                source="NOAA Coral Reef Watch",
                title=title[:200],
                authors="NOAA CRW",
                date=date_str,
                doi_or_url=article_url,
                abstract=abstract,
                key_finding=f"NOAA CRW update: {title[:150]}",
                relevance_score=score
            ))

        logger.info(f"NOAA CRW: fetched {len(entries)} entries")
    except Exception as e:
        logger.error(f"NOAA CRW fetch failed: {e}")

    return entries


# ---------------------------------------------------------------------------
# Source 2: AIMS Research Publications RSS
# ---------------------------------------------------------------------------

def fetch_aims_rss() -> list[Entry]:
    """Parse AIMS research publications RSS feed."""
    entries = []
    if not feedparser:
        logger.warning("feedparser not installed — skipping AIMS RSS")
        return entries

    feed_url = "https://www.aims.gov.au/research/news/rss"
    try:
        time.sleep(REQUEST_DELAY_SECONDS)
        feed = feedparser.parse(feed_url)
        for item in feed.entries[:15]:
            title = getattr(item, "title", "")
            summary = getattr(item, "summary", "")
            link = getattr(item, "link", feed_url)
            published = getattr(item, "published", "")

            combined_text = title + " " + summary
            score = compute_combined_score(published, combined_text)

            if score < 0.15:
                continue  # Skip clearly irrelevant entries

            entries.append(Entry(
                source="AIMS Research Publications",
                title=title[:200],
                authors="Australian Institute of Marine Science (AIMS)",
                date=published[:10] if published else datetime.now().strftime("%Y-%m-%d"),
                doi_or_url=link,
                abstract=summary[:500],
                key_finding=f"AIMS: {title[:150]}",
                relevance_score=score
            ))
        logger.info(f"AIMS RSS: fetched {len(entries)} entries")
    except Exception as e:
        logger.error(f"AIMS RSS fetch failed: {e}")

    return entries


# ---------------------------------------------------------------------------
# Source 3: Coral Triangle Initiative Updates
# ---------------------------------------------------------------------------

def fetch_cti_news() -> list[Entry]:
    """Scrape Coral Triangle Initiative news page."""
    entries = []
    if not requests or not BeautifulSoup:
        logger.warning("requests or BeautifulSoup not installed — skipping CTI")
        return entries

    url = "https://www.coraltriangleinitiative.org/news"
    try:
        time.sleep(REQUEST_DELAY_SECONDS)
        resp = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        articles = soup.select("article, .news-item, .views-row")
        if not articles:
            articles = soup.select("h2 a, h3 a")

        for art in articles[:10]:
            title_tag = art.find(["h2", "h3", "a"]) if hasattr(art, "find") else art
            if not title_tag:
                continue
            title = title_tag.get_text(strip=True)[:200]
            href = title_tag.get("href", url) if hasattr(title_tag, "get") else url
            if href and href.startswith("/"):
                href = "https://www.coraltriangleinitiative.org" + href
            summary = art.get_text(strip=True)[:400] if hasattr(art, "get_text") else title
            date_str = datetime.now().strftime("%Y-%m-%d")

            score = compute_combined_score(date_str, title + " " + summary)
            entries.append(Entry(
                source="Coral Triangle Initiative",
                title=title,
                authors="CTI-CFF Secretariat",
                date=date_str,
                doi_or_url=href or url,
                abstract=summary,
                key_finding=f"CTI update: {title[:150]}",
                relevance_score=score
            ))
        logger.info(f"CTI: fetched {len(entries)} entries")
    except Exception as e:
        logger.error(f"CTI fetch failed: {e}")

    return entries


# ---------------------------------------------------------------------------
# Source 4: Marine Pollution Bulletin (ScienceDirect — abstract metadata)
# ---------------------------------------------------------------------------

def fetch_marine_pollution_bulletin() -> list[Entry]:
    """
    Fetch recent Marine Pollution Bulletin articles from ScienceDirect.
    Retrieves abstract + metadata only (open access metadata, no full text).
    """
    entries = []
    if not requests or not BeautifulSoup:
        logger.warning("requests or BeautifulSoup not installed — skipping MPB")
        return entries

    # ScienceDirect journal page for Marine Pollution Bulletin
    url = "https://www.sciencedirect.com/journal/marine-pollution-bulletin/vol/latest/suppl/C"
    try:
        time.sleep(REQUEST_DELAY_SECONDS)
        resp = requests.get(url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (compatible; coral-conservation-skill/1.0)",
            "Accept": "text/html"
        })
        # ScienceDirect may require JS rendering — if blocked, use CrossRef API instead
        if resp.status_code != 200:
            raise ValueError(f"HTTP {resp.status_code} — ScienceDirect may require JS rendering")

        soup = BeautifulSoup(resp.text, "html.parser")
        articles = soup.select(".article-content-title, h3.subtitle, .result-list-title-link")

        for art in articles[:10]:
            title = art.get_text(strip=True)[:200]
            href = art.get("href", "")
            if href and not href.startswith("http"):
                href = "https://www.sciencedirect.com" + href
            score = compute_combined_score(datetime.now().strftime("%Y-%m-%d"), title)
            if score < 0.15:
                continue

            entries.append(Entry(
                source="Marine Pollution Bulletin (ScienceDirect)",
                title=title,
                authors="(See DOI/URL for full authorship)",
                date=datetime.now().strftime("%Y-%m-%d"),
                doi_or_url=href or url,
                abstract=f"Article from Marine Pollution Bulletin: {title}. Retrieve full abstract at: {href}",
                key_finding=f"New MPB article: {title[:150]}",
                relevance_score=score
            ))
        logger.info(f"MPB ScienceDirect: fetched {len(entries)} entries")
    except Exception as e:
        logger.warning(f"ScienceDirect direct scrape failed ({e}). Falling back to CrossRef API.")
        # Fallback: CrossRef API for Marine Pollution Bulletin recent papers
        entries = fetch_mpb_via_crossref()

    return entries


def fetch_mpb_via_crossref() -> list[Entry]:
    """Fallback: query CrossRef API for recent Marine Pollution Bulletin articles."""
    entries = []
    if not requests:
        return entries
    try:
        time.sleep(REQUEST_DELAY_SECONDS)
        api_url = (
            "https://api.crossref.org/works"
            "?filter=container-title:Marine+Pollution+Bulletin"
            "&sort=published&order=desc&rows=10"
            "&mailto=skill-238@claude.code"
        )
        resp = requests.get(api_url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        for item in data.get("message", {}).get("items", []):
            title = " ".join(item.get("title", ["Untitled"]))[:200]
            authors_list = item.get("author", [])
            authors = ", ".join(
                f"{a.get('given', '')} {a.get('family', '')}".strip()
                for a in authors_list[:3]
            ) or "Unknown Authors"
            if len(authors_list) > 3:
                authors += " et al."
            doi = item.get("DOI", "")
            doi_url = f"https://doi.org/{doi}" if doi else ""
            published = item.get("published", {}).get("date-parts", [[]])[0]
            date_str = "-".join(str(p) for p in published) if published else ""
            abstract = item.get("abstract", "")[:500]
            score = compute_combined_score(date_str, title + " " + abstract)
            if score < 0.1:
                continue

            entries.append(Entry(
                source="Marine Pollution Bulletin (CrossRef)",
                title=title,
                authors=authors,
                date=date_str,
                doi_or_url=doi_url or f"https://api.crossref.org/works/{doi}",
                abstract=abstract,
                key_finding=f"MPB: {title[:150]}",
                relevance_score=score
            ))
        logger.info(f"MPB CrossRef fallback: fetched {len(entries)} entries")
    except Exception as e:
        logger.error(f"CrossRef MPB fallback also failed: {e}")

    return entries


# ---------------------------------------------------------------------------
# Source 5: ReefBase News
# ---------------------------------------------------------------------------

def fetch_reefbase_news() -> list[Entry]:
    """Fetch news and database updates from ReefBase."""
    entries = []
    if not requests or not BeautifulSoup:
        logger.warning("requests or BeautifulSoup not installed — skipping ReefBase")
        return entries

    url = "http://www.reefbase.net"
    try:
        time.sleep(REQUEST_DELAY_SECONDS)
        resp = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        links = soup.find_all("a", href=True)
        seen_titles = set()
        for link in links[:30]:
            title = link.get_text(strip=True)
            if (title and len(title) > 15 and title not in seen_titles
                    and any(kw.lower() in title.lower() for kw in ["reef", "coral", "marine", "bleach"])):
                seen_titles.add(title)
                href = link["href"]
                if href.startswith("/"):
                    href = "http://www.reefbase.net" + href
                score = compute_combined_score("", title)
                entries.append(Entry(
                    source="ReefBase",
                    title=title[:200],
                    authors="ReefBase / GCRMN",
                    date=datetime.now().strftime("%Y-%m-%d"),
                    doi_or_url=href,
                    abstract=f"ReefBase resource: {title}",
                    key_finding=f"ReefBase: {title[:150]}",
                    relevance_score=score
                ))
        logger.info(f"ReefBase: fetched {len(entries)} entries")
    except Exception as e:
        logger.error(f"ReefBase fetch failed: {e}")

    return entries


# ---------------------------------------------------------------------------
# Source 6: ArXiv q-bio.PE (Population Ecology — coral reef papers)
# ---------------------------------------------------------------------------

def fetch_arxiv_coral() -> list[Entry]:
    """Query ArXiv API for recent coral reef papers in q-bio.PE and related categories."""
    entries = []
    if not arxiv:
        logger.warning("arxiv package not installed — skipping ArXiv")
        return entries

    try:
        time.sleep(REQUEST_DELAY_SECONDS)
        client = arxiv.Client()
        search = arxiv.Search(
            query="coral reef bleaching restoration acidification",
            max_results=10,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )
        for result in client.results(search):
            title = result.title[:200]
            authors = ", ".join(str(a) for a in result.authors[:3])
            if len(result.authors) > 3:
                authors += " et al."
            date_str = result.published.strftime("%Y-%m-%d") if result.published else ""
            abstract = result.summary[:500]
            doi_url = result.entry_id  # ArXiv ID URL

            score = compute_combined_score(date_str, title + " " + abstract)
            if score < 0.15:
                continue

            entries.append(Entry(
                source="ArXiv (q-bio.PE / marine science)",
                title=title,
                authors=authors,
                date=date_str,
                doi_or_url=doi_url,
                abstract=abstract,
                key_finding=f"ArXiv preprint: {title[:150]}",
                relevance_score=score
            ))
        logger.info(f"ArXiv: fetched {len(entries)} entries")
    except Exception as e:
        logger.error(f"ArXiv fetch failed: {e}")

    return entries


# ---------------------------------------------------------------------------
# Append to SECOND-KNOWLEDGE-BRAIN.md
# ---------------------------------------------------------------------------

def append_entries(entries: list[Entry], brain_path: Path, dry_run: bool = False) -> int:
    """
    Append new entries to SECOND-KNOWLEDGE-BRAIN.md.
    Deduplicates against existing content.
    Returns count of new entries appended.
    """
    existing_fingerprints = load_existing_fingerprints(brain_path)
    fetch_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Sort by relevance score descending
    entries_sorted = sorted(entries, key=lambda e: e.relevance_score, reverse=True)

    new_entries = []
    for entry in entries_sorted:
        if entry.fingerprint in existing_fingerprints:
            logger.debug(f"SKIP (duplicate): {entry.title[:60]}")
            continue
        if entry.relevance_score < 0.10:
            logger.debug(f"SKIP (low score {entry.relevance_score:.2f}): {entry.title[:60]}")
            continue
        new_entries.append(entry)
        existing_fingerprints.add(entry.fingerprint)  # Prevent duplicates within this run

    if not new_entries:
        logger.info("No new entries to append.")
        return 0

    if dry_run:
        print(f"DRY RUN: Would append {len(new_entries)} new entries:")
        for e in new_entries:
            print(f"  [{e.relevance_score:.2f}] {e.source}: {e.title[:80]}")
        return len(new_entries)

    # Ensure brain file exists
    if not brain_path.exists():
        logger.error(f"SECOND-KNOWLEDGE-BRAIN.md not found at {brain_path}")
        return 0

    # Append to Knowledge Update Log section, or add at end of file
    brain_content = brain_path.read_text(encoding="utf-8", errors="replace")
    new_block = f"\n\n<!-- AUTO-UPDATED: {fetch_date} — {len(new_entries)} new entries -->\n"
    for entry in new_entries:
        new_block += entry.to_markdown(fetch_date)

    # Update the Knowledge Update Log table
    log_line = f"| {fetch_date} | Multiple ({len(set(e.source for e in new_entries))} sources) | {len(new_entries)} | Automated crawl |"
    if "## 7. Knowledge Update Log" in brain_content:
        brain_content = brain_content.replace(
            "| Date | Source | Entries Added | Notes |",
            "| Date | Source | Entries Added | Notes |\n" + log_line,
            1
        )

    # Append new entries at end of file
    updated_content = brain_content.rstrip() + "\n" + new_block

    brain_path.write_text(updated_content, encoding="utf-8")
    logger.info(f"Appended {len(new_entries)} new entries to {brain_path}")
    print(f"Appended {len(new_entries)} new entries to SECOND-KNOWLEDGE-BRAIN.md")

    return len(new_entries)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="knowledge_updater.py — Coral Reef Conservation Skill #238 crawl pipeline"
    )
    parser.add_argument("--dry-run", action="store_true", help="Fetch and score but do not write to file")
    parser.add_argument("--source", choices=["noaa", "aims", "cti", "mpb", "reefbase", "arxiv", "all"],
                        default="all", help="Run only one source (default: all)")
    parser.add_argument("--limit", type=int, default=0, help="Max entries to append (0 = unlimited)")
    args = parser.parse_args()

    logger.info(f"=== knowledge_updater.py started === source={args.source}, dry_run={args.dry_run}")
    print(f"Marine Biology Coral Conservation Skill #238 — Knowledge Updater")
    print(f"Target: {KNOWLEDGE_BRAIN_PATH}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE UPDATE'}")
    print("-" * 60)

    all_entries: list[Entry] = []

    source_map = {
        "noaa": fetch_noaa_crw_news,
        "aims": fetch_aims_rss,
        "cti": fetch_cti_news,
        "mpb": fetch_marine_pollution_bulletin,
        "reefbase": fetch_reefbase_news,
        "arxiv": fetch_arxiv_coral,
    }

    if args.source == "all":
        sources_to_run = source_map.keys()
    else:
        sources_to_run = [args.source]

    for source_key in sources_to_run:
        print(f"Fetching: {source_key.upper()}...")
        try:
            entries = source_map[source_key]()
            print(f"  -> {len(entries)} entries retrieved")
            all_entries.extend(entries)
        except Exception as e:
            print(f"  -> ERROR: {e}")
            logger.error(f"Source {source_key} failed: {e}")

    print(f"\nTotal entries retrieved: {len(all_entries)}")

    if args.limit > 0:
        # Sort by score and take top N
        all_entries.sort(key=lambda e: e.relevance_score, reverse=True)
        all_entries = all_entries[:args.limit]
        print(f"Limited to top {args.limit} entries by relevance score")

    new_count = append_entries(all_entries, KNOWLEDGE_BRAIN_PATH, dry_run=args.dry_run)
    print(f"\nDone. New entries appended: {new_count}")
    logger.info(f"=== knowledge_updater.py completed. New entries: {new_count} ===")


if __name__ == "__main__":
    main()
