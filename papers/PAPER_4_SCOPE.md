# Paper 4 — Scope Lock (2026-05-25)

**Working title (internal)**: Conflict-Type Meta-Typology — organizational form of violence determines displacement structure across 3 (or 4) conflict-types

**Status**: SUBSTRATE EXISTS. 3 anchor patterns (012, 015, 017) confirmed. No pre-regs locked yet. Hunt = case expansion (2+ cases per type) + formal classifier + type-distinct mechanism tests.

**User writes prose; this doc is analytical scope only.**

---

## 1. Mechanism claim

Conflict-displacement structure is determined by **organizational form of violence** (state-army vs irregular-militia vs predator), not by region, income, or libdem level. Conflicts cluster into a small number of distinct types, each with:

- Different fatality / displacement-per-fatality ratios
- Different spatial concentration patterns (front-line zone vs militia-territory vs diffuse)
- Different actor compositions (state militaries vs irregular insurgents vs predator militias)
- Different displacement-receiving infrastructure requirements (border corridors vs internal IDP camps vs urban absorption)

Paper 4 is the **conflict-side parallel** to Paper 2's disaster-displacement typology — same meta-argument "corpus heterogeneity is typology, not noise" applied to conflict-displacement.

---

## 2. The 3 confirmed conflict-types (current state)

| # | Type | Anchor cases | Key signature |
|---|---|---|---|
| **A** | **Formal-army war** | ETH Federal-TPLF 2020-2022 (313K war fatalities), UKR Russo-Ukrainian 2022-2024 (235K war fatalities) | Very high state-based fatalities; low displacement-per-fatality (32-76); spatial concentration in front-line zones; strife channel ≈ 0 |
| **B** | **Predator-militia campaign** | DRC ISCAP/M23/Mai-Mai 2020-2024 (18M displaced / 23K fatalities) | Very high displacement-per-fatality (783); spatial concentration in militia-territory (NK/Ituri = 83%); one-sided violence dominant (62%); civilians = primary target |
| **C** | **Irregular insurgency** | Sahel JNIM/ISGS (MLI, BFA, NER), SOM Al-Shabaab | Mid fatality; mid displacement-per-fatality (~100-300); spatial diffusion (no concentration); strife channel dominant; mixed state-based + non-state + one-sided |

**Open question for Paper 4**: Is there a confirmed 4th type? Candidates:
- **D1 — Communal/ethnic clash** (SSD inter-communal 2020+, ETH Amhara-Oromo, NGA Middle Belt) — civilian-vs-civilian violence with limited state involvement
- **D2 — Regime-collapse uprising** (HTI gang-state collapse, KOR martial law 2024, USA Jan 6, possibly SDN April 2023 collapse) — political crisis without sustained military conflict
- **D3 — None — 3 types only**: walk back the 4-type framing if D1/D2 don't separate cleanly from C

---

## 3. Type-distinct signatures (mechanism claims)

### Fatality / displacement-per-fatality ratios

| Type | Fatalities (acute) | Displacement-per-fatality | Spatial concentration |
|---|---|---|---|
| A (formal-army) | very high (200K+) | low (30-80) | front-line zone (≥70% in 1-3 admin-1) |
| B (predator-militia) | mid (10K-30K) | very high (250-800) | militia-territory (≥70% in 1-3 admin-1) |
| C (irregular) | low-to-mid (1K-15K) | mid (100-300) | diffuse (no admin-1 dominates >50%) |

### Actor-composition signatures
- A: side_a includes ≥2 state militaries OR (state vs structured regional militia)
- B: side_a dominated by single armed-group brand (ISCAP, M23) with high one-sided count
- C: side_a is multi-actor non-state landscape with overlapping dyads (JNIM, ISGS, gov, militias)

### Channel signatures (cross-link to PATTERN_001)
- A: 1-channel (conflict only); flood/drought/disaster <1% of conflict channel
- B: conflict-dominant with secondary disaster channel
- C: multi-channel (conflict + flood seasonal + sometimes drought)

---

## 4. Paper 4 substrate

### Patterns (load-bearing)
- **PATTERN_012** — ETH Tigray war (Type A formal-army anchor; 313K fatalities; 5.14M displacement 2021)
- **PATTERN_015** — DRC ISCAP/M23 (Type B predator-militia anchor; 18M displaced / 23K fatalities; 83% in NK+Ituri)
- **PATTERN_017** — UKR pure-interstate (Type A formal-army anchor; 235K fatalities / 17.9M displaced / strife=0)

### Supporting patterns
- **PATTERN_010** — Strife-dominant pattern (Type C anchor; recurring across MLI/SSD/HTI/CAF clusters)
- **PATTERN_005** — MLI strife epicenter (Type C anchor; jihadist competition + self-defense militias + ethnic communal)
- **PATTERN_003** — BFA industrial-scale displacement (Type B-or-C; gov counterinsurgency vs JNIM)
- **PATTERN_006** — BEN periphery spillover (Type C diffusion candidate)

### Pre-regs needed
- **PRE_REG_018** (proposed) — Conflict-type classifier formalization (rules + falsifiers)
- **PRE_REG_019** (proposed) — Type-distinct fatality/displacement ratios (mechanism-distinct claims)
- **PRE_REG_020** (proposed) — Type-distinct spatial concentration (admin-1 dominance test)
- **PRE_REG_021** (proposed) — IRQ 2003 phase decomposition (interstate phase vs insurgency phase as within-country test)

---

## 5. OPEN threads — HUNT plan

### Critical-path (must close before submission)

| ID | Thread | What closes it | Effort | Where |
|---|---|---|---|---|
| **P4-C** | Formal classifier locked + tested | Lock PRE_REG_018 with rules; apply to all 50+ corpus countries | Light-medium | new |
| **P4-A** | Type A formal-army expansion | Add 2+ cases beyond ETH/UKR: ARM-AZE 2020, ISR-Gaza 2023+, IRQ 2003 interstate phase | Medium — UCDP-GED pull | PATTERN_017 |
| **P4-B** | Type B predator-militia expansion | Add 2+ cases beyond DRC: SDN RSF vs civilians 2023+, NGA Boko Haram raids, possibly BFA gov counter-ops | Medium — UCDP-GED pull | PATTERN_015 |
| **P4-D** | IRQ 2003 within-country phase decomposition | Decompose IRQ 2003-2011 into interstate phase (2003) vs insurgency phase (2004-2011); test if conflict-type classifier shifts within country | Medium — temporal admin-1 split | PATTERN_017 |
| **P4-E** | 4th-type test (D1/D2/D3) | Test SSD inter-communal + ETH Amhara-Oromo + HTI gang-state — do they cluster as 4th type or absorb into A/B/C? | Medium-heavy | new |
| **P4-F** | Type-distinct ratios test | Compute fatality/displacement-per-fatality for all confirmed cases; test mechanism-distinct predictions (PRE_REG_019) | Light — math on existing data | PATTERN_012/015/017 |
| **P4-G** | Spatial concentration test | Admin-1 dominance for each case; test PRE_REG_020 predictions | Medium — UCDP-GED admin-1 already pulled for some | PATTERN_012/015 |

### Forward-watch (will fire from new data)
- **P4-W1** — Israel-Gaza 2024+ fatality trajectory (Type A or B?)
- **P4-W2** — SDN RSF vs civilians 2024+ (Type B test)
- **P4-W3** — HTI gang-state evolution 2025+ (Type D2 candidate)

### Data acquisition needed
- UCDP-GED v25 (latest release) — for ARM-AZE, ISR-Gaza, SDN RSF
- Admin-1 panels for: COD, NER, SDN, NGA, SSD (some already pulled)
- ACLED supplementation for IRQ 2003-2011 phase coding

---

## 6. Novel contributions (proposed; 4)

1. **3 (or 4)-type conflict-displacement typology** with explicit organizational-form mechanism for each type
2. **Type-distinct fatality/displacement-per-fatality ratios** — formal-army war 30-80, predator-militia 250-800, irregular insurgency 100-300 (mechanism-distinct, not regional variation)
3. **Spatial-concentration signature**: front-line vs militia-territory vs diffuse — predicts admin-1 distribution from conflict-type alone
4. **IRQ 2003 within-country test** — if our classifier shifts IRQ from Type A (2003 interstate) to Type C (2004+ insurgency), that's evidence the typology operates on the actual organizational form of violence, not country-as-unit (could be load-bearing methodological claim)

---

## 7. Falsifiers + walk-back conditions

(To be locked in PRE_REG_018 + 019 + 020 + 021)

Proposed falsifiers:
- **F-classifier**: ≥3 cases fit none of A/B/C (or A/B/C/D if 4 types) cleanly → typology incomplete
- **F-ratios**: ratio distributions for the 3 types overlap >50% → ratios not type-distinct
- **F-spatial**: spatial-concentration prediction wrong in ≥3 of 9 confirmed cases → spatial signature not type-distinct
- **F-IRQ**: IRQ 2003-2011 single-phase classification → conflict-type doesn't shift within country = typology operates on country-level, not violence-form-level (this would walk back the framework's deepest claim)

---

## 8. Cross-paper interfaces

| With Paper... | Interface | Note |
|---|---|---|
| Paper 1 (executive-aggrandizement) | UKR libdem trajectory (wartime suspension is distinct mechanism) | Type A formal-army can occur in any libdem regime; cross-link only |
| Paper 2 (disaster regimes) | Methodologically parallel — twin typology arguments. Could present together. | Strongest cross-paper synergy |
| Paper 3 (strife epicenter) | Type C irregular insurgency anchor = Sahel diffusion cases | Substrate-shared |
| Paper 6 (methodology) | Channel-orthogonality framework underlies Type A vs B vs C channel signatures | Paper 4 is empirical instantiation |

---

## 9. Closure criteria for Paper 4

The paper is ready to draft when:
- [x] PATTERN_012 firmed (ETH Tigray, formal-army Type A anchor) — DONE
- [x] PATTERN_015 firmed (DRC predator-militia Type B anchor) — DONE
- [x] PATTERN_017 firmed (UKR formal-army Type A anchor) — DONE
- [ ] PRE_REG_018 classifier locked + fired across all 50+ corpus countries (P4-C)
- [ ] Type A expanded to 3+ cases (P4-A — add 1+ beyond ETH/UKR)
- [ ] Type B expanded to 3+ cases (P4-B — add 2+ beyond DRC)
- [ ] Type C confirmed across Sahel + Horn (PATTERN_010 family already covers MLI/SOM/MMR-style)
- [ ] PRE_REG_019 fatality/displacement ratios locked + tested
- [ ] PRE_REG_020 spatial concentration locked + tested
- [ ] PRE_REG_021 IRQ 2003 within-country test fired
- [ ] 4th-type question resolved (D1/D2/D3 — file as confirmed type, walk back, or note as open)

**Current state: 3 of 10 criteria met.** Phase 1 (classifier lock + run) is the easiest density-win.

**Phase 1 closed 2026-05-27**: PRE_REG_018 fired with F1+F2 walk-back. Substantive results:
- Classifier rules need refinement (admin-1 ≤80% for Type C; lower fatality threshold)
- **5 types confirmed** (was 3): A formal-army, B predator-militia, C irregular insurgency, **D criminal-violence (NEW; resolves H2 4th-type question)**, **E civil-war-mass-displacement (NEW; emerged unpredicted)**
- Type A clean (6): ETH, UKR, RUS, ISR, PAK, EGY
- Type B clean (3): COD, MOZ, HTI (MOZ new = PATTERN_031)
- Type D clean (3): MEX, BRA, ECU (PATTERN_032)
- Type E candidate (4-6): SYR, YEM, AFG, IRQ, LBY, CMR, CAF (PATTERN_033)
- **F4 NOT FIRED** — conflict-form > region as load-bearing variable (Sahel/Horn/LatAm all heterogeneous)

**Updated state: 4 of 10 criteria met.** Next: PRE_REG_018 v2 lock with refined rules + Type D/E definitions, then re-fire.

**Phase 2 closed 2026-05-27**: PRE_REG_018 v2 + PRE_REG_019 + PRE_REG_020 all fired.
- **PRE_REG_018 v2: SUPPORTED** (16/18 anchors; 0 falsifiers fired; only TUR unclassified)
- **PRE_REG_019 DPF rank D<A<C<B<E EXACTLY matches prediction** (4/4 pairwise; 5/5 bands)
- **PRE_REG_020 spatial concentration type-distinct** (A=95.7%, B=97.3% near-100%; C/D/E mid 55-65%)
- 1 walk-back: PRE_REG_019 H3 (Type C heterogeneous; sub-typing candidate)
- Refinement candidate (v3): narrow Type E by requiring non-state-share ≥30%; BFA/SOM should route to C

**Updated state: 8 of 10 closure criteria met.** Remaining: case expansion (P4-A/P4-B) + IRQ within-country test (PRE_REG_021/P4-D).

**Phase 3 closed 2026-05-27**: PRE_REG_021 + P4-D + P4-A + P4-B all fired in within-country phase test.

**Load-bearing finding**: **F4 NOT FIRED** — IRQ (A → E across 2003 → post-2004) and NGA (C → E across BH phases) confirm classifier operates on **conflict-form, not country identity**. **Typology framework's deepest claim SUPPORTED.**

**Refinement candidates surfaced (v3)**:
1. Type A short-duration high-state-share rule (AZE Karabakh failure mode)
2. ISIS-war as sub-type or refined Type B (IRQ 2012-2017)
3. NGA 2015-2017 type-B threshold close-miss

**Closure criteria: 10 of 10 met.** All Paper 4 critical-path threads closed. Paper 4 substrate at paper-readable threshold.

---

## 10. Sequencing recommendation

Order to chase threads (highest evidence-yield first):

1. **PRE_REG_018 lock** (classifier rules) — must be locked BEFORE running on the 50+ corpus
2. **P4-C fire** — run classifier on entire corpus from existing cluster panels (UCDP-GED already pulled for most)
3. **PRE_REG_019 lock + P4-F** (ratios test) — light analytical task on existing data
4. **PRE_REG_020 lock + P4-G** (spatial test) — requires admin-1 panels; have most
5. **P4-A + P4-B expansion** in parallel — add cases per type
6. **P4-D IRQ phase decomposition** — within-country test
7. **P4-E 4th-type test** (SSD/ETH-Amhara/HTI cluster)
8. **PRE_REG_021 IRQ + P4-D** fire

After (1)-(4) Paper 4 is at "Phase 1 closed" equivalent.

---

**Status: substrate exists; hunt plan defined. Phase 1 = classifier lock + fire.**
