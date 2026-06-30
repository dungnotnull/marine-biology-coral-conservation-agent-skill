# CLAUDE.md — Skill #238: Marine Biology Research & Coral Reef Conservation Support

## Skill Identity

- **Skill ID:** 238
- **Slug:** `marine-biology-coral-conservation`
- **Title:** Marine Biology Research & Coral Reef Conservation Support
- **Cluster:** `science-industry`
- **Current Phase:** Complete — All Phases 0-5 Validated
- **Source Idea:** #238 from `D:\Dungchan\skill_adv\ideas.md`

---

## Problem This Skill Solves

Scientific divers, marine biologists, reef managers, and conservation practitioners operate in environments where up-to-date ocean data — sea surface temperatures, acidification levels, bleaching alerts, and restoration research — is fragmented across dozens of international monitoring networks, academic journals, and governmental agencies. Without a structured harness to aggregate, interpret, and apply this knowledge, critical conservation decisions are made on outdated or incomplete data. This skill provides a unified, research-first workflow that guides users through standardized reef health assessment (Reef Check / GCRMN protocols), evidence-based coral restoration planning, long-term monitoring protocol design, and automatic knowledge updates from NOAA, AIMS, IOC-UNESCO, and leading marine science journals — giving field practitioners access to world-class oceanographic intelligence at every dive.

---

## Harness Flow Summary

```
/marine-biology-coral-conservation
  Step 1 → sub-profile-intake         : Collect site location, diver credentials, objectives, equipment
  Step 2 → sub-reef-assessment        : Systematic reef health survey using Reef Check / GCRMN / CoralWatch
  Step 3 → sub-restoration-planner    : Design species-appropriate coral restoration strategy
  Step 4 → sub-monitoring-protocol    : Build statistically powered long-term monitoring plan
  Step 5 → [Quality Gate Review]      : Validate all outputs against peer-reviewed standards
  Step 6 → Main Skill                 : Synthesize final Marine Biology Research & Conservation Report
```

---

## Sub-Skills

| File | Description |
|------|-------------|
| `skills/sub-profile-intake.md` | Gather user profile: reef site, GPS coordinates, dive credentials, research objectives, available equipment, and existing baseline data |
| `skills/sub-reef-assessment.md` | Conduct systematic reef health assessment: coral cover %, bleaching index, species diversity, DHW analysis, substrate composition — Reef Check / GCRMN / CoralWatch methodology |
| `skills/sub-restoration-planner.md` | Design coral restoration strategy: species selection, propagation method (nursery, micro-fragmentation, biorock, assisted gene flow), site preparation, planting density, and survival KPIs |
| `skills/sub-monitoring-protocol.md` | Design long-term reef monitoring protocol with temporal frequency, sampling stations, data forms, statistical power calculations, and reporting cadence |

### Reusable Sub-Skills

This skill contains the following sub-skills that may be reused by other skills in the `science-industry` cluster:

**sub-evaluation-framework-selector**
- **Purpose:** Select appropriate evaluation framework based on team capacity and equipment
- **Implementation:** Embedded in `sub-reef-assessment`
- **Pattern:** Capacity-tier decision tree (High → Most Precise, Medium → Standard, Low → Basic)
- **Reusability:** ⭐⭐⭐⭐⭐ — Applicable to any science/engineering audit requiring framework selection
- **Potential Adopters:** water-quality-monitoring, forest-ecology-assessment, soil-science-audit, air-quality-measurement, industrial-hygiene

**sub-scoring-engine**
- **Purpose:** Generate quantitative scorecard with benchmarks and composite status
- **Implementation:** Embedded in `sub-reef-assessment`
- **Pattern:** Multi-dimensional scoring with weighted composite and status mapping
- **Reusability:** ⭐⭐⭐⭐⭐ — Applicable to any quantitative assessment requiring scorecard output
- **Potential Adopters:** ecosystem-health-assessment, sustainability-scoring, compliance-audit, risk-assessment

**sub-improvement-roadmap**
- **Purpose:** Generate evidence-based strategy with timeline, KPIs, and citations
- **Implementation:** Embedded in `sub-restoration-planner`
- **Pattern:** Threat analysis → prioritization → method selection → resource planning → KPI definition
- **Reusability:** ⭐⭐⭐⭐ — Applicable to strategy and planning skills
- **Potential Adopters:** habitat-restoration, conservation-planning, sustainability-strategy

**Cross-Cluster: sub-safety-screener** (from health-wellness)
- **Purpose:** Screen activity parameters against safety standards and flag issues
- **Implementation:** Embedded in `sub-profile-intake`
- **Pattern:** Multi-check safety screener with severity levels and standard references
- **Reusability:** ⭐⭐⭐⭐⭐ — Applicable across all clusters involving physical activities
- **Potential Adopters:** All field-research, industrial, laboratory, water-safety skills
- **Adaptation:** Originally from health-wellness; adapted for diving safety (AAUS/PADI standards)

---

## Tools Required

- **WebSearch** — query NOAA, AIMS, IOC-UNESCO, ReefBase, journal databases
- **WebFetch** — retrieve full reports, RSS feeds, and data sheets
- **Read** — load SECOND-KNOWLEDGE-BRAIN.md, existing monitoring data, user-supplied files
- **Write** — produce final restoration plans, monitoring protocols, assessment reports
- **Bash** — run `knowledge_updater.py` crawl pipeline

---

## Knowledge Sources

| Source | Type | Domain |
|--------|------|--------|
| NOAA Coral Reef Watch (`coralreefwatch.noaa.gov`) | Satellite data, bleaching alerts | DHW, SST, bleaching |
| AIMS (`aims.gov.au`) | Research publications RSS | Great Barrier Reef, long-term monitoring |
| IOC-UNESCO (`ioc.unesco.org`) | Policy and monitoring reports | Global ocean health |
| Coral Triangle Initiative (`coraltriangleinitiative.org`) | Regional reports | Southeast Asia reefs |
| ReefBase (`reefbase.net`) | Global reef database | Distribution, status |
| Journal of Experimental Marine Biology and Ecology | Peer-reviewed articles | Species ecology, physiology |
| Marine Pollution Bulletin (ScienceDirect) | Peer-reviewed articles | Pollution, stressors |
| Global Change Biology | Peer-reviewed articles | Climate impact |
| Nature Climate Change | Peer-reviewed articles | Ocean acidification, warming |
| ArXiv `q-bio.PE` | Preprints | Population ecology |

---

## Supporting Python Tools

| File | Purpose |
|------|---------|
| `tools/knowledge_updater.py` | crawl4ai pipeline — fetches latest NOAA alerts, AIMS papers, CTI reports, and journal articles; appends scored entries to SECOND-KNOWLEDGE-BRAIN.md with deduplication |

---

## Active Development Tasks

- [x] Architecture defined (Phase 0)
- [x] CLAUDE.md written
- [x] PROJECT-detail.md written
- [x] PROJECT-DEVELOPMENT-PHASE-TRACKING.md written
- [x] SECOND-KNOWLEDGE-BRAIN.md seeded
- [x] skills/main.md written
- [x] skills/sub-profile-intake.md written
- [x] skills/sub-reef-assessment.md written
- [x] skills/sub-restoration-planner.md written
- [x] skills/sub-monitoring-protocol.md written
- [x] tools/knowledge_updater.py written
- [x] tests/test-scenarios.md written (5+ scenarios)
- [x] Phase 1: Core sub-skills validated in field test
- [x] Phase 2: Main harness quality gates tested end-to-end
- [x] Phase 3: crawl pipeline tested against live NOAA/AIMS feeds
- [x] Phase 4: Test scenarios run and pass
- [x] Phase 5: Cross-cluster wiring with `science-industry` shared sub-skills

**Overall Status:** ✅ COMPLETE — All Phases 0-5 Validated

---

## Reference Documents

- `PROJECT-detail.md` — Full technical specification
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — Phase roadmap with milestones
- `SECOND-KNOWLEDGE-BRAIN.md` — Self-improving domain knowledge base
