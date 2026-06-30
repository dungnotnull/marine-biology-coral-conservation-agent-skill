# PROJECT-detail.md — Skill #238: Marine Biology Research & Coral Reef Conservation Support

## Executive Summary

Skill #238 delivers a structured, research-first harness for scientific divers and marine conservation practitioners. It integrates globally standardized reef monitoring protocols (Reef Check, GCRMN, CoralWatch), real-time oceanographic data from NOAA Coral Reef Watch and AIMS, and evidence-based coral restoration methodologies (Coral Restoration Foundation protocols, SECORE assisted gene flow, micro-fragmentation) into a single unified workflow. The output is a professional-grade Marine Biology Research & Conservation Report including a quantitative reef health scorecard, a species-appropriate restoration plan, a statistically powered monitoring protocol, and a curated reference list of peer-reviewed citations — automatically kept current by a crawl4ai knowledge pipeline.

---

## Problem Statement

Coral reefs cover less than 1% of the ocean floor but support approximately 25% of all marine species. Since 1950, global coral cover has declined by roughly 50%, driven by ocean warming (bleaching events triggered at Degree Heating Weeks ≥ 8), ocean acidification (current surface pH ≈ 8.1, down from pre-industrial 8.2), direct physical disturbance, and nutrient pollution. The science of reef restoration has advanced rapidly — micro-fragmentation protocols developed by the Coral Restoration Foundation achieve fragment survival rates above 90% under controlled conditions; SECORE International's assisted gene flow experiments show promise for developing thermal-resistant genotypes — yet field practitioners frequently lack structured workflows to:

1. Rapidly assess current reef health against standardized global benchmarks.
2. Select the correct restoration methodology for their site's species composition, depth, and threat profile.
3. Design monitoring protocols with sufficient statistical power to detect meaningful change.
4. Stay current with the fast-moving literature (NOAA bleaching alert updates, new AIMS long-term monitoring reports, emerging micro-fragmentation techniques).

This skill solves all four problems in a single harness session.

---

## Target Users & Use Cases

| User Type | Trigger Example | Skill Action |
|-----------|----------------|--------------|
| Scientific diver / reef ecologist | "I completed a Reef Check transect at [site]. Coral cover was 18%, bleaching was observed on ~40% of Acropora colonies. What does this mean and what should we do?" | Runs sub-reef-assessment to score against GCRMN benchmarks, interprets DHW context from NOAA, flags bleaching severity tier, outputs restoration priority recommendation |
| Reef restoration project manager | "We want to start a coral nursery at Tubbataha Reef. Which species should we target and what propagation method is best?" | Runs sub-profile-intake + sub-restoration-planner to recommend species, propagation method (nursery fragmentation vs. micro-fragmentation vs. biorock), planting density, and 18-month survival KPIs |
| Marine protected area (MPA) manager | "We need to set up a long-term monitoring program for our MPA. We have 3 scientific divers and can survey quarterly." | Runs sub-monitoring-protocol to design sampling station layout, minimum sample size for 80% power to detect 5% cover change, data recording forms, reporting cadence |
| Graduate researcher / thesis student | "What are the latest peer-reviewed studies on coral thermal tolerance and assisted evolution?" | Queries SECOND-KNOWLEDGE-BRAIN.md + triggers WebSearch across NOAA, AIMS, ArXiv, journals; returns structured literature review with evidence tier ratings |
| Conservation NGO / donor briefing | "We need a comprehensive report on the health of Coral Triangle reefs for our 2026 funding proposal." | Runs full harness end-to-end; produces professional report with OHI scores, DHW trend analysis, restoration strategy, monitoring plan, and references |

---

## Harness Architecture

```
/marine-biology-coral-conservation
│
├── STAGE 1: Profile Intake
│   └── sub-profile-intake.md
│       Inputs:  User prompt (site name, location, objectives)
│       Outputs: Standardized site profile (JSON-like), diver credential level, equipment inventory
│       Gate:    GPS coordinates confirmed, research objectives categorized (assessment/restoration/monitoring/research)
│
├── STAGE 2: Reef Health Assessment
│   └── sub-reef-assessment.md
│       Inputs:  Site profile, existing survey data (if any), NOAA DHW data
│       Outputs: Reef Health Scorecard (coral cover %, bleaching index, species diversity index, OHI sub-scores)
│       Gate:    All GCRMN/Reef Check fields populated; DHW context from NOAA retrieved
│
├── STAGE 3: Restoration Planning
│   └── sub-restoration-planner.md
│       Inputs:  Reef Health Scorecard, site profile, user resources (budget, team size)
│       Outputs: Restoration Strategy Document (species list, propagation method, planting plan, survival KPIs)
│       Gate:    Species selection justified by peer-reviewed literature; propagation method matched to site conditions
│
├── STAGE 4: Monitoring Protocol Design
│   └── sub-monitoring-protocol.md
│       Inputs:  Site profile, restoration plan, team capacity
│       Outputs: Long-Term Monitoring Protocol (stations, frequency, forms, power analysis, reporting schedule)
│       Gate:    Statistical power ≥ 80% for primary outcome; sampling design peer-reviewed
│
├── STAGE 5: Quality Gate Review
│   Internal check — harness validates:
│   - All claims have peer-reviewed citations (GCRMN, Reef Check, journal papers)
│   - DHW data sourced from NOAA Coral Reef Watch (not estimated)
│   - Safety notes for scientific diving included (dive tables, buddy system, gas management)
│   - Output is free of unsupported generalizations
│
└── STAGE 6: Final Synthesis
    Main harness synthesizes all stage outputs into:
    → Marine Biology Research & Conservation Report (professional artifact)
```

---

## Full Sub-Skill Catalog

### sub-profile-intake

| Field | Detail |
|-------|--------|
| **Purpose** | Gather all contextual information needed before any assessment or planning begins |
| **Inputs** | User's natural-language description of their reef site and goals |
| **Outputs** | Structured site profile: GPS coordinates, site name, reef type (fringing/barrier/atoll/patch), depth range, dominant taxa, known stressors, previous surveys, diver certification level, equipment available |
| **Tools Used** | Read (SECOND-KNOWLEDGE-BRAIN.md for regional context), WebSearch (site-specific NOAA SST data) |
| **Quality Gate** | Site classified by GCRMN region; research objective categorized; dive safety level confirmed |

### sub-reef-assessment

| Field | Detail |
|-------|--------|
| **Purpose** | Guide and interpret systematic reef health assessment using globally standardized protocols |
| **Inputs** | Site profile from sub-profile-intake; existing Reef Check data sheets (if available); NOAA DHW values |
| **Outputs** | Reef Health Scorecard with: (1) Live coral cover % vs. GCRMN benchmarks; (2) CoralWatch bleaching index (1–5 scale); (3) Shannon diversity index for coral genera; (4) Fish biomass estimate; (5) Substrate composition; (6) DHW context (Alert Level 0/1/2); (7) Ocean acidification risk tier; (8) OHI sub-score |
| **Tools Used** | WebSearch (NOAA DHW, AIMS monitoring data), WebFetch (Reef Check data sheets, GCRMN reports) |
| **Quality Gate** | DHW value confirmed from NOAA CRW satellite data; coral cover measured against minimum 2 × 50m transects (Reef Check standard) |

### sub-restoration-planner

| Field | Detail |
|-------|--------|
| **Purpose** | Design an evidence-based coral restoration strategy appropriate to the site's species, depth, and threat profile |
| **Inputs** | Reef Health Scorecard; site profile; user's available resources (budget tier, team size, nursery infrastructure) |
| **Outputs** | Restoration Strategy Document: (1) Target species list with thermal tolerance ratings; (2) Propagation method selected (in-situ nursery / ex-situ micro-fragmentation / biorock / assisted gene flow) with justification; (3) Nursery design or substrate preparation specs; (4) Planting density per m²; (5) 6/12/18-month survival rate KPIs; (6) Cited references for all recommendations |
| **Tools Used** | WebSearch (CRF protocols, SECORE papers, micro-fragmentation studies), WebFetch (AIMS restoration guidance) |
| **Quality Gate** | Species thermal tolerance validated against NOAA CoRTAD database; propagation method justified by ≥ 2 peer-reviewed citations |

### sub-monitoring-protocol

| Field | Detail |
|-------|--------|
| **Purpose** | Design a statistically valid long-term monitoring protocol that can detect ecologically meaningful change over time |
| **Inputs** | Site profile; restoration plan; team capacity (number of trained divers, survey frequency, budget for equipment) |
| **Outputs** | Long-Term Monitoring Protocol: (1) Sampling station layout with GPS waypoints; (2) Survey methods (belt transects, photo-quadrats, video transects); (3) Statistical power analysis (minimum n for 80% power to detect Δ5% coral cover); (4) Data recording forms (aligned with Reef Check / GCRMN standards); (5) Reporting schedule and KPI dashboard template; (6) Equipment list with alternatives for resource-limited settings |
| **Tools Used** | Read (SECOND-KNOWLEDGE-BRAIN.md), WebFetch (GCRMN monitoring guide, Reef Check manual) |
| **Quality Gate** | Statistical power calculation shown explicitly; monitoring design peer-reviewed (GCRMN/Reef Check compliant) |

---

## Skill File Format Specification

All skill files use this frontmatter schema:

```yaml
---
name: marine-biology-coral-conservation        # or sub-skill slug
description: One-line summary for /help picker
---
```

Required sections for `main.md`:
- `## Role & Persona`
- `## Workflow` (numbered steps, each invoking a sub-skill or internal action)
- `## Sub-skills Available`
- `## Tools`
- `## Output Format`
- `## Quality Gates`

Required sections for `sub-*.md`:
- `## Purpose`
- `## Inputs`
- `## Workflow` (numbered steps)
- `## Outputs`
- `## Quality Gate`

---

## E2E Execution Flow

```
1. User invokes /marine-biology-coral-conservation
2. Harness greets user as marine biology research support system
3. INVOKE sub-profile-intake
   3a. Ask: reef site name, GPS or region, reef type, depth range
   3b. Ask: user's role (researcher / manager / diver / student)
   3c. Ask: primary objective (assessment / restoration / monitoring / literature review)
   3d. Ask: existing data available? (Reef Check sheets, temperature loggers, photo surveys)
   3e. Ask: team size, dive certification level, equipment available
   3f. OUTPUT: Structured site profile
4. BRANCH by objective:
   4a. Assessment → INVOKE sub-reef-assessment
   4b. Restoration → INVOKE sub-reef-assessment THEN sub-restoration-planner
   4c. Monitoring only → INVOKE sub-monitoring-protocol
   4d. Full workflow → INVOKE all four sub-skills in sequence
   4e. Literature review → WebSearch + SECOND-KNOWLEDGE-BRAIN.md query only
5. INVOKE sub-reef-assessment (if applicable)
   5a. Pull NOAA DHW data for site coordinates
   5b. Interpret user-provided survey data against GCRMN benchmarks
   5c. Score bleaching via CoralWatch scale
   5d. OUTPUT: Reef Health Scorecard
6. INVOKE sub-restoration-planner (if applicable)
   6a. Select target species based on thermal tolerance and site conditions
   6b. Recommend propagation method with peer-reviewed justification
   6c. Define nursery/planting plan with density and survival KPIs
   6d. OUTPUT: Restoration Strategy Document
7. INVOKE sub-monitoring-protocol (if applicable)
   7a. Design sampling station layout
   7b. Calculate statistical power
   7c. Produce data recording templates
   7d. OUTPUT: Long-Term Monitoring Protocol
8. QUALITY GATE REVIEW (internal)
   8a. All claims cited? If not, retrieve citations via WebSearch
   8b. DHW data from NOAA? If not, flag and retrieve
   8c. Safety notes present for any dive recommendations?
   8d. OHI sub-score calculated?
9. SYNTHESIZE final Marine Biology Research & Conservation Report
10. PRESENT report with executive summary, scorecard, strategy, protocol, citations
```

Error handling:
- If GPS coordinates unknown: use regional NOAA DHW polygon data
- If no existing survey data: skip assessment scoring, output survey setup guide instead
- If WebSearch/WebFetch unavailable: fall back to SECOND-KNOWLEDGE-BRAIN.md and flag limitation

---

## SECOND-KNOWLEDGE-BRAIN Integration

- **File:** `238/SECOND-KNOWLEDGE-BRAIN.md`
- **Updated by:** `238/tools/knowledge_updater.py`
- **Schedule:** Weekly (recommended cron: Sunday 02:00 UTC)
- **Crawl sources:**
  - NOAA Coral Reef Watch news & alerts
  - AIMS research publications RSS
  - Coral Triangle Initiative reports
  - Marine Pollution Bulletin (ScienceDirect new articles)
  - ReefBase news
  - ArXiv `q-bio.PE` (population ecology preprints)
- **Append format:** `## [YYYY-MM-DD] {Source} — {Title}` with Abstract, DOI/URL, Relevance tier
- **Deduplication:** DOI hash check; URL fingerprint for non-DOI sources

---

## Quality Gates Definition

Before final output is shown to the user, all of the following must be true:

| Gate | Criterion | Action if Failed |
|------|-----------|-----------------|
| QG-1 | Every numerical claim (coral cover %, DHW threshold, fragment survival rate) has a cited source | Retrieve missing citation via WebSearch before proceeding |
| QG-2 | DHW data sourced from NOAA Coral Reef Watch satellite data, not estimated | Fetch NOAA CRW data for site coordinates |
| QG-3 | Species thermal tolerance ratings cited from NOAA CoRTAD or peer-reviewed study | Retrieve thermal tolerance data |
| QG-4 | Propagation method recommendation justified by ≥ 2 peer-reviewed citations | Search for additional citations if only 1 found |
| QG-5 | Statistical power analysis explicitly shown in monitoring protocol | Calculate or re-calculate power before output |
| QG-6 | Dive safety note included whenever dive depth or technique is recommended | Append PADI/AAUS scientific diving safety reference |
| QG-7 | OHI or equivalent composite score computed and explained | Compute from available sub-scores |
| QG-8 | Output structured as professional research artifact (not chat reply format) | Reformat if needed |

---

## Test Scenarios

See `tests/test-scenarios.md` for 5 detailed scenario tests.

---

## Key Design Decisions

1. **Protocol primacy:** Reef Check and GCRMN protocols are treated as the gold standard for field assessment methodology — no ad hoc survey designs are recommended without citing a peer-reviewed reason.
2. **DHW-first bleaching analysis:** All bleaching risk assessments start with NOAA DHW data before interpreting visual survey data, because thermal stress context determines whether observed bleaching is acute or cumulative.
3. **Branching workflow:** The harness branches by user objective (assessment / restoration / monitoring / literature review) to avoid presenting irrelevant stages — a monitoring-only user should not be required to complete a full restoration plan.
4. **Quantitative outputs mandatory:** Every assessment produces numerical scores (cover %, bleaching index, DHW value, Shannon H', power %) — no qualitative-only outputs.
5. **Propagation method decision tree:** Restoration planner uses a structured decision tree (species availability → depth → thermal stress level → resource constraints → method selection) rather than a fixed recommendation, because site conditions vary dramatically.
6. **Safety-gated diving recommendations:** Any recommendation involving dive depth > 18m triggers automatic AAUS/PADI scientific diving safety note.
7. **Self-improving knowledge base:** The skill becomes more accurate over time as the crawl pipeline adds new NOAA alerts, AIMS papers, and journal articles — the agent always checks SECOND-KNOWLEDGE-BRAIN.md before querying the web.
8. **Graceful degradation:** If live web sources are unavailable, the skill signals this clearly and uses SECOND-KNOWLEDGE-BRAIN.md as fallback, rather than fabricating data.
