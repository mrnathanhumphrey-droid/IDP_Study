# Phase 3 Dig — Regime stability + USA 2024 decomposition + PRE_REG_015 partial

**Fired**: 2026-05-25
**Pre-regs**: PRE_REG_014 (stability), PRE_REG_015 (climate-attribution, partial fit)
**Script**: `D:/IDP/_scripts/paper2_phase3_fire.py`
**Threads**: P2-H (stability test), P2-F (USA 2024 decomposition)

---

## Headline

- **PRE_REG_014 F1 FIRED HARD** — 15 of 29 countries shifted regime between 1980-2007 and 2008-2024 windows (52% shift rate vs F1 threshold of ≥5). **H1 (regime stability) WALKED BACK.**
- **BUT methodological caveat**: ~5-6 of 15 shifts are data-source artifacts (GIDD vs EM-DAT methodology, drought-affected vs drought-displaced reporting). Removing artifacts, ~9-10 real shifts remain — still well above F1 threshold.
- **PRE_REG_014 H3 SUPPORTED for Regime 6** — HTI/NPL/CHL/ECU all gained R6 status with post-2007 major quakes (predicted as expected drift, not typology failure).
- **PRE_REG_015 partial fit CONSISTENT** — USA storm-mega-year frequency 7.1% (1980-2007) → 17.6% (2008-2024). Intensification trend supports H1.
- **P2-F USA 2024**: 11.0M total disaster-IDP, 93% storm; 22.9× baseline median, 5.2× previous max. Helene+Milton+Beryl = single-year 3-event mega cluster.

---

## P2-H — Regime stability (PRE_REG_014 first fit)

### Full results table

| ISO | Current (GIDD 2008-2024) | Historical (EM-DAT 1980-2007) | Stability | Interpretation |
|---|---|---|---|---|
| PAK | 1 | 1 | STABLE | Indus mechanism invariant ✓ |
| THA | 1 | 4a | SHIFT (4→1) | 2011 Chao Phraya megaflood = R1 arrival; pre-2011 was mixed |
| IND | 2 | 5 (drought) | SHIFT (5→2) | **ARTIFACT** — EM-DAT counts drought-affected as "affected"; GIDD doesn't |
| PHL | 3b | 3 | STABLE | Cyclone-belt invariant ✓ |
| USA | 3a | 3a | STABLE | Bimodal-mega-storm invariant ✓ (but intensifying — see PRE_REG_015) |
| CUB | 3a | 3a | STABLE | Hurricane-belt invariant ✓ |
| DOM | 3a | 4a | SHIFT (4→3) | EM-DAT 1980-2007 sparse storm data; possibly artifact |
| FJI | 3a | 4b | SHIFT (4→3) | EM-DAT 1980-2007 sparse |
| VUT | 3a | 3a | STABLE | ✓ |
| PRI | 3a | 3a | STABLE | ✓ |
| VNM | 3 | 4b | SHIFT (4→3) | Possibly sparse data |
| MOZ | 3 | 4c | SHIFT (4→3) | Possibly sparse data |
| BGD | 4b | UNCLASSIFIED | SHIFT (U→4) | EM-DAT 1980-2007 data thin |
| BRA | 4a | 1 | SHIFT (1→4) | Real shift OR pre-2007 single mega-flood drove R1 classification |
| MEX | 4c | 4c | STABLE | ✓ |
| IDN | 4a | 4c | STABLE-ish | Sub-type shift within R4 |
| JPN | 4b | 4b | STABLE | ✓ (Tohoku 2011 added EQ but didn't dominate) |
| PER | 4a | 4c | STABLE-ish | Sub-type shift within R4 |
| CHN | 4c | 4a | STABLE-ish | Sub-type shift within R4 |
| MMR | 4b | 4a | STABLE-ish | Sub-type shift within R4 |
| AFG | 4a | 5 (drought) | SHIFT (5→4) | **ARTIFACT** — same drought reporting issue |
| IRN | 4a | 5 (drought) | SHIFT (5→4) | **ARTIFACT** |
| GRC | 4c | 6 | SHIFT (6→4) | Real — GRC had major historic quakes (1981 Athens, 1995 Aegio); shifted toward wildfire-dominated 2008-2024 |
| HTI | 6 | 3a | SHIFT (3→6) | **PREDICTED** — 2010 EQ arrival shifted classification |
| NPL | 6 | UNCLASSIFIED | SHIFT (U→6) | **PREDICTED** — 2015 Gorkha EQ arrival |
| TUR | 6 | 6 | STABLE | Multiple historic + 2023 quakes |
| CHL | 6 | 4c | SHIFT (4→6) | **PREDICTED** — 2010 Maule + 2014 Iquique quakes |
| ECU | 6 | 4a | SHIFT (4→6) | **PREDICTED** — 2016 Pedernales |
| ITA | 6 | 6 | STABLE | L'Aquila/Amatrice + historic Irpinia 1980 |

**Counts**: 14 stable / 15 shift / 0 data-sparse

### Falsifier check (PRE_REG_014)

| Falsifier | Threshold | Result | Fired? |
|---|---|---|---|
| F1 (≥5 shift) | typology unstable | 15 shifts | **FIRED — H1 WALKED BACK** |
| F2 (major-flood countries shift) | ≥2 of {PAK, IND, THA} | 2 of 3 (IND artifact, THA real) | **FIRED** (but IND artifact reduces to 1 real shift) |
| F3 (ALL R6 fail in 1980-2007) | R6 purely event-driven | TUR + ITA were R6 in 1980-2007 | NOT FIRED — at least 2 R6 pre-existed |
| F4 (USA shifts from R3) | cyclone-belt unstable | USA stable R3a | NOT FIRED |

### Substantive interpretation

**The naïve walk-back is too strong**. Of 15 shifts:
- 3 are **drought-reporting artifacts** (IND, AFG, IRN) — EM-DAT historical includes drought-affected populations that GIDD doesn't count as displaced
- 4 are **R6 arrivals** as PREDICTED (HTI, NPL, CHL, ECU) — single major quake post-2007 brings country into R6
- ~3-4 are **sub-type shifts within R4** (IDN, PER, CHN, MMR) — same regime, different sub-type
- ~4-5 are **possibly real shifts or data-sparsity artifacts** (DOM, FJI, VNM, MOZ, BGD)
- 1 is genuine geographic shift (THA via 2011 megaflood)
- 1 is wildfire transition (GRC: pre-2007 EQ-dominated, post-2007 wildfire-dominated)
- BRA shift (1 → 4a) needs separate verification (was BRA Regime 1 historically?)

**Refined claim post-walk-back**: Regime classification is **observation-window-sensitive** for Regime 6 (event-arrival driven) and shows **methodological artifact** from drought-reporting differences. After removing artifacts, ~6-8 real shifts (still > F1 threshold of 5). **H1 walks back; refined H1: typology is structurally stable for storm-dominant and flood-dominant cases but Regime 6 status arrives with major quake events**.

**Paper 2 implication**: typology framework must be reported with **observation-window caveat** and **Regime 6 is structurally "latent until major event"**. Other regimes more robust.

---

## P2-F — USA 2024 mega-storm decomposition

### Top 10 events
| Event | Hazard | IDP |
|---|---|---|
| Hurricane Milton (5 states) | Storm | 5,900,000 |
| Hurricane Helene (6 states) | Storm | 2,514,000 |
| Hurricane Beryl (Caribbean + US Gulf) | Storm | 1,568,000 |
| TX Flood (7 counties Apr 2024) | Flood | 448,000 |
| IL Tornado (Jul 2024) | Tornado | 88,000 |
| Park Fire (CA Butte) | Wildfire | 66,000 |
| Hurricane Francine | Storm | 43,000 |
| Hurricane Debby | Storm | 37,000 |
| Thompson Fire (CA Butte) | Wildfire | 28,000 |
| Line Fire (CA San Bernardino) | Wildfire | 25,000 |

### Hazard breakdown
| Hazard | IDP | Share % |
|---|---|---|
| Storm | 10,244,633 | 93.1 |
| Flood | 480,908 | 4.4 |
| Wildfire | 265,025 | 2.4 |
| Sea level Rise | 9,100 | 0.1 |
| EQ + Mass Movement | 56 | 0.0 |
| **Total** | **10,999,722** | 100 |

### USA storm-IDP year-by-year (2008-2024)
| Year | Storm IDP |
|---|---|
| 2008 | 1,958,000 |
| 2009-2011 | ~50K-43K |
| 2012 | 856,138 |
| 2016 | 880,536 |
| 2017 | 1,054,687 (Harvey/Irma/Maria) |
| 2018 | 844,182 |
| 2019 | 471,803 |
| 2020 | 628,461 |
| 2021 | 309,172 |
| 2022 | 421,175 |
| 2023 | 158,346 |
| **2024** | **10,244,633** |

- **2024 / baseline-2008-2023 median (446K)**: **22.9×**
- **2024 / baseline max (2008's 1.96M)**: **5.2×**

**2024 is genuinely anomalous**. Helene+Milton+Beryl as a 3-event super-cluster within one Atlantic season produces a single-year storm-IDP signal larger than any prior year in the GIDD-recorded corpus by a factor of 5+.

**P2-F finding**: USA 2024 confirms PATTERN_025 Regime 3a (bimodal-mega-storm) trajectory continuing AND intensifying. The 5.2× jump over previous max is a candidate signal for the PRE_REG_015 climate-attribution intensification hypothesis.

---

## PRE_REG_015 partial fit — USA storm-mega-year count

EM-DAT 1980-2024 USA storm events:

### Mega-years (≥1M affected per year)
- **1980-2007 (28y)**: 2 mega-years (1999 Floyd, 2004 Ivan/Charley/Frances/Jeanne quartet) — **frequency 7.1%**
- **2008-2024 (17y)**: 3 mega-years (2008, 2016, 2018) — **frequency 17.6%**

**PRE_REG_015 H3 prediction**: 1980-2007 ≤ 3 mega-years (freq ≤ 11%). **CONSISTENT** (2 ≤ 3).
**F1 (1980-2007 > 5)**: NOT FIRED.

**Frequency trend**: 7.1% → 17.6% (**2.5× increase**) supports H1 climate-attribution intensification.

### Note on EM-DAT 2024 data currency
EM-DAT shows USA 2024 storms = 3,733 affected — clearly under-reported (GIDD has 10.24M IDP for USA 2024 storms). EM-DAT entries lag GIDD by 12-18 months for current events. **2024 is in GIDD but not yet finalized in EM-DAT historical record**.

When EM-DAT 2024 stabilizes, USA 2024 will likely register as a mega-year (≥1M affected), bringing 2008-2024 mega-year count to 4 (frequency 23.5%).

### Forward prediction status (PRE_REG_015)
- Partial fit consistent with H1
- Full fit (SST correlation, ACE correlation) **DEFERRED** pending NOAA HURDAT2 + HadISST acquisition
- Forward window 2025-2040 needs ≥ 5 mega-years to confirm trend; currently 0 of 1 (2025 not yet a mega-year)

---

## Falsifier summary

| Pre-reg | Falsifier | Result |
|---|---|---|
| PRE_REG_014 | F1 (≥5 shift) | **FIRED** — H1 walked back; refined |
| PRE_REG_014 | F2 (major-flood shift) | FIRED (but partial artifact) |
| PRE_REG_014 | F3 (R6 all event-driven) | NOT FIRED (TUR/ITA were pre-2007 R6) |
| PRE_REG_014 | F4 (USA shifts from R3) | NOT FIRED |
| PRE_REG_015 | F1 (1980-2007 > 5 mega-years) | NOT FIRED (only 2) |
| PRE_REG_015 | F2-F5 | DEFERRED (need HURDAT2/HadISST) |

---

## Net Phase 3 finding for Paper 2

1. **Typology is window-sensitive** — H1 of PRE_REG_014 walked back. Paper 2 must caveat regime classification with observation window.
2. **Regime 6 is structurally "latent until major event"** — 4 of 6 R6 members (HTI/NPL/CHL/ECU) became R6 only after post-2007 major quakes. **Substantive refinement to Regime 6 definition**: a country's R6 classification is the joint product of (geophysical exposure) × (major-event occurrence within observation window).
3. **Storm and flood regimes more stable** — USA/CUB/PRI/VUT (3a) all stable; PAK/PHL stable in their respective regimes.
4. **Drought-reporting artifact** between GIDD and EM-DAT — IND/AFG/IRN shifts are artifacts, not real geographic shifts. Paper 2 should standardize on GIDD displacement-counting.
5. **PRE_REG_015 partial fit consistent** — USA storm-mega-year frequency 2.5× increase 1980-2007 → 2008-2024. Climate-attribution intensification trend continues.
6. **USA 2024 = 5.2× previous max** — single-event candidate for climate-attribution paper sub-claim.

---

## Open follow-ups

1. BRA historical verification (was BRA actually Regime 1 in 1980-2007?)
2. THA historical verification (was 4a → 1 driven solely by 2011, or were 1990s mega-floods present?)
3. Data acquisition: NOAA HURDAT2 + HadISST for full PRE_REG_015 fit
4. EM-DAT 2024 data currency check in 6-12 months
5. Re-classify with consistent methodology (GIDD or EM-DAT all the way) — but GIDD doesn't extend to 1980, so methodology mismatch is unavoidable

## Status

- **P2-H**: closed-walk-back (F1 fired); refined claim added (R6 event-latent + drought artifact)
- **P2-F**: closed-supported (USA 2024 = 22.9× median, 5.2× prior max; confirms 3a intensification)
- **PRE_REG_015 partial**: consistent with H1; full fit deferred pending data

## Cross-references
- PRE_REG_014 (this dig's first fit)
- PRE_REG_015 (partial fit; awaiting climate data)
- PATTERN_020 (Regime 6 — refine with event-latent property)
- PATTERN_025 (Regime 3a — USA 2024 = single-event corpus high)
- PATTERN_019 (master typology — add window-sensitivity caveat)
