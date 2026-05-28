# Paper 8 — Scope Lock (2026-05-28)

**Working title (internal)**: Compound-Crisis Coupling — when displacement channels stop being orthogonal

**Status**: PROMOTED 2026-05-28 from substrate. Grows directly out of PRE_REG_004's F2 yellow flag (unpredicted conflict-drought couplings in BRA + ETH beyond the pre-specified SOM/SDN). Open hunt = characterize the coupling regime, test mechanism (ENSO teleconnection vs synchronized-shock-window vs state-collapse compounding).

**Relationship to Papers 2/4/6**: Those papers establish that displacement channels SEPARATE — 92% orthogonality (PRE_REG_004), clean disaster regimes (Paper 2), clean conflict types (Paper 4), residue-class typology (Paper 6). Paper 8 is the **shadow**: the minority of countries where channels COUPLE. The orthogonality finding makes the coupling finding meaningful — coupling is a distinct, rare regime, not noise.

**User writes prose; this doc is analytical scope only.**

---

## 1. Mechanism claim

For ~92% of countries, displacement channels (conflict / flood / drought / storm / quake) are orthogonal — a country has a dominant channel and the others are independent (PRE_REG_004). But a minority of countries exhibit **channel coupling**: two or more channels rise and fall together at the country-year level. Coupling is not measurement noise — it is a **distinct compound-crisis regime** with an identifiable mechanism.

The candidate mechanisms (to be discriminated):
1. **ENSO teleconnection** — El Niño/La Niña cycles drive both hydrological hazards (drought/flood) AND conflict timing (food-price shocks, pastoralist competition), coupling the channels through a shared climate driver.
2. **Synchronized-shock window** — when multi-channel shocks happen to hit within the same 2-3 year window (ETH 2020-2024: Tigray war + Rift Valley flood + Horn drought), the channels couple through shared baseline pressure (state-capacity collapse, food-system collapse, refugee compounding). This coupling may be window-specific, not structural.
3. **State-collapse compounding** — in countries where state capacity collapses, all hazard types convert to displacement at higher rates simultaneously (the state can't buffer ANY channel), producing artificial coupling.

---

## 2. The coupling cases (current substrate)

| Country | Coupled pairs (Spearman ρ) | Note |
|---|---|---|
| **ETH** | CF 0.691, **CD 0.830**, FD 0.582 | TRIPLE-channel — only corpus case with all 3 pairs > 0.5; CD strongest in corpus |
| SOM | CD 0.786 | pre-specified (Horn famine-conflict) |
| BRA | CD 0.697 | UNPREDICTED (Amazon drought → extractive-frontier conflict?) |
| SDN | CD (Darfur drought-conflict) | pre-specified |
| All others (~92%) | < 0.5 on all pairs | orthogonal (the norm) |

ETH is the anchor — the most extreme channel-coupling in the entire corpus.

---

## 3. Paper 8 substrate

### Patterns (load-bearing)
- **PATTERN_023** — ETH triple-channel coupling (CF/CD/FD all > 0.5) — PRIMARY anchor
- **PATTERN_021** — BRA conflict-drought coupling (CD 0.697, unpredicted)

### Supporting patterns
- **PATTERN_001** — 3-channel orthogonality (the norm this paper's cases violate)
- **PATTERN_008** — drought channel real globally (the drought pressure)
- **PATTERN_012** — Tigray war (ETH conflict pressure)

### Pre-regs
- **PRE_REG_004** — 3-channel orthogonality (92%; SOM/SDN pre-specified, BRA/ETH unpredicted F2) — the parent

### New pre-regs to lock (this promotion)
- **PRE_REG_033** — coupling-vs-orthogonality classifier (which countries couple; is coupling predictable from a synchronized-shock-window feature?)
- **PRE_REG_034** — ENSO teleconnection test (do coupling-years align with El Niño/La Niña phases?)
- **PRE_REG_035** — temporal-window / synchronized-shock test (is ETH coupling driven by the single 2020-2024 window? split + bootstrap)

---

## 4. Novel contributions (proposed; 3)

1. **Compound-crisis coupling as a distinct regime** — coupling is rare (≤8% of corpus), identifiable, and mechanistically distinct from orthogonal single-channel displacement
2. **Mechanism discrimination** — ENSO teleconnection vs synchronized-shock-window vs state-collapse compounding, tested against each other
3. **The synchronized-shock-window finding** (if PRE_REG_035 fires) — coupling may be a transient property of overlapping shock windows, not a permanent country trait, which would have implications for forecasting (coupling is predictable from shock-calendar overlap, not country type)

---

## 5. Hunt plan (phases)

- **Phase 1** — Coupling census (PRE_REG_033): compute all-pairs channel correlations for every corpus country; formally separate the coupling minority from the orthogonal majority; test whether coupling correlates with a state-fragility or shock-window feature
- **Phase 2** — ENSO test (PRE_REG_034): align coupling-years with ONI (Oceanic Niño Index) phases; test whether coupled channels peak in El Niño/La Niña years
- **Phase 3** — Temporal-window test (PRE_REG_035): split ETH (and other coupling cases) into pre-2018 vs 2018-2024; bootstrap the coupling; test whether coupling is window-driven (transient) or structural (persistent)
- **Phase 4** — Mechanism synthesis: which of the 3 mechanisms best explains the coupling cases

---

## 6. Falsification posture

- If coupling cases share NO common feature (no ENSO alignment, no shock-window, no state-collapse) → coupling is idiosyncratic, not a regime (Paper 8 walks back to "documented exceptions" rather than "compound-crisis regime")
- If ETH coupling vanishes on the pre-2018 split → coupling is window-transient, not structural (refines the claim toward synchronized-shock-window mechanism)
- If ENSO alignment is absent → drop the teleconnection mechanism

---

## 7. Acknowledgments at lock time
- Coupling cases are FEW (ETH/SOM/BRA/SDN) — small-n; this is a characterization paper, not a large-sample test
- Drought-data sparsity limited FD-pair testing in prior digs (only ETH had testable FD)
- Coupling ≠ causation (carried from project-wide stance); the mechanisms are correlational hypotheses
- ENSO test requires external ONI data acquisition (NOAA)

## 8. Cross-references
- PATTERN_023 (primary), PATTERN_021
- PRE_REG_004 (orthogonality parent; F2 yellow flag is this paper's seed)
- PATTERN_001 (the orthogonality norm)
- Climate-attribution thread (Paper 2 PRE_REG_015 — ENSO/SST overlaps)
