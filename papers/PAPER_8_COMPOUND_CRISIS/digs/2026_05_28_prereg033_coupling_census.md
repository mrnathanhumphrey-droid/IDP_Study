# Paper 8 — PRE_REG_033 Phase 1: Coupling census

**Fired**: 2026-05-28
**Pre-reg**: PRE_REG_033 (coupling-vs-orthogonality classifier)
**Data**: GIDD conflict + flood/drought/storm channels, 101 countries × country-year 2008-2024; V-Dem libdem for Set B
**Status**: Set A SUPPORTED (8% couple), Set C SUPPORTED (ETH unique triple), Set B SUPPORTED via shock-overlap (p=0.001) not fragility. Two coupling families discovered (CD famine-conflict + CF including negative "displacement substitution").

---

## Headline

**Channel coupling is rare (8% of countries) and the strongest predictor of it is the synchronized-shock-window, not state fragility.** Of 101 countries with ≥10 country-years, only 8 show any channel-pair coupling (|ρ|>0.5); ETH is the unique triple-coupler. Coupling countries have significantly higher shock-window overlap (2.50 vs 1.59 channels peaking in the same 3-year window, p=0.001) but only weakly lower democracy (libdem 0.258 vs 0.377, p=0.125, n.s.). The census also reveals **two distinct coupling families** — conflict-drought (famine-conflict) and conflict-flood (including a negative "displacement substitution" variant in war-dominated UKR/TUR).

---

## Set A — Coupling census: SUPPORTED

| Country | n | shock-overlap | CF | CD | FD | family |
|---|:---:|:---:|---:|---:|---:|---|
| **ETH** | 17 | 3 | +0.69 | **+0.83** | +0.58 | TRIPLE |
| SOM | 17 | 3 | +0.26 | **+0.79** | +0.41 | CD (famine-conflict) |
| BRA | 16 | 3 | +0.40 | **+0.69** | +0.34 | CD (Amazon) |
| COD | 17 | 3 | **+0.64** | — | — | CF |
| UKR | 13 | 2 | **−0.62** | — | — | CF (negative) |
| TUR | 11 | 1 | **−0.61** | — | — | CF (negative) |
| BGD | 17 | 2 | **+0.57** | — | — | CF |
| MEX | 17 | 3 | **+0.52** | — | — | CF |

**8 of 101 countries (8%) couple → SUPPORTED** (predicted ≤15%; F1 fires only if >25%). The orthogonality finding (PRE_REG_004's 92%) is confirmed from the complementary direction: 92% of countries are orthogonal.

Predicted coupling set {ETH, SOM, BRA, SDN}: ETH/SOM/BRA all found coupling. SDN was not testable (insufficient testable drought-channel country-years; excluded by the ≥3-nonzero-years guard) — not a miss, a data-coverage exclusion.

---

## Set C — Triple-coupling uniqueness: SUPPORTED

**ETH is the only triple-coupler** (all of CF/CD/FD > 0.5). Confirmed exactly as predicted. ETH's status as the most extreme channel-coupling case in the corpus (PATTERN_023) holds against the full census.

---

## Set B — Coupling correlate: shock-window, NOT fragility

| Metric | Coupling (n=8) | Orthogonal (n=93) | Test |
|---|---:|---:|---|
| mean libdem | 0.258 | 0.377 | Mann-Whitney p = **0.125 (n.s.)** |
| mean shock-overlap | 2.50 | 1.59 | Mann-Whitney p = **0.001** |

**The discriminating correlate is the synchronized-shock-window, not state fragility.** Coupling countries are only weakly (non-significantly) less democratic, but they have significantly more channels peaking within the same 3-year window. This is direct evidence for the **synchronized-shock mechanism** over the state-collapse-compounding mechanism — coupling arises when multiple hazards happen to strike in the same window, not simply because a state is weak.

This sets up PRE_REG_035 (temporal-window test): if shock-overlap drives coupling, then ETH's triple-coupling should be concentrated in its 2020-2024 synchronized-shock window and weaker before it.

---

## Unanticipated finding: two coupling families

The census reveals coupling is not one phenomenon but (at least) two:

### Family 1 — Conflict-drought (CD): famine-conflict / Amazon
ETH (0.83), SOM (0.79), BRA (0.69). The pre-specified Horn famine-conflict mechanism (drought → food insecurity → conflict) plus BRA's Amazon variant. These are the strong, positive, mechanistically-coherent couplings. PRE_REG_034 (ENSO) targets this family.

### Family 2 — Conflict-flood (CF): including negative "displacement substitution"
- **Positive**: COD (+0.64), BGD (+0.57), MEX (+0.52) — conflict and flood displacement rise together
- **Negative**: UKR (−0.62), TUR (−0.61) — conflict and flood displacement move OPPOSITELY

The negative CF couplings are a distinct and unanticipated phenomenon: **displacement substitution**. In UKR (2022+ war) and TUR, when conflict-displacement surges, the disaster-displacement signal is suppressed or masked — either because war crowds out disaster-response/reporting, or because the population is already displaced by war when floods hit (no additional flood-displacement to record). This is the mirror image of compound-crisis coupling: instead of channels amplifying together, one channel eclipses the other.

This negative-coupling finding is genuinely new — it suggests the "coupling" axis is signed, with amplification (compound crisis) at one end and substitution (one crisis eclipsing another) at the other.

---

## Falsifier status

| F | Status |
|---|---|
| F1 (coupling not rare, >25%) | NOT FIRED (8%) |
| F2 (no correlate — both fragility AND shock-window null) | NOT FIRED (shock-window p=0.001) |
| F3 (triple not unique) | NOT FIRED (ETH only) |

All falsifiers NOT FIRED. H1 (coupling rare + distinct) SUPPORTED; H2 (coupling has a correlate) SUPPORTED via shock-window; H3 (ETH unique triple) SUPPORTED.

---

## Net result

**PRE_REG_033 SUPPORTED on all three prediction sets.** Coupling is rare (8%), ETH-uniquely-triple, and driven by synchronized-shock-window overlap rather than state fragility. The unanticipated two-family structure (CD famine-conflict vs CF including negative displacement-substitution) is a candidate sub-finding and reframes "coupling" as a signed axis (amplification ↔ substitution).

**Mechanism implication**: the shock-window correlate (p=0.001) favors the synchronized-shock hypothesis and directly motivates PRE_REG_035 (is ETH coupling window-transient?). The CD family motivates PRE_REG_034 (ENSO drives Horn drought-conflict coupling).

---

## Cross-references
- PRE_REG_033 (this dig's fit); PRE_REG_034 (ENSO — targets CD family); PRE_REG_035 (temporal-window — tested by shock-overlap result)
- PATTERN_023 (ETH triple — confirmed unique), PATTERN_021 (BRA CD — confirmed)
- PRE_REG_004 (orthogonality 92% — confirmed complementarily at 92%)
- `analysis/paper8_prereg033_census_2026_05_28.json`
- `_scripts/paper8_prereg033_coupling_census.py`

## Status

**Phase 1 done. PRE_REG_033 SUPPORTED.** Paper 8 closure 1/9 → first fire lands strong. Two new threads surfaced: negative CF coupling (displacement substitution; UKR/TUR) + the signed-coupling-axis reframe. Next: PRE_REG_035 (temporal-window, data in hand — directly motivated by the shock-overlap p=0.001 result) + PRE_REG_034 (ENSO, needs NOAA ONI).
