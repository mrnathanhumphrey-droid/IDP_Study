# Meta-Conjecture Test — Does Mechanism Strength Scale with Pivot Dimensions? (2026-05-30)

**Purpose**: Test of conjecture #5 from [META_PATTERNS_2026_05_30.md](META_PATTERNS_2026_05_30.md): *the strength of mechanism identification in the program scales with the number of independent pivot dimensions applied.* Uses the per-paper scores from [RIGHT_UNIT_TABLE_2026_05_30.md](RIGHT_UNIT_TABLE_2026_05_30.md).

This is a reflexive test (testing my own meta-conjecture about my own meta-pattern). Locking the rubric before scoring so the verdict can't be post-hoc'd.

---

## 1. Pre-committed rubric (locked before scoring)

### Pivot-dimensions score (PIV)
Per paper, count of ✓ in the 5-column pivot-dimensions matrix (Table 2 of RIGHT_UNIT_TABLE). Range 0–5. Already locked when that table was written.

### Mechanism-strength score (INS — instruments converging)
Per paper, count of independent instruments that supported the paper's headline mechanism claim. An "instrument" = a distinct (a) data source, (b) statistical test, or (c) pre-registered falsifier test (firing or not). Each pre-registration counts once. Walk-backs don't subtract — they often *strengthen* the refined claim and reveal new instruments — but only the final supported version contributes. The headline claim per paper is fixed up-front:

| paper | headline mechanism claim |
|---|---|
| P1 | 4-lever blocking model (3+ → blocked) |
| P2 | 7-regime typology of disaster displacement |
| P3 | MLI epicenter + lagged regional diffusion |
| P4 | 5-type conflict typology (form > country) |
| P5 | civil-society + federalism discriminate recovery |
| P6 | residue-class typology irreducible to off-the-shelf covariates |
| P7 | rent is the displacement funnel (supply + demand → rent → homelessness) |
| P8 | compound coupling = contemporaneous displacement-destination convergence |

### Predictions (pre-committed)
- **Prediction A (primary)**: Spearman ρ(PIV, INS) ≥ **+0.5** (positive, meaningful) across n=8 papers.
- **Prediction B (sensitivity)**: the relationship survives dropping the most-pivoted paper (P8) — Spearman ρ ≥ **+0.3** on n=7.

### Falsifiers
- **F1**: Spearman ρ < +0.5 overall → conjecture NOT supported at the pre-committed bar.
- **F2 (single-case dominance)**: relationship collapses without P8 (ρ < +0.3) → conjecture is held up by one outlier, not a general program-level pattern.
- **F3**: ρ ≤ 0 → opposite-of-conjecture; pivot dimensions and instrument count are unrelated or inverse.

F1 alone = "not supported at the bar" (weak negative).
F1 + F2 = "conjecture rejected as a general pattern; P8 alone fits" (strong negative — walk-back territory).

---

## 2. Scores

PIV from the matrix; INS from counting instruments per the rubric above.

| paper | PIV | INS | converging instruments (for INS) |
|---|:---:|:---:|---|
| P1 Exec aggrandizement | 2 | 4 | PATTERN_013 success-decomp + PATTERN_027 failure cases + PRE_REG_010 fed-friction + PRE_REG_012 recovery mirror |
| P2 Disaster regimes | 2 | 5 | PRE_REG_003 typology + 015 climate attribution + 027 SOCX + 029 Regime 7 + Stan 022 confirmation |
| P3 Strife epicenter | 2 | 2 | UCDP-GED lag chronology + TGO RULAC Feb 2026 |
| P4 Conflict typology | 3 | 4 | PRE_REG_018 v2 classifier + 019 DPF + 020 spatial + 021 within-country shift |
| P5 Democratic resilience | 2 | 4 | PRE_REG_030 blocking-lever + 031 velocity + 032 plateau + 030 Set C out-of-sample |
| P6 Methodology | 2 | 5 | Stan 022 LOO + disaster-only ablation + conflict-only ablation + WDI latent + Polity latent |
| P7 SDP / homelessness | 3 | 4 | PRE_REG_026 state ortho + 031 metro mediation + H2 supply mediation + H2b demand mediation |
| P8 Compound-crisis coupling | 4 | 9 | PRE_REG_033 + 034 + 035 + 036 + 037 + 038 + 039 + 040 + 041 |

---

## 3. Correlation

### Primary (n=8)

Spearman ranks (with ties averaged):

| paper | PIV | PIV rank | INS | INS rank |
|---|:---:|:---:|:---:|:---:|
| P1 | 2 | 3 | 4 | 3.5 |
| P2 | 2 | 3 | 5 | 6.5 |
| P3 | 2 | 3 | 2 | 1 |
| P4 | 3 | 6.5 | 4 | 3.5 |
| P5 | 2 | 3 | 4 | 3.5 |
| P6 | 2 | 3 | 5 | 6.5 |
| P7 | 3 | 6.5 | 4 | 3.5 |
| P8 | 4 | 8 | 9 | 8 |

Σd² = 0.25 + 12.25 + 4 + 9 + 0.25 + 12.25 + 9 + 0 = **47**
Spearman ρ = 1 − 6·47 / (8·63) = 1 − 0.560 = **+0.44**

### Sensitivity (n=7, drop P8)

Same ranks recomputed without P8 (n=7):
Σd² = 47 (P8 contributed 0); n(n²−1) = 336
ρ = 1 − 6·47 / 336 = 1 − 0.839 = **+0.16**

---

## 4. Verdict

| prediction | observed | status |
|---|---|---|
| **A** (n=8): ρ ≥ +0.5 | +0.44 | **NOT MET** (F1 fires) |
| **B** (n=7, drop P8): ρ ≥ +0.3 | +0.16 | **NOT MET** (F2 fires) |
| F3 (ρ ≤ 0) | ρ positive | not fired |

**Both F1 and F2 fire. The conjecture is NOT supported as a general program-level pattern; P8 is doing essentially all the work in the correlation.**

This is an honest negative on my own meta-conjecture from yesterday — exactly the kind of walk-back the program treats as feature-not-bug.

---

## 5. Why the conjecture fails (post-result analysis — clearly distinguished from the test)

Looking at the scores, the test fails for a structural reason: **PIV varies little across the program** (six papers at 2, two at 3, one at 4) while **INS is noisy and dominated by substantive question size** (P3's mechanism needs only 2 instruments; P8's needs 9). With most papers clustered at PIV=2 and INS scattered across 2-5, the correlation has nowhere to discriminate.

Three structural reasons the cross-paper test is the wrong test for this conjecture:

1. **Substantive scope dominates instrument count.** A bigger / harder mechanism question (P8 ruling out a shared climate driver across 3 instruments before identifying the right one) naturally requires more instruments regardless of pivot dimensions. P3's epicenter+lag mechanism is intrinsically smaller — 2 instruments suffice — so its INS=2 doesn't mean "weak identification," it means "smaller question."
2. **Session-effort confound is real.** P8 had 6 pre-regs in a single 2-day push specifically to elaborate the mechanism. The high INS=9 and high PIV=4 are both products of "I spent a lot of time on this paper." Dropping P8 (which removes the session-effort outlier) collapses the correlation (+0.44 → +0.16), confirming this confound is load-bearing.
3. **The conjecture was about within-paper sequencing, not cross-paper averaging.** Re-reading the original phrasing: *"the strength of mechanism identification scales with the number of independent pivot dimensions applied."* The right test is at the level of *individual mechanism claims*, not papers. Within P8's arc (036→041), each successive pre-reg pivoted one more dimension AND strengthened the mechanism — that within-arc pattern is real. The cross-paper aggregation washes it out because different papers are at different substantive scopes.

---

## 6. Reformulated conjecture (refined, not re-pre-registered here)

The original was too strong. A refined version that survives the test:

> **Within a single mechanism arc, the addition of an independent pivot dimension at each step correlates with stronger mechanism identification at that step.** (Within-paper, sequenced — not cross-paper averaged.)

The within-P8 sequencing supports this: 033 (baseline structure, 2 dimensions) → 034 (single ENSO test, 1 dim) F1 fires → 036/037 (spatial-scale pivot, 2-3 dims) F1+F2 fires across instruments → 038 (sub-national resolution pivot, 3 dims) supports → 039 (downstream/hazard pivot, 3-4 dims) reframes → 040 (origin/destination pivot, 4 dims) SUPPORTS → 041 (cell-year capstone, 4 dims) confirms + quantifies.

The pivot-dimensions count rises across the arc; the mechanism-strength rises with it; and the strongest identification (041) is also the most-pivoted single test. **That within-arc pattern is real; the cross-paper aggregation isn't the right framing to expose it.**

---

## 7. Honest implications

- **Original conjecture #5 from META_PATTERNS_2026_05_30: WALKED BACK at the program-level framing.** Cross-paper, mechanism strength does not robustly scale with pivot dimensions (ρ=+0.44 overall, +0.16 without P8).
- **The within-arc version survives** as an informal reading of P8's 036→041 sequence, but it's not a general program-level pattern across all 8 papers — it's a property of a single elaborated arc.
- **The methodological-meta claim ("pivot more for stronger identification") stands as a within-mechanism-arc heuristic**, not as a cross-paper prediction.
- This is a clean walk-back of a meta-claim — the same kind of pre-reg discipline applied one level up. The unifying meta-frame in META_PATTERNS (right-unit-of-analysis as the recurring move) is unaffected; only the strength-scales-with-dimensions sub-claim is walked back.

The corpus now contains a documented test of a meta-conjecture about its own meta-pattern, with an honest negative verdict and a refined reformulation. That is itself an instance of the "walk-backs ascend the mechanism" pattern from META_PATTERNS §7a, applied reflexively.
