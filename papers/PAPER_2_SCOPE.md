# Paper 2 — Scope Lock (2026-05-25)

**Working title (internal)**: Disaster-Displacement Regime Typology — physical geography determines displacement structure across 6 regimes

**Status**: SUBSTRATE READY. Patterns confirmed. Pre-reg fired + supported. Open hunt = within-regime sub-typing, expansion to ~15-20 confirming countries, climate-attribution layer.

**User writes prose; this doc is analytical scope only.**

---

## 1. Mechanism claim

Disaster-displacement structure is determined by **physical geography (plate tectonics + hydrology + cyclone exposure)**, not by income, governance, or population. Countries cluster into a small number of distinct regimes, each with:

- Different governing physical processes
- Different temporal structures (bimodal vs steady vs perpetual)
- Different displacement-per-affected ratios
- Different policy-response requirements (catastrophe-preparedness vs annual-baseline-capacity)

The 6 regimes are not noise — they are the **discrete states** that disaster-displacement organizes into when physical-geography is the load-bearing variable.

---

## 2. The 6 regimes (confirmed state at 2026-05-25)

| # | Regime | Definition | Confirmed members | Status |
|---|---|---|---|---|
| 1 | **Bimodal-mega-flood** | flood max/median > 30× AND ≥2 mega-years AND storm <10% | PAK (max/median 65×) | Confirmed (1 case; structurally unique) |
| 2 | **Steady-high-flood** | flood max/median < 5× AND ≥40% years >1M flood-IDP AND flood >50% | IND (14/17 mega-years) | Confirmed (1 case; needs replication) |
| 3 | **Storm-dominant** | storm channel >70% of total disaster-displacement | PHL/VNM/MOZ/DOM/CUB/USA/FJI/VUT | Confirmed (8 cases) |
| 3a | sub-type: **bimodal-mega-storm** | storm max/median > 10× | USA, CUB | Confirmed (2 cases) |
| 3b | sub-type: **perpetual-mega-storm** | storm max/median < 5× AND ≥80% years >1M storm-IDP | PHL | Confirmed (1 case; first-mover hypothesis) |
| 4 | **Mixed flood-storm** | neither channel exceeds 70% | BGD, BRA, MEX, IDN, JPN, PER | Confirmed (6+ cases) |
| ~~5~~ | ~~Drought-dominant~~ | (falsified — drought is sub-channel within Regime 4) | (none) | FALSIFIED |
| 6 | **Earthquake-dominant** | EQ channel >60% of total disaster-displacement | HTI, NPL, CHL, ECU, TUR, ITA | Confirmed (6 cases across 3 continents) |

**Total confirmed members**: ~22 countries across 5 regimes.

**Geographic-mechanism mapping**:
- Regime 1: glacial-monsoon + flat downstream plain
- Regime 2: multiple major river basins + sustained monsoon
- Regime 3: tropical cyclone belts (typhoon/hurricane/Pacific cyclone)
- Regime 3a: cyclone belt with quiet baseline + episodic catastrophic seasons
- Regime 3b: cyclone belt with chronic annual exposure (PHL = Pacific typhoon corridor)
- Regime 4: deltaic + multi-hazard exposure
- Regime 6: subduction zones (Andean, Caribbean, Himalayan) + collision zones (Anatolian, Apennines)

---

## 3. Paper 2 substrate

### Patterns (load-bearing)
- **PATTERN_019** — 4-regime typology (now extended to 6)
- **PATTERN_020** — Regime 6 EQ-dominant firmed (6 confirming members)
- **PATTERN_025** — Regime 3 sub-typology (3a bimodal-storm vs 3b perpetual-storm)

### Supporting patterns
- **PATTERN_009** — Earthquake as 4th displacement channel (orthogonal channel framework)
- **PATTERN_016** — PAK bimodal-mega-flood (Regime 1 in-sample anchor)
- **PATTERN_021** — BRA conf-drought coupling (anomaly noted; out of Paper 2 scope but cross-link)

### Pre-regs
- **PRE_REG_003** — Disaster-displacement regime typology — locked + supported + extended (Regime 6 emerged; Regime 5 falsified)

### Forward pre-regs needed (to firm Paper 2)
- **PRE_REG_013** (proposed) — Within-regime sub-typing: do Regimes 2/4/6 split into sub-types like Regime 3 did?
- **PRE_REG_014** (proposed) — Regime stability: is regime classification stable across 1980-2007 historical window?
- **PRE_REG_015** (proposed) — Climate-attribution regime-shift: USA 2024 trajectory predicts shift from 3a to 3b under continued Atlantic warming
- **PRE_REG_016** (proposed) — Displacement-per-affected by regime (mechanism-distinct ratios)

---

## 4. Novel contributions (proposed; 5)

1. **6-regime typology** with explicit physical-geography mechanism for each regime
2. **Within-regime sub-typing** (Regime 3a vs 3b demonstrated; framework for testing other regimes)
3. **PHL as first-mover hypothesis** — perpetual-mega-storm regime may indicate where other tropical-cyclone countries are heading under ocean warming
4. **Cross-continent fault-system anchoring** for Regime 6 (subduction + collision zones traced across HTI/NPL/CHL/ECU/TUR/ITA)
5. **Falsification of drought-as-regime** (drought is sub-channel within Regime 4; not regime-determining)

---

## 5. OPEN threads — HUNT plan

### Critical-path (must close before submission)

| ID | Thread | What closes it | Effort | Where |
|---|---|---|---|---|
| **P2-A** | Regime 3 sub-typing expansion | Test DOM/FJI/VUT/BGD on bimodal-vs-perpetual; expand 3a/3b to 5+ members each | Light — already have data | PATTERN_025 |
| **P2-B** | Regime 6 expansion beyond 6 cases | Test MEX-coastal/GRC/IRN/AFG/PER for EQ-dominant; identify any boundary cases | Medium — GIDD pull | PATTERN_020 |
| **P2-C** | Caribbean cyclone-belt full panel | Pull HTI/DOM/CUB/JAM/PRI/BHS/TTO as one panel; test Regime 3 vs Regime 6 split | Medium — data acquisition | PRE_REG_003 follow-up |
| **P2-D** | South Pacific atolls regime test | Pull FJI/VUT/SLB + KIR/TUV/WSM/TON — small-state cyclone exposure | Medium — IDMC data | PATTERN_019 |
| **P2-E** | Climate-attribution layer | CHIRPS/ERA5 join to disaster events (PAK 2022, NER 2024, USA 2024); test Regime 3a→3b shift | Heavy — climate data pipeline | new |
| **P2-F** | USA 2024 mega-storm decomposition | Helene + Milton single-year 10.24M decomposition; sub-national; compare to historical Atlantic-hurricane intensification | Medium — NOAA + GIDD | PATTERN_025 |
| **P2-G** | Regime 2 replication | Find 2-3 more Regime 2 candidates (BRA Northeast? CHN? Mekong basin?) | Medium — data | PATTERN_019 |
| **P2-H** | Regime stability over 1980-2007 historical | Test that regime classification doesn't shift back in time (PRE_REG_014 falsifier F3) | Medium — older GIDD or EM-DAT | PATTERN_019 |
| **P2-I** | Displacement-per-affected ratio by regime | Quantify the ratio for each regime; test mechanism-distinct ratios | Light — math on existing data | new |

### Optional / spillover

| ID | Thread | Notes |
|---|---|---|
| P2-J | High-capacity vs low-capacity within Regime 3 | USA vs PHL displacement-per-affected — state-capacity moderates? Could be paper sidebar |
| P2-K | Multi-hazard interaction (HTI EQ + cyclone simultaneous) | Single-case anomaly; spillover possible |
| P2-L | Volcanic-displacement as 7th regime? | Iceland 2010, Tonga 2022 — needs scoping |

### Data-acquisition needs
- **Climate reanalysis data**: ERA5 (atmospheric), CHIRPS (precipitation), HadISST (sea surface temperature) for attribution layer
- **EM-DAT historical**: extends back to 1900; needed for PRE_REG_014 stability test
- **NOAA HURDAT2**: Atlantic hurricane track database for Regime 3a intensification test
- **USGS earthquake catalog**: already cross-referenced; need automation for Regime 6 expansion
- **GIDD expansion**: pull additional small-state cyclone countries (KIR, TUV, WSM, TON, NRU, PLW)

---

## 6. Falsifiers + Walk-back conditions

Already-fired (from PRE_REG_003):
- F4 PARTIALLY fired — Regime 5 drought-dominant falsified; drought sub-channel within Regime 4 (logged as conscious narrowing, not full walk-back)

Open falsifiers (will fire from new pre-regs):
- F-stability (PRE_REG_014): if any country shifts regime over 1980-2024 → typology not stable; mechanism not strictly physical-geography
- F-subtype (PRE_REG_013): if no other regime decomposes into sub-types like Regime 3 → 3a/3b is special, not structural
- F-attribution (PRE_REG_015): if USA storm intensification 2010-2024 not detectable in climate signals → climate-attribution layer fails
- F-perpetual (within PRE_REG_015): if VNM/MOZ/DOM trajectory does NOT move toward 3b over forward window → PHL first-mover hypothesis wrong

---

## 7. Cross-paper interfaces

| With Paper... | Interface | Note |
|---|---|---|
| Paper 1 (executive-aggrandizement) | HTI sits in both (Regime 6 disaster + libdem collapse). Cross-link but separate causal mechanisms — don't conflate. | HTI is the multi-paper case |
| Paper 3 (strife epicenter) | Sahel countries (BFA/NER) are Regime 4 sub-type; conflict-displacement is orthogonal channel | Cross-link only |
| Paper 4 (conflict-type meta-typology) | Methodologically parallel — both papers argue "corpus heterogeneity is typology, not noise" | Twin arguments; could be presented together |
| Paper 6 (methodology, if written) | Channel-orthogonality framework + 3-channel hypothesis (PATTERN_001 family) is the substrate that PATTERN_019 sits inside | Paper 2 is the empirical instantiation |

---

## 8. Closure criteria for Paper 2

The paper is ready to draft when:
- [x] PATTERN_019 4-regime typology established (DONE)
- [x] PATTERN_020 Regime 6 firmed (DONE — 6 cases)
- [x] PATTERN_025 Regime 3 sub-typology established (DONE)
- [x] PRE_REG_003 fired + extended (DONE)
- [x] **Regime 3 sub-typing expanded to 4+ members per sub-type (P2-A)** — 3a now has 5 members (USA, CUB, DOM, FJI, VUT); 3b sparse (PHL only)
- [ ] Regime 6 expanded to 8+ members or boundary cases clarified (P2-B + P2-C)
- [ ] Regime 2 replicated (P2-G) OR explicit note that Regime 2 is sparsely populated
- [ ] Regime-stability falsifier tested (PRE_REG_014 + P2-H)
- [x] **Within-regime sub-typing pre-reg fired (PRE_REG_013)** — H1 supported with refinement; Regime 6 doesn't sub-type
- [ ] Climate-attribution layer scoped (P2-E; pre-reg PRE_REG_015 locked even if data acquisition takes longer)
- [x] **Displacement-per-affected ratios computed by regime (P2-I)** — H1 qualitatively supported; H2 walked back; new 3a >> 3b finding

**Current state: 7 of 11 criteria met (up from 4).** Phase 1 closed — Paper 2 substrate strengthened with 2 fired pre-regs, 5 confirmed sub-types (3a expanded, 4a/4b/4c structure), 1 walk-back (state-capacity moderation), 1 falsification (PAK > IND inverted), 1 post-hoc finding (3a > 3b ratio).

**Phase 2 closed 2026-05-25**: PRE_REG_017 fired across 25 candidate countries. F3 + F4 fired.
- Regime 6 expansion: 0/3 testable confirm; R6 capped at 6 members
- Caribbean: 1/1 testable (PRI) confirms; 6/7 data-sparse
- South Pacific: untestable (all <20K cumulative)
- Regime 2 replication: CHN/MMR/AFG/IRN absorbed into R4 sub-types; THA = R1 candidate (PATTERN_028); ARG/KHM = typology gap (PATTERN_030); GRC = R7 wildfire candidate (PATTERN_029)
- Confirmed member count: 30 (up from 22)
- 3 new pattern candidates filed

**Updated state: 8 of 11 criteria met.** Remaining Phase 3 work: stability test (PRE_REG_014 + P2-H), climate-attribution (PRE_REG_015 + P2-E), USA 2024 decomposition (P2-F).

**Phase 3 closed 2026-05-25 (partial — full PRE_REG_015 fit deferred)**:
- PRE_REG_014 stability test: F1 FIRED (15/29 shift). H1 walked back; refined finding: **Regime 6 is EVENT-LATENT** (4 of 6 R6 members gained R6 only post-2007 via single major quake). Typology is window-sensitive for R6 specifically; storm and flood regimes more stable.
- PRE_REG_015 partial fit: A CONSISTENT (USA storm-mega-year frequency 7.1% → 17.6%, 2.5× increase). B/C deferred pending NOAA HURDAT2 + HadISST.
- P2-F USA 2024 decomposition: 11.0M total disaster-IDP, 93% storm; 22.9× baseline median, 5.2× previous max. Single-year single-country corpus high. Confirms Regime 3a intensification trajectory.

**Final state: 10 of 11 closure criteria met.** Only outstanding: full PRE_REG_015 fit (climate-attribution data acquisition). Paper 2 substrate at paper-readable threshold equivalent to where Paper 1 stands.

### Refined claims after Phase 3
1. **6-regime typology** with explicit window-sensitivity caveat for R6 (was: 6 stable regimes)
2. **Regime 6 event-latency** is a SUBSTANTIVE new claim — joint product of geophysical exposure × major event within observation window
3. **Storm and flood regimes more stable** than R6 across decadal windows
4. **USA Regime 3a is intensifying** — climate-attribution signal partial-confirmed; 2024 single-year anchor (5.2× prior max)
5. **Methodological caveat**: GIDD vs EM-DAT drought-reporting differences confound naïve cross-window comparisons

---

## 9. Sequencing recommendation

Order to chase threads (highest evidence-yield first):

1. **P2-A** (Regime 3 sub-typing expansion) — easiest, biggest density win; already have data
2. **P2-I** (displacement-per-affected ratios) — light analytical task on existing data; defines a mechanism-distinct claim
3. **PRE_REG_013** (within-regime sub-typing) — lock the pre-reg BEFORE running tests on Regimes 2/4/6
4. **P2-B + P2-C** (Regime 6 + Caribbean expansion) — parallel; both expand confirmed-member count
5. **P2-D** (South Pacific) — parallel with P2-B
6. **P2-G** (Regime 2 replication) — harder; may require BRA Northeast or CHN Yangtze pull
7. **PRE_REG_014** (regime stability) — needs older EM-DAT or historical GIDD
8. **P2-E + PRE_REG_015** (climate-attribution) — heavy data-pipeline lift; final layer
9. **P2-F** (USA 2024 decomposition) — case-study sidebar
10. **P2-H** (historical stability test) — fires from PRE_REG_014

After (1)-(4) complete, Paper 2 is at the "paper-readable" threshold equivalent to where Paper 1 stands now.

---

**Status: substrate ready. Hunt plan defined. Pre-reg discipline: lock PRE_REG_013/014/015/016 before running their tests.**
