# Pre-Registration 036 — SPEI Meteorological-Drought ENSO Test (P8-F)

**ID:** PRE_REG_036
**Locked:** 2026-05-28 (predictions + falsifiers pre-committed BEFORE SPEI NetCDF opens — file still downloading at lock time)
**Substrate:** PRE_REG_034 Set A (displacement-based ENSO test, F1 fired but flagged underpowered/wrong-instrument) + PATTERN_023 (ETH) + PATTERN_008 (Horn drought)
**Paper:** 8 (Compound-Crisis Coupling)
**Status:** LOCKED — first fit fires when SPEI_12.nc finishes downloading and integrity-checks (non-truncated, full dims)

---

## 0. Why this test exists (the question 034 left open)

PRE_REG_034 Set A tested "do Horn drought-DISPLACEMENT mega-years cluster in La Niña years?" and got 50% La Niña vs 47% baseline (F1 fired). But that test was diagnosed as **underpowered and likely instrument-confounded**: GIDD drought-displacement has only ~4 testable years/country (all 2017-2023), and displacement LAGS meteorological drought (2020-2023 Horn drought recorded as displacement in 2022-2023). So displacement-year ≠ rainfall-year, and the ENSO mapping is smeared.

**This pre-reg re-runs the identical ENSO test against SPEI meteorological-drought severity instead of displacement counts.** SPEI is (a) contemporaneous with rainfall (no reporting lag) and (b) dense (monthly, 1950-2024 → ~75 years, not 4). If the Horn La-Niña signal appears in SPEI but not displacement, **034 Set A's failure was a displacement-instrument artifact** (the pre-committed expectation). If it fails in SPEI too, the ENSO teleconnection is genuinely weak and 034's walk-back stands on firmer ground.

---

## 1. Hypothesis

**H1 (Horn = La Niña meteorological drought):** For the Horn-of-Africa coupling cases (ETH, SOM), SPEI-defined drought years fall disproportionately in La Niña years (La Niña → East-African OND short-rains failure → Horn drought). This is the well-established climatology that displacement counts were too sparse/lagged to detect.

**H2 (Amazon = opposite phase):** For BRA (Amazon), SPEI-defined drought years fall disproportionately in El Niño years (El Niño + Atlantic SST → Amazon drought) — the OPPOSITE ENSO sign from the Horn, confirming the PRE_REG_034 Set C / PRE_REG_033 two-family split at the meteorological level.

---

## 2. Pre-locked predictions

Instrument and windows pre-committed before the file opens:
- **SPEI accumulation:** SPEI_12 (12-month, annual integrated moisture balance), December value of each year = the primary annual drought index. SPEI_03 (3-month) December value (= OND season) reported as the Horn short-rains mechanistic secondary if SPEI_03 integrity-checks.
- **Spatial aggregation:** area-mean SPEI over each country's bounding box — ETH ≈ [3-15°N, 33-48°E]; SOM ≈ [-2-12°N, 41-51°E]; BRA-Amazon ≈ [-12-5°N/S, -73 to -50°E]. (Boxes pre-committed; if the grid's lon convention is 0-360 instead of -180-180, BRA box is converted, no other change.)
- **Drought year:** area-mean seasonal SPEI ≤ **-1.0** (moderate-to-severe). Sensitivity reported at -0.8 and -1.5.
- **ENSO phase:** OND-season NOAA ONI (same as 034): La Niña ≤ -0.5, El Niño ≥ +0.5, neutral between.
- **Window:** primary 1950-2024 (full ONI overlap → ~75 yrs, the power gain); also report 2008-2024 (the 034-comparable window).

### Prediction set A — Horn La Niña enrichment (the headline)
- **Predicted:** in ETH + SOM combined, ≥ **60%** of SPEI-drought years are La Niña, AND this exceeds the baseline La Niña rate (~30-35% over 1950-2024) by a clear margin (enrichment ≥ +15pp).

### Prediction set B — Amazon El Niño alignment
- **Predicted:** in BRA-Amazon, SPEI-drought years are El-Niño-aligned: La Niña share < 30%, and El Niño share > La Niña share. BRA La Niña share is strictly less than Horn La Niña share (opposite-phase families).

### Prediction set C — instrument-artifact resolution
- **Predicted:** Horn SPEI La-Niña share (this test) **exceeds** the displacement-based 50% from PRE_REG_034 Set A by ≥ +15pp. If so, 034 Set A's F1 is confirmed as a displacement-instrument artifact (the headline reason this test exists). If Horn SPEI share ≈ 50% too, the failure was real.

---

## 3. Falsifiers (pre-committed)

- **F1 (no Horn ENSO alignment even in SPEI):** Horn SPEI-drought years < 50% La Niña → ENSO teleconnection genuinely weak; 034's walk-back stands; coupling is NOT single-year-ENSO-driven even with the correct instrument.
- **F2 (instrument doesn't resolve it):** Horn SPEI La Niña share is within ±10pp of the displacement-based 50% → the better instrument doesn't change the answer; climate mechanism remains open, NOT artifact.
- **F3 (Amazon breaks two-family split):** BRA-Amazon SPEI-drought is also La-Niña-aligned (La Niña share ≥ Horn share) → the opposite-signature two-family finding (034 Set C) does not survive the meteorological instrument.
- **F4 (ENSO is a global drought driver):** if a non-coupling control region also shows ≥60% La-Niña drought alignment, La Niña explains drought everywhere and doesn't discriminate the COUPLING cases (coupling still needs the conflict-channel link). [Reported if a control region is added.]

F1 firing = the ENSO mechanism is genuinely weak (not instrument); the Paper 8 mechanism story stays "structural chronic synchrony, climate driver unresolved."
F1 NOT firing + Set C confirmed = the climate mechanism is real and family-specific; 034 Set A was an artifact.

---

## 4. Methodology
- SPEIbase NetCDF (SPEI_12 primary, SPEI_03 secondary), opened via xarray (engine auto; h5netcdf/netcdf4). Verify non-truncated (full time + lat/lon dims) BEFORE any analysis.
- Area-mean SPEI over each country bbox, December (annual SPEI_12) and OND (SPEI_03 Dec) per year.
- Classify each year by OND ONI phase.
- Contingency: drought-year (SPEI ≤ -1.0) × ENSO-phase; report exact counts + Fisher/χ² where n permits.
- Baseline La Niña rate over the same window for enrichment comparison.
- Sensitivity sweep over SPEI threshold (-0.8/-1.0/-1.5) and window (1950-2024 / 2008-2024).

## 5. Acknowledgments at lock time
- SPEI bbox area-mean blends sub-national climate zones; Ethiopian highlands vs Somali lowlands differ. Reported per-country before combining.
- SPEI_12 (annual) blends OND short rains with MAM long rains; SPEI_03-Dec isolates short rains better but only if SPEI_03 integrity-checks (currently also truncated on disk).
- ENSO ≠ sole driver (IOD/Indian Ocean Dipole co-drives Horn; Atlantic SST co-drives Amazon). Single-phase test is deliberately simple; IOD deferred.
- Coupling ≠ causation; this tests the climate DRIVER of the drought channel, not the drought→conflict coupling itself (that was 034 Set B, contemporaneous).
- Drought-year threshold is a pre-committed cut; sensitivity reported.

## 6. Cross-references
- PRE_REG_034 (displacement-based ENSO test — this is its meteorological re-run); PRE_REG_033 (two-family coupling census); PRE_REG_035 (structural coupling).
- PATTERN_023 (ETH triple-coupling), PATTERN_021 (BRA Amazon), PATTERN_008 (Horn drought).
- Paper 2 PRE_REG_015 (climate-attribution — SST/ENSO/ACE overlap).
- Data: `data/spei/SPEI_12.nc` (downloading at lock), `data/oni.txt` (NOAA ONI 1950-2026, on disk).

## 7. Provenance
Locked 2026-05-28 while SPEI_12.nc was still downloading (95.9MB of ~314MB; `SPEI_12.nc.crdownload` in Downloads). Predictions + falsifiers committed before the NetCDF opened. First fit fires on a non-truncated SPEI file.

---

## 8. Results — first fit
_(pending SPEI download completion + integrity check)_
