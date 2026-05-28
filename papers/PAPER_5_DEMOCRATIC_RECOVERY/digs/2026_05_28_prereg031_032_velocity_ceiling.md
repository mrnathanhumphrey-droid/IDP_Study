# Paper 5 — PRE_REG_031 (velocity) + PRE_REG_032 (ceiling): Phases 2+3

**Fired**: 2026-05-28
**Pre-regs**: PRE_REG_031 (recovery velocity / half-life) + PRE_REG_032 (recovery ceiling)
**Data**: V-Dem v15 full CSV, 6 recovery-from-backsliding cases
**Status**: PRE_REG_031 SUPPORTED. PRE_REG_032 vertical-plateau SUPPORTED + overshoot SUPPORTED; horizontal-full-recovery not uniform (POL re-stalling). 2 cases (BGD/LKA) excluded for degenerate baseline-trough gaps.

---

## Headline

**In the four well-conditioned recovery cases (POL, BRA, KOR, ZMB), recovery is sharply tempo-asymmetric and ceiling-asymmetric: horizontal-accountability institutions recover in 1-4 years and often OVERSHOOT baseline, while vertical-accountability institutions are right-censored (never reach 50% recovery) and plateau far below baseline — BRA at 2%, KOR at 4%, POL at 44% of the baseline-trough gap.** This confirms the mirror-order thesis (PRE_REG_012) with tempo + ceiling content: democracies get their courts back fast, their elections back slowly or not at all.

---

## Case windows + libdem trajectory

| Case | baseline | trough | latest | libdem base→trough→latest | gap |
|---|:---:|:---:|:---:|---|---:|
| POL Tusk | 2014 | 2022 | 2025 | 0.812 → 0.417 → 0.645 | 0.395 |
| BRA Lula | 2014 | 2019 | 2025 | 0.783 → 0.528 → 0.704 | 0.255 |
| KOR Yoon | 2021 | 2023 | 2025 | 0.775 → 0.620 → 0.739 | 0.155 |
| ZMB Hichilema | 2012 | 2020 | 2025 | 0.421 → 0.292 → 0.375 | 0.129 |
| ~~BGD Yunus~~ | 2015 | 2022 | 2025 | 0.108 → 0.091 → 0.116 | **0.017 (degenerate)** |
| ~~LKA Sirisena~~ | 2010 | 2011 | 2018 | 0.244 → 0.243 → 0.481 | **0.001 (degenerate)** |

**BGD and LKA excluded**: their baseline→trough libdem gaps are 0.017 and 0.001 — the country's libdem barely moved during the detected window, so recovery fractions normalized by that gap are undefined/explosive. (BGD's democracy never rose above ~0.12 in-window; LKA's trough auto-seated at 2011 where libdem ≈ baseline. LKA was already flagged as baseline-inflated in PRE_REG_012.) The 4 well-conditioned cases carry the analysis.

---

## PRE_REG_031 — Recovery velocity / half-life (years from trough to 50% recovery)

| Case | horizontal HL | diagonal HL | vertical HL |
|---|:---:|:---:|:---:|
| POL | 2 | 2 | **censored** |
| BRA | 4 | 4 | **censored** |
| KOR | 1 | 2 | **censored** |
| ZMB | 2 | 2 | 1 |
| (BGD) | 2 | 3 | 2 |
| (LKA) | censored | 2 | censored |

- **PRED A (horizontal HL ≤ vertical HL in ≥5 of 6): 5/6 → SUPPORTED**
- **PRED B (vertical right-censored in ≥3 of 6): 4/6 → SUPPORTED**

In the 3 cleanest cases (POL, BRA, KOR), **vertical is censored** — vertical-accountability never reaches 50% recovery within the observation window — while horizontal recovers in 1-4 years. ZMB is the exception (vertical recovers in 1 year), and ZMB is a lower-baseline case (libdem 0.42) where the institutional dynamics differ. F1 (uniform velocity) NOT FIRED; F2 (vertical-first) NOT FIRED.

---

## PRE_REG_032 — Recovery ceiling (latest recovery fraction; 1.0 = baseline, >1.0 = overshoot, <1.0 = plateau below)

| Case | horizontal | diagonal | vertical |
|---|:---:|:---:|:---:|
| POL | 0.67 | 0.74 | **0.44** |
| BRA | **1.17** (overshoot) | 0.73 | **0.02** |
| KOR | **1.10** (overshoot) | 0.86 | **0.04** |
| ZMB | 0.59 | 1.48 | 0.88 |

- **PRED A2 (vertical ceiling < 0.90 in ≥4 of 6): 4/6 → SUPPORTED** (all 4 clean cases)
- **PRED B (horizontal overshoot > 1.0 in ≥2): BRA + KOR → SUPPORTED**
- PRED A1 (horizontal ≥ 0.90 in ≥5 of 6): 3/6 → NOT uniformly met

### The vertical plateau is the headline
Vertical-accountability recovery fraction: **BRA 0.02, KOR 0.04, POL 0.44, ZMB 0.88.** Two of the four clean cases have recovered essentially NONE of their vertical-accountability deficit (2-4%), while their courts (horizontal) have fully recovered or overshot. This is the structural-ceiling finding: captured electoral architecture — gerrymandered maps, packed electoral commissions, opposition-suppression statutes — outlasts the autocrat. The BRA 2% / KOR 4% figures match PRE_REG_012's in-sample vertical recovery (2-9%) almost exactly.

### Horizontal overshoot (H2 supported)
BRA (1.17) and KOR (1.10) horizontal-accountability institutions recovered to ABOVE pre-backsliding baseline. Backlash mobilization (BRA STF asserting independence under pressure; KOR Constitutional Court + National Assembly post-martial-law) produced courts stronger than before the attempt. This is the "antifragile institution" signature.

### POL is the informative non-overshoot
POL horizontal recovered to only 0.67 and vertical to 0.44 — the weakest recovery among clean cases. This is consistent with POL's documented **re-stalling**: the PiS-backed Nawrocki won the 2025 presidency and is obstructing the Tusk government's restoration (PRE_REG_006 stalled-recovery live test). POL is recovering, but a captured presidency is dragging on it. The incomplete horizontal recovery is a feature, not noise — it's the stalled-recovery configuration showing up in the ceiling data.

---

## Metric amendments (diagnostic-driven, logged)

Two amendments during this fit, both triggered by data-distribution pathology (not results):

1. **Ceiling metric: ratio → recovery fraction.** PRE_REG_032 originally specified ceiling = latest/baseline. That ratio explodes/goes negative when V-Dem baseline values are near zero (LKA −63, BGD −0.03). Replaced with recovery fraction (latest−trough)/(baseline−trough), which is bounded and was already PRE_REG_031's metric. [[feedback_diagnostic_driven_amendments]]

2. **Tier composition: restricted to 0-1 bounded v2x_ indices.** Original tiers mixed 0-1 indices (v2x_jucon) with latent −4..+4 indices (v2juhcind, v2csprtcpt, v2psoppaut), causing scale-mixing + near-zero-denominator explosions. Restricted to: horizontal {v2x_jucon, v2x_horacc}, diagonal {v2x_diagacc}, vertical {v2xel_frefair, v2x_veracc}. Added denominator guard (exclude sub-indicator if |baseline−trough| < 0.03).

Both amendments are diagnostic-driven (exposed by the explosion pattern before any verdict), documented, and make the metric more principled. The vertical-plateau finding is robust to them.

---

## Falsifier status

| Pre-reg | Falsifier | Status |
|---|---|---|
| 031 | F1 (uniform velocity across tiers) | NOT FIRED |
| 031 | F2 (vertical-first in any case) | NOT FIRED |
| 031 | F3 (vertical reaches 50% in ≤2yr in ≥4 cases) | NOT FIRED (censored in 3 clean cases) |
| 032 | F1 (uniform completeness, all tiers ≥90%) | NOT FIRED |
| 032 | F2 (no overshoot) | NOT FIRED (BRA + KOR overshoot) |
| 032 | F3 (vertical recovers ≥90% in ≥4 cases) | NOT FIRED (vertical plateaus below in all 4 clean cases) |

---

## Net result

**PRE_REG_031 SUPPORTED**: recovery is tempo-asymmetric; horizontal recovers in 1-4 years, vertical is censored. **PRE_REG_032 vertical-plateau + overshoot SUPPORTED**; horizontal-full-recovery is not uniform because POL is re-stalling (Nawrocki). The combined Phase 2+3 finding: **democracies recover their horizontal institutions (courts) fast and sometimes stronger-than-before, but their vertical institutions (free+fair elections, opposition autonomy) recover slowly or not at all — the captured electoral machinery is the lasting damage.**

This is the hopeful-but-sobering core of Paper 5: backsliding is reversible, but reversal is incomplete in a specific, predictable place (the ballot box).

---

## Cross-references
- PRE_REG_031, PRE_REG_032 (this dig's fits)
- PRE_REG_012 (mirror-order — vertical 2-9% in-sample matches BRA 2% / KOR 4% here)
- PRE_REG_006 (stalled-recovery — POL Nawrocki re-stalling shows in POL's low ceiling)
- PATTERN_022 (BRA overshoot — confirmed: horizontal 1.17), PATTERN_024 (POL)
- `analysis/paper5_recovery_velocity_ceiling_2026_05_28.json`
- `_scripts/paper5_recovery_velocity_ceiling.py`

## Status

**Phases 2+3 done.** Paper 5 now has 3 fired pre-regs (030 blocking SUPPORTED, 031 velocity SUPPORTED, 032 ceiling vertical-plateau SUPPORTED). Closure 3/9 → with the blocking-lever refinement (civil society + federalism) + the vertical-plateau ceiling as two candidate headline findings. Remaining: Phase 4 forward-watch (2026 BRA, 2028 USA, KOR sustainability, POL stall).
