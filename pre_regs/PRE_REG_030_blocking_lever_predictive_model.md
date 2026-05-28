# Pre-Registration 030 — Blocking-Lever Predictive Model

**ID:** PRE_REG_030
**Locked:** 2026-05-27 (predictions + falsifiers pre-committed before formal scoring)
**Substrate:** PATTERN_027 (failed-backsliding archive, 4 levers) + PATTERN_013 (consolidation cases)
**Paper:** 5 (Democratic Resilience)
**Status:** LOCKED — first fit fires on corpus scoring

---

## 1. Hypothesis

**H1 (lever-count predicts outcome):** Whether an executive-aggrandizement attempt is BLOCKED or CONSOLIDATES is predictable from a count of four structural blocking levers present at the onset of the attempt:
1. Independent Constitutional/Supreme Court (not captured at onset)
2. Mass civil-society mobilization capacity
3. Electoral cycle within reach during the attempt window
4. Federal/regional parallel power

**Decision rule (pre-committed):** ≥3 levers present → BLOCKED; ≤2 levers → CONSOLIDATES.

**H2 (lever erosion):** Lever-count is not static. A country can lose levers between attempts (e.g., USA 2020 court-independent → 2025 court-captured), converting a previously-protected country into an at-risk one. Predicted: USA lever-count drops from ≥3 (2020, Trump I blocked) to ≤2 (2025, Trump II consolidating).

---

## 2. Operationalization (pre-committed before scoring)

Each lever scored 0/1 at attempt onset:

| Lever | V-Dem / structural proxy | =1 if |
|---|---|---|
| Court independence | high-court independence (hcind) + judicial constraints (jucon) | hcind above country's own pre-attempt median AND not yet packed |
| Civil-society capacity | CSO participatory env (v2csprtcpt) + CSO entry/exit (v2cseeorgs) | both in upper half of corpus distribution at onset |
| Electoral cycle reach | scheduled national election within attempt window | regular election falls within 0-3 yrs of attempt onset |
| Federal/regional power | federalism / subnational autonomy (v2elreggov, v2elsrgel) | meaningful elected regional government with independent authority |

Ambiguous/borderline scores documented explicitly; sensitivity check with ±1 lever.

---

## 3. Pre-locked predictions

### Prediction set A — In-corpus separation
The 12 corpus cases (5 blocked + 7 consolidated) separate by lever-count:
- 5 blocked cases (BRA, ISR, USA-I, KOR, PER-Castillo): predicted ≥3 levers each
- 7 consolidated cases (SLV, HUN, TUR, VEN, POL-PiS, TUN, BLR): predicted ≤2 levers each

**Match threshold**: ≥10 of 12 cases on the correct side of the ≥3 cutoff → H1 supported.

### Prediction set B — Lever erosion (USA)
USA scored at two timepoints:
- 2017-2020 (Trump I): predicted ≥3 levers (blocked → plateau)
- 2025 (Trump II): predicted ≤2 levers (consolidating → fast-pole)

### Prediction set C — Out-of-sample forward
Score additional democracies not in the original 12 (e.g., IND, MEX, ZAF, IDN, GEO, SVN). Predict which are at-risk (≤2 levers) vs protected (≥3). Falsifiable as their trajectories unfold.

---

## 4. Falsifiers

- **F1**: < 10 of 12 corpus cases on the correct side of the ≥3 cutoff → lever-model doesn't separate; post-hoc storytelling
- **F2**: PER complication generalizes — i.e., ≥3 "blocked" cases actually consolidate later via legal channels → blocking a dramatic attempt ≠ preventing backsliding; the model predicts the wrong thing
- **F3**: USA lever-count does NOT drop 2020→2025 → lever-erosion (H2) walked back

F1 firing = blocking-lever model walks back to descriptive-only.

---

## 5. Methodology
- V-Dem v15/v16 sub-indicators for all 12 corpus cases at attempt onset
- Binary lever scoring + sensitivity (±1)
- Confusion matrix vs observed blocked/consolidated
- Out-of-sample scoring for Prediction set C

## 6. Acknowledgments at lock time
- Lever scoring has subjective elements (esp. civil-society capacity) — mitigated by V-Dem proxies + ±1 sensitivity
- n=12 is small; the model is a structured hypothesis, not a trained classifier
- PER shows blocking a self-coup ≠ preventing legal-channel backsliding — F2 explicitly watches this

## 7. Cross-references
- PATTERN_027 (the 4 levers + 5 blocked cases)
- PATTERN_013 (7 consolidated cases)
- PATTERN_026 (USA fast-pole — H2 anchor)
- PRE_REG_012 (recovery counterpart)

## 8. Provenance
Locked 2026-05-27 before formal lever scoring. First fit fires on corpus scoring.
