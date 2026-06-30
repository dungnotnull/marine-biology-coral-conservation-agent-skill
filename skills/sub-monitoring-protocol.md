---
name: marine-biology-coral-conservation/sub-monitoring-protocol
description: Design a statistically powered long-term reef monitoring protocol — sampling station layout, survey method selection, power analysis, data recording forms, and reporting schedule aligned with Reef Check and GCRMN standards.
---

## Purpose

Design a statistically valid, operationally feasible long-term reef monitoring protocol that can detect ecologically meaningful change over time. The protocol must be matched to the team's actual capacity (number of divers, survey frequency, equipment), statistically powered to detect the target minimum detectable change (MDC) with 80% probability, and aligned with GCRMN and Reef Check international standards to enable data sharing with global networks.

This sub-skill bridges the gap between what a team wants to monitor and what they can realistically achieve — avoiding common failures such as under-powered sampling designs, inconsistent methodology between survey rounds, and data collection without a corresponding analysis plan.

---

## Inputs

- **Structured Site Profile** from `sub-profile-intake` (team size, diver certification, survey frequency, equipment, budget)
- **Reef Health Scorecard** from `sub-reef-assessment` (coral cover %, H', substrate composition — needed for statistical power inputs)
- **Restoration Strategy** from `sub-restoration-planner` (if applicable — defines what restoration outcomes need monitoring)
- **User's monitoring objectives** (what change do they want to detect? What reporting is required?)

---

## Workflow

### Step 1 — Define Monitoring Objectives

**1a.** Clarify what the user needs to detect and report:

| Objective Type | Example | Primary Metric |
|---------------|---------|---------------|
| Status assessment | "Is this reef getting better or worse?" | Live coral cover % trend |
| Restoration evaluation | "Did our outplanting work?" | Transplant survival rate + growth rate |
| Bleaching impact | "How much coral died in the bleaching event?" | Coral cover change before/after |
| Biodiversity conservation | "Are we maintaining species diversity?" | Shannon H' trend |
| Fishing impact | "Is no-take zone protection working?" | Fish biomass trend |
| Water quality compliance | "Are nutrient levels within limits?" | Chlorophyll-a, turbidity trend |

**1b.** Define the Minimum Detectable Change (MDC) — the smallest change that is biologically meaningful and should trigger a management response:
- Standard MDC for coral cover: **Δ5%** (5 percentage points) — changes below this level may be within natural variability
- MDC for fish biomass: **Δ20%** of baseline
- MDC for bleaching prevalence: **Δ10%** of surveyed colonies

If user has different requirements, document their MDC and use in power calculations.

---

### Step 2 — Select Survey Method Based on Team Capacity

Apply capacity-based method selector:

| Team Capacity | Recommended Method | Standard | Data Quality |
|--------------|-------------------|----------|-------------|
| ≥4 trained divers, quarterly surveys, camera + quadrat frame | GCRMN photo-quadrat + belt transect | GCRMN (2009) | High |
| 2–3 divers, bi-annual surveys, basic underwater equipment | Reef Check standard transects | Reef Check (2020) | Standard |
| 1–2 divers, annual surveys, minimal equipment | CoralWatch bleaching index + cover estimate | CoralWatch (2022) | Basic |
| Drone/ROV available | Aerial / ROV photogrammetry + AI classification | ReefCloud / Allen Coral Atlas standard | Variable, improving |

**Important:** If team capacity is Low (1–2 divers, annual), note that the monitoring program will have limited statistical power and results should be interpreted with caution. Recommend recruiting additional trained volunteers or partnering with a university diving club.

---

### Step 3 — Sampling Station Design

**3a.** Determine minimum number of permanent monitoring stations:

Run power calculation (Step 4) BEFORE finalizing station count.

Initial guidance:
- For a single reef site (< 5 km² reef area): minimum 4–6 permanent stations
- For a large reef system (> 20 km² reef area): minimum 8–12 stations
- For an MPA network: minimum 2–4 stations per zone (no-take, restricted-use, unprotected control)

**3b.** Station placement principles:
- Stratify by depth: shallow (0–6m), mid (6–18m), deep (18–30m) — include all strata present at site
- Stratify by exposure: windward (high energy) vs. leeward (low energy) — if applicable
- Include reference/control stations: select 1–2 stations in areas NOT subject to active restoration, to distinguish natural variability from restoration effects
- Avoid transient features: permanent stations should not be placed on sand patches or rubble fields that shift seasonally

**3c.** GPS marking of permanent stations:
- Drop a permanent marker buoy at each station (mooring weight or concrete block with surface float)
- Record GPS to ±5m accuracy
- Photograph station from 3 compass angles for relocation in future surveys

**3d.** Station layout template:

```
MONITORING STATIONS — [Site Name]

Station | Lat | Long | Depth (m) | Zone | Notes
--------|-----|------|-----------|------|------
S-01    | XX.XXXX | YY.YYYY | 6 | Windward shallow | Control (no restoration)
S-02    | XX.XXXX | YY.YYYY | 12 | Windward mid | Near nursery
S-03    | XX.XXXX | YY.YYYY | 18 | Windward deep | Reference
...
```

---

### Step 4 — Statistical Power Analysis

**4a.** Run the two-sample t-test power calculation for detecting change in coral cover (primary outcome):

**Formula:**
```
n = 2 × (Zα/2 + Zβ)² × σ² / δ²
```

Where:
- n = minimum number of transects required per survey
- Zα/2 = 1.96 (for α = 0.05, two-tailed — the probability of falsely detecting a change)
- Zβ = 0.842 (for β = 0.20, i.e., 80% power — the probability of correctly detecting a real change)
- σ = standard deviation of coral cover across transects (use Reef Health Scorecard data; if unavailable, use literature value σ ≈ 10–12% from GCRMN 2020)
- δ = minimum detectable change (MDC) = 5% (default)

**Example calculation (σ = 10%, δ = 5%):**
```
n = 2 × (1.96 + 0.842)² × (10)² / (5)²
n = 2 × 7.85 × 100 / 25
n = 2 × 7.85 × 4
n = 62.8 → round up to n = 63 transect readings

However, if using 50m transects and recording 50 points per transect:
  63 / 50 = 1.26 → minimum 2 transects per station
  With 6 stations × 2 transects = 12 transects total → 600 point readings (sufficient)
```

**4b.** Interpret power calculation result:
- State the minimum number of transects required
- State the minimum number of permanent stations required to achieve this
- If team capacity cannot achieve minimum n: note under-powered status and recommend either increasing frequency or recruiting additional divers

**4c.** For secondary outcomes (fish biomass, H'):
- Fish biomass: use biomass variance from published Caribbean/Indo-Pacific studies (typically σ ≈ 30–50% of mean) — apply same formula
- H': typically less variable (σ ≈ 0.3 H' units) — apply same formula with δ = 0.5 H'

---

### Step 5 — Data Recording Forms

Produce standardized data recording templates:

#### Form A — Reef Check Benthic Transect Sheet

```
REEF CHECK BENTHIC TRANSECT
Site: ___________  Station: ___  Transect #: ___  Date: ___________
Observer: ___________  Depth: ___ m  Visibility: ___ m
Method: [Belt Transect / Intercept Transect]  Transect Length: 50m

BENTHIC COVER (record substrate type directly below line tape at 0.5m intervals)
0.5m: [HC/SC/CA/TA/MA/R/S/SI/O/BL]   1.0m: ___   1.5m: ___   2.0m: ___
... [continue to 50m]

SUMMARY
  Live Hard Coral (HC): ___ / 100 points = ___%
  Soft Coral (SC): ___ / 100 = ___%
  Bleached Coral (BL): ___ / 100 = ___%
  Macroalgae (MA): ___ / 100 = ___%
  Rubble (R): ___ / 100 = ___%
  Sand/Silt (S/SI): ___ / 100 = ___%
  Other (O): ___ / 100 = ___%

CORAL BLEACHING (circle extent):  None / <10% / 10–50% / >50% / Fully bleached
WATER TEMP: ___ °C      PHOTOS TAKEN: Yes / No
```

#### Form B — CoralWatch Bleaching Survey Sheet

```
CORALWATCH BLEACHING SURVEY
Site: ___________  Station: ___  Date: ___________  Observer: ___________
Depth: ___ m  Current CoralWatch Chart used: Yes / No (if No, explain)

COLONY SCORES (record: Colony ID | Genus | Score 1–6 | Notes)
C01: _______ / _______ / _______ / _______
C02: _______ / _______ / _______ / _______
... (minimum 20 colonies)

BLEACHING INDEX = Sum of scores / Number of colonies = ___ / ___
STATUS: [5.0–6.0 Healthy | 4.0–4.9 Mild | 3.0–3.9 Moderate | 2.0–2.9 Severe | 1.0–1.9 Fully Bleached]
```

#### Form C — Restoration Monitoring Sheet (Post-Outplanting)

```
RESTORATION MONITORING SURVEY
Site: ___________  Station: ___  Outplanting Date: ___________  Survey Date: ___________
Observer: ___________  Depth: ___ m

TRANSPLANT STATUS (record each labeled fragment):
Fragment ID | Species | Size at outplant (cm) | Current size (cm) | Status | Notes
F001        | _______ | ___                   | ___               | [Alive/Dead/Missing/Bleached] | ___
...

SUMMARY
  Total fragments surveyed: ___
  Alive: ___  Dead: ___  Missing: ___  Bleached (alive): ___
  Survival rate (%): ___
  Average growth (cm/month): ___
  Bleaching prevalence (%): ___

PHOTOS: [Fragment photos taken? Y/N] [Station overview photo? Y/N]
```

---

### Step 6 — Reporting Schedule

Define the reporting cadence:

**Field Reports (each survey event):**
- Complete data forms (A, B, C as applicable)
- Photograph station overview and any notable changes
- Enter data into Reef Check online database (if enrolled: reefcheck.org/data) or GCRMN data portal
- Produce 1-page summary: survey date, station, key metrics, notable observations

**Quarterly Synthesis Report (if surveying quarterly):**
- Compare current quarter to same quarter previous year (avoids seasonal bias)
- Trend plot: coral cover %, bleaching index, H' across all stations
- Flag any stations showing significant change (>MDC)
- Report to MPA manager / NGO / funding body

**Annual Report (mandatory):**
- Full analysis: all stations, all metrics, year-on-year trend
- DHW context for the year (NOAA CRW annual bleaching summary)
- Restoration progress (if applicable): survival rates, growth rates, Phase 1/2 milestones
- Management recommendations based on data

**Trigger-Based Reports (event-driven):**
- NOAA CRW Alert Level 2 triggered: survey within 2 weeks to document bleaching onset
- Mass mortality event (>30% cover loss in any station): immediate report to GCRMN, national authority
- Disease outbreak detected: report to NOAA CRCP disease reporting system within 48 hours

---

### Step 7 — Equipment List

| Equipment | Purpose | Low-Cost Alternative |
|-----------|---------|---------------------|
| 50m transect tape × 2 | Belt transect / Reef Check | Thin paracord with 0.5m markers |
| Underwater data slate + pencil | Data recording | Waterproof paper (Z-Rite) + pencil |
| Underwater camera | Photo documentation | GoPro Hero (affordable, wide-angle) |
| Photo-quadrat frame (50cm × 50cm) | Benthic photo-quadrat | PVC pipe frame (DIY, < $10) |
| CoralWatch Coral Health Chart | Bleaching assessment | Printed waterproof laminated card |
| Fish ID guide (regional) | Fish identification | REEF fish ID card (laminated) |
| Depth gauge + compass | Navigation, depth recording | BCD console with depth gauge |
| Temperature logger (HOBO U22 or similar) | Continuous SST record | Less accurate alternatives available but not recommended |
| GPS unit (surface) | Station marking | Smartphone GPS app (Garmin Explore) |
| Surface marker buoy (SMB) | Dive safety + station marking | Standard DSMBs |
| Permanent mooring anchors | Station marking | HDPE concrete blocks with stainless eye bolt |

---

## Outputs

**Long-Term Monitoring Protocol** containing:
1. Monitoring objectives and MDC definition
2. Survey method selection and justification
3. Sampling station design (layout table with GPS coordinates)
4. Statistical power analysis (formula, inputs, calculation, result — minimum n)
5. Data recording forms (A, B, C as applicable)
6. Reporting schedule (field reports, quarterly, annual, trigger-based)
7. Equipment list with low-cost alternatives
8. Data management guidance (where to submit, how to store)

---

## Quality Gate

| Check | Criterion |
|-------|-----------|
| MDC defined | Minimum Detectable Change stated numerically (default Δ5% coral cover) |
| Power calculation shown | Formula, inputs (σ, δ, α, β), and result (minimum n) all explicit |
| Power ≥ 80% | Monitoring design achieves ≥80% statistical power at the stated MDC |
| Station count justified | Number of stations derived from power calculation and stratification logic |
| Method matches capacity | Survey method is feasible for team's stated diver count, certification, and frequency |
| Data forms complete | At least Form A (benthic transect) produced; Form C if restoration is being monitored |
| Reporting schedule present | At least quarterly field report + annual report cadence defined |
| Trigger-based events defined | Bleaching alert trigger + mass mortality trigger documented |
| GCRMN / Reef Check alignment | Data forms noted as compatible with Reef Check database or GCRMN data portal |
