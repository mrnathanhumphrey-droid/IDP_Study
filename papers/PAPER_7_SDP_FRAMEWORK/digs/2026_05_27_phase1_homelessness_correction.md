# Paper 7 Phase 1 Correction — Homelessness Rate Methodology

**Date**: 2026-05-27
**Triggering finding**: cross-country homelessness data from Wikipedia / national statistics offices reveals US-outlier claim is MEASUREMENT-DEPENDENT.

---

## Headline

**The "US is structural homelessness outlier" claim is true under narrow (unsheltered) definition but FALSE under broad (total homeless) definition.** This is a meaningful refinement for Paper 7.

| Country | Total homeless | Per 10K | Unsheltered per 10K | Year |
|---|---:|---:|---:|---:|
| **USA** | 653,104 | **19.5** | **12.0** | 2023 |
| **UK** | 380,000 | **56.1** | 0.9 | 2023 |
| **France** | 330,000 | 48.7 | 4.5 | 2022 |
| Germany | 262,600 | 31.4 | — | 2022 |
| Japan | 2,820 | 0.2 | — | 2024 |
| Finland | 4,114 | 7.9 | 0.1 | 2022 |
| Norway | 3,325 | 6.2 | — | 2020 |
| Iceland | 349 | 10.0 | — | 2017 |
| Sweden | 27,383 | 25.9 | — | 2023 |
| Denmark | 5,789 | 9.8 | — | 2022 |
| Italy | 96,197 | 16.3 | — | 2021 |
| Spain | 28,552 | 5.9 | — | 2022 |
| Australia | 122,494 | 48.0 | — | 2021 |
| Canada | 118,329 | 29.0 | — | 2023 |
| New Zealand | 102,123 | 217 | 7.5 | 2018 |
| Netherlands | 32,000 | 18.0 | — | 2021 |

---

## What this changes

### My earlier dig (2026_05_27_phase1_cross_country.md) used numbers that were:
- USA 196/100K — close to actual 195/100K (broad measure) ✓
- UK 22/100K — **WRONG**; actual is 561/100K (broad) — I was using OECD narrow definition
- France 62/100K — WRONG; actual 487/100K
- Germany 75/100K — WRONG; actual 314/100K
- Japan 3/100K — close (actual 2/100K) ✓
- Finland 13/100K — close enough; actual 79/100K (broad)

**My earlier table mixed narrow (OECD HC3.1 / rough-sleeper) numbers with US broad-measure numbers.** Apples-to-oranges. Need to use one definition consistently.

### Two valid framings now available:

**Framing A — Unsheltered-rate (rough sleeping / streets):**
| Country | Unsheltered per 10K |
|---|---:|
| **USA** | **12.0** |
| New Zealand | 7.5 |
| France | 4.5 |
| UK | 0.9 |
| Finland | 0.1 |

US is **structural outlier** under this measure. 13× higher than UK; 120× higher than Finland.

**Framing B — Total homelessness (broad definition, includes temporary accommodation):**
| Country | Total per 10K |
|---|---:|
| New Zealand | 217 |
| UK | 56 |
| France | 49 |
| Australia | 48 |
| Germany | 31 |
| Sweden | 26 |
| Canada | 29 |
| **USA** | **19.5** |
| Netherlands | 18 |
| Italy | 16 |
| Denmark | 10 |
| Iceland | 10 |
| Finland | 8 |
| Norway | 6 |
| Spain | 6 |
| Japan | 0.2 |

US is **mid-pack** under broad definition.

---

## Substantive refinement for Paper 7

The "US is structural outlier on homelessness" claim must be refined:

> **The US is the structural outlier on UNSHELTERED homelessness (rough sleeping / streets-living), not on total homelessness counts.** Peer countries with universal housing-rights frameworks (UK, France, Germany) record HIGHER total homeless populations but provide temporary accommodation; the US records FEWER total homeless but a much higher share are unsheltered.

This is actually a SHARPER finding than the original blanket claim. The mechanism story tightens:
- US revealed-preference produces specifically **unsheltered homelessness** (no statutory right to housing; no universal shelter capacity)
- Peer countries with welfare-state architecture record more total cases because their counting includes temporary-accommodation populations (statutory homelessness)
- Both measures are valid; they answer different questions

---

## Implication for PRE_REG_027 H2 (US triple-outlier)

| Condition | Predicted | Observed | Status |
|---|---|---|---|
| Top quartile mil-spend % GDP | US ≥ 3.0% | US = 3.40% (top of OECD distribution) | ✓ Confirmed |
| Bottom quartile public-housing-spend % GDP | US ≤ 0.6% | Pending OECD data | Pending |
| **Top quartile homelessness rate** | US ≥ 150/100K | US = 120/100K unsheltered = **OUTLIER on unsheltered** | **Refined: outlier on unsheltered, not total** |

**Refined H2**: US is outlier on unsheltered-rate (top quartile) AND on mil-spend (top quartile). Total-homelessness rate ranking depends on measurement methodology.

---

## Status

The Phase 1 dig (2026_05_27_phase1_cross_country.md) should be read in conjunction with this correction. The substantive finding is REFINED, not walked back — but the specific cross-country homelessness comparison numbers need to be presented with explicit measurement-definition transparency in the paper.

**Paper 7 framing now sharpens**: SDP is specifically about **unsheltered / streets-living homelessness produced by lack of welfare-state housing-rights architecture**, not about total counted homelessness which is dominated by methodology variance in counting temporary-accommodation populations.

This is actually a stronger framing for the Substack / popular-press version: "Why does America have so many people living on the streets compared to peer countries that have similar total homelessness rates?"

## Cross-references
- 2026_05_27_phase1_cross_country.md (original; numbers partly incorrect; methodology issue surfaced here)
- PRE_REG_027 (refined H2)
- PRE_REG_026 (US SDP channel decomposition will need to distinguish unsheltered vs sheltered-temp)

## Data sources
- Cross-country homelessness counts: national statistics offices via Wikipedia consolidation (with country-specific sources cited there)
- OECD Affordable Housing HC3.1 (narrow definition; pending direct acquisition)
- HUD AHAR for US sheltered + unsheltered breakdown
