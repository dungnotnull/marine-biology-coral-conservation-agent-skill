---
name: marine-biology-coral-conservation/sub-restoration-planner
description: Design an evidence-based coral restoration strategy — species selection with thermal tolerance ratings, propagation method selection (nursery/micro-fragmentation/biorock/assisted gene flow), planting plan, and survival KPIs — all justified by peer-reviewed marine science.
---

## Purpose

Design a site-appropriate, evidence-based coral restoration strategy that accounts for the reef's current health status, dominant stressors, available species, depth, and team resources. This sub-skill applies a structured decision tree (not fixed recommendations) because restoration methods that succeed in the Caribbean often fail in the Indo-Pacific and vice versa, and method choice depends critically on the site's thermal stress history, species assemblage, substrate condition, and available infrastructure.

Every method recommendation must be supported by at least two peer-reviewed citations. Survival rate KPIs must be grounded in published literature, not aspirational targets.

---

## Inputs

- **Reef Health Scorecard** from `sub-reef-assessment` (coral cover %, bleaching index, OHI sub-scores, DHW history, substrate condition)
- **Structured Site Profile** from `sub-profile-intake` (depth, species present, team capacity, budget tier, equipment)
- **User's restoration objectives** (target coverage increase, timeline, budget constraints)

---

## Workflow

### Step 1 — Threat Profile Analysis

Using the Reef Health Scorecard and Site Profile, identify the primary stressors driving reef degradation:

| Stressor | Indicators | Restoration Implication |
|---------|-----------|------------------------|
| Thermal stress (bleaching) | DHW ≥ 4, CoralWatch <3.0 | Prioritize thermally tolerant species or assisted gene flow |
| Ocean acidification | Ωarag < 2.5 | Consider biorock to enhance carbonate accretion; limit branching corals |
| Crown-of-thorns starfish (COTS) | >0.1 COTS per 100m² (Reef Check) | COTS removal program must precede outplanting |
| Nutrient pollution | Macroalgae >25%, turbidity high | Address land-based nutrient sources; algae removal before planting |
| Physical damage (cyclone/anchor/blast) | High rubble %, broken colonies | Substrate stabilization before outplanting |
| Fishing pressure | Low fish biomass, indicator species absent | MPA enforcement parallel to restoration |
| Disease (SCTLD, etc.) | Tissue loss on multiple species | Quarantine protocol; research-grade intervention only |

Rank stressors by severity (primary / secondary / tertiary). If primary stressor cannot be controlled (e.g., chronic thermal stress in a DHW-persistent zone), flag this as a Restoration Viability Risk and consider whether active restoration is appropriate before passive recovery.

**Restoration Viability Threshold:** If DHW has exceeded 8°C-weeks in more than 3 of the past 10 years AND current coral cover is <5%, active restoration alone is unlikely to succeed without concurrent climate mitigation. Document this clearly and recommend building thermal tolerance programs alongside traditional restoration.

---

### Step 2 — Target Species Selection

**2a.** Identify which coral genera/species are depleted at the site (from Reef Check genera survey) and which are still present as potential donor colonies.

**2b.** For each candidate target species, retrieve thermal tolerance data:
- Query SECOND-KNOWLEDGE-BRAIN.md first
- If not found, WebSearch NOAA CoRTAD database and LaJeunesse et al. (2018) Symbiodiniaceae taxonomy
- Rate each species: Thermally Sensitive / Moderate Tolerance / Thermally Tolerant

**2c.** Apply species selection criteria:

| Criterion | Guidance |
|-----------|---------|
| Functional importance | Prioritize framework-building species (Acropora spp., Orbicella spp., Porites spp.) |
| Thermal tolerance | In DHW-prone sites, favor Porites lobata, Platygyra spp., Goniastrea spp. over Acropora where possible |
| IUCN status | Flag Critically Endangered (Acropora cervicornis, A. palmata) — may require permits |
| Propagation suitability | Branching species → nursery; massive/encrusting → micro-fragmentation |
| Local availability | Prioritize species with healthy donor colonies present at or near the site |
| Genetic diversity | Aim for ≥10 genetically distinct donor colonies per species (prevents inbreeding depression) |

**2d.** Produce target species table:

| Species | IUCN Status | Thermal Tolerance | Propagation Method | Donor Availability | Priority |
|---------|-------------|------------------|--------------------|-------------------|---------|
| [Species 1] | [status] | [tier] | [method] | [yes/no/limited] | [1/2/3] |

---

### Step 3 — Propagation Method Decision Tree

Apply the following decision tree to select the primary restoration method:

```
START
│
├── Is substrate stable? (rubble <15%, minimal surge)
│   ├── NO → Biorock substrate stabilization FIRST, then re-evaluate
│   └── YES → Continue
│
├── Is Ωarag < 1.8 (severe acidification)?
│   ├── YES → Biorock (mineral accretion improves calcification in low-pH conditions)
│   └── NO → Continue
│
├── Is DHW ≥ 8 in ≥3 of past 10 years (chronic thermal stress)?
│   ├── YES → SECORE Assisted Gene Flow (thermotolerant genotype development)
│   │         AND parallel nursery program with most thermotolerant available genotypes
│   └── NO → Continue
│
├── Are target species primarily BRANCHING corals (Acropora, Pocillopora)?
│   ├── YES → CRF Nursery Fragmentation Protocol
│   │         (PVC tree nursery, 2–5cm nubbins, 4–8m depth, 6–9 months to outplanting size)
│   └── NO → Continue
│
├── Are target species primarily MASSIVE/ENCRUSTING (Orbicella, Diploria, Porites)?
│   ├── YES → Micro-Fragmentation Protocol (Mote Marine / Vaughan method)
│   │         (2–5mm fragments, ex-situ tank culture, wound-response accelerated growth)
│   └── NO → Foliose/plate corals → specialized tying/netting methods (cite applicable papers)
│
└── MULTI-SPECIES SITE → Combine: nursery for branching + micro-fragmentation for massive
```

For each selected method, perform:
- WebSearch for the 2 most recent peer-reviewed papers validating the method at comparable sites
- Note: survival rate range from published literature (do not invent)
- Note: known failure modes and how to mitigate them

---

### Step 4 — Method Specification

Provide detailed specifications for each recommended method:

#### Option A: CRF Nursery Fragmentation Protocol

**Setup:**
- PVC pipe trees (1.5m height, 6–8 branches per tree, suspended at 4–8m depth on monofilament)
- Alternatively: rope/mesh nursery for lower-current sites
- Minimum nursery depth: 3m (to reduce UV stress and surge)

**Fragment collection:**
- Collect 5–10cm branches from minimum 10 genetically distinct donor colonies per species
- Never remove >20% of any donor colony's tissue
- Transport to nursery in coolers with site water within 2 hours

**Fragment size and attachment:**
- Cut to 2–5cm nubbins using bone cutters or underwater scissors
- Attach with cable ties or monofilament; space ≥5cm between fragments
- Label with batch ID and donor colony ID

**Growth targets and monitoring:**
- Monthly measurement: length (mm/month); standard growth ≥ 10mm/month for Acropora
- Monthly survival count: target ≥ 90% at 3 months, ≥ 80% at 6 months
- Outplanting size: 7–15cm (6–12 months typical)

**Outplanting:**
- Substrate cleared of algae within 30cm of planting point
- Attach with epoxy putty (e.g., Z-Spar Splash Zone A-788), cement, or cable ties
- Planting density: 4–6 fragments/m² for Acropora; 2–3/m² for Pocillopora (species-specific)

Source: Schopmeyer et al. (2017) DOI: 10.1371/journal.pone.0169966; CRF Restoration Manual (2020)

---

#### Option B: Micro-Fragmentation Protocol (Mote Marine)

**Equipment required:**
- Tile saw (diamond blade), or Dremel rotary tool with diamond bit — for 2–5mm cuts
- Flow-through seawater aquarium tanks (≥ 200L per culture unit)
- LED grow lights (PAR 150–300 µmol photons m⁻² s⁻¹)

**Process:**
- Collect 10–15cm parent fragment from donor colony
- Cut into 2–5mm fragments under seawater to prevent desiccation
- Place in sterile culture tank at site-ambient temperature (±0.5°C)
- Change 20% water volume daily for first 2 weeks; weekly thereafter
- Growth rate: 25–40× faster than standard fragmentation (Forsman et al. 2015)
- Outplanting size: 2–4cm achievable in 3–6 months (vs. 12+ months for standard methods)

**Applicable species:** Orbicella faveolata, Diploria labyrinthiformis, Montastraea cavernosa, Porites lobata, Platygyra spp.

Source: Forsman et al. (2015) DOI: 10.1371/journal.pone.0133056; Page et al. (2018) DOI: 10.1016/j.jembe.2017.12.014

---

#### Option C: SECORE Assisted Gene Flow / Sexual Propagation

**Seasonal timing:** Must align with mass spawning event (1–3 nights after full moon in spawning season — species and hemisphere-specific)

**Process:**
- Deploy collection nets over target spawning colonies
- Collect gamete bundles (sperm + eggs) from multiple genetically diverse parent colonies
- Cross-fertilize pairs in 20L buckets; maintain at ambient temperature, oxygenated
- Allow 48–72 hours for larval development
- Apply larvae to SECORE Substrate Units (SU) for settlement
- Culture settled recruits for 6–8 months before outplanting

**Advantages:** Genetic diversity; novel thermotolerant phenotypes from cross-breeding
**Limitations:** Highly seasonal; requires trained personnel; lower survival than fragmentation in early stages

Source: Randall et al. (2020) DOI: 10.1007/s00338-020-01893-6; SECORE International Technical Manual

---

#### Option D: Biorock (Mineral Accretion Technology)

**Setup:**
- Steel frame (any shape) installed on target reef substrate
- Connect to low-voltage DC power supply (1.2–12V): solar panel or grid
- Mineral accretion begins within weeks

**Specifications:**
- Current density: 1–2 A/m² of cathode surface
- Growth rate enhancement: 2–6× normal coral growth
- Survival benefit: corals attached to Biorock show 16–50% higher survival during bleaching events (Goreau & Hilbertz 2005)

**Best applications:**
- Heavily degraded substrates (rubble, silt, low pH zones)
- Warm-water environments where thermal stress is chronic
- Coastal protection in combination with coral growth

Source: Goreau & Hilbertz (2005). World Resource Review, 17(3), 375–409

---

### Step 5 — Planting Plan

Produce a quantitative planting plan for the site:

```
PLANTING PLAN — [Site Name]

TARGET AREA:      [X] m²
TARGET SPECIES:   [species list]
PRIMARY METHOD:   [method]

PRODUCTION REQUIREMENTS
  Fragments needed: [target area × planting density = N]
  Donor colonies required: [N fragments / 20% max removal = donor count]
  Nursery capacity needed: [N fragments × 1.25 buffer = nursery size]
  Culture period: [X months]
  
TIMELINE
  Month 0:   Nursery setup; donor colony collection
  Month 1–3: Fragment establishment; monthly survival counts
  Month 3–6: Growth monitoring; record growth rate (mm/month)
  Month 6–9: Outplanting-ready fragments (7–15cm); substrate preparation
  Month 9:   First outplanting event (Phase 1: [X] fragments)
  Month 12:  Second outplanting event (Phase 2: [X] fragments)
  Month 15:  18-month post-outplanting survival survey

PLANTING DENSITY
  [Species A]: [X] fragments/m²
  [Species B]: [X] fragments/m²

SURVIVAL KPIS
  3-month nursery survival:  ≥ 90%
  6-month nursery survival:  ≥ 80%
  6-month post-outplant:     ≥ 70%
  12-month post-outplant:    ≥ 60%
  18-month post-outplant:    ≥ 50% (target: fragments reach reproductive size)
```

---

### Step 6 — Citations and Evidence Summary

For each recommendation, produce a citation block:

```
METHOD CITATIONS — [Method Name]
1. [Author et al. (Year). Title. Journal. DOI: ...]
   Key finding: [1 sentence relevant to this site's conditions]
   Evidence tier: [Systematic Review / RCT / Observational / Expert Protocol]

2. [Author et al. (Year). Title. Journal. DOI: ...]
   Key finding: [1 sentence]
   Evidence tier: [tier]
```

Minimum 2 citations per method selected. If only 1 citation found: perform additional WebSearch before proceeding.

---

## Outputs

**Restoration Strategy Document** containing:
1. Threat profile analysis (stressors ranked by severity)
2. Target species table (IUCN status, thermal tolerance, priority)
3. Propagation method selection with decision tree path documented
4. Detailed method specifications (whichever methods were selected)
5. Quantitative planting plan (fragments needed, timeline, density)
6. 18-month survival KPI table
7. Method citations (≥ 2 per method, with evidence tier)
8. Risk log (failure modes and mitigations)

---

## Quality Gate

| Check | Criterion |
|-------|-----------|
| Threat analysis complete | Primary stressor identified and ranked; restoration viability flagged if DHW ≥ 8 in ≥3/10 years |
| Target species listed | All target species have: IUCN status, thermal tolerance tier, donor availability |
| Method decision tree documented | Decision path through tree shown explicitly (not just method name) |
| Citations present | ≥ 2 peer-reviewed citations per method; all with DOI |
| Evidence tier stated | Each citation labeled with evidence tier |
| Planting plan quantitative | Fragment count, nursery size, timeline, planting density all calculated numerically |
| Survival KPIs from literature | No aspirational KPIs — all targets cite published survival rate ranges |
| Restoration viability flag | If primary stressor uncontrollable, flag documented with explanation |
