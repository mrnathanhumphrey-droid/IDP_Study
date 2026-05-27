# Paper 6 — Hunt Plan

**Last updated**: 2026-05-27
**Purpose**: structured thread-pulling for Paper 6 (methodology / channel-orthogonality + residue-class).

---

## Workflow per thread

1. **Pick** highest-priority open thread
2. **Pre-reg lock** if testing a new hypothesis (slots 022/023/024)
3. **Stan model + fit / data pull / analysis**
4. **Findings to dig** — write to `digs/2026_MM_DD_P6_X_short_title.md`
5. **Update status** in this file + THREADS_REGISTER
6. **Update PAPER_6_SCOPE.md** closure criteria checkboxes

---

## Thread board

### Active hunt — Phase 1 (residue-class Stan fit)

| ID | Status | Title | Effort | Next step |
|---|---|---|---|---|
| **PRE_REG_022** | pending lock | Residue-class Stan model outperforms classical hierarchical baseline | Pre-reg | Write Stan model spec + LOO-CV / WAIC comparison plan; lock predictions before fitting |
| P6-B | open | Fit Stan residue-class model on full corpus | Heavy | Use Papers 2 + 4 type assignments as class labels; country-year × class generative model |
| P6-C | open | Compare residue-class to no-typology baseline | Medium | LOO-CV / WAIC + R² + posterior predictive checks |

### Hunt — Phase 2 (admin-1 + cross-paper unification)

| ID | Status | Title | Effort | Next step |
|---|---|---|---|---|
| **PRE_REG_023** | pending lock | Channel-orthogonality at admin-1 sub-national level | Pre-reg | Lock predictions BEFORE running on admin-1 panels |
| P6-D | open | Admin-1 sub-national orthogonality test | Medium-heavy | Some admin-1 panels exist (COD NK/Ituri, MLI Mopti, ETH Tigray); need to construct sub-national channel decomposition |
| P6-E | open | Cross-paper unification synthesis writeup | Light | Argue Papers 2 + 4 + 6 form coherent framework |

### Hunt — Phase 3 (forward validation)

| ID | Status | Title | Effort | Next step |
|---|---|---|---|---|
| **PRE_REG_024** | pending lock | Forward-prediction residue-class outperforms no-typology baseline | Pre-reg | Lock forward window predictions for 2025-2027 |
| P6-F | open | Forward-watch fires when 2025-2027 data arrives | forward-watch | UCDP-GED + GIDD 2025/2026/2027 releases |

### Optional / sidebar

| ID | Status | Title | Notes |
|---|---|---|---|
| P6-G | open | Within-type slope heterogeneity test | Test whether all members of Type B have same DPF response to attack intensity |
| P6-H | open | HTI multi-paper case (Type B + Regime 6) | Multi-paper interaction; methodological |
| P6-I | open | Bayesian model comparison framework | Posterior checks + Bayes factors |

---

## Pre-reg slot status

| Slot | Topic | Status | Block on |
|---|---|---|---|
| PRE_REG_022 | Residue-class Stan model | NOT LOCKED | Write Stan model spec first |
| PRE_REG_023 | Admin-1 sub-national orthogonality | NOT LOCKED | Lock before admin-1 test |
| PRE_REG_024 | Forward-prediction validation | NOT LOCKED | Lock forward window before 2025-2027 data arrives |

---

## Data acquisition status

| Source | For | Status |
|---|---|---|
| UCDP-GED v25 | P6-B, P6-D | In hand |
| GIDD conflict + disaster | P6-B, P6-D | In hand |
| Admin-1 panels (COD/MLI/ETH/SDN/BFA) | P6-D | Partial — some exist from Phase 1/Paper 4 |
| V-Dem v15 | P6-B covariates | In hand (Paper 1 substrate) |
| Stan / PyMC | P6-B compute | Need to verify install + compute window |

---

## Methodology infrastructure to build

- [ ] Stan residue-class model code (`stan_models/residue_class.stan`)
- [ ] Stan baseline hierarchical model code (`stan_models/baseline.stan`)
- [ ] LOO-CV / WAIC comparison wrapper
- [ ] Posterior predictive check plots
- [ ] Admin-1 channel decomposition pipeline

---

## Closure summary

**Phase 1 complete when**: PRE_REG_022 locked + Stan fit succeeds + LOO-CV shows residue-class outperforms baseline
**Phase 2 complete when**: admin-1 orthogonality test fired (PRE_REG_023) + cross-paper synthesis written
**Phase 3 complete when**: forward-prediction framework locked (PRE_REG_024)
**Paper-draftable when**: 9/9 closure criteria from PAPER_6_SCOPE.md Section 6 met

**Current state**: 3/9 criteria met (substrate from Papers 2 + 4 in hand).
