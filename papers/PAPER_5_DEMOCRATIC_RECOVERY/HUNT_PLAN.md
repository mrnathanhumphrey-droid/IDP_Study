# Paper 5 — Hunt Plan

## Phase 1 — Blocking-lever predictive model (PRE_REG_030)
**Goal**: formalize the 4-lever score and test the ≥3-blocks decision rule.
- Score every corpus country-episode on the 4 levers (court independence, civil-society capacity, electoral cycle reach, federal/regional parallel power)
- Operationalize each lever from V-Dem sub-indicators where possible (hcind/jucon for court; v2cseeorgs/v2csprtcpt for civil society; regularized election timing; v2elreggov/federalism index for parallel power)
- Test: does lever-count ≥3 separate the 5 blocked from the 7 consolidated cases? Out-of-sample: score additional countries and predict
- **Falsifier**: lever-score doesn't separate blocked from consolidated → model is post-hoc

## Phase 2 — Recovery velocity / half-life (PRE_REG_031)
**Goal**: quantify the tempo asymmetry across tiers.
- Year-by-year recovery deltas per sub-indicator across the 6 recovery cases (POL/BRA/KOR/BGD/Sri Lanka/ZMB)
- Compute per-tier recovery half-life (years to reach 50% of baseline-trough gap)
- **Predicted**: horizontal half-life << vertical half-life
- **Falsifier**: uniform half-lives across tiers → no sequence effect

## Phase 3 — Recovery completeness / ceiling (PRE_REG_032)
**Goal**: do recoveries return to baseline, overshoot, or plateau below?
- Per case: baseline (pre-backsliding) → trough → recovery-ceiling (latest)
- BRA overshot (0.608 baseline → 0.712); does this generalize or is BRA special?
- **Predicted**: horizontal/diagonal tiers reach ≥90% of baseline; vertical tier plateaus below
- **Falsifier**: all tiers uniformly reach baseline → no structural ceiling

## Phase 4 — Forward-watch
- 2026 BRA election (Bolsonaro return → lever-test)
- 2028 USA election (the natural reset window)
- KOR sustainability (2027 V-Dem release)
- ISR judicial-overhaul reactivation post-Gaza (watch hcind 2026)
- POL stalled-recovery live test (PRE_REG_006; Nawrocki PiS-backed presidency 2025)
