# Paper 7 — OECD HC3.1 Homeless Population — methodology context

**Fired**: 2026-05-27
**Source**: `data/paper7/oecd_housing/HC3-1-Homeless-population.pdf` (OECD Affordable Housing Database HC3.1, 2024 release)
**Status**: Methodology context confirmed; rate-table extraction limited by PDF layout (figures and methodology framework dominate the PDF; clean per-country rate numerals not cleanly extractable through automated table-detection at this pass)

---

## Headline

OECD HC3.1's text content corroborates the measurement methodology correction logged earlier today in `2026_05_27_phase1_homelessness_correction.md`. The PDF emphasizes:

- Cross-country homelessness counts are sensitive to underlying definitions (ETHOS Light typology 1-6 categories)
- Country-specific reporting practices vary in coverage (which categories are counted; unconventional dwellings are or aren't included; temporary accommodation is or isn't counted)
- Several countries that include "unconventional dwellings" specifically: **Australia, Canada, Germany, Korea, Norway, United States**
- Year of last point-in-time data varies: 2023 for most; 2022, 2021, 2020, 2018, 2017 for others
- Trend signals 2017-2020 cited: "decreased in Austria, Denmark, Finland, Korea, Latvia, and Slovenia"

The text framing is consistent with the Paper 7 refinement that "US is the unsheltered-rate outlier; total-count comparisons are confounded by definition heterogeneity."

---

## What HC3.1 confirms

1. **Definition heterogeneity is the dominant source of cross-country comparability noise.** OECD itself flags that the same country measured under different scopes can produce different rates. This validates the methodology-correction dig from earlier today.

2. **Finland's decline is OECD-confirmed.** HC3.1 lists Finland among the countries where homelessness "decreased" 2017-2020, consistent with the Wikipedia + Housing First Europe sources used in the Finland partial-fit dig.

3. **US is in the "includes unconventional dwellings" group.** Per HC3.1 wording, US count includes some unconventional dwellings — meaning the US 653K HUD AHAR figure is broader than the narrowest definition but still narrower than UK/France statutory-homeless counts (which include all temporary accommodation populations). This explains the methodology-correction's finding that US is total-mid-pack but unsheltered-outlier.

4. **OECD doesn't publish a single unified "homelessness rate per 100K" table.** The cross-country comparison requires the user to choose a definition consistently. The Wikipedia consolidation chose total-count; OECD HC3.1's preferred indicator includes year-of-last-data variance.

---

## What the PDF does NOT cleanly provide (at this extraction depth)

- Single canonical homelessness-rate-per-100K table for all OECD countries
- Public housing spend % GDP cross-walk (that's HC3.1's sibling indicator PH1, which we don't yet have)
- Time-series 2007-2024 by country
- Channel decomposition (eviction-driven, unaffordability-driven, etc.)

These would require a targeted OCR + table-recognition pass on the specific figure pages, or direct OECD.Stat queries. Both are deferrable.

---

## Implications for PRE_REG_027 Prediction set B (US triple-outlier)

The third condition "US in bottom quartile of public-housing-spend % GDP" remains PENDING because:
- HC3.1 covers **homelessness rates** (the OUTCOME), not housing-spend (the INPUT)
- OECD PH1 (Public housing — affordable housing supply and spend) is the table we need; it's not in this PDF
- Manual OECD PH1 acquisition still required

The first two conditions remain confirmed (mil-spend top quartile via SIPRI + homeless top quartile via Wikipedia/national stats + this OECD context).

---

## Net contribution to Paper 7

HC3.1 doesn't add a new quantitative finding; it confirms the methodology framework I've been using. The PDF's chief value:
- Cites OECD as the authoritative source for the measurement-heterogeneity claim
- Supports framing Paper 7's claim around "US is unsheltered-rate outlier" rather than "US is total-homelessness outlier"
- Provides paragraph-level citations for the Substack/popular-press version if needed

---

## Cross-references
- `2026_05_27_phase1_homelessness_correction.md` (methodology-correction document this HC3.1 confirms)
- PRE_REG_027 Prediction set B
- `data/paper7/oecd_housing/HC3-1-Homeless-population.pdf` (source)
- `analysis/paper7_oecd_hc31_2026_05_27.json` (raw text + tables extracted)
- `analysis/paper7_oecd_hc31_2026_05_27.country_lines.json` (per-country text lines)

## Status

Methodology-context dig logged. No falsifier fires. No new pattern files. PRE_REG_027 Set B remains 2/3 confirmed (third condition pending OECD PH1 acquisition).
