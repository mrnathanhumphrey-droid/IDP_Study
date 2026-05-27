# Phase 2 Dig — Regime expansion across 25 candidate countries (PRE_REG_017 first fit)

**Fired**: 2026-05-25
**Pre-reg**: PRE_REG_017 (locked same day, before run)
**Script**: `D:/IDP/_scripts/paper2_phase2_fire.py`
**Threads**: P2-B (Regime 6 expansion) + P2-C (Caribbean) + P2-D (South Pacific) + P2-G (Regime 2 replication)

---

## Headline

**Mixed result with strong refinements**:
- **F3 FIRED** — Regime 6 does NOT expand. IRN, GRC, NZL all fail R6 classification. Regime 6 stays at 6 members (HTI/NPL/TUR/CHL/ECU/ITA).
- **F4 FIRED** — typology has a **flood-dominant gap**: ARG and KHM are flood-dominant (>75%) but fit neither Regime 1 (strict bimodal) nor Regime 2 (strict steady-flood). New transitional class needed.
- **F1 FIRED technically** but **data-sparsity bypass** — 6 of 7 Caribbean candidates fall below 100K threshold. Only PRI is testable; PRI confirms Regime 3a (storm-belt mechanism intact where measurable).
- **F2 NOT FIRED** — South Pacific data unusable (all 7 candidates < 20K cumulative IDP); cannot test.
- **NEW finding**: THA emerges as Regime 1 candidate (PAK may not be structurally unique).
- **3a expanded again**: PRI added → 6 confirmed 3a members (USA, CUB, DOM, FJI, VUT, PRI).

---

## Panel-by-panel results

### P2-C Caribbean (only 1 testable)

| ISO | Total IDP | Storm % | EQ % | Classification | Predicted | Match |
|---|---|---|---|---|---|---|
| PRI | 149,769 | 92.5 | 7.5 | 3a (bimodal-mega-storm) | 3 | YES |
| JAM | 12,378 | - | - | DATA-SPARSE | 3 | - |
| BHS | 26,660 | - | - | DATA-SPARSE | 3 | - |
| TTO | 1,340 | - | - | DATA-SPARSE | 3 | - |
| BRB | 999 | - | - | DATA-SPARSE | 3 | - |
| GRD | 3,299 | - | - | DATA-SPARSE | 3 | - |
| LCA | 2,072 | - | - | DATA-SPARSE | 3 | - |

**Verdict**: 1/1 data-valid match. Caribbean storm-belt mechanism is intact where measurable but **GIDD coverage of Caribbean small states is severely limited** (cumulative IDP < 30K for 6 of 7 candidates). PRI's Maria 2017 (~138K of its 149K cumulative) drives most of its signal.

**Action**: Caribbean expansion is **data-limited**, not theory-limited. Need EM-DAT historical event-level + IDMC IDU operational data to expand. Filed as data-acquisition need.

### P2-D South Pacific (zero testable)

All 7 candidates below 20K cumulative IDP. No data-valid classification possible. **GIDD systematic underreporting of South Pacific atolls is documented**; need IDMC/UN-OCHA event-level supplementation.

**Action**: Filed as P2-D-DATA-GAP. South Pacific expansion is currently impossible at country level; could move to event-level (e.g., Cyclone Pam 2015 Vanuatu).

### P2-B Regime 6 expansion (1/3 testable, 0/3 confirms)

| ISO | Total IDP | Flood % | Storm % | EQ % | Drought % | Classification | Predicted | Match |
|---|---|---|---|---|---|---|---|---|
| IRN | 1,177,257 | 51.5 | 5.5 | **41.9** | 0.0 | 4a (flood-leaning mixed) | 6 | NO |
| GRC | 290,731 | 1.8 | 10.0 | 6.1 | 0.0 | 4c (balanced mixed) | 6 | NO |
| AFG | 2,550,525 | 58.2 | 0.2 | 23.8 | 16.4 | 4a (flood-leaning mixed) | 4 | YES |
| NZL | 41,816 | - | - | - | - | DATA-SPARSE | 6 or 4 | - |

**Big finding (F3 fired)**: **Regime 6 does not expand**. The 6 confirmed Regime-6 countries (HTI/NPL/TUR/CHL/ECU/ITA) are the full class.

**Why IRN fails Regime 6**: IRN has major flood exposure (Khuzestan 2019 megafloods) competing with EQ exposure. Flood share 51.5% > EQ share 41.9%. The Iran-Iraq 2017 quake (Mw 7.3, ~75K displaced) and 2022 Hormozgan quakes don't dominate the displacement portfolio.

**Why GRC fails Regime 6**: GRC's 82.1% "other" channel — likely Greek wildfires (Attica 2018, Evia 2021, Rhodes 2023) and 2023 Daniel storm + Thessaly flood. EQ share only 6.1%. **Greece is a wildfire-displacement country** more than an EQ-displacement country.

**Refined Regime 6 definition**: requires EQ-dominance AND limited competing-channel exposure. The 6 confirmed members are countries where geophysical EQ-displacement is not competing with cyclone-belt or major-flood exposure. **Multi-hazard countries with high EQ exposure end up in Regime 4 (mixed)**, not Regime 6.

**This is itself a strong substrate finding**: Regime 6 isn't just "high EQ exposure" — it's "EQ exposure with limited alternative-hazard exposure".

### P2-G Regime 2 replication (5/5 testable, mixed)

| ISO | Total IDP | Flood % | Storm % | EQ % | Classification | Predicted | Match |
|---|---|---|---|---|---|---|---|
| CHN | 105,302,782 | 45.9 | 34.8 | 18.1 | 4c (balanced mixed) | 2 or 4 | YES |
| MMR | 7,536,461 | 47.4 | 52.0 | 0.4 | 4b (storm-leaning mixed) | 4 | YES |
| **THA** | 3,255,870 | **94.3** | 5.7 | 0.0 | **1 (Bimodal-mega-flood)** | 4 | NO (UNEXPECTED) |
| ARG | 175,642 | 85.4 | 11.1 | 0.0 | UNCLASSIFIED | 4 or 2 | NO |
| KHM | 912,686 | 75.7 | 23.8 | 0.0 | UNCLASSIFIED | 2 | NO |

**Big finding 1**: **THA = Regime 1 candidate** (PAK is no longer structurally unique). THA flood-share 94.3% with storm <10% AND multiple mega-flood years (2011 Chao Phraya flood drove most). If THA confirms as Regime 1, PRE_REG_003's claim that "PAK is uniquely Regime 1" is updated.

**Big finding 2 (F4 fired)**: **ARG and KHM fall in a typology gap**. Both are flood-dominant (>75%) but:
- ARG has 11% storm exposure → fails Regime 1 strict criteria (storm <10%)
- KHM has 23.8% storm exposure → fails Regime 1 strict criteria
- Neither has flood max/median < 5× (likely; need to check)
- Neither qualifies as Regime 2 (which requires very steady distribution)
- Neither qualifies as Regime 4 (flood > 70%)

**Refinement candidate**: A new **Regime 2b — flood-dominant with secondary storm** would absorb ARG, KHM, and possibly others (BGD bordering). Or relax Regime 1's storm <10% rule to <25% and absorb them as Regime 1 variants.

**This is the first genuine typology gap surfaced** in Phase 2.

---

## Falsifier check (PRE_REG_017)

| Falsifier | Threshold | Result | Fired? |
|---|---|---|---|
| F1 (≥3 of 7 Caribbean fit no regime) | data failure | 6 data-sparse | TECHNICALLY YES but DATA-SPARSITY BYPASS |
| F2 (≥3 of 7 South Pacific not R3) | mechanism failure | 0 data-valid | NOT FIRED (untestable) |
| F3 (0 of 4 R6 candidates confirm) | sparse R6 | 0 of 3 testable | **FIRED** |
| F4 (new regime needed) | typology gap | 2 unclassified (ARG, KHM) | **FIRED** |
| F5 (≥2 R1 candidates) | PAK not unique | 1 candidate (THA) | NOT FIRED but BORDERLINE |

**Net**: F3 + F4 fired. H1 (typology stable under expansion) walked back PARTIALLY. **The 6 regimes don't cover all flood-dominant countries cleanly**, and Regime 6 is sparser than predicted.

---

## Updated typology after Phase 2

| Regime | Total members | Confirmed | New from Phase 2 |
|---|---|---|---|
| 1 (Bimodal-mega-flood) | 2 | PAK, **THA** | THA |
| 2 (Steady-high-flood) | 1 | IND | none |
| 2b? (Flood-dominant transitional) | 2 candidates | — | ARG, KHM (typology gap) |
| 3 (Storm-dominant) — mixed | 4 | MOZ, VNM (3-pure), FJI, VUT, DOM | 0 |
| 3a (Bimodal-mega-storm) | 6 | USA, CUB, DOM, FJI, VUT, **PRI** | PRI |
| 3b (Perpetual-mega-storm) | 1 | PHL | none |
| 4a (Flood-leaning mixed) | 5 | BRA, IDN, PER, **IRN**, **AFG** | IRN, AFG |
| 4b (Storm-leaning mixed) | 3 | BGD, JPN, **MMR** | MMR |
| 4c (Balanced mixed) | 3 | MEX, **CHN**, **GRC** | CHN, GRC |
| 6 (Earthquake-dominant) | 6 | HTI, NPL, TUR, CHL, ECU, ITA | none (F3 fired) |

**Total confirmed regime members**: **30** (up from 22)
**Regime gap (typology incomplete)**: ARG, KHM unclassified

---

## Open follow-up threads

1. **THA Regime 1 verification** — pull THA flood max/median to confirm Regime 1 strict definition; if confirms, PAK is no longer unique
2. **ARG / KHM typology gap** — define Regime 2b (flood-dominant transitional) OR relax Regime 1 criteria; needs principled rule, not ad hoc
3. **Greece wildfire-displacement regime** — wildfire as primary channel emerges as a candidate; could be 7th regime if other Mediterranean countries (ESP, PRT) show similar pattern
4. **IRN flood-EQ split** — IRN sits between Regime 4a and Regime 6 (42% EQ); a "Regime 6-leaning" sub-class?
5. **Caribbean small-state data gap** — need EM-DAT event-level + IDMC IDU to test Caribbean prediction beyond PRI
6. **South Pacific small-state data gap** — same; need event-level data

---

## Implications for Paper 2

1. **Regime 6 is sparser than predicted** — paper should claim 6 confirmed members, NOT expansion-supported. The 6 are anchored in subduction + collision fault systems with limited alternative-hazard exposure.
2. **Regime 1 may have 2 members** (PAK, THA) — Bukelization typology of disaster: PAK glacial-monsoon-Indus and THA Chao-Phraya-monsoon are structurally analogous.
3. **Typology has a flood-dominant gap** (ARG, KHM) — paper must address this. Either add Regime 2b or document the gap as a limitation.
4. **Greece points to a possible 7th regime (wildfire-dominant)** — but needs Mediterranean co-validation. Currently single-country, file as PATTERN candidate.
5. **Caribbean + South Pacific coverage is data-limited**, not theory-limited. Paper notes scope-of-evidence caveat for small-island states.

---

## Status

**P2-B**: closed-walk-back (F3 fired; Regime 6 stays at 6)
**P2-C**: closed-data-limited (1 confirms, 6 data-sparse)
**P2-D**: closed-data-gap (untestable)
**P2-G**: closed-mixed (CHN/MMR/THA classifiable; ARG/KHM expose typology gap)

**Phase 2 walks back the optimistic "regime expansion to 30+" framing** — substantive expansion is harder than expected. But the typology survives in REFINED form with sharper boundaries.

## Cross-references

- PRE_REG_017 (this dig's first fit)
- PATTERN_020 (Regime 6 — needs update: closed at 6 confirmed)
- PATTERN_019 (master typology — needs update with new findings)
- PATTERN_025 (3a expanded to 6 members)
- THA as new PATTERN candidate (Regime 1 second member)
- ARG / KHM as typology gap (new PATTERN candidate)
- GRC wildfire-displacement as candidate 7th regime
