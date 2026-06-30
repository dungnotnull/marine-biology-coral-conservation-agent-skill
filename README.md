# 🌊 Marine Biology Coral Conservation Agent Skill

<div align="center">

**AI-Powered Marine Biology Research & Coral Reef Conservation Support**

[![Phase Status](https://img.shields.io/badge/Phase-Complete-success)](https://github.com/dungnotnull/marine-biology-coral-conservation-agent-skill)
[![Validation](https://img.shields.io/badge/Validation-100%25%20Pass-brightgreen)](docs/phase4-validation-report.md)
[![Skill ID](https://img.shields.io/badge/Skill%20ID-238-blue)](CLAUDE.md)
[![Cluster](https://img.shields.io/badge/Cluster-science--industry-orange)](CLAUDE.md)

*A production-grade AI skill for scientific divers, marine biologists, reef managers, and conservation practitioners*

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Validation](#-validation) • [Contributing](#-contributing)

</div>

---

## 📖 Overview

This skill provides a unified, research-first workflow for coral reef conservation, integrating globally standardized monitoring protocols (Reef Check, GCRMN, CoralWatch), real-time oceanographic data from NOAA Coral Reef Watch, and evidence-based restoration methodologies. It delivers professional-grade reef health assessments, restoration strategies, and monitoring protocols—all automatically kept current through a knowledge pipeline that crawls peer-reviewed literature.

### What It Does

- **Reef Health Assessment**: Systematic evaluation using Reef Check/GCRMN protocols with NOAA DHW thermal stress data
- **Restoration Planning**: Evidence-based coral restoration strategies with species selection and propagation methods
- **Monitoring Protocol Design**: Statistically powered long-term monitoring plans with power analysis
- **Literature Review**: Automated knowledge synthesis from peer-reviewed marine science publications
- **Knowledge Updates**: Weekly crawl pipeline from NOAA, AIMS, CTI, ScienceDirect, ReefBase, and ArXiv

---

## ✨ Features

### 🐠 Professional-Grade Assessment
- Quantitative reef health scorecard with 8 dimensions
- Integration with NOAA Coral Reef Watch Degree Heating Weeks (DHW) data
- CoralWatch bleaching index calculations
- Shannon diversity analysis for coral genera
- Ocean Health Index (OHI) sub-score computation

### 🌿 Evidence-Based Restoration Planning
- Species selection based on thermal tolerance ratings
- Propagation method decision tree (nursery, micro-fragmentation, biorock, assisted gene flow)
- Survival KPIs grounded in peer-reviewed literature
- Planting density calculations and timeline planning
- Citation-backed recommendations (≥2 peer-reviewed sources per method)

### 📊 Statistically Powered Monitoring
- Power analysis for detecting Δ5% coral cover change
- Capacity-tiered method selection (High/Medium/Low)
- GCRMN and Reef Check compatible data forms
- Professional reporting schedules and templates

### 🧠 Self-Improving Knowledge Base
- Automated crawl pipeline from 6 scientific sources
- Scoring algorithm (60% recency, 40% relevance)
- Deduplication via SHA-256 fingerprinting
- Weekly update schedule with cron/Task Scheduler support

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Required packages (install via pip):
  - crawl4ai
  - feedparser
  - requests
  - beautifulsoup4
  - arxiv

### Installation

1. Clone the repository:
```bash
git clone https://github.com/dungnotnull/marine-biology-coral-conservation-agent-skill.git
cd marine-biology-coral-conservation-agent-skill
```

2. Install dependencies:
```bash
pip install crawl4ai feedparser requests beautifulsoup4 arxiv
```

### Knowledge Updates

Run the knowledge pipeline to fetch latest research:

```bash
# Dry run (fetch and score without writing)
python tools/knowledge_updater.py --dry-run

# Full update (fetches and appends to SECOND-KNOWLEDGE-BRAIN.md)
python tools/knowledge_updater.py

# Single source only
python tools/knowledge_updater.py --source noaa

# Limit entries
python tools/knowledge_updater.py --limit 10
```

### Weekly Schedule Setup

**Linux/macOS (cron):**
```bash
0 2 * * 0 cd /path/to/marine-biology-coral-conservation-agent-skill && python tools/knowledge_updater.py >> tools/knowledge_updater_cron.log 2>&1
```

**Windows (Task Scheduler):**
- Trigger: Weekly on Sunday at 2:00 AM
- Program: `python.exe`
- Arguments: `tools\knowledge_updater.py`
- Start in: Repository root directory

---

## 📚 Documentation

### Core Documentation

| Document | Description |
|----------|-------------|
| [CLAUDE.md](CLAUDE.md) | Skill identity, harness workflow, and reusable sub-skills |
| [PROJECT-detail.md](PROJECT-detail.md) | Full technical specification and architecture |
| [PROJECT-DEVELOPMENT-PHASE-TRACKING.md](PROJECT-DEVELOPMENT-PHASE-TRACKING.md) | Phase completion status and task tracking |
| [SECOND-KNOWLEDGE-BRAIN.md](SECOND-KNOWLEDGE-BRAIN.md) | Self-improving domain knowledge base |

### Validation Reports

| Report | Description | Status |
|--------|-------------|--------|
| [Phase 1 Validation](docs/phase1-validation-report.md) | Core sub-skills validation | 8/8 test cases passed |
| [Phase 2 Validation](docs/phase2-validation-report.md) | Main harness + quality gates | 20/20 gates passed |
| [Phase 3 Validation](docs/phase3-validation-report.md) | Knowledge pipeline testing | 6/6 sources working |
| [Phase 4 Validation](docs/phase4-validation-report.md) | End-to-end testing | 34/34 criteria passed |
| [Phase 5 Validation](docs/phase5-validation-report.md) | Integration & cross-skill wiring | 4 reusable sub-skills documented |

### Skill Files

| File | Purpose |
|------|---------|
| [skills/main.md](skills/main.md) | Main harness workflow |
| [skills/sub-profile-intake.md](skills/sub-profile-intake.md) | Site profile and resource assessment |
| [skills/sub-reef-assessment.md](skills/sub-reef-assessment.md) | Reef health assessment protocols |
| [skills/sub-restoration-planner.md](skills/sub-restoration-planner.md) | Evidence-based restoration strategies |
| [skills/sub-monitoring-protocol.md](skills/sub-monitoring-protocol.md) | Long-term monitoring protocol design |

---

## 🧪 Validation & Testing

### Test Results Summary

All 5 test scenarios passed with 100% success rate:

| Scenario | Result | Criteria | Status |
|----------|--------|----------|--------|
| Maldives Bleaching Emergency | PASS | 6/6 | ✅ |
| Philippines Community Restoration | PASS | 6/6 | ✅ |
| West Papua MPA Monitoring | PASS | 7/7 | ✅ |
| Great Barrier Reef Literature Review | PASS | 7/7 | ✅ |
| Red Sea Post-Bleaching Recovery | PASS | 8/8 | ✅ |
| **TOTAL** | **100%** | **34/34** | ✅ |

### Quality Gates

All 8 quality gates validated:

- QG-1: Citation completeness (all numerical claims cited)
- QG-2: NOAA DHW sourcing (satellite data, not estimated)
- QG-3: Thermal tolerance sourcing (NOAA CoRTAD or peer-reviewed)
- QG-4: Restoration method support (≥2 peer-reviewed citations)
- QG-5: Statistical power analysis (explicit calculations)
- QG-6: Dive safety notes (AAUS/PADI standards)
- QG-7: Composite health scores (OHI sub-scores)
- QG-8: Professional report format (structured artifacts)

---

## 🌐 Knowledge Sources

The skill aggregates data from authoritative marine science sources:

| Source | Type | Update Frequency |
|--------|------|------------------|
| NOAA Coral Reef Watch | Satellite DHW/SST data | Daily |
| AIMS Long-Term Monitoring | GBR research publications | Annual + ongoing |
| Coral Triangle Initiative | Regional reports | Annual |
| Marine Pollution Bulletin | Peer-reviewed articles | Ongoing |
| ReefBase | Global reef database | Ongoing |
| ArXiv q-bio.PE | Population ecology preprints | Weekly |

---

## 🔧 Technical Architecture

### Harness Flow

```
Profile Intake → Assessment Branch → Restoration Planning → Monitoring Protocol
                                  ↓
                          Quality Gate Review (8 gates)
                                  ↓
                          Final Report Synthesis
```

### Decision Trees

**Propagation Method Selection:**
- Branching corals + low thermal stress → CRF Nursery Fragmentation
- Massive corals → Micro-fragmentation (Mote Marine protocol)
- Chronic thermal stress → SECORE Assisted Gene Flow
- Unstable substrate/pH < 1.8 → Biorock mineral accretion

**Monitoring Method Selection:**
- High capacity (≥4 divers, quarterly) → GCRMN photo-quadrat + belt transect
- Medium capacity (2-3 divers, bi-annual) → Reef Check standard transects
- Low capacity (1-2 divers, annual) → CoralWatch + basic cover estimate

---

## 🎯 Use Cases

### For Scientific Divers
- Rapid reef health assessment against global benchmarks
- DHW context for dive planning and safety
- Standardized data collection protocols

### For Reef Managers
- Evidence-based restoration planning
- Statistically powered monitoring design
- Professional reporting for stakeholders

### For Researchers
- Literature synthesis on thermal tolerance and restoration
- Species selection guidance with citations
- Knowledge base auto-updated with latest research

### For Conservation NGOs
- Restoration viability assessment
- Funding proposal support with data-driven recommendations
- Long-term monitoring protocols for impact evaluation

---

## 📈 Statistical Methodology

### Power Analysis Formula

For detecting Δ5% coral cover change with 80% power:

```
n = 2 × (Zα/2 + Zβ)² × σ² / δ²

Where:
- Zα/2 = 1.96 (α = 0.05, two-tailed)
- Zβ = 0.842 (β = 0.20, 80% power)
- σ = standard deviation (10-12% from literature)
- δ = 5% (minimum detectable change)
```

### DHW Alert Levels

| DHW (°C-weeks) | Alert Level | Expected Outcome |
|----------------|-------------|-------------------|
| 0 | No Alert | No bleaching expected |
| 1-3 | Watch | Bleaching possible |
| 4-7 | Alert Level 1 | Bleaching likely (up to 30%) |
| 8+ | Alert Level 2 | Mass bleaching and mortality likely |
| 16+ | Extreme | Near-total mortality |

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution

- Additional knowledge sources for the crawl pipeline
- Regional reef health databases
- Translation of materials for local communities
- Integration with local monitoring networks
- Documentation improvements

---

## 📜 Citation

If you use this skill in your research or conservation work, please cite:

```
Marine Biology Coral Conservation Agent Skill #238
Version 1.0.0
https://github.com/dungnotnull/marine-biology-coral-conservation-agent-skill
```

### Key References

- Hughes et al. (2017). Global coral bleaching 2014–2017. Nature. DOI: 10.1038/s41586-017-0049-y
- Schopmeyer et al. (2017). Enhanced long-term survival of coral fragments. PLOS ONE. DOI: 10.1371/journal.pone.0169966
- Souter et al. (2021). Status of Coral Reefs of the World: 2020. GCRMN. DOI: 10.59387/WOTJ9184
- NOAA Coral Reef Watch. https://coralreefwatch.noaa.gov

---

## 🏆 Acknowledgments

This skill builds upon the work of:

- **NOAA Coral Reef Watch** — Satellite monitoring and bleaching alerts
- **Reef Check Foundation** — Global standardized monitoring protocols
- **GCRMN (Global Coral Reef Monitoring Network)** — Scientific methodologies
- **CoralWatch (University of Queensland)** — Bleaching assessment tools
- **AIMS (Australian Institute of Marine Science)** — Long-term monitoring data
- **SECORE International** — Assisted gene flow and sexual propagation
- **Coral Restoration Foundation** — Nursery fragmentation protocols
- **Mote Marine Laboratory** — Micro-fragmentation techniques

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌍 Supporting Coral Reef Conservation

Coral reefs cover less than 1% of the ocean floor but support approximately 25% of all marine species. Since 1950, global coral cover has declined by roughly 50%. This skill aims to empower conservation practitioners with the best available science and tools to protect these vital ecosystems.

**Status:** ✅ Production-Ready & Open-Source
**Completion:** All Phases (0-5) Validated
**Test Coverage:** 100% (34/34 criteria passed)

---

<div align="center">

**Built with ❤️ for marine conservation practitioners worldwide**

[🔝 Back to top](#-marine-biology-coral-conservation-agent-skill)

</div>
