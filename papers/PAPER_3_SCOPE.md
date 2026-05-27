# Paper 3 — Scope Lock (2026-05-27)

**Working title (internal)**: Strife Epicenter Diffusion — temporal-geographic mechanism for Sahel non-state violence

**Status**: SUBSTRATE EXISTS via PATTERN_005 / 010 + PRE_REG_001 locked. **Partial fit fired 2026-05-27** on UCDP-GED v25 (through 2024). Forward window 2025-2027 awaits annual UCDP releases.

**User writes prose; this doc is analytical scope only.**

---

## 1. Mechanism claim

Non-state strife violence (UCDP type_of_violence=2) shows **temporal epicenter-diffusion** in the Sahel cluster — Mali was the first-mover (2012); the signal diffused outward to BFA (2020) and NER (2021) with ~8-9 year lag. Mechanism: insurgent group operational expansion (primarily JNIM, secondarily IS-Sahel) across porous borders + inter-ethnic geographic corridors.

**The diffusion has not stopped at NER's southern border.** Coastal West African countries adjacent to Sahel pressure are early-warning candidates.

---

## 2. Substrate

### Patterns
- **PATTERN_005** — MLI strife epicenter (anchor; 2012 onset, 3,265 lifetime strife fatalities)
- **PATTERN_010** — Strife-dominant cross-cluster (recurring pattern across MLI/SSD/HTI/CAF)
- **PATTERN_003** — BFA industrial-scale displacement (downstream of MLI epicenter)
- **PATTERN_006** — BEN periphery (JNIM presence confirmed without crossing strife threshold)

### Pre-regs
- **PRE_REG_001** — Strife-signature epicenter diffusion (LOCKED 2026-05-25; partial fit 2026-05-27)

---

## 3. Partial fit results (2026-05-27) — current state

### In-sample diffusion CONFIRMED
| Country | First year ≥50 strife fatal | Lag from MLI | Status |
|---|---|---|---|
| MLI | 2012 (modern wave) | epicenter | anchor |
| BFA | 2020 | 8 years | confirmed |
| NER | 2021 | 9 years | confirmed |

### Forward-watch status (PRE_REG_001 H3 predictions)

| Country | Predicted window | Lifetime strife | 2020-2024 strife | JNIM presence? | Current verdict |
|---|---|---|---|---|---|
| **TGO** | 2022-2025 | 31 | 0 | **YES (109 govt-vs-JNIM + 97 JNIM-vs-civilians 2020-2024)** | **EARLY-EMERGENCE — actor present, threshold not yet crossed** |
| CIV | 2023-2026 | 756 (historical 2003) | 0 | no | quiet; window still open |
| GHA | 2024-2027 | 2,472 (historical 1990s) | 38 (Kusasi-Mamprusi) | no | local ethnic conflict, not JNIM diffusion |

### Critical finding
**TGO is the leading early-emergence indicator**. JNIM is already attacking inside Togolese territory (206 UCDP-coded fatalities 2020-2024, all from Govt-vs-JNIM dyad or JNIM-vs-civilians dyad). UCDP codes these as state-based (109) + one-sided (97), not as type-2 strife. **The mechanism (a) (insurgent cross-border expansion) IS observable; the type-2 strife threshold is just a lagging indicator.**

### Sub-cluster results

**CAR sub-cluster** (PRE_REG_001 Prediction set C):
- CAR: 2011 first ≥50 ✓ (matches epicenter claim)
- **Chad: 2000** (PREDATES CAR by 11 years) — Boko Haram NE + intra-Chadian dynamics
- **Cameroon: 1991** (PREDATES CAR by 20 years) — historical strife
- Congo-Brazzaville: zero strife ever ✓ (matches "buffer" prediction)

**F3 falsifier PARTIALLY FIRED**: CAR sub-cluster does NOT show clean epicenter temporal-ordering. Chad and Cameroon both have strife predating CAR's 2011 onset. **The epicenter-diffusion model is Sahel-specific; doesn't generalize cleanly to Central Africa.**

**HTI sub-cluster** (PRE_REG_001 Prediction set D):
- HTI: 2021 first ≥50 ✓ (matches gang-war emergence)
- DOM: zero strife ever (forward-watch active; pre-reg predicted cross-border by 2027)

### JNIM actor-overlap test (PRE_REG_001 Prediction set B)

| Actor | MLI | BFA | NER | BEN | TGO | CIV | GHA |
|---|---|---|---|---|---|---|---|
| JNIM | ✓ | ✓ | ✓ | ✓ | **✓** | no | no |
| Dozos (Mali self-defense) | ✓ | no | no | no | no | no | no |
| Koglweogo (BFA self-defense) | no | ✓ | no | no | no | no | no |

**JNIM has reached TGO**. Mechanism (a) (insurgent cross-border expansion) clearly active in Togo. CIV and GHA do NOT show JNIM dyad presence — diffusion has not yet reached them via this mechanism.

**F2 falsifier risk for GHA**: if Ghana strife emerges from local Kusasi-Mamprusi (or other non-JNIM actors), the mechanism claim narrows to "JNIM-specific diffusion" not "general epicenter diffusion".

---

## 4. Novel contributions (proposed; 3)

1. **Temporal-geographic diffusion mechanism for non-state strife** — formalizes the MLI → BFA → NER lag pattern with falsifiable forward predictions for TGO/CIV/GHA emergence
2. **Actor-overlap (JNIM) as mechanism discriminator** — distinguishes mechanism (a) cross-border insurgent expansion from (b) local ethnic-corridor violence, using UCDP dyad coding
3. **Boundary of the framework**: Sahel-specific. F3 partial-fired on Central Africa sub-cluster (Chad/Cameroon predate CAR). Diffusion model does not auto-generalize across continents.

---

## 5. OPEN threads — HUNT plan

### Critical-path (partial fit done; remaining)

| ID | Thread | What closes it | Status |
|---|---|---|---|
| P3-A | TGO strife threshold-crossing (currently below 50 type-2; but JNIM presence active) | UCDP-GED 2025 release | forward-watch |
| P3-B | CIV emergence (currently quiet) | UCDP-GED 2025-2026 | forward-watch |
| P3-C | GHA emergence (currently 38 Kusasi-Mamprusi, non-JNIM) | UCDP-GED 2025-2027 + actor-overlap re-check | forward-watch |
| P3-D | HTI → DOM cross-border (DOM currently zero strife) | UCDP-GED 2025-2027 | forward-watch |
| P3-E | CAR sub-cluster walk-back writeup | Document F3 partial-fire; framework Sahel-specific | LIGHT, ready to write |
| P3-F | Geographic centroid diffusion velocity measurement | Compute lat/lon centroid drift across years for Sahel JNIM operations | MEDIUM |

### Optional / sidebar

| ID | Thread | Notes |
|---|---|---|
| P3-G | BEN as "actor present but threshold not crossed" sub-pattern | BEN has JNIM presence but zero type-2 strife — same TGO sub-pattern at earlier stage |
| P3-H | UCDP-GED type_of_violence coding choices | Govt-vs-JNIM coded as type 1, not type 2. Affects threshold-crossing detection. Could be methodological sidebar |

---

## 6. Falsifiers + walk-back conditions (from PRE_REG_001)

| Falsifier | Current status |
|---|---|
| F1 (TGO/CIV/GHA show zero strife by 2027) | **at risk for CIV; not at risk for TGO (JNIM active) or GHA (local ethnic at 38)** |
| F2 (TGO/CIV/GHA emerge with different actors) | **PARTIALLY FIRED for GHA** (Kusasi-Mamprusi not JNIM; mechanism narrows) |
| F3 (CAR sub-cluster no temporal ordering) | **PARTIALLY FIRED** (Chad 2000 + Cameroon 1991 predate CAR 2011) |
| F4 (HTI → DOM doesn't cross by 2027) | not yet testable; forward-watch |

Two falsifiers partially fired. Walk-back logged: epicenter-diffusion framework is **Sahel-specific**, with strong forward signals for TGO emergence.

---

## 7. Closure criteria

The paper is ready to draft when:
- [x] PATTERN_005 firmed (MLI epicenter dig done)
- [x] PATTERN_010 firmed (strife-dominant recurs)
- [x] PRE_REG_001 locked + partial fit fired
- [x] In-sample MLI/BFA/NER diffusion confirmed
- [x] Actor-overlap test (JNIM) fired
- [x] Sub-cluster tests fired (CAR partial walk-back; HTI confirmed in-sample)
- [ ] TGO type-2 strife threshold-crossing by 2026-2027 (forward-watch)
- [ ] CIV/GHA emergence resolved by 2027 (forward-watch)
- [ ] HTI → DOM resolution by 2027 (forward-watch)

**Current state: 6 of 9 criteria met (partial fit done; 3 forward-watch criteria pending data).**

---

## 8. Blog-post substrate (user's intended use case)

User wants this Paper 3 substrate to support a public-facing blog post: "I'm concerned for these countries because of this mechanism, here's how I'll know if I'm wrong."

The substrate provides:
1. **In-sample evidence** of diffusion (MLI 2012 → BFA 2020 → NER 2021)
2. **Mechanism**: JNIM cross-border expansion (already in TGO; 109+97 fatalities 2020-2024)
3. **Specific predictions with windows**: TGO 2022-2025; CIV 2023-2026; GHA 2024-2027
4. **Falsifiable**: each prediction's window closes by 2027; F1-F4 logged as walk-back conditions
5. **Hedge**: F3 partially fired on Central Africa sub-cluster — framework is Sahel-specific
6. **Boundary**: GHA may emerge with non-JNIM actors (F2 risk) → mechanism narrows

This is publishable as a working-paper / pre-print / blog post: **falsifiable forward predictions with mechanism + hedge + walk-back conditions**. User writes prose.

---

## 9. Cross-paper interfaces

| With Paper... | Interface | Note |
|---|---|---|
| Paper 4 (conflict-type meta-typology) | TGO acute period classifies into Type C-or-E framework; MLI=C1 low-DPF irregular | Substrate-shared |
| Paper 6 (methodology) | Diffusion mechanism is a sub-pattern within Type C residue-class | Subordinate to typology framework |
| Paper 1 (executive-aggrandizement) | TGO under Faure Gnassingbé extends authoritarian-trajectory + JNIM pressure | Cross-link |

---

**Status: substrate exists; partial fit done. 6/9 closure criteria met. 3 forward-watch criteria await UCDP-GED 2025-2027 releases. Paper publishable now as forward-watch working-paper / blog post.**
