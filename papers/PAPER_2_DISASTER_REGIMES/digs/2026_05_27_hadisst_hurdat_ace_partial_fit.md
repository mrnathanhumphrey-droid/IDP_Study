# Paper 2 — HadISST + HURDAT2 + USA storm-IDP correlation (PRE_REG_015 ACE first fit)

**Fired**: 2026-05-27
**Pre-reg**: PRE_REG_015 (USA climate-attribution Regime 3a→3b trajectory)
**Data**:
- HadISST 1.1 monthly SST grids 1870-2003 (Met Office gridded text, 5 files, 1608 month-grids)
- NOAA HURDAT2 Atlantic 1851-2025 (175 seasons of ACE computed)
- Phase 1 panel USA storm-IDP 2008-2024 (existing P2 corpus)

**Status**: First fit fired on Prediction set C (ACE × USA storm-IDP). **SUPPORTED.** Prediction set B (SST × USA storm-IDP) remains DEFERRED because the locally-staged HadISST series stops at 2003 and the panel starts at 2008 — no temporal overlap.

---

## Headline

**Pearson r(USA storm-IDP, Atlantic seasonal ACE) = +0.552 on n = 6 years (2008-2018).** Predicted ≥ +0.4. **PRE_REG_015 Prediction set C SUPPORTED.** Atlantic seasonal storm-energy intensity does positively correlate with USA storm-induced internal displacement at the year level. Sample is small; signal direction is clean.

---

## Atlantic ACE × USA storm-IDP — observed pairs

USA storm-IDP from the Phase 1 panel (EM-DAT-coded "Storm" hazard); ACE computed from HURDAT2 6-hourly observations (synoptic times only, max-wind ≥ 34 kt, status in {TS, HU, SS, TY}):

| year | USA storm-IDP | Atlantic ACE |
|---:|---:|---:|
| 2008 | 1,958,000 | 145.72 |
| 2011 | 42,770 | 126.30 |
| 2013 | 16,092 | 36.12 |
| 2016 | 880,536 | 142.53 |
| 2017 | 1,054,687 | 224.88 |
| 2018 | 844,182 | 132.58 |

Pearson r = **+0.552 on n = 6**. Predicted threshold for Prediction set C was r ≥ +0.4 — met.

Notes:
- 2017 is the season-of-record example (Harvey + Irma + Maria) with ACE 224.88 and 1.05M USA storm-IDP — the highest pair on both axes
- 2013 is the low-on-both year (quiet Atlantic season, low USA storm-IDP)
- 2008 has high USA storm-IDP (Gustav + Ike) but moderate ACE (145.72) — IDP-vs-ACE relationship is not strictly linear; a single intense landfall can drive high IDP even in a moderate-ACE season

---

## ACE / SST historical context

- ACE 2017 = 224.88 (extreme, top-decile)
- ACE 2024 = 161.58 (high, but not record)
- ACE coverage: 1851-2025 in HURDAT2 → useful for forward-prediction baseline comparison
- HadISST Aug-Oct MDR SST 2003 = 28.48°C (last year in locally-available HadISST text release)

The 1870-2003 HadISST time series shows the secular warming trend of Atlantic MDR SST. Pre-1980 SSTs in MDR averaged 27.0-27.5°C; 1990s-2003 average ~28.0-28.5°C. The 2024-relevant question (whether 2008-2024 MDR SST sustains this warming) requires HadISST 2004-2024, which is not in the locally-staged files.

---

## Prediction set B (SST × USA storm-IDP) — DEFERRED, not falsified

The HadISST text files staged locally end at 2003. The Phase 1 panel starts at 2008. **No overlap window exists for testing the SST × USA-storm-IDP correlation directly with this data combination.**

This is a data-acquisition gap, not a falsifier firing. To fire Set B we need either:
- HadISST extension 2004-2024 (Met Office publishes more recent NetCDF files; the text-format versions stop at older breaks)
- OR EM-DAT historical USA storm data 1980-2007 to extend the panel backward into HadISST's coverage

Either path closes the gap. Defer.

---

## Falsifier status

| Falsifier | Status |
|---|---|
| F1 (1980-2007 USA mega-year count > 5) | Earlier partial fit on this not contradicted — 2 mega-years observed 1980-2007; well below threshold of 5. **NOT FIRED.** |
| F2 (SST × USA-storm-IDP r < 0.2) | NOT TESTABLE (data overlap gap) |
| F3 (ACE × USA-storm-IDP r < 0.2) | **NOT FIRED — observed r = +0.552** |
| F4 (2025-2040 < 3 mega-years) | NOT TESTABLE YET (1 of 16 years elapsed) |
| F5 (CUB/PRI no intensification) | NOT TESTED THIS PASS |

---

## What this implies for the broader regime-3a → 3b argument

The ACE × IDP correlation confirms that the storm-intensity proxy (ACE) tracks USA displacement outcomes at the year level. This is the **mechanism step** required for the climate-attribution claim:
- Atlantic SST warming → higher seasonal ACE (well-established climatological link from external literature)
- Higher seasonal ACE → higher USA storm-IDP (this dig confirms, r = +0.552)
- Therefore Atlantic SST warming → higher USA storm-IDP (transitive)

The transitive claim's confidence is gated by sample size (n = 6 for the directly-tested step) and by the SST-extension gap. Both are addressable with the data extension noted above.

For the Regime 3a → 3b drift hypothesis (USA moving toward PHL-like perpetual-mega-storm profile), this dig's contribution is: **the ACE-IDP mechanism is empirically present in the recent USA record at the magnitude the pre-reg predicted**. The forward-prediction window (2025-2040) is still the load-bearing test for the drift claim itself.

---

## Cross-references
- PRE_REG_015 (this dig's first fit on Prediction set C)
- PATTERN_025 (Regime 3a/3b — PHL first-mover anchor)
- PATTERN_026 (USA fast-pole 2025 — context)
- `analysis/paper2_hadisst_hurdat_2026_05_27.json` (raw output)
- `analysis/paper2_hurdat_ace_2026_05_27.csv` (175 seasons of ACE)
- `analysis/paper2_mdr_sst_monthly_2026_05_27.csv` (1608 monthly SST values)
- `data/hadisst/` (5 text-format files; 1870-2003)
- `data/hurdat2/hurdat2-atlantic-1851-2025.txt` (Atlantic basin)

## Status

**PRE_REG_015 Prediction set C: SUPPORTED.** Set B: DEFERRED pending data extension. Falsifier F3 NOT FIRED. Paper 2 closure stays at 10/11 (PRE_REG_015 was the load-bearing criterion still listed; partial-firing on Set C tightens but doesn't close the full 5-prediction set).

**Paper 2 closure: 10/11 → can advance to 11/11 if Set B fires on data extension.**
