---
name: marine-biology-coral-conservation/sub-reef-assessment
description: Systematic reef health assessment using Reef Check, GCRMN, and CoralWatch protocols — produces a quantitative Reef Health Scorecard with DHW context, coral cover %, bleaching index, species diversity, and OHI sub-scores.
---

## Purpose

Guide a systematic reef health assessment using globally standardized protocols (Reef Check, GCRMN, CoralWatch) and satellite-derived oceanographic data (NOAA DHW). The sub-skill interprets field survey data against published benchmarks, contextualizes findings with current thermal stress levels, and produces a quantitative Reef Health Scorecard that drives restoration planning and monitoring protocol design.

The assessment is always grounded in real data: satellite DHW from NOAA CRW is retrieved before interpreting visual survey data, because thermal stress context determines whether observed bleaching is acute, cumulative, or recovering.

---

## Inputs

- **Structured Site Profile** from `sub-profile-intake`
- **Field survey data** (if available): Reef Check data sheets, GCRMN transect summaries, photo-quadrat analyses, fish counts
- **User observations** (if no formal survey data): verbal description of coral cover, bleaching extent, fish presence
- **NOAA DHW data** (fetched during this sub-skill)

---

## Workflow

### Step 1 — Retrieve NOAA DHW Data

**1a.** Use the site GPS coordinates from the Site Profile to query NOAA Coral Reef Watch:
- URL: `https://coralreefwatch.noaa.gov/product/vs/data/{station_id}.txt` (for monitored stations)
- Or use the interactive map: `https://coralreefwatch.noaa.gov/product/vs/map.php`
- WebFetch or WebSearch for current DHW value and Alert Level for the nearest 5km pixel

**1b.** Record:
- Current DHW value (°C-weeks)
- Alert Level: 0 (No Alert) / Watch (1–3) / Alert 1 (4–7) / Alert 2 (≥8)
- Maximum DHW in past 12 months (peak thermal stress)
- 4-month DHW forecast (if available from NOAA CRW)

**1c.** Cross-reference against historical baselines:
- Has this site experienced DHW ≥ 8 in the past 10 years? If yes, how many times?
- NOAA bleaching event history is available at: `https://coralreefwatch.noaa.gov/satellite/analyses_tools/bleachingHotSpots.php`

If NOAA CRW data is unavailable: note limitation, use user-reported water temperature vs. historical mean as proxy, and flag in report.

---

### Step 2 — Reef Check Assessment (Primary Protocol for Standardized Sites)

For sites with existing Reef Check data, or to guide the user in collecting new data:

**Reef Check Transect Setup:**
- 2 transects × 50m each, at the target survey depth
- Measure: 1m above substrate for benthic; within 2m horizontally for fish
- Separate observers for fish (trained ID required) and benthic/invertebrate (less specialized)

**Benthic Parameters — record for each 50m transect:**
| Parameter | Code | Definition |
|-----------|------|------------|
| Hard coral | HC | Living hard coral (scleractinian) |
| Soft coral | SC | Living soft coral (octocoral) |
| Coralline algae | CA | Crustose coralline algae |
| Turf algae | TA | Low-lying algal turf (<1cm) |
| Macroalgae | MA | Fleshy macroalgae (Sargassum, Halimeda, etc.) |
| Rubble | R | Loose coral rubble |
| Sand | S | Sand or sediment |
| Silt | SI | Fine silty sediment |
| Other | O | Bare rock, seagrass, etc. |
| Bleached coral | BL | Coral with ≥50% white tissue |

Calculate: % cover for each category (count of points / total points × 100)

**Fish Parameters (indicator taxa only):**
- Count all individuals of: Butterfly fishes (Chaetodontidae), Groupers ≥30cm, Humphead wrasse, Surgeonfish
- Record: species/family, count, size estimate

**Invertebrate Parameters:**
- Count: Crown-of-thorns starfish, Diadema urchins, Giant clams, Sea cucumbers, Lobsters

Interpret per Reef Check Training Manual (2020).

---

### Step 3 — GCRMN Photo-Quadrat Analysis (If Equipment Available)

For higher-resolution benthic data:

**Method:**
- 50cm × 50cm quadrat frame placed at 0.5m intervals along a 50m transect
- Photograph each quadrat from directly above, perpendicular to substrate
- 100 random points per quadrat analyzed using CoralNet or CPCe

**Output:**
- % cover per benthic category (higher precision than Reef Check visual estimate)
- Coral morphology breakdown: branching / massive / encrusting / foliose / free-living
- Recent mortality % (white skeleton, pale tissue)

If photo-quadrat analysis is not feasible: proceed with Reef Check visual estimate only and note the limitation.

---

### Step 4 — CoralWatch Bleaching Index

**Method:**
- Using CoralWatch Coral Health Chart, score a minimum of 20 coral colonies per site
- Score each colony 1–6 on the lightest/darkest portion of the colony
- Calculate mean score across all colonies (bleaching index)

| Mean Score | Health Status | Response Required |
|-----------|--------------|------------------|
| 5.0–6.0 | Healthy | Routine monitoring |
| 4.0–4.9 | Mildly stressed | Heightened monitoring |
| 3.0–3.9 | Moderately bleached | Alert — assess causes, increase survey frequency |
| 2.0–2.9 | Severely bleached | Emergency — consider restoration pre-planning |
| 1.0–1.9 | Fully bleached | Crisis — mortality likely; restoration planning urgent |

Cross-reference CoralWatch index with DHW Alert Level to assess coherence (high DHW should correlate with low CoralWatch scores).

---

### Step 5 — Species Diversity Calculation

**Shannon Diversity Index (H'):**

H' = -Σ (pi × ln(pi))

Where pi = proportion of coral cover attributed to genus i.

Record all coral genera present (Acropora, Porites, Pocillopora, Platygyra, Montastraea, Orbicella, Pavona, Favia, Fungia, Stylophora, Goniastrea, etc.).

Interpret H':
- H' > 2.5: High diversity — resilient reef
- H' 1.5–2.5: Moderate diversity — monitor
- H' < 1.5: Low diversity — degraded reef, restoration priority

---

### Step 6 — Ocean Acidification Risk Assessment

Using the site's GCRMN region and available data:

**6a.** Check SECOND-KNOWLEDGE-BRAIN.md Section 9 for regional Ωarag values.

**6b.** Classify acidification risk:
| Ωarag | Risk Tier | Implication |
|--------|-----------|------------|
| > 3.0 | Low | Reef-building capacity intact |
| 2.0–3.0 | Moderate | Reduced calcification; monitor |
| 1.5–2.0 | High | Net erosion possible; restoration harder |
| < 1.5 | Critical | Dissolution risk; biorock may be needed |

**6c.** If in-situ pH data is available from user: convert to Ωarag using region-appropriate seawater chemistry values.

---

### Step 7 — OHI Sub-Score Calculation

Compute relevant Ocean Health Index components for the site:

- **Biodiversity (Species sub-goal):** Score 0–100 based on: proportion of IUCN-listed species present (in Good/Least Concern category vs. Threatened/Extinct). Use IUCN Red List and OBIS species occurrence data.
  - Excellent (90–100): <10% species are Threatened/Extinct
  - Good (70–89): 10–25% Threatened
  - Fair (50–69): 25–40% Threatened
  - Poor (<50): >40% Threatened

- **Carbon Storage:** Score 0–100 based on live coral cover vs. reference point (30% cover = 100 score; linear scale).

Report both sub-scores with brief justification.

---

### Step 8 — Compile Reef Health Scorecard

Assemble all dimensional scores into the Reef Health Scorecard:

```
REEF HEALTH SCORECARD — [Site Name] — [Date]

PHYSICAL / THERMAL
  Current DHW:          X °C-weeks  [NOAA CRW, date retrieved]
  NOAA Alert Level:     [0 / Watch / Alert 1 / Alert 2]
  12-month peak DHW:    X °C-weeks
  SST vs. MMM:          +X°C

BENTHIC (Reef Check / GCRMN)
  Live Coral Cover:     X%   [Benchmark: 30% healthy; 17.6% global avg 2020]
  Bleached Coral:       X%   [% of hard coral showing bleaching]
  Macroalgae Cover:     X%   [>20% indicates phase shift risk]
  Rubble:               X%   [>30% indicates structural damage]
  Coralline Algae:      X%

BLEACHING (CoralWatch)
  Bleaching Index:      X/5  [>3.5 = healthy; <3.0 = alert]
  Colonies scored:      N

BIODIVERSITY
  Shannon H':           X    [>2.5 high; 1.5–2.5 moderate; <1.5 low]
  Genera present:       [list]

ACIDIFICATION
  Ωarag (estimated):    X    [>3.0 low risk; 2.0–3.0 moderate; <2.0 high/critical]

OHI SUB-SCORES
  Biodiversity:         X/100
  Carbon Storage:       X/100

OVERALL REEF STATUS: [Excellent / Good / Fair / Poor / Critical]
  (Composite: weight 40% coral cover, 30% DHW, 15% H', 15% OHI avg)
```

Overall status thresholds:
- Excellent: coral cover ≥30%, DHW Alert Level 0, H' ≥2.5
- Good: coral cover 20–29%, DHW ≤ Watch, H' 2.0–2.5
- Fair: coral cover 10–19%, DHW Alert 1 or below, H' 1.5–2.0
- Poor: coral cover 5–9%, any recent Alert 2, H' 1.0–1.5
- Critical: coral cover <5%, repeated Alert 2, H' <1.0

---

## Outputs

**Reef Health Scorecard** — quantitative, structured document including:
- All dimensional scores with benchmarks and source citations
- DHW value and Alert Level from NOAA CRW
- CoralWatch bleaching index
- Shannon diversity
- Acidification risk tier
- OHI sub-scores
- Overall reef status rating
- Narrative interpretation (2–3 paragraphs)

---

## Quality Gate

| Check | Criterion |
|-------|-----------|
| DHW sourced from NOAA | DHW value from NOAA CRW satellite data (date of retrieval recorded) |
| Coral cover methodology stated | Reef Check or GCRMN protocol stated; transect count recorded |
| CoralWatch sample size ≥ 20 | If <20 colonies scored, flag as limited sample |
| All benchmarks cited | GCRMN 2020 global average cited for coral cover; Liu et al. (2006) for DHW |
| H' formula shown | Shannon calculation explicitly shown (not just result stated) |
| OHI sub-scores present | Both Biodiversity and Carbon Storage sub-scores computed |
| Overall status rating assigned | One of: Excellent / Good / Fair / Poor / Critical |
| Narrative present | At least 2 paragraphs interpreting scores in ecological context |
