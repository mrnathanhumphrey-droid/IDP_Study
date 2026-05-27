# Paper 2 — Hunt Plan

**Last updated**: 2026-05-25
**Purpose**: structured thread-pulling for Paper 2 from substrate-ready → paper-draftable.

---

## Workflow per thread

1. **Pick** the highest-priority open thread (default = sequencing list below)
2. **Pre-reg lock** if the thread tests a new hypothesis (use PRE_REG_013/014/015/016 slots)
3. **Data pull / analysis** — log script + provenance in `data_notes/`
4. **Findings to dig** — write to `digs/2026_MM_DD_P2_X_short_title.md`
5. **Update status** in this file + THREADS_REGISTER
6. **Update PAPER_2_SCOPE.md** closure criteria checkboxes

---

## Thread board

### Phase 1 — CLOSED 2026-05-25 (sub-typing + ratios; easy density wins)

| ID | Status | Title | Result |
|---|---|---|---|
| PRE_REG_013 | locked + fired | Within-regime sub-typing | H1 SUPPORTED with refinement (Regime 4 5/6; Regime 6 walked back into sharper definition) |
| PRE_REG_016 | locked + fired | Displacement-per-affected ratios | H1 supported, H2 walked back (state-capacity moderation); H3 falsified |
| P2-A | closed-supported + refined | Regime 4 sub-typing 5/6; Regime 6 uniform single-event-driven (refinement); Regime 3 extended to 5 members of 3a | `digs/2026_05_25_P2_A_within_regime_sub_typing.md` |
| P2-I | closed-partial + walk-back + post-hoc | Hazard ratios mechanism-distinct; state-capacity moderation walked back; 3a >> 3b is post-hoc finding | `digs/2026_05_25_P2_I_displacement_per_affected_ratios.md` |

### Phase 2 — CLOSED 2026-05-25

| ID | Status | Title | Result |
|---|---|---|---|
| PRE_REG_017 | locked + fired | Phase 2 regime-expansion predictions | F3 + F4 fired; H1 walked back partially; substantive refinements |
| P2-B | closed-walk-back | Regime 6 expansion | F3 fired — 0/3 testable confirm. R6 capped at 6 (HTI/NPL/TUR/CHL/ECU/ITA) |
| P2-C | closed-data-limited | Caribbean expansion | 1/1 testable confirms (PRI = 3a); 6/7 sub-100K data-sparse |
| P2-D | closed-data-gap | South Pacific expansion | 0/0 testable (all <20K). GIDD systematic under-reporting |
| P2-G | closed-mixed | Regime 2 replication | CHN/MMR/AFG/IRN → Regime 4 sub-types. THA → R1 candidate. ARG/KHM = typology gap |

**New patterns surfaced from Phase 2:**
- PATTERN_028 — THA Regime 1 second member (PAK no longer uniquely R1)
- PATTERN_029 — GRC wildfire-dominant candidate (potential Regime 7)
- PATTERN_030 — Flood-dominant transitional gap (ARG, KHM)

**Confirmed member count: 30** (up from 22)

### Phase 3 — PARTIALLY CLOSED 2026-05-25

| ID | Status | Title | Result |
|---|---|---|---|
| PRE_REG_014 | locked + fired | Regime stability 1980-2024 | **F1 FIRED** — 15/29 shifts; H1 walked back; refined to R6 event-latency |
| P2-H | closed-walk-back + refined | Historical stability test | H1 walked back; substantive finding: R6 event-latency confirmed |
| PRE_REG_015 | locked + partial fit | Climate-attribution USA 3a-3b | A CONSISTENT (USA mega-year freq 7.1%→17.6%, 2.5× increase). B/C deferred |
| P2-F | closed-supported | USA 2024 decomposition | 11.0M total; 93% storm; 22.9× median, 5.2× prior max — corpus single-year high |
| P2-E | open (data acquisition needed) | Climate-attribution data pipeline (HURDAT2/HadISST) | Required for full PRE_REG_015 fit |

**New substantive findings from Phase 3**:
- **Regime 6 is EVENT-LATENT** (PATTERN_020 refined): R6 = (geophysical exposure) × (major event in window). 4 of 6 members became R6 only post-2007.
- **Typology is window-sensitive** for R6 specifically; storm/flood regimes more stable.
- **USA Regime 3a intensifying** trajectory — 2.5× mega-year frequency increase + 5.2× 2024 single-year anchor.

### Optional / sidebar threads

| ID | Status | Title | Effort | Notes |
|---|---|---|---|---|
| P2-J | open | High-capacity vs low-capacity Regime 3 (USA vs PHL) | Light | Could be paper sidebar or Paper 6 methodology |
| P2-K | open | Multi-hazard interaction (HTI EQ + cyclone simultaneous) | Light | Single-case anomaly; spillover OK |
| P2-L | open | Volcanic-displacement as 7th regime? (Iceland, Tonga) | Medium | Scoping only; likely 2-case |

---

## Pre-reg slot status

| Slot | Topic | Status | Block on |
|---|---|---|---|
| PRE_REG_013 | Within-regime sub-typing | NOT LOCKED | Write + lock before P2-A advances to Regimes 2/4/6 |
| PRE_REG_014 | Regime stability over 1980-2024 | NOT LOCKED | Write + lock before P2-H |
| PRE_REG_015 | Climate-attribution regime-shift | NOT LOCKED | Write + lock before P2-E |
| PRE_REG_016 | Displacement-per-affected ratios | NOT LOCKED | Write + lock before P2-I formal claim |

**Pre-reg discipline rule (from substrate-wide CLAUDE.md): "we are always the right method"** — every new hypothesis gets a locked pre-reg with falsifiers BEFORE running the test.

---

## Data acquisition queue

| Source | For | Status |
|---|---|---|
| GIDD Disasters (additional countries) | P2-B, P2-C, P2-D | Have GIDD, need to pull additional countries |
| EM-DAT historical (1900-2007) | PRE_REG_014, P2-H | Not yet pulled |
| NOAA HURDAT2 (Atlantic hurricanes) | P2-F, P2-E (3a intensification) | Not yet pulled |
| ERA5 reanalysis | P2-E (climate-attribution) | Not yet pulled; Copernicus API key at `C:/Users/Nate/.cdsapirc` |
| CHIRPS precipitation | P2-E | Not yet pulled |
| HadISST sea-surface temp | P2-E (Atlantic warming for 3a→3b) | Not yet pulled |
| USGS earthquake catalog (full automation) | P2-B (Regime 6 expansion) | Cross-referenced; need automation |

---

## Methodology infrastructure to build

- [ ] Year-by-year hazard-type breakdown function (reusable across countries)
- [ ] Regime classification rule encoder (deterministic from H1 of PRE_REG_003)
- [ ] Displacement-per-affected calculator (P2-I + PRE_REG_016)
- [ ] Climate-attribution join pipeline (P2-E; heavy)

---

## Closure summary

**Phase 1 complete when**: P2-A + P2-I closed + PRE_REG_013 locked
**Phase 2 complete when**: 30+ confirmed regime members across 6 regimes + Regime 6 expanded to 8+
**Phase 3 complete when**: PRE_REG_014 fired + climate-attribution layer scoped (PRE_REG_015 locked even if data pull lags)
**Paper-draftable when**: 11/11 closure criteria from `PAPER_2_SCOPE.md` Section 8 met

**Current state**: 4/11 closure criteria met. Phase 1 is the easiest density-win and ready to fire.
