# Paper 7 — Eviction Lab 2020-2021 partial fit (PRE_REG_026 channel-orthogonality)

**Fired**: 2026-05-27
**Source**: Eviction Lab Eviction Tracking System — monthly + weekly state-aggregated tract data, 2020-2021 only (`data/paper7/eviction_lab/`)
**Pre-reg**: PRE_REG_026 (US SDP channel-orthogonality, especially Prediction set B state-channel mapping)
**Status**: Coverage gap — Eviction Lab Tracking System covers ~10 states; none of the 8 states named in PRE_REG_026 Set B appear in the dataset

---

## Headline

**Eviction Lab's 2020-2021 public Eviction Tracking System covers 10 states (MN, MO, IN, WI, PA, CT, RI, NM, VA, DE). None of the 8 states named in PRE_REG_026 Prediction set B (CA, NY, MS, TX, FL, LA, MA, MI) are present.** This is a data-coverage limit, not a falsifier firing. The test cannot be run on PRE_REG_026 Set B until either (a) Eviction Lab's broader pre-pandemic county-level dataset is obtained or (b) state-specific eviction-record acquisitions cover the named states.

---

## State coverage (10 states) — per-state filings_2020 vs prepandemic-baseline ratio

77 months observed per state (2020-2021 + 2019 baseline months):

| Rank | State | filings_2020_sum | baseline_sum | ratio_2020_vs_baseline |
|---:|---|---:|---:|---:|
| 1 | Minnesota | 118,096 | 101,143 | **1.168** |
| 2 | Missouri | 253,976 | 254,015 | 1.000 |
| 3 | Indiana | 403,487 | 437,231 | 0.923 |
| 4 | Wisconsin | 151,212 | 166,343 | 0.909 |
| 5 | Pennsylvania | 602,907 | 684,611 | 0.881 |
| 6 | Connecticut | 102,429 | 118,106 | 0.867 |
| 7 | Rhode Island | 41,226 | 49,780 | 0.828 |
| 8 | New Mexico | 78,449 | 101,623 | 0.772 |
| 9 | Virginia | 676,610 | 975,682 | 0.693 |
| 10 | Delaware | 65,821 | 105,324 | 0.625 |

The ratio reflects 2020-2021 filings (during pandemic moratoria) vs the prepandemic 2016-2019 baseline. Most states are below 1.0 — consistent with moratorium suppression. Minnesota's >1.0 is anomalous and worth noting; it lacked the same moratorium continuity as some other states.

---

## PRE_REG_026 Prediction set B — cannot be tested at this data coverage

The pre-reg's predicted state → channel map:

| State | Predicted dominant channel | Observed in this dataset? |
|---|---|:---:|
| CA | Unaffordability | NO |
| NY | Eviction | NO |
| MS | Institutional/DV | NO |
| TX | Disaster + Unaffordability | NO |
| FL | Disaster + Unaffordability | NO |
| LA | Disaster + Institutional | NO |
| MA | Unaffordability | NO |
| MI | Eviction + Institutional | NO |

**0 of 8 predicted states present in Eviction Lab Tracking System 2020-2021.** The test cannot fire on Prediction set B with this data.

---

## What the data DOES support

The data covers a different question — pandemic-period eviction filings vs prepandemic baseline in 10 states. This is informative for:

- **Channel-1 (Eviction-driven SDP)** trajectory during a known moratorium-protected window
- **Within-window state heterogeneity**: even within a 10-state subset, the ratio range (0.625 to 1.168) spans nearly 2× — suggesting state-level moratorium implementation + filings practices varied substantially
- **Minnesota outlier**: only state where 2020 filings EXCEEDED prepandemic baseline. Notable.

These observations are valid but DON'T address the orthogonality + state-channel-mapping predictions in PRE_REG_026.

---

## What would unblock PRE_REG_026

To fully fire PRE_REG_026 Set B:
- **Eviction Lab county-level archive** 2007-2018 (the full Eviction Lab dataset, not just the pandemic-era Tracking System) — would cover CA/NY/TX/FL/LA/MS/MA/MI
- **HUD AHAR PIT counts** 2007-2024 by CoC for state-level homelessness aggregation
- **ACS housing cost-burdened share** 2007-2024 by state

The HUD AHAR 2024 Part 1 PDF is locally available at `data/paper7/hud_ahar/2024-AHAR-Part-1.pdf` and could provide PIT counts but doesn't itself address the channel-orthogonality question without HMIS-level detail.

---

## Falsifier status

| Falsifier | Status |
|---|---|
| F1 (orthogonality < 40%) | NOT TESTABLE (data doesn't permit channel decomposition for the named states) |
| F2 (state mapping random — < 4 of 9) | NOT TESTABLE (0 of 8 named states present) |
| F3 (no residue-class structure) | NOT TESTABLE (need broader state coverage) |

**No falsifiers fire; none can be tested with this data.** PRE_REG_026 first fit remains DEFERRED pending broader Eviction Lab acquisition.

---

## Net result

**Coverage-limited deferral.** The data we have is high-quality and well-organized but covers a state set that doesn't intersect the pre-reg's named-state predictions. This is the cleanest possible "data acquisition not yet sufficient" outcome — no goalpost movement; no spurious channel mapping invented from off-pre-reg states.

Logging Minnesota's >baseline 2020 filings as a sub-finding worth follow-up: it's the only state in the 10-state coverage where 2020 filings exceeded prepandemic baseline despite the pandemic moratorium. Possible reasons: weaker state-level moratorium, larger pre-existing eviction crisis, or counting methodology differences. Filed for later attention; not a paper-7 finding by itself.

---

## Cross-references
- PRE_REG_026 (this fit deferred)
- `analysis/paper7_eviction_lab_2026_05_27.json` (raw output)
- `analysis/paper7_eviction_per_state_2026_05_27.csv` (per-state aggregates)
- `data/paper7/eviction_lab/` (source files; 4 files, 692 MB total)

## Status

PRE_REG_026 first fit DEFERRED — coverage gap. No pattern files generated. No falsifier fires. The dataset's value to Paper 7 is contextual (pandemic-period eviction dynamics in 10 states) rather than test-firing for the pre-reg's named state mapping.
