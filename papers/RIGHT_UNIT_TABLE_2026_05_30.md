# Right-Unit-of-Analysis Comparison Across All 8 IDP Papers (2026-05-30)

**Purpose**: Side-by-side comparison of the right-unit-of-analysis finding in each paper, extending §1 of [META_PATTERNS_2026_05_30.md](META_PATTERNS_2026_05_30.md). Two views: per-paper deep table + pivot-dimensions matrix.

---

## Table 1 — Per-paper right-unit comparison

| # | Paper | Conventional unit (field uses) | RIGHT unit (paper found) | Decisive evidence | What conventional unit *hides* | Practical leverage |
|---|---|---|---|---|---|---|
| 1 | **P1** Executive aggrandizement | country-year V-Dem | **success cases × failure cases (4-lever configuration)** PATTERN_013 ∩ PATTERN_027 | 3+ levers → blocked (5/5 failure cases); ≤2 → succeeds; monotonic in lever count | mechanism legible only *with both sides*; one set alone is noise | fix the least-present discriminating lever, not the most-present |
| 2 | **P2** Disaster regimes | country, or country-year event | **regime (country-period typology R1–R7)** incl. new R7 wildfire | 7 mechanism-distinct displacement modes (003/015/027/029); Stan PRE_REG_022 ΔLOO +13.66 irreducible | regime structure — "disaster-prone" lumps R1 flood-chronic with R3 high-capacity with R7 wildfire | regime-specific instruments (R1 flood-infra ≠ R3 capacity ≠ R5 drought) |
| 3 | **P3** Strife epicenter | regional aggregate (Sahel) | **epicenter + lag-diffused neighbors** (MLI source; BFA 8yr, NER 9yr) | TGO NIAC Feb 2026 declared per lag prediction; consistent 8/9yr lags | conceals directed diffusion + the identifiable origin | monitor source-state signals → ETA for neighbor emergence (TGO/CIV/GHA) |
| 4 | **P4** Conflict typology | country with conflict | **country-PERIOD type (A/B/C/D/E)** — form, not nation | PRE_REG_021 F4 NOT fired — IRQ/NGA within-country type-shifts; DPF rank D<A<C<B<E 5/5 bands | same country = different types in different periods; treating "country X's conflict" as one thing loses regime-shifts | type-shift = early-warning signal (form change precedes outcome change) |
| 5 | **P5** Democratic resilience | country recovery trajectory | **discriminating-lever configuration** (which of civil-society + federalism present, given courts/elections universal at onset) | blocking-lever model 10/12; vertical-tier plateau (BRA 2% / KOR 4%); out-of-sample roster (GEO/PHL/IND at-risk) | the universally-present levers are *not* the discriminating ones | invest in civil-society / federalism, not saturated levers |
| 6 | **P6** Methodology | country-year + WDI/Polity covariates | **residue class** (joint cell in disaster-regime × conflict-type cross-product) | Stan PRE_REG_022 ΔLOO **+13.66**; covariate ablation: WDI +1.28 / Polity −0.42 *both fail* to absorb the lift | off-the-shelf country covariates miss the joint-typology structure entirely | joint typology = irreducible; don't proxy with WDI |
| 7 | **P7** SDP / US-homelessness | state-level homelessness vs state supply | **metro/CoC + rent (mediator)** | PRE_REG_031 n=302 CoCs; H1 rent R²=0.76; H2 supply mediation indirect +0.18 fully-mediated; H2b demand indirect +0.56 (~3× dominant) | direct supply→homelessness regression hides rent as the funnel; demand dominates supply 3× *through rent* | demand-side rent stabilization, not pure supply expansion |
| 8 | **P8** Compound-crisis coupling | country-year national coupling (PRE_REG_033) | **destination hub × year** (sub-national 0.5° receiving cells absorbing both flows) | 4-instrument arc: 038 disp-coloc + 039 hazard-non-coloc + 040 origin −0.10/dest +0.41 + 041 burden (8 cells = 56%) + same-year ρ=+0.80 | country-year coupling is the aggregate signature of a few destination hubs; the temporal correlation IS the spatial concentration | target receiving hubs for compound-crisis response, NOT hazard zones |

---

## Table 2 — Pivot-dimensions matrix

Five orthogonal pivot directions; ✓ where the paper performs that pivot type.

| paper | (a) finer resolution (sub-aggregate) | (b) downstream of apparent cause | (c) typed / configured | (d) relational / structural | (e) mediator-/destination-channel | **n dims** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 Exec aggrandizement | | | ✓ (lever config) | ✓ (success × failure pairing) | | **2** |
| P2 Disaster regimes | ✓ (regime period < country) | | ✓ (typology) | | | **2** |
| P3 Strife epicenter | ✓ (epicenter + neighbor) | | | ✓ (graph: source + lag) | | **2** |
| P4 Conflict typology | ✓ (period < country) | | ✓ (5-type) | ✓ (within-country shift) | | **3** |
| P5 Democratic resilience | | | ✓ (lever configuration) | ✓ (P1↔P5 mirror) | | **2** |
| P6 Methodology | | | ✓ (residue class) | ✓ (joint cell, cross-product) | | **2** |
| P7 SDP / homelessness | ✓ (CoC < state) | ✓ (consequence chain) | | | ✓ (rent funnel) | **3** |
| P8 Compound-crisis coupling | ✓ (cell < country) | ✓ (destination < origin) | | ✓ (cell × year) | ✓ (destination hub) | **4** |

*(Note: revised P8 from 5→4 after re-checking — column (c) "typed/configured" is not a primary P8 pivot; the destination-hub is a relational/spatial unit, not a categorical type. Honest re-count.)*

---

## What the matrix surfaces

1. **P8 is the most-pivoted case** (4 of 5 dimensions). Its mechanism arc required 6 pre-regs (036→041) because each pivoted one more dimension.
2. **P1 ↔ P5 share configuration + relational and nothing else** — same analytical move run forward (capture) vs backward (recovery). The mirror structure is the same operation twice.
3. **P7 + P8 are the only papers with column (e)** — the program's two displacement-system-mechanism papers; both find a downstream channel where distinct upstream causes converge.
4. **P2/P4/P6 cluster on typology** — the program's classification papers. They define the right type; other papers apply it in their pivots.
5. **Column (b) "downstream" is rare** — only P1 (consequence), P7 (mediator), P8 (destination) genuinely pivot downstream. The most under-used pivot, and probably where the most counterintuitive findings live.
6. **Combination is what wins** — papers exhibiting more pivot dimensions appear to produce the cleanest mechanism identification (P8 = 4 dims → fully triangulated). **Conjecture worth testing**: mechanism strength scales with the number of independent pivot dimensions applied. Tested in [META_CONJECTURE_TEST_2026_05_30.md](META_CONJECTURE_TEST_2026_05_30.md).
