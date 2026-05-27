# Paper 4 — Hunt Plan

**Last updated**: 2026-05-25
**Purpose**: structured thread-pulling for Paper 4 from substrate-existing → paper-draftable.

---

## Workflow per thread

1. **Pick** the highest-priority open thread (default = sequencing list below)
2. **Pre-reg lock** if the thread tests a new hypothesis (use PRE_REG_018/019/020/021 slots)
3. **Data pull / analysis** — log script + provenance in `data_notes/`
4. **Findings to dig** — write to `digs/2026_MM_DD_P4_X_short_title.md`
5. **Update status** in this file + THREADS_REGISTER
6. **Update PAPER_4_SCOPE.md** closure criteria checkboxes

---

## Thread board

### Phase 1 — CLOSED 2026-05-27

| ID | Status | Title | Result |
|---|---|---|---|
| PRE_REG_018 | locked + fired | Conflict-type classifier | F1+F2 walk-back; substantive typology expands to 5 types; H2 RESOLVED via Type D |
| P4-C | closed-walk-back + 2 NEW TYPES | Apply classifier to full corpus | 35 country-periods; Type D (MEX/BRA/ECU) + Type E (SYR/YEM/AFG/...) emerge |

**New patterns surfaced from Phase 1**:
- PATTERN_031 — MOZ Cabo Delgado as Type B (second member beyond COD)
- PATTERN_032 — LatAm criminal-violence as Type D (NEW 4th type)
- PATTERN_033 — Civil-war-mass-displacement as Type E (NEW 5th candidate)

**Next**: PRE_REG_018 v2 with refined rules + Type D/E definitions; re-fire classifier.

### Hunt — Phase 2 (ratios + spatial; type-distinct mechanism tests)

| ID | Status | Title | Effort | Next step |
|---|---|---|---|---|
| **PRE_REG_019** | pending lock | Type-distinct fatality/displacement ratios | Pre-reg | Lock prediction: A ≈ 30-80, B ≈ 250-800, C ≈ 100-300 |
| P4-F | open | Compute ratios for each confirmed case | Light | Math on existing UCDP-GED + GIDD |
| **PRE_REG_020** | pending lock | Type-distinct spatial concentration | Pre-reg | Lock prediction: A front-line ≥70%, B militia-territory ≥70%, C diffuse no admin-1 >50% |
| P4-G | open | Admin-1 dominance per case | Medium | UCDP-GED admin-1 already pulled for ETH/COD/UKR; need NER/SDN/NGA |

### Hunt — Phase 3 (case expansion + IRQ within-country test)

| ID | Status | Title | Effort | Next step |
|---|---|---|---|---|
| P4-A | open | Type A expansion (ARM-AZE 2020, ISR-Gaza 2023+) | Medium | UCDP-GED pull for additional countries |
| P4-B | open | Type B expansion (SDN RSF 2023+, NGA Boko Haram) | Medium | UCDP-GED + ACLED for fresh cases |
| **PRE_REG_021** | pending lock | IRQ 2003 within-country phase decomposition | Pre-reg | Lock: classifier should shift IRQ from A (2003) to C (2004+) |
| P4-D | open | IRQ 2003-2011 phase test | Medium-heavy | Temporal admin-1 split + UCDP+ACLED |
| P4-E | open | 4th-type test (D1/D2/D3) | Medium-heavy | Run classifier on SSD/ETH-Amhara/HTI; see if 4th cluster emerges |

### Optional / sidebar

| ID | Status | Title | Notes |
|---|---|---|---|
| P4-J | open | Funding-per-fatality by type | Cross-link to FTS data; could be sidebar finding |
| P4-K | open | Displacement-per-affected by conflict-type | Mirror to Paper 2 P2-I; potential 5th novel contribution |
| P4-L | open | Conflict-type × disaster-regime co-occurrence | Twin-paper synthesis sub-claim |

---

## Pre-reg slot status

| Slot | Topic | Status | Block on |
|---|---|---|---|
| PRE_REG_018 | Conflict-type classifier | NOT LOCKED | Write + lock before P4-C runs |
| PRE_REG_019 | Type-distinct ratios | NOT LOCKED | Write + lock before P4-F runs |
| PRE_REG_020 | Type-distinct spatial concentration | NOT LOCKED | Write + lock before P4-G runs |
| PRE_REG_021 | IRQ within-country test | NOT LOCKED | Write + lock before P4-D runs |

**Pre-reg discipline rule (from substrate-wide CLAUDE.md): "we are always the right method"** — every new hypothesis gets a locked pre-reg with falsifiers BEFORE running the test.

---

## Data acquisition queue

| Source | For | Status |
|---|---|---|
| UCDP-GED v25 (latest release) | P4-A, P4-B, P4-D | Have UCDP-GED v24; check v25 release |
| Admin-1 panels: SDN, NGA, IRQ | P4-G, P4-D | Need to pull |
| ACLED 2024-2025 | P4-A (ISR-Gaza), P4-B (SDN RSF) | Need to pull |
| ARM-AZE 2020 UCDP data | P4-A (Nagorno-Karabakh) | Already in UCDP-GED v24; query |

---

## Methodology infrastructure to build

- [ ] Conflict-type classifier function (deterministic from PRE_REG_018 rules)
- [ ] Fatality/displacement-per-fatality calculator per country-period
- [ ] Admin-1 dominance ratio (top-3 admin-1 share of total country fatalities)
- [ ] Actor-composition signature (state vs irregular vs single-brand-dominant)
- [ ] Channel-share calculator (already exists for PATTERN_001/019 family)

---

## Closure summary

**Phase 1 complete when**: PRE_REG_018 locked + P4-C corpus-wide classifier fired
**Phase 2 complete when**: PRE_REG_019 + 020 fired; type-distinct mechanism claims tested
**Phase 3 complete when**: Each type has 3+ confirmed cases; IRQ within-country test fired; 4th-type question resolved
**Paper-draftable when**: 10/10 closure criteria from `PAPER_4_SCOPE.md` Section 9 met

**Current state**: 3/10 closure criteria met (anchor patterns firmed). Phase 1 is the easiest density-win and ready to fire on next call.
