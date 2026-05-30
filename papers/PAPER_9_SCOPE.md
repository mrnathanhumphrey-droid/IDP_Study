# Paper 9 — Scope (locked 2026-05-30)

**Working title**: *Routing as Mechanism: Legal-Status Classification as an Active Channel in US Displacement Outcomes* (placeholder — user names the manuscript)

**Substrate folder**: `papers/PAPER_9_LEGAL_STATUS_ROUTING/`

**Selected via**: [META_PIVOT_QUANTIFICATION_2026_05_30.md](META_PIVOT_QUANTIFICATION_2026_05_30.md). Paper 9 is the program's second CHANNEL-archetype paper (after P7) and the first **ACTIVE CHANNEL** sub-archetype: P7's channel was a market price (rent), P8's was a passive spatial receiver (destination hubs), P9's is **a deliberate administrative routing decision with an institutional actor**.

---

## 0. The right-unit-of-analysis flip

| | conventional unit | RIGHT unit |
|---|---|---|
| What | origin population (Ukrainians, Venezuelans, Hondurans, Syrians, Afghans... studied *separately*) | **legal-track × jurisdiction × cohort** (TPS, Asylum, Refugee, SIV, Parole, Undocumented, pooled across origins) |
| Decisive evidence | (to be tested) — same track → similar outcomes regardless of origin; different tracks → different outcomes despite similar origins | |
| What conventional hides | the institutional routing decision is doing the analytical work that origin labels appear to do | |
| Practical leverage | the routing criteria are the lever (modify track assignment → modify outcomes) | |

## 1. Pivot signature (per META_PATTERNS framework)

Five-dimensional pivot vector for Paper 9: **(a finer ✓ / b downstream ✓ / c typed ✗ / d relational ✓ / e mediator ✓) — 4 dimensions, all ACTIVE CHANNEL signatures.**

Rarity-weighted novelty score: 1.6 + 4.0 + 1.33 + 4.0 = **10.93** (tied with P8 as the highest in the corpus).

The framework predicts CHANNEL-mode papers produce novel mechanism findings (META_PIVOT_QUANTIFICATION §6). Paper 9 is the test of that prediction in a substantive domain the program hasn't touched.

## 2. Core claim architecture

**Load-bearing claim (Claim 1):** Legal-track routing — not origin — is the dominant explanatory variable for *work-authorization-dependent* outcomes (labor-force participation, formal employment, earnings, public-benefit eligibility takeup) among displacement-driven foreign-born populations in the US.

**Load-bearing claim (Claim 2 — differential prediction, the sharpest test):** Track effects dominate origin effects on outcomes whose mechanism *runs through legal authorization* (LFP, formal employment, earnings, benefits); origin effects dominate on outcomes whose mechanism *runs through human capital* (English proficiency, educational attainment, occupational matching). If true, the routing-as-mechanism claim has the right mechanistic shape — the channel operates precisely where authorization is binding.

**Auxiliary claim (Claim 3):** Within a single origin population routed multiple ways (Ukrainians under UFU parole vs TPS Ukraine vs asylum, Cubans under CHNV vs asylum vs adjustment, Venezuelans under CHNV vs TPS vs asylum), outcomes diverge by track in a manner consistent with Claims 1+2.

**Mechanism statement (Paper 9 substantive):** The US receiving-state apparatus classifies heterogeneous upstream displacement events into a small number of downstream legal categories. Each category attaches a distinct bundle of authorization rights (work authorization timing, public-benefit eligibility, deportation protection, family reunification, path-to-LPR). The downstream variation in displaced-population outcomes is dominated by which category they were routed into, not by which displacement event they came from. The institutional routing decision is the mechanism.

**Policy corollary:** policy should target the routing criteria and the rights-bundle attached to each track, not origin-specific integration programming.

---

## 3. Phase structure

| Phase | Question | Data | Output |
|---|---|---|---|
| **Phase 1** (Phase-now) | Does track-effect dominate origin-effect on work-auth-dependent outcomes? (Claims 1+2) | ACS 5-yr 2018-2023, ORR refugee data, USCIS TPS Fact Sheets, EOIR asylum decisions, DOS SIV reports, MPI undocumented estimates | variance decomposition + differential outcome prediction |
| Phase 2 | Within-origin track comparison (Claim 3) — Ukrainians, Cubans, Venezuelans routed differently | Same as Phase 1 + UFU + CHNV parole rosters | identification refinement |
| Phase 3 (optional) | Cross-jurisdiction comparison — same population routed differently across countries | EU Eurostat + EU-SILC; Canada IRCC; US baselines | external validity, scope expansion |
| Phase 4 (forward-watch) | TPS designation changes 2026-2028 (Honduran TPS termination litigation, Ukrainian extension cycle, Afghan parole transition); natural experiment opportunities | DHS announcements + court rulings + cohort tracking | causal-identification windows |

---

## 4. Pre-registration roster (planned)

| ID | Title | Phase | Status |
|---|---|---|---|
| PRE_REG_042 | Track-vs-origin variance decomposition + differential outcome prediction | Phase 1 | **locked + committed 2026-05-30** (this scope-lock) |
| PRE_REG_043 (planned) | Within-origin track comparison (Ukrainians under UFU/TPS/asylum) | Phase 2 | not yet locked |
| PRE_REG_044 (planned) | Within-origin track comparison (Cubans / Venezuelans) | Phase 2 | not yet locked |
| PRE_REG_045 (planned) | Cross-jurisdiction routing (Ukrainians US-EU-CA) | Phase 3 | not yet locked |
| PRE_REG_046 (planned) | Forward-watch: TPS termination cohort outcomes | Phase 4 | not yet locked |

---

## 5. Substrate elements

### Patterns to anchor (to be catalogued as fired)
- The **track-rights bundle structure**: each track attaches a distinct combination of (work-authorization, benefit-eligibility, deportation-protection, family-reunification, LPR-pathway). Document as a TRACK-RIGHTS TABLE.
- The **routing-determinants pattern**: which displacement events get routed to which track depends on (origin, time-of-arrival, presence-or-absence of receiving-state designation, individual case characteristics).
- The **multi-routing within origin pattern**: Ukrainians, Venezuelans, Cubans are each routed multiple ways depending on entry mode / time — making within-origin comparison feasible.

### Data sources (load-bearing)
| Source | Granularity | What it provides | Status |
|---|---|---|---|
| **ACS 5-year (2018-2023)** | state, PUMA, individual | foreign-born, country of birth, year of entry, citizenship status, LFP, earnings, English proficiency, education, public benefit receipt | public, free (Census API or IPUMS) |
| **ORR refugee resettlement** | state × origin × FY | refugee population by state × origin × cohort (precise track identification for Refugee track) | public, free (HHS ORR reports) |
| **USCIS TPS Fact Sheets** | national + sometimes state × origin × period | TPS designations + estimated populations | public, free |
| **EOIR Statistics** | court (= rough state) × origin × decision | asylum filings, grants, denials, appeals | public, free |
| **DOS SIV reports** | annual × origin (Afghan + Iraqi) | SIV approvals + visa issuances | public, free |
| **MPI undocumented estimates** | state × origin | undocumented population estimates | public via MPI Data Hub |
| **CHNV/UFU parole reports** | quarterly × origin | parole-program enrollment | public via USCIS dashboards |

### Cross-walk method
For each (state × origin × cohort) cell in ACS, construct a **track-distribution vector** using the external administrative data (probability person from this cell is on each of {Refugee, TPS, Asylum, SIV, Parole, Undocumented, LPR-other}). Two analytical paths:
- **Cell-aggregate**: compute aggregate outcomes per (state × origin × cohort) and regress against track-distribution vector.
- **Probabilistic individual assignment**: assign individuals in ACS to most-probable track conditional on (state × origin × cohort); analyze at individual level with multiple-imputation uncertainty.

Phase 1 will lock the cell-aggregate path as primary; probabilistic assignment as robustness.

---

## 6. Literature engagement

The wedge is methodological: the literature studies displacement integration **either origin-by-origin** (Ukrainian integration in the US, Venezuelan in Colombia, Syrian in Turkey) **or track-by-track** (TPS holder outcomes, refugee outcomes, undocumented outcomes) — rarely both jointly in a routing-as-mechanism frame.

Closest prior work (acknowledge and differentiate):
- **Amuedo-Dorantes et al.** on TPS effects (specific to one track; doesn't compare across tracks within origins)
- **Hainmueller et al.** on naturalization effects (naturalization is a *late-stage* status transition; we examine the *initial routing* decision)
- **Kossoudji & Cobb-Clark** on IRCA legalization (analogous "track-switch" study; we generalize to current routing structure)
- **Hatton** on asylum decisions (administrative-decision framing; we extend to the full routing menu)
- **Bansak et al.** on refugee resettlement matching (within-track operational decisions; we examine across-track routing)
- **MPI** policy reports (descriptive; we provide the unified mechanism framework)

The right-unit pivot — pooling across origins and splitting by routing decision — is the empirical gap.

---

## 7. Connection to the rest of the program

- **P7 (SDP / rent funnel)**: shared CHANNEL archetype but PASSIVE (market price). P9 is ACTIVE.
- **P8 (destination convergence)**: shared CHANNEL archetype but PASSIVE (spatial receivers). P9 is ACTIVE.
- **P1/P5 (lever configurations)**: P9 borrows the "configuration-of-rights" idea — each track is a rights-configuration analogous to P1/P5's lever-configuration. The mirror could be productive.
- **Migration project (D:/Migration)**: P9 is a US-receiver study; D:/Migration's PUMA-to-PUMA work is destination-clustering pre-routing. Possible cross-fertilization on the "destination convergence" side.
- **P7 (parallel agent, SDP)**: P9 is adjacent to P7 (both about US receiving-side displacement outcomes). Coordination flag — discuss with parallel agent before deep data work to avoid scope overlap.

## 8. Honest pre-launch risks

- **Data cross-walk uncertainty**: ACS doesn't directly identify track; the cross-walk introduces measurement error. Quantify and report. Sensitivity tests via probabilistic assignment.
- **Selection into track**: track assignment is non-random (Ukrainians may *choose* parole over asylum because parole was offered first). Within-origin comparisons are the cleanest, but selection within origin remains. Use eligibility-window timing (when each program opened) as quasi-exogenous variation where possible.
- **Political sensitivity**: this paper will be read as policy-relevant regardless of analytical care. Maintain pre-reg discipline; report results irrespective of policy implications.
- **Parallel agent overlap**: coordinate with P7 (SDP) on receiving-side scope to avoid territory collision.
- **TPS terminations during analysis window**: 2025-2026 TPS termination decisions affect cohort definitions. Lock cohort boundaries in pre-reg before terminations resolve.

## 9. Phase 1 plan (immediate)

1. **Lock PRE_REG_042** — track-vs-origin variance decomposition + differential outcome prediction. (DONE this scope-lock.)
2. **Build data substrate**: scrape/acquire ORR + USCIS TPS + EOIR + DOS SIV + MPI undoc; pull ACS 5-yr 2018-2023 extract.
3. **Construct cross-walk**: (state × origin × cohort) → track-distribution vector.
4. **Fire Phase 1** on labor-market outcomes (LFP, earnings, formal employment).
5. **Differential test**: same on human-capital outcomes (English, education) — predict origin > track.
6. **Dig + register + commit/push** per standard workflow.

Estimated Phase 1 build: 1-2 sessions for data acquisition + cross-walk, 1 session for analysis + dig.

Status: **scope locked, pre-reg locked, data identified, Phase 1 ready to fire on next session.**
