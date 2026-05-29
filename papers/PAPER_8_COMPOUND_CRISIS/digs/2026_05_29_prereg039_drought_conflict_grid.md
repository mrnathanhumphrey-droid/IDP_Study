# Paper 8 — PRE_REG_039: sub-national drought×conflict co-location (mechanism frontier, Phase 2)

**Fired**: 2026-05-29
**Pre-reg**: PRE_REG_039 (locked + committed before any join, HEAD 4e59662)
**Data**: SPEI v2.10 drought-frequency via GEE (`CSIC/SPEI/2_10`, Dec SPEI_12 ≤ −1.0, 1990-2023) at 0.5° cells × UCDP-GED v25.1 geocoded conflict (354k events 1990-2023). 20 countries.
**Status**: **F1 + F3 fired; Set C reversed.** The hazard-level test REJECTS same-place drought-conflict co-occurrence — and reframes the Phase 1 displacement co-location.

---

## Headline

Phase 1 (PRE_REG_038) found the Horn coupling case SOM co-locates its conflict- and drought-**DISPLACEMENT** (+0.30). Phase 2 used dense **hazard** data (UCDP conflict fatalities × SPEI drought frequency) to test whether the underlying hazards share geography. **They do not:**

- **Conflict cells are NOT more drought-prone** — in coupling cases, conflict-intensity vs drought-frequency is flat-to-negative (ETH −0.07, **SOM −0.24 p=0.002**, BRA +0.09, COD +0.005). SOM is significantly *inverse*: its most-conflict cells are its *least* drought-prone.
- **Conflict is NOT locally triggered by drought** — the confound-robust within-cell test (does a cell have more conflict in its drought years?) is **negative** for the coupling cases: ETH/SOM/COD have conflict *higher* in drought years in only 17-27% of cells (Wilcoxon p≈0). If anything, drought years have *less* local conflict.
- **The only positive drought→conflict cases are SYR, AFG, IRQ** (frac-positive 0.58-0.73, p<0.01) — the protracted-war / "Syria 2007-10 drought" climate-conflict cases — which are **NOT** the displacement-coupling countries.
- **Spatial co-location does not track national coupling** (cross-country ρ = −0.15, p=0.52, n=20).

**So compound-crisis coupling is NOT "the same places get hit by drought AND conflict."** The hazards are spatially distinct, and drought does not locally trigger conflict in the coupling cases. This reframes the Phase 1 displacement co-location: the coupling more plausibly operates through **shared displacement destinations** (drought- and conflict-displaced converge on the same receiving areas) and/or **national-temporal overlap**, not co-located hazards.

---

## Results by set

### Set A — coupling cases co-locate (predicted ETH/SOM/BRA spatial ρ > +0.2): NOT SUPPORTED (F1)
| coupling case | conflict-cell vs non-conflict drought-freq (MW) | ρ(conflict-intensity, drought-freq) |
|---|---|:---:|
| ETH | 5 vs 6 (ns, not greater) | −0.07 |
| SOM | 3 vs 5 (ns) | **−0.24 (p=0.002)** |
| BRA | 8 vs 7 (p=0.15) | +0.09 |
| COD | 5 vs 5 (shift p=0.0002) | +0.005 |

None reach +0.2; SOM is significantly negative. **F1 FIRED** — conflict and drought do not share sub-national geography at the hazard level. (Conflict concentrates in populated/contested zones; drought frequency is a climatological property of often-sparse pastoral peripheries.)

### Set B — spatial co-location tracks national coupling: NOT SUPPORTED (F3)
Cross-country Spearman(per-country spatial ρ, national coupling) = **−0.15 (p=0.52, n=20)**. **F3 FIRED** — sub-national hazard co-location does not explain the national coupling sign.

### Set C — within-cell drought→conflict (confound-robust): REVERSED
| group | countries | within-cell drought→conflict |
|---|---|---|
| coupling cases | ETH, SOM, COD, UKR, TUR | **NEGATIVE** (frac-positive 0.17-0.27, p≈0) — conflict *lower* in drought years |
| coupling (weak) | BRA, BGD, MEX | ≈0 (ns) |
| **positive exceptions** | **SYR (+9.5, 0.73), AFG (+2.4, 0.64), IRQ (+0.9, 0.58)** | conflict *higher* in drought years (p<0.01) |
| controls | PHL, NGA, MLI, NER, SDN, COL, MMR, MOZ | negative / ≈0 |

**Predicted: positive in coupling cases, ~0 in controls. Observed: the OPPOSITE** — coupling cases negative, and the only positives are protracted-war cases (SYR/AFG/IRQ) that are NOT displacement-coupling countries. The famous "drought→war" signal shows up exactly where the literature found it (Syria/Afghanistan/Iraq) and NOT in the compound-displacement-coupling cases.

### Set D — orthogonal control: trivially supported (uninformative)
PHL −0.005, NGA −0.09 (≤0 as predicted) — but since nearly all countries are ~0/negative, the control no longer discriminates (unlike Phase 1's displacement test, where controls were distinctly negative against a positive SOM).

---

## Falsifier status

| F | Status |
|---|---|
| F1 (coupling cases no spatial co-location) | **FIRED** (ETH/SOM/BRA/COD ≤ +0.09; SOM −0.24) |
| F2 (universal co-location) | n/a — co-location is absent generally, not universally present |
| F3 (sign doesn't track) | **FIRED** (cross-country ρ=−0.15, p=0.52) |
| F4 (spatial holds but within-cell absent) | n/a — both H1 and H2 are negative for coupling cases (consistent: no static co-vulnerability AND no dynamic triggering) |

---

## Reconciling Phase 1 (+0.30) and Phase 2 (−0.24) for SOM — the mechanism reframe

The two phases measure different objects:
- **Phase 1 (IDU displacement events):** where people are *displaced* — conflict-IDP and drought-IDP co-locate (+0.30). Displacement endpoints cluster around accessible/receiving areas.
- **Phase 2 (UCDP conflict sites × SPEI drought frequency):** where the *hazards* occur — conflict fatalities vs climatological dryness — do NOT co-locate (−0.24), and drought does not locally precede/coincide with conflict.

**Interpretation: the compound crisis is not co-located hazards; it is more likely co-located displacement *outcomes*.** Drought (in pastoral peripheries) and conflict (in populated/contested zones) strike different places, but both push displaced populations toward the same receiving areas, and both elevate national displacement in overlapping years. The "coupling" lives in the displacement system's destinations + national temporal overlap, not in the hazard geography. (Caveat: IDU lat/lon mixes origin/destination roles — disentangling that is the clean Phase 3 follow-up.)

This also dissolves the apparent tension with the ENSO-null (036/037): there is no single shared climate driver AND no local hazard co-occurrence — consistent with coupling being a displacement-system / temporal-overlap phenomenon rather than a co-located physical compound hazard.

**Notable side-finding:** the local drought→conflict trigger (the classic climate-security claim) appears in SYR/AFG/IRQ — exactly the protracted-war cases the literature debates — and is **absent (even inverse) in the displacement-coupling cases**. The drought-displaced-out → fewer-people → less-local-conflict reading is plausible for ETH/SOM/COD (drought depopulates before it inflames), but annual resolution + conflict's own escalation dynamics warrant caution.

---

## Net result for Paper 8

**Phase 2 falsifies the hazard-co-location mechanism (F1+F3) and reverses the local drought→conflict prediction in the coupling cases.** Compound-crisis coupling is NOT same-place drought+conflict and NOT locally drought-triggered conflict. Combined with Phase 1 (displacement co-location) and the ENSO-null, the emerging mechanism is: **coupling is a property of the displacement system — shared receiving destinations and national-temporal overlap of two spatially-distinct, separately-driven hazards — not a co-located physical compound crisis.**

This is the strongest mechanistic statement Paper 8 has reached, and it is a genuine, multiply-triangulated negative on the intuitive "same place, same time, shared driver" picture (ENSO-null + hazard-co-location-null + within-cell-trigger-null), with a constructive reframe toward the displacement-destinations hypothesis.

### Phase 3 candidates (not fired)
1. **Origin vs destination decomposition** of IDU coordinates — test the shared-destination hypothesis directly (do conflict-IDP and drought-IDP share DESTINATIONS while having distinct ORIGINS?).
2. **National-temporal-overlap mechanism** — is the coupling just two independent hazards whose national displacement totals overlap in time (and if so, why those countries — shock-frequency?).

---

## Cross-references
- PRE_REG_039 (this dig); PRE_REG_038 (Phase 1 displacement co-location — reframed here); PRE_REG_033 (coupling census, Set B); PRE_REG_036/037 (ENSO-null); PRE_REG_034 Set B (national contemporaneity).
- `analysis/paper8_prereg039_grid_2026_05_29.json`; `_scripts/paper8_prereg039_grid.py`.
- Data: `data/ucdp/GEDEvent_v25_1.csv` (NOTE: v26_0_4 is 2026-candidate only — use v25_1 for history); SPEI v2.10 via GEE [[reference-google-earth-engine-access]].

## Status
**PRE_REG_039 fired (Phase 2): F1+F3 fired, Set C reversed. Hazard-level drought×conflict do NOT co-locate (SOM −0.24) and drought does not locally trigger conflict in the coupling cases (within-cell negative); positive drought→conflict only in SYR/AFG/IRQ (protracted-war cases, not coupling cases).** Reframes Phase 1: coupling = shared displacement destinations + national-temporal overlap, NOT co-located hazards. Triple-negative (ENSO-null + hazard-co-location-null + local-trigger-null) → displacement-system mechanism. Phase 3 = IDU origin-vs-destination decomposition.
