# test-scenarios.md — Skill #238: Marine Biology Research & Coral Reef Conservation Support

## Overview

This file contains 5 scenario-based tests for the `marine-biology-coral-conservation` skill. Each scenario specifies the user input, which workflow branch is triggered, the expected outputs (with quantitative targets), and pass/fail criteria. Tests should be executed end-to-end by invoking the main harness (`skills/main.md`) with the scenario input and comparing actual outputs against the expected column.

---

## Scenario 1 — Coral Bleaching Emergency Response (Maldives)

### Input

```
User: "I'm a marine biologist diving at South Male Atoll, Maldives (GPS: 3.5°N, 73.5°E). 
I've just completed a Reef Check survey and found: live coral cover 22%, bleached colonies 
represent about 45% of Acropora coverage. NOAA is showing a DHW of 9.8 °C-weeks right now. 
We have 4 divers, AAUS certification, quarterly survey capacity, and underwater cameras. 
I need to know how serious this is and what to do."
```

### Expected Workflow Branch

Branch A (Assessment) → Emergency escalation pathway

### Expected Outputs

#### Stage 1 — Profile Intake
- Site: South Male Atoll, Maldives; GPS 3.5°N, 73.5°E; GCRMN Region: Indian Ocean
- Reef type: Atoll; Diver count: 4; Certification: AAUS Scientific Diver
- Objective: A (Assessment)
- No safety flags (AAUS certified, depth not specified as >18m)

#### Stage 2 — Reef Health Assessment
- DHW confirmed from NOAA CRW: 9.8 °C-weeks → **Alert Level 2** (mass bleaching / mortality likely)
- Live coral cover: 22% → Fair (below 30% healthy benchmark, above 17.6% global avg)
- Bleaching index: If 45% of Acropora colonies are bleached → CoralWatch index estimated 2.5–3.0 → **Moderately to Severely Bleached**
- Overall Reef Status: **Poor** (Alert Level 2 + 45% bleaching prevalence is acute crisis indicator)
- OHI Carbon Storage sub-score: ~73/100 (22% cover / 30% benchmark × 100)

#### Stage 3 — Emergency Recommendations
- Immediate action: Increase survey frequency to weekly
- Document: photograph bleaching extent with species resolution; submit to NOAA CRW bleaching field observation system
- NOAA CRW 4-month DHW forecast retrieved and reported
- Do NOT initiate outplanting during active bleaching (outplanting onto thermally stressed substrate leads to transplant mortality)
- Recommend: Set aside healthy Acropora genotypes in deep-water refugia if available
- Begin planning nursery rescue if DHW forecast shows cooling within 8 weeks

#### Report Format
- Professional Reef Health Scorecard (8 dimensions populated)
- Narrative: 2+ paragraphs interpreting DHW Alert Level 2 context
- Citations: Liu et al. (2006) for DHW interpretation; Hughes et al. (2017) for bleaching impact

### Pass Criteria

| Check | Pass Criterion |
|-------|---------------|
| DHW = 9.8 reported | NOAA CRW Alert Level 2 correctly identified |
| Emergency flag raised | Skill raises urgent response flag (not routine monitoring recommendation) |
| Outplanting NOT recommended during active bleaching | No outplanting recommended while DHW ≥ 8 |
| CoralWatch index estimated | Bleaching index < 3.0 (moderate to severe) |
| ≥ 2 citations | At least 2 peer-reviewed papers cited in assessment |
| Professional report format | Output is structured artifact, not chat reply |

---

## Scenario 2 — Community Coral Restoration Project (Philippines)

### Input

```
User: "We're starting a coral restoration project at Tubbataha Reef, Philippines (8.8°N, 119.8°E). 
Current Reef Check data (2025): live coral cover 31%, genera present: Acropora, Pocillopora, 
Porites, Goniastrea. Bleaching was observed on ~15% of Acropora colonies last year. No major 
bleaching event this year. We have 3 divers, PADI Advanced Open Water, bi-annual surveys, 
a basic underwater camera, and a small grant (moderate budget). Goal: restore Acropora to 40% 
of baseline. What restoration approach should we use and what KPIs should we target?"
```

### Expected Workflow Branch

Branch B (Full restoration: assessment + restoration + monitoring)

### Expected Outputs

#### Stage 1 — Profile Intake
- Site: Tubbataha Reef, Philippines; GPS 8.8°N, 119.8°E; GCRMN Region: East Asia / Coral Triangle
- Reef type: Atoll (Tubbataha is a reef atoll within the Sulu Sea)
- Budget: Moderate; Diver count: 3; Certification: PADI Advanced OW (≤30m); Bi-annual surveys
- Objective: B (Restoration planning)
- Safety flag: PADI Advanced OW allows surveys to 30m — appropriate for most Tubbataha depths

#### Stage 2 — Reef Health Assessment
- DHW: retrieve from NOAA CRW for 8.8°N, 119.8°E — expected ≤ Watch level (no current event stated)
- Live coral cover: 31% → **Good** (above 30% healthy benchmark)
- Bleaching 15% of Acropora → CoralWatch index: ~3.8–4.2 → **Mild to Mildly Stressed**
- Overall Reef Status: **Good** (high baseline; restoration will accelerate recovery of depleted Acropora)

#### Stage 3 — Restoration Planning
- Primary stressor: Mild thermal stress (15% Acropora bleaching) — not acute
- Decision tree path: Branching corals (Acropora) → DHW < Alert Level 1 → CRF Nursery Fragmentation
- Target species: Acropora millepora, A. hyacinthus, Pocillopora damicornis (also depleted based on prompt context)
- Thermal tolerance: Acropora = Sensitive; recommend collecting from deepest available donor colonies (more thermotolerant microhabitats)
- Nursery method: Rope/PVC tree nursery at 5–8m depth
- Fragment collection: from 10+ distinct donor colonies; ≤20% removal per colony
- Timeline: 9–12 months to outplanting size (7–15cm)
- Target restoration area: estimate from 40% Acropora baseline target
- Planting density: 4–5 fragments/m²
- Survival KPIs: 3-month 90%, 6-month 80%, 12-month post-outplant 60%

#### Stage 4 — Monitoring Protocol
- Survey method: Reef Check (bi-annual, 3 divers matches Moderate capacity tier)
- Statistical power: σ ≈ 10%, δ = 5%, n = 63 readings → approximately 2 transects per station; 4 stations → 8 transects (500+ readings): **Adequate power**
- Reporting: Bi-annual field report + annual synthesis; input to GCRMN database if enrolled

### Pass Criteria

| Check | Pass Criterion |
|-------|---------------|
| CRF nursery method selected | Nursery fragmentation recommended (not micro-fragmentation) for Acropora |
| ≥ 2 restoration citations | At least 2 peer-reviewed papers cited (e.g., Schopmeyer 2017 + one CTI/Philippines paper) |
| Survival KPIs stated numerically | 3/6/12/18-month targets all numerical |
| Power analysis shown | n = formula shown with inputs; result confirms adequate power for bi-annual design |
| Planting plan quantitative | Fragment count, density, timeline all numerical |
| GCRMN alignment noted | Data forms noted as Reef Check compatible |

---

## Scenario 3 — Long-Term MPA Monitoring Protocol Design (Coral Triangle)

### Input

```
User: "I manage a Marine Protected Area in the Bird's Head Seascape, West Papua, Indonesia 
(around 1°S, 131°E). We want to set up a long-term reef monitoring program. We have 5 trained 
divers with AAUS scientific diving certification, can survey quarterly, have a photo-quadrat 
frame, underwater cameras, and CoralWatch charts. No previous survey data — this is our first 
baseline. Budget is well-funded. MPA area: approximately 80 km² of reef. 
I just need a monitoring protocol — no restoration needed yet."
```

### Expected Workflow Branch

Branch C (Monitoring only)

### Expected Outputs

#### Stage 1 — Profile Intake
- Site: Bird's Head Seascape, West Papua; GPS ~1°S, 131°E; GCRMN Region: East Asia
- Team: 5 AAUS divers, quarterly, photo-quadrat frame + camera + CoralWatch
- Objective: C (Monitoring protocol)
- Budget: Well-funded; No existing data (baseline survey)
- Safety flags: None (AAUS certified)

#### Stage 2 — Monitoring Protocol
- Survey method: **GCRMN photo-quadrat + belt transect** (highest capacity tier: ≥4 divers, quarterly)
- Station count: 80 km² reef → minimum 10–12 permanent stations
- Depth strata: Shallow (0–6m), mid (6–18m), deep (18–30m) — minimum 2 stations per stratum
- Power analysis:
  - σ = 12% (use literature value for first baseline)
  - δ = 5%, α = 0.05, β = 0.20
  - n = 2 × (1.96 + 0.842)² × 144 / 25 = 2 × 7.85 × 5.76 = 90.5 → 91 transect readings
  - 91 / 50 points per transect ≈ 2 transects minimum per station
  - 12 stations × 2 transects = 24 transects = 1,200 point readings: **Well-powered (>80%)**
- First survey: Baseline — no prior data; all metrics recorded from scratch
- GPS station marking: table with 12 placeholder waypoints to be filled by field team
- Equipment list: photo-quadrat frame (already have), GCRMN point-count forms, CoralWatch charts (already have), temperature logger (add recommendation: 1 HOBO logger per depth stratum)
- GCRMN data portal submission recommended

#### Report Format
- Long-Term Monitoring Protocol document
- Statistical power calculation explicitly shown
- Data forms: Form A (benthic transect), Form B (CoralWatch), baseline-specific Form D (first survey orientation)
- Reporting: Quarterly field reports; Annual synthesis input to GCRMN

### Pass Criteria

| Check | Pass Criterion |
|-------|---------------|
| GCRMN photo-quadrat method selected | Highest-capacity method matched to 5-diver AAUS team |
| 10+ stations recommended | MPA size (80 km²) triggers large-site station count |
| Power calculation shown | Formula with σ=12%, δ=5%, result ≥ 91 readings stated |
| Power ≥ 80% confirmed | 24 transects × 50 readings = 1200 points achieves target |
| Baseline orientation noted | Skill notes this is first survey; no comparison possible until Survey 2 |
| GCRMN alignment stated | Data submission to GCRMN data portal recommended |
| Temperature logger recommended | HOBO or equivalent added to equipment list |

---

## Scenario 4 — Thesis Literature Review (Great Barrier Reef Thermal Tolerance)

### Input

```
User: "I'm a PhD student studying coral thermal tolerance evolution on the Great Barrier Reef. 
I need a comprehensive literature review covering: (1) Symbiodiniaceae thermal tolerance 
mechanisms, (2) assisted evolution / assisted gene flow approaches, (3) the latest on 
micro-fragmentation for massive corals. Can you compile a structured literature table with 
the most important papers and their key findings?"
```

### Expected Workflow Branch

Branch D (Literature review)

### Expected Outputs

#### Stage 1 — Profile Intake (abbreviated)
- Role: Graduate student; Objective: D (Literature review)
- No site coordinates required (desktop research query)
- No safety checks required

#### Stage 2 — Knowledge Query (SECOND-KNOWLEDGE-BRAIN.md + WebSearch)
- Check SECOND-KNOWLEDGE-BRAIN.md Section 2 for:
  - LaJeunesse et al. (2018) — Symbiodiniaceae taxonomy and thermal tolerance
  - Randall et al. (2020) — SECORE assisted gene flow
  - Forsman et al. (2015) — micro-fragmentation
  - Hughes et al. (2017, 2018) — GBR bleaching events
  - De'ath et al. (2009) — GBR calcification decline
- Supplement with WebSearch for papers post-2020 on: "Symbiodiniaceae thermal tolerance", "assisted gene flow coral", "coral micro-fragmentation 2022 2023 2024"
- Apply evidence hierarchy: prefer Systematic Reviews and RCTs over single observational studies

#### Expected Literature Table
Minimum 10 papers across 3 topic areas, formatted as:

| Title | Authors | Year | Venue | DOI | Key Finding | Evidence Tier | Topic Area |
|-------|---------|------|-------|-----|------------|--------------|-----------|
| Symbiodiniaceae… | LaJeunesse et al. | 2018 | Science | 10.1126/science.aar3316 | Revised Symbiodiniaceae taxonomy, thermal tolerance varies by clade | RCT/Experimental | 1 |
| [9+ more entries] | ... | ... | ... | ... | ... | ... | ... |

### Pass Criteria

| Check | Pass Criterion |
|-------|---------------|
| SECOND-KNOWLEDGE-BRAIN.md checked first | Skill explicitly checks internal knowledge before web search |
| ≥ 10 papers in table | Table has minimum 10 rows across all 3 topic areas |
| All DOIs present | No paper in the table is missing a DOI |
| Evidence tier labeled | Each paper labeled with evidence tier |
| Topic areas covered | All 3 user-specified topics (Symbiodiniaceae, assisted evolution, micro-fragmentation) have ≥ 2 papers each |
| GBR context maintained | Papers explicitly linked to GBR context where possible |
| Post-2020 papers included | At least 3 papers published after 2020 (requires WebSearch supplement) |

---

## Scenario 5 — Post-Bleaching Recovery Assessment (Red Sea)

### Input

```
User: "We are reef ecologists at a research station on the Saudi Arabian Red Sea coast 
(22°N, 38.8°E). Following the 2024 bleaching event (DHW peaked at 14.2 °C-weeks in August), 
we conducted a recovery survey in February 2026. Results: live coral cover 8%, recent 
mortality 35% of surveyed area (white skeleton visible), CoralWatch mean score 4.1 (recovering). 
We have existing Reef Check data from 2022 showing 28% live coral cover pre-bleaching. 
Team: 2 divers, PADI Open Water, annual survey capacity, basic equipment. 
We need: an assessment of recovery trajectory, and a long-term monitoring plan."
```

### Expected Workflow Branch

Branch B (full workflow: assessment + restoration + monitoring)

### Expected Outputs

#### Stage 1 — Profile Intake
- Site: Red Sea (Saudi Arabia); GPS 22°N, 38.8°E; GCRMN Region: Red Sea & Gulf of Aden
- Team: 2 divers, PADI OW (≤18m); Annual surveys; Basic equipment
- Existing data: 2022 Reef Check (28% cover pre-bleaching)
- Safety flag: PADI Open Water limits surveys to 18m maximum — depths below 18m require Advanced OW

#### Stage 2 — Reef Health Assessment
- DHW context: Peak 14.2 °C-weeks in August 2024 → Extreme bleaching event (DHW >12 threshold)
- Current cover: 8% → Reef Status: **Critical** (below even the 10% crisis threshold)
- Cover change: 28% (2022) → 8% (Feb 2026) = **−20 percentage points loss** = 71% relative decline
- CoralWatch 4.1 = Mild stress (corals recovering but not fully healthy)
- Recent mortality 35% = severe acute mortality event
- Recovery trajectory: Early-stage recovery (CoralWatch 4.1 suggests some zooxanthellae re-uptake); cover increase from 8% to 20% may require 5–10 years under normal conditions
- OHI Carbon Storage sub-score: 8/30 × 100 = ~27/100 → Very Poor

#### Stage 3 — Restoration Planning
- Restoration viability: DHW 14.2 is extreme; if recurrence risk is high (check NOAA CRW historical for this site), flag that active restoration may be undermined by future events
- With 2 PADI OW divers and basic equipment: recommend limiting to CRF-style rope nursery at 5–10m depth (within 18m certification limit)
- Species: Surviving Porites and Goniastrea colonies (thermotolerant) preferred as donor colonies
- DO NOT collect fragments from still-recovering colonies (white skeleton visible); wait until CoralWatch ≥ 4.5 before collecting
- Recommended: Contact SECORE or regional coral genetics lab for thermotolerant genotype sourcing given extreme bleaching history

#### Stage 4 — Monitoring Protocol
- Team capacity: Low tier (2 divers, annual)
- Method: CoralWatch bleaching index + cover estimate (basic)
- Under-powered flag: Annual surveys by 2 divers are insufficient to detect Δ5% cover change at 80% power; recommend recruiting additional volunteer divers or partnering with a university
- Minimum viable monitoring: Annual CoralWatch + photo-quadrat at 3 permanent stations
- Trigger-based: Any new NOAA Alert Level 2 → immediate survey
- First priority: Document recovery trajectory (compare 2025, 2026, 2027 annually) before investing in restoration

### Pass Criteria

| Check | Pass Criterion |
|-------|---------------|
| Pre-bleaching vs. post comparison | 28% → 8% cover loss (-20pp, 71% relative) stated explicitly |
| DHW 14.2 categorized correctly | Labeled as extreme event (>DHW 12 threshold) |
| Reef Status = Critical | 8% cover + 35% recent mortality + DHW 14.2 → Critical rating |
| Fragment collection timing warning | Skill explicitly says do NOT collect from recovering colonies (white skeleton visible) |
| Under-powered monitoring flag | 2-diver annual survey flagged as under-powered; supplement recommendation given |
| Safety flag for 18m limit | PADI OW depth limit (18m) flagged in intake; restoration limited to ≤18m depth |
| Recovery timeline realistic | 5–10 year recovery timeline cited from peer-reviewed literature |
| SECORE / thermotolerant genotype recommendation | Given extreme thermal history, skill recommends thermotolerant genotype sourcing |

---

## Test Execution Log

| Scenario | Date Run | Result | Notes |
|---------|---------|--------|-------|
| 1 — Bleaching Emergency (Maldives) | TBD | Pending | — |
| 2 — Community Restoration (Philippines) | TBD | Pending | — |
| 3 — MPA Monitoring Protocol (West Papua) | TBD | Pending | — |
| 4 — Thesis Literature Review (GBR) | TBD | Pending | — |
| 5 — Post-Bleaching Recovery (Red Sea) | TBD | Pending | — |

All 5 scenarios must achieve Pass on ALL criteria before Phase 4 is marked complete.
