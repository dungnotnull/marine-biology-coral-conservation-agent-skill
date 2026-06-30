---
name: marine-biology-coral-conservation/sub-profile-intake
description: Gather structured site profile for a coral reef research or conservation project — location, reef type, diver credentials, research objectives, available data, and team resources.
---

## Purpose

Collect all contextual information required before any reef assessment, restoration planning, or monitoring protocol work begins. This sub-skill ensures that all downstream sub-skills receive consistent, structured inputs — eliminating ambiguity about site conditions, user expertise, and available resources. It also performs an initial dive safety check and classifies the site within the GCRMN regional framework.

A poor intake produces poor outputs downstream. This sub-skill therefore challenges ambiguous answers and seeks specificity over approximation at every field.

---

## Inputs

- User's natural-language description of their reef site and conservation/research goals (free-form text)
- Any attached files: previous survey data, GPS coordinates, photos, temperature logger exports

---

## Workflow

### Step 1 — Site Identification

Ask the user to provide:

1. **Site name:** Common name or coordinates (e.g., "Tubbataha Reef, Philippines" or "Lighthouse Reef, Belize")
2. **GPS coordinates or region:** Exact lat/long preferred. If unavailable, accept island/country/ocean basin.
3. **GCRMN Region:** Map to one of: Caribbean & Gulf of Mexico / Pacific Ocean / Indian Ocean / Arabian Seas / East Asia / Australia & Pacific Islands / Red Sea & Gulf of Aden / Atlantic Ocean. Use site name + coordinates to assign if not stated.
4. **Reef type:** Fringing / Barrier / Atoll / Patch reef / Artificial reef
5. **Depth range:** Minimum and maximum survey depth in meters

If GPS coordinates are not provided, query WebSearch for the site name to retrieve approximate coordinates.

---

### Step 2 — User Role & Objectives

Ask:

6. **User role:** Scientific diver / Reef manager (MPA/NGO) / Academic researcher / Graduate student / Conservation NGO / Government agency / Other
7. **Primary objective (select one or more):**
   - A. Reef health assessment (evaluate current status)
   - B. Coral restoration planning (design nursery or outplanting program)
   - C. Long-term monitoring protocol design (set up ongoing surveillance)
   - D. Literature review / knowledge update (research question, not field survey)
   - E. Full integrated workflow (all of the above)
8. **Urgency context:** Is there an active bleaching event, recent cyclone/storm damage, disease outbreak, or other acute stressor? Yes/No — if yes, describe.

---

### Step 3 — Existing Data Inventory

Ask:

9. **Previous surveys:** Has this site been surveyed before? If yes:
   - Which protocol was used (Reef Check / GCRMN / CoralWatch / custom)?
   - When was the most recent survey?
   - What parameters were recorded (coral cover, fish, invertebrates, bleaching, water quality)?
   - Can the user share the raw data or summary results?
10. **Temperature data:** Are in-situ temperature loggers deployed? If yes, what is the current SST trend vs. historical mean?
11. **Photo/video records:** Are site photos or video transects available from previous surveys?
12. **Water quality data:** Is pH, pCO2, dissolved oxygen, or turbidity data available?

If no existing data: note that this is a baseline survey situation. Advise the user that the skill will guide them in setting up their first survey.

---

### Step 4 — Team Capacity Assessment

Ask:

13. **Team size:** How many trained scientific divers are available for surveys?
14. **Dive certification level:** What is the highest certification held by team members?
    - PADI/NAUI Open Water (≤18m)
    - Advanced Open Water (≤30m)
    - Rescue Diver
    - Divemaster / Dive Leader
    - AAUS Scientific Diver (no depth restriction with appropriate training)
15. **Survey frequency:** How often can surveys be conducted? (Daily / Weekly / Monthly / Quarterly / Annual)
16. **Equipment available:** Select all that apply:
    - Reef Check transect tapes and data slates
    - Underwater camera (specify model/resolution if known)
    - Fish ID reference cards
    - CoralWatch Coral Health Charts
    - Water quality sonde (YSI, Hach, etc.)
    - Temperature loggers (HOBO, etc.)
    - Photo-quadrat frame
    - Underwater drone/ROV
17. **Budget tier:** Shoestring (volunteer, minimal consumables) / Moderate (NGO project budget) / Well-funded (government or large grant)

---

### Step 5 — Safety Check

18. **Maximum planned dive depth:** What is the deepest survey station planned?

Apply the following safety flags:
- Depth > 18m AND certification < Advanced: FLAG — "Team certification limits surveys to 18m maximum (PADI OW standard). Advanced OW or Scientific Diver certification required for deeper work. Consult AAUS standards (aaus.org) for scientific diving protocols."
- Depth > 30m: FLAG — "Dives beyond 30m require specialized training (AAUS / IANTD / PADI TecRec). Ensure all team members hold appropriate technical diving certification and follow AAUS Code of Practice for Scientific Diving."
- Night surveys or low-visibility (< 5m): FLAG — "Night or low-visibility diving requires additional safety planning. Follow AAUS buddy system requirements: all divers must remain within buddy contact distance."

---

### Step 6 — Compile Structured Site Profile

Compile all collected information into a structured Site Profile document:

```
SITE PROFILE — [Site Name]
Generated: [Date]

LOCATION
  Name: [site name]
  Coordinates: [lat, long]
  GCRMN Region: [region]
  Reef Type: [fringing/barrier/atoll/patch]
  Depth Range: [min]–[max] m

USER & OBJECTIVES
  Role: [role]
  Primary Objectives: [A / B / C / D / E]
  Acute Stressor: [yes/no — description]

EXISTING DATA
  Previous surveys: [yes/no — protocol, date, parameters]
  Temperature data: [yes/no]
  Photo/video records: [yes/no]
  Water quality data: [yes/no]

TEAM CAPACITY
  Diver count: [n]
  Max certification: [level]
  Survey frequency: [frequency]
  Equipment: [list]
  Budget tier: [tier]

SAFETY FLAGS
  [list any flags triggered, or "None"]
```

---

## Outputs

**Structured Site Profile** — standardized document passed to all downstream sub-skills

The Site Profile includes:
- Site identity (name, GPS, GCRMN region, reef type, depth)
- Research objectives (categorized by type A–E)
- Existing data inventory (what is available to interpret vs. what must be collected from scratch)
- Team capacity profile (determines which survey methods are feasible in sub-monitoring-protocol)
- Safety flags (propagated to main harness and included in final report)

---

## Quality Gate

Before passing the Site Profile to the next sub-skill, verify:

| Check | Criterion |
|-------|-----------|
| GPS confirmed | Exact coordinates or verified region assigned; GCRMN region labeled |
| Objective categorized | Primary objective classified as A, B, C, D, or E |
| Safety flags applied | All three safety checks evaluated and flags recorded if triggered |
| Dive certification documented | Team's maximum dive certification level recorded |
| Data inventory complete | Existing data clearly listed as available or not available (not ambiguous) |

If any field is missing or ambiguous: ask a targeted follow-up question before proceeding. Do not pass incomplete Site Profiles downstream.
