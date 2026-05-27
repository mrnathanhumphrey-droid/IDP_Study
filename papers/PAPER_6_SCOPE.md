# Paper 6 — Scope Lock (2026-05-27)

**Working title (internal)**: Channel-Orthogonality Framework + Residue-Class Methodology — a unified methodology for cross-country displacement modeling

**Status**: SUBSTRATE EXISTS via Papers 2 + 4. Framework articulated but never formally fit. Hunt = Stan residue-class fit + cross-paper unification.

**User writes prose; this doc is analytical scope only.**

---

## 1. Mechanism + methodology claim

Displacement data is **structurally heterogeneous** across countries — not statistical noise. Two parallel typology arguments support this:

- **Paper 2**: Disaster-displacement decomposes into 6 regimes (physical geography)
- **Paper 4**: Conflict-displacement decomposes into 5 types (organizational form of violence)

Paper 6 unifies these into a **methodology framework**:

> **Channel-orthogonality**: at the country-year level, displacement decomposes into orthogonal channels (conflict / disaster / disaster-sub-channels). Within each channel, structural variation across countries is captured by residue-classes (disaster regimes for the disaster channel; conflict types for the conflict channel).

> **Residue-class partial-pooling**: classical hierarchical models pool countries via continuous covariates (GDP, population, governance). The residue-class framework pools countries via DISCRETE TYPE membership. Each type has its own intercept + slope; partial pooling within type captures the cross-country variation that a single global model misses.

**Load-bearing methodological claim**: corpus heterogeneity is typology, not noise. Modeling without residue-classes systematically under-fits.

---

## 2. Substrate (the load-bearing artifacts)

### Patterns
- **PATTERN_001 family** (001/004/007/008/009/010/011/017/018/021/023) — channel-orthogonality framework
- **PATTERN_019/020/025/028/029/030** — disaster regimes (Paper 2 substrate)
- **PATTERN_012/015/017/031/032/033** — conflict types (Paper 4 substrate)

### Pre-regs
- **PRE_REG_004** — 3-channel orthogonality (locked + supported 92%)
- **PRE_REG_022** (proposed) — Residue-class Stan model outperforms classical hierarchical model
- **PRE_REG_023** (proposed) — Channel-orthogonality holds at admin-1 sub-national level
- **PRE_REG_024** (proposed) — Forward-prediction with residue-class beats no-typology baseline

### Cross-paper unification claims (Papers 2 + 4 → Paper 6)
- Both papers argue "corpus heterogeneity is typology, not noise"
- Paper 6 formalizes this as a STATISTICAL MODELING FRAMEWORK
- Provides theoretical justification for why classical hierarchical models under-fit displacement data

---

## 3. The methodology framework (3 layers)

### Layer 1 — Channel decomposition
Displacement at country-year level decomposes into:
- Conflict channel (UCDP-GED + GIDD conflict-displacement)
- Flood channel (GIDD disaster-flood)
- Storm channel (GIDD disaster-storm)
- Drought sub-channel (GIDD disaster-drought; orthogonal to conflict)
- Earthquake channel (GIDD disaster-EQ)
- Wildfire sub-channel (potential 7th regime)

**Channel-orthogonality (PRE_REG_004 supported)**: 92% of country-years show ≤1 channel firing meaningfully (>50% of total displacement).

### Layer 2 — Residue-class typing within each channel
- **Disaster channel** → 6 regimes (PATTERN_019/020/025)
- **Conflict channel** → 5 types (PRE_REG_018 v2)
- **Within each class**: countries share a generative process (mechanism-distinct)

### Layer 3 — Partial-pooling Stan model
- Country-year displacement = f(channel × class × covariates)
- Stan model: hierarchical with class-level intercepts + slopes
- Partial pooling within class; no pooling across class
- Compare against classical models (no typology) using LOO-CV or WAIC

---

## 4. OPEN threads — HUNT plan

### Critical-path (must close before submission)

| ID | Thread | What closes it | Effort |
|---|---|---|---|
| **P6-A** | Lock PRE_REG_022 residue-class Stan model | Define Stan model + LOO-CV vs baseline comparison | Pre-reg |
| **P6-B** | Fit Stan residue-class model on full corpus | Use Papers 2 + 4 type assignments as classes | Heavy — Stan compilation + sampling |
| **P6-C** | Compare to baseline (no-typology hierarchical) | LOO-CV / WAIC + R² + predictive checks | Medium |
| **P6-D** | Admin-1 sub-national orthogonality test (PRE_REG_023) | Requires admin-1 panels (some exist: NK/Ituri for COD; Mopti for MLI etc.) | Medium-heavy |
| **P6-E** | Cross-paper unification synthesis | Argue Papers 2 + 4 + 6 form coherent framework | Light |
| **P6-F** | Forward-prediction validation (PRE_REG_024) | 2025-2027 V-Dem + GIDD + UCDP — residue-class outperforms baseline | Forward-watch |

### Optional / sidebar

| ID | Thread | Notes |
|---|---|---|
| P6-G | Within-type slope heterogeneity test | Do all members of Type B have same DPF response to attack intensity? |
| P6-H | Cross-class interaction (HTI Regime 6 + Type B) | Multi-paper case; methodological |
| P6-I | Bayesian model comparison framework | Posterior predictive checks + bayes factors |

---

## 5. Novel contributions (proposed; 4)

1. **Channel-orthogonality framework** — formalization of orthogonal-channel decomposition for displacement modeling. Argues displacement IS decomposable rather than entangled.
2. **Residue-class partial-pooling** — alternative to continuous-covariate hierarchical pooling. Pool by discrete-type membership when the structure is typological.
3. **Twin-typology unification** — Papers 2 + 4's parallel typology arguments unified under one methodology. "Corpus heterogeneity is typology, not noise" demonstrated on both disaster + conflict sides.
4. **LOO-CV evidence of typology improvement** — empirical demonstration that residue-class outperforms baseline in held-out predictive performance.

---

## 6. Closure criteria for Paper 6

The paper is ready to draft when:
- [x] PATTERN_001 family + channel-orthogonality framework articulated (DONE)
- [x] Paper 2 disaster typology established (DONE)
- [x] Paper 4 conflict typology established (DONE)
- [ ] PRE_REG_022 residue-class Stan model pre-reg locked (P6-A)
- [ ] Stan model fit on full corpus (P6-B)
- [ ] LOO-CV / WAIC vs baseline computed (P6-C)
- [ ] Admin-1 sub-national orthogonality tested (P6-D + PRE_REG_023)
- [ ] Cross-paper unification synthesis written (P6-E)
- [ ] Forward-prediction validation framework locked (PRE_REG_024)

**Current state: 3 of 9 criteria met (substrate from Papers 2 + 4 already in hand).**

---

## 7. Cross-paper interfaces

| With Paper... | Interface | Note |
|---|---|---|
| Paper 1 (executive-aggrandizement) | libdem variable as covariate within types | Subordinate to typology classification |
| Paper 2 (disaster regimes) | 6-regime typology IS the residue-class structure for disaster channel | Anchor input |
| Paper 4 (conflict-types) | 5-type typology IS the residue-class structure for conflict channel | Anchor input |
| Paper 3 (strife epicenter) | Type C irregular insurgency intersection | Subordinate sub-claim |

**Paper 6 is the methodology unification of Papers 2 + 4.** Could be presented as joint paper or as supplementary methodology framework.

---

## 8. Sequencing recommendation

Order to chase threads:

1. **PRE_REG_022 lock** (residue-class Stan model design) — lock BEFORE fitting
2. **P6-B Stan fit** — substantial compute lift; expect Stan compile time + sampling
3. **P6-C LOO-CV vs baseline** — light once Stan fit succeeds
4. **PRE_REG_023 + P6-D admin-1 orthogonality** — parallel work
5. **P6-E cross-paper unification synthesis** — light, writing-heavy
6. **PRE_REG_024 forward-prediction lock** — forward-watch only

Phase 1 = P6-A + P6-B + P6-C (Stan fit + comparison)
Phase 2 = P6-D admin-1 + P6-E unification
Phase 3 = PRE_REG_024 forward validation

---

**Status: substrate from Papers 2 + 4 ready. Hunt plan defined. Phase 1 = Stan residue-class model fit + LOO-CV comparison.**
