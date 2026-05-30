# Paper 9 — Hunt Plan (locked 2026-05-30)

Phased pre-registration schedule for Paper 9 (Legal-Status Routing as Active CHANNEL).

---

## Phase 1 — Establish the channel + differential mechanism (the load-bearing test)

| # | Pre-reg | Hypothesis | Falsifier |
|---|---|---|---|
| 042 | **Track-vs-origin variance decomposition + differential outcome prediction** (locked 2026-05-30) | (H1) Across (state×origin×cohort) cells, track explains substantial variance in work-authorization-dependent outcomes (LFP, formal employment, earnings, benefit takeup); (H2) Track effect > origin effect on work-auth-dependent outcomes; origin effect > track effect on human-capital outcomes (English proficiency, education) | F1 track effect negligible (<5% of variance); F2 track effect uniform across outcome types (no differential prediction); F3 origin dominates everywhere |

**Status**: LOCKED. Fires on next session after data acquisition + cross-walk.

---

## Phase 2 — Within-origin routing identification (cleaner causal story)

| # | Pre-reg (planned) | Hypothesis | Cleanest natural experiment |
|---|---|---|---|
| 043 | **Ukrainians under UFU parole vs TPS vs asylum** | Same origin, different track → diverging LFP, earnings, benefit takeup trajectories by track | UFU opened April 2022; TPS Ukraine designated April 2022; asylum is residual. Entry-mode timing as quasi-exogenous |
| 044 | **Cubans under CHNV parole vs Cuban Adjustment Act vs asylum** | Same origin, different track → diverging outcomes; CAA-track has unique LPR fast-path | CHNV opened January 2023; CAA exists since 1966; pre-CHNV Cubans pooled vs post-CHNV cohorts |
| 044b (or merge) | **Venezuelans under CHNV vs TPS vs asylum** | Same origin, three tracks; CHNV is parole-track, TPS Venezuela has multiple designations 2021/2023 | CHNV opened January 2023; TPS Venezuela 2021 (then expanded); pre-2021 Venezuelans largely asylum/undoc |

**Falsifier shared (Phase 2)**: within-origin track effects disappear when conditioned on observables (suggests selection-into-track explains outcomes, not the rights-bundle).

---

## Phase 3 — Cross-jurisdiction routing (external validity, optional)

| # | Pre-reg (planned) | Hypothesis |
|---|---|---|
| 045 | **Same population, multiple jurisdictions** — Ukrainians routed under US TPS+UFU vs EU Temporary Protection Directive vs Canada CUAET | Track effect dominates within each jurisdiction; cross-jurisdiction differences in the *rights-bundle* attached to each "equivalent" track explain residual variation |

**Data**: EU-SILC + Eurostat asylum decisions; Canada IRCC + LFS; US baselines from Phase 1.

---

## Phase 4 — Forward-watch (calendar-gated, natural experiments)

| # | Pre-reg (planned) | Trigger | Test |
|---|---|---|---|
| 046 | **TPS termination cohort outcomes** | DHS termination decisions (Honduran TPS litigation; potential others 2026-2028) | Pre-vs-post cohort comparison; do outcomes degrade when rights-bundle is stripped? Causal identification window |
| 046b | **Afghan parole → SIV conversion** | Cohort eligible for parole-to-SIV conversion | Same individuals on different tracks at different times → within-person fixed effects |

---

## Substrate hygiene

- Phase 1 = lock + fire + dig + register + commit cycle (standard workflow).
- Phase 2 fires only after Phase 1 lands.
- Phase 3 contingent on the user's appetite for international scope.
- Phase 4 is calendar-gated — track DHS announcements; lock predictions when triggers approach.

## Risk flags (live across phases)
- **Data cross-walk uncertainty** in Phase 1 → quantify, report, sensitivity-test.
- **Selection into track** in Phase 2 → exploit eligibility-window timing.
- **Political sensitivity** throughout → pre-reg discipline is the safeguard; report results irrespective of policy direction.
- **Parallel-agent territory overlap (P7 SDP)** → coordinate before any deep data work in shared regions.

## Where this is going
If Phase 1 fires SUPPORTED, the substantive contribution is the routing-as-mechanism framework with a quantified track-vs-origin decomposition. If Phases 2-4 also land, the paper closes with a fully-identified causal story (within-origin + within-person + cross-jurisdiction).

If Phase 1 F1 or F3 fires (track effect negligible, or origin dominates), the meta-framework prediction (CHANNEL mode produces novel mechanism) is FALSIFIED for this paper — informative either way.
