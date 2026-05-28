# Paper 7 — OECD SOCX × homelessness correlation (PRE_REG_027 Prediction set A first fit)

**Fired**: 2026-05-27
**Pre-reg**: PRE_REG_027 (cross-country spending-allocation × SDP outcome)
**Data**: OECD SOCX aggregates 1980-2024, public expenditure % GDP, 43 countries; Phase 1 panel 16 countries × 6 metrics from earlier session
**Status**: First fit fired — Prediction set A SUPPORTED on 2/4 testable dimensions

---

## Headline

**Across OECD peer countries, public social-expenditure share of GDP correlates NEGATIVELY with homelessness rate per 100K (r = -0.503, n = 8), and military-spending share of GDP correlates POSITIVELY with homelessness rate (r = +0.852, n = 7).** Both directions match PRE_REG_027 H1 predictions. Both exceed the |r| ≥ 0.3 threshold; military correlation exceeds the |r| ≥ 0.5 threshold for the "at least 1 dimension" sub-condition.

**PRE_REG_027 Prediction set A SUPPORTED on 2 of 4 dimensions tested.** Match threshold "≥ 2 of 4 correlations in predicted direction with |r| ≥ 0.3" — MET.

---

## OECD SOCX latest-year social expenditure (% GDP)

Public social-expenditure aggregates, most-recent available year per country (2021-2024):

| Rank | Country | year | social_spend_pct_gdp |
|---:|---|:---:|---:|
| 1 | Austria | 2024 | **31.554** |
| 2 | Finland | 2024 | **31.437** |
| 3 | France | 2024 | 30.649 |
| 4 | Belgium | 2024 | 28.573 |
| 5 | Germany | 2024 | 27.854 |
| 6 | Italy | 2024 | 27.569 |
| 7 | Denmark | 2024 | 26.423 |
| 8 | Sweden | 2024 | 26.086 |
| 9 | Spain | 2024 | 25.871 |
| 10 | Japan | 2022 | 24.736 |
| … | (OECD average) | 2024 | 21.229 |
| — | **United States** | **2024** | **19.814** |
| — | Netherlands | 2024 | 18.873 |
| — | Norway | 2024 | 24.055 |
| — | Korea | 2024 | 15.326 |
| — | Costa Rica | 2022 | 12.644 |
| — | Mexico | 2023 | 10.034 |

US sits in lower-middle of OECD distribution at 19.814% — below OECD average (21.229%), well below European welfare states (Austria/Finland/France/Belgium ≥ 28%).

## Correlations on the merged Phase 1 panel (16 focus countries)

| Pair | r | n | Predicted direction | Match |
|---|---:|---:|---|---|
| social_spend_pct_gdp × homeless_per_100k | **-0.503** | 8 | NEG (≤ -0.3) | **✓ SUPPORTED** |
| military_pct_gdp × homeless_per_100k | **+0.852** | 7 | POS (≥ +0.3) | **✓ SUPPORTED** |
| public_housing_pct_gdp × homeless_per_100k | — | — | NEG (≤ -0.3) | DEFERRED (no public-housing-spend column yet) |
| health_pct_gdp × homeless_per_100k | not computed in run | — | NEG (≤ -0.2) | DEFERRED |

Both tested correlations exceed |r| ≥ 0.3 threshold. The military correlation also clears the |r| ≥ 0.5 "strongest single dimension" sub-condition.

### Notes on sample sizes
- n = 8 (social_spend) and n = 7 (military) reflect the intersection of OECD SOCX coverage with my 16-country focus panel's homelessness column. Smaller-than-ideal but adequate for first-fit directional signal. Power is limited; magnitude estimates should be read as orders-of-magnitude.

---

## US position in the joint distribution

Using SOCX (2024 social spend) + Phase 1 panel:

| Dimension | US value | Peer band | US position |
|---|---:|---|---|
| social_spend_pct_gdp | 19.814 | 24-32 (W. Europe), 24-26 (Japan/Nordic) | Lower-middle (above only S. America peers, Korea, Switzerland) |
| military_pct_gdp | 3.40 | 1.0-2.1 (peer OECD) | TOP |
| homeless_per_100k (Phase 1) | 196 | 3-82 (peer OECD) | TOP |

**US triple-position outlier check (Prediction set B):**
- Mil-spend top quartile: ✓ (3.40% vs peer band 1.0-2.1)
- Public-housing-spend bottom quartile: PENDING (HC3.1 has data context but not clean numerical breakout in extracted tables)
- Homelessness top quartile: ✓ (196/100K vs peer band 3-82, when measured on broad definition; see methodology note in `2026_05_27_phase1_homelessness_correction.md`)

**2 of 3 confirmed.** Public-housing-spend dimension remains pending OECD PH1 acquisition (HC3.1 covers homelessness counts, not housing-spending; PH1 is the housing-spend table).

---

## Falsifier status

| Falsifier | Status |
|---|---|
| F1 (all 4 correlations \|r\| < 0.2) | **NOT FIRED** (both tested correlations clear 0.5 and 0.3 respectively) |
| F2 (US not triple-outlier) | NOT FIRED (2/3 confirmed) |
| F3 (Finland trajectory fails) | NOT FIRED (separate Finland dig supports trajectory) |
| F4 (CR + Mauritius cases fail) | NOT FIRED (CR supports; MU partial) |
| F5 (any correlation sign-flips with \|r\| ≥ 0.3) | NOT FIRED (both signs match prediction) |

---

## Net result

**PRE_REG_027 Prediction set A: SUPPORTED on the 2 dimensions testable with currently-acquired data.** The framework's central revealed-preference claim — that state spending allocations correlate (in the predicted directions) with SDP outcomes — has empirical backing in this first fit.

Caveats:
- Correlation ≠ causation (locked at PRE_REG_025; never claimed)
- n = 7-8 is small; magnitudes are order-of-magnitude indicators, not point estimates
- The Phase 1 panel's homelessness column uses a broad definition (US 196/100K total), not OECD HC3.1's narrow definition. The methodology-correction document (`2026_05_27_phase1_homelessness_correction.md`) addresses this — under the narrow (unsheltered) definition US sits at 120/100K and remains a top-quartile outlier.
- The two missing dimensions (public-housing-spend, healthcare-spend) need OECD PH1 + OECD Health to complete the 4-correlation panel.

---

## Implications for the broader framework

The directional results so far align with what PRE_REG_025's revealed-preference hypothesis would expect:
- Countries that allocate more to **social spending** have lower SDP outcomes (negative correlation).
- Countries that allocate more to **military spending** have higher SDP outcomes (positive correlation).

This is the SDP framework's central empirical claim, and the testable portion fires SUPPORTED. The remaining dimensions (public-housing-spend, healthcare-spend) will sharpen or weaken the joint claim when added.

---

## Cross-references
- PRE_REG_027 (this dig's first fit)
- `2026_05_27_phase1_cross_country.md` (parent Phase 1 dig)
- `2026_05_27_phase1_homelessness_correction.md` (measurement methodology)
- `analysis/paper7_socx_correlation_2026_05_27.json` (raw output)
- `analysis/paper7_socx_merged_2026_05_27.csv` (merged panel)
- `data/paper7/oecd_socx/socx.csv` (source data)

## Status

**PRE_REG_027 Prediction set A first fit: SUPPORTED on 2/4 dimensions tested.** Falsifier F1 NOT FIRED. Sets B/C/D NOT FIRED across this session and the prior Finland dig.

**Paper 7 closure: 8/9 criteria** (up from 7 — adding "primary cross-country correlation tested and SUPPORTED").
