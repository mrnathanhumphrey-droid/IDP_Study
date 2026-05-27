# Paper 6 — Methodology / Channel-Orthogonality + Residue-Class Framework

**Locked**: 2026-05-27
**Status**: substrate exists (Papers 2 + 4 anchors); Stan fit not yet executed
**Scope doc**: [../PAPER_6_SCOPE.md](../PAPER_6_SCOPE.md)

## What this paper argues (analytical, not prose)

Displacement data is **structurally heterogeneous** across countries — not statistical noise. Two parallel typology arguments (Paper 2 disaster regimes + Paper 4 conflict types) support this. Paper 6 unifies into a **methodology framework**:

1. **Channel-orthogonality**: country-year displacement decomposes into orthogonal channels (conflict / flood / storm / EQ / drought / wildfire). PRE_REG_004 supports 92% orthogonality.
2. **Residue-class typing**: within each channel, structural variation is captured by discrete TYPE membership (regimes for disaster; types for conflict).
3. **Partial-pooling Stan model**: countries pool by type, not by continuous covariate. Each type has its own intercept + slope.

**Load-bearing claim**: corpus heterogeneity is typology, not noise. Modeling without residue-classes systematically under-fits.

## Folder map

- `README.md` — this file
- `digs/` — thread closures
- `literature/` — methodology positioning (Stan / Bayesian hierarchical lit; typology lit)
- `figures/` — posterior plots, LOO-CV comparisons
- `stan_models/` — Stan model code (residue-class + baseline)
- `data_notes/` — data provenance

## Pre-regs in scope

- **PRE_REG_004** (locked + supported 92% orthogonality)
- **PRE_REG_022** (proposed) — Residue-class Stan model outperforms classical hierarchical baseline
- **PRE_REG_023** (proposed) — Channel-orthogonality holds at admin-1 sub-national level
- **PRE_REG_024** (proposed) — Forward-prediction residue-class outperforms no-typology baseline

## Patterns in scope

**Channel-orthogonality substrate** (PATTERN_001 family):
- PATTERN_001/004/008/010/011/017/018/021/023

**Typology substrate (residue-class structure)**:
- Paper 2: PATTERN_019/020/025/028/029/030 (6 regimes)
- Paper 4: PATTERN_012/015/017/031/032/033 (5 types)

## Substrate inputs from Papers 2 + 4

From Paper 2 (disaster regimes; 6 regimes / 30 confirmed members):
- Regime 1 (PAK, THA candidate)
- Regime 2 (IND)
- Regime 3a/3b (8 storm-dominant members)
- Regime 4 (6 mixed members)
- Regime 6 (6 EQ-dominant)
- Regime 7 candidate (GRC wildfire)

From Paper 4 (conflict types; 5 types / 34 classified):
- Type A formal-army (6 members)
- Type B predator-militia (3)
- Type C irregular insurgency (5 + sub-types)
- Type D criminal-violence (3)
- Type E civil-war-mass-displacement (17)

## Hunt order (sequencing from scope doc)

1. **PRE_REG_022 lock** — Stan model design
2. **P6-B** — Fit Stan residue-class model
3. **P6-C** — LOO-CV / WAIC vs baseline
4. **PRE_REG_023 + P6-D** — admin-1 orthogonality (parallel)
5. **P6-E** — cross-paper unification synthesis
6. **PRE_REG_024** — forward-prediction lock

## Cross-paper interfaces

- Paper 2 + Paper 4 are the typology substrate inputs
- Paper 1 (libdem) becomes a covariate within types
- Paper 3 (strife epicenter) is subordinate Type C analysis
- Paper 6 IS the methodology unification

## Reading list when drafting

1. `PAPER_6_SCOPE.md` — anchor
2. `PAPER_2_SCOPE.md` + `SYNTHESIS_PAPER2_2026_05_25.md`
3. `PAPER_4_SCOPE.md` + `SYNTHESIS_PAPER4_2026_05_27.md`
4. `PRE_REG_004_three_channel_orthogonality.md`
5. `D:/IDP/patterns/001_sahel_two_channel_displacement/README.md`
6. `D:/IDP/papers/PAPER_6_METHODOLOGY/digs/*` (will populate)

---

**Next action**: lock PRE_REG_022 (residue-class Stan model design), then fit.
