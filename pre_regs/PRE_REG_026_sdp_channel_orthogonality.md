# Pre-Registration 026 — US SDP Channel-Orthogonality

**ID:** PRE_REG_026
**Locked:** 2026-05-27
**Substrate:** PRE_REG_025 (SDP framework definitional) + Papers 6 methodology + US homelessness data (to be pulled)
**Status:** LOCKED — predictions pre-committed; first fit fires after HUD + Eviction Lab + ACS data pulled

---

## 1. Hypothesis

**H1 (SDP channel-orthogonality):** US homelessness decomposes into orthogonal channels at state-year level. Most state-years show ≤1 channel dominant (>50% of state's homeless population in that year).

**Proposed SDP channels**:
1. **Eviction-driven** — homelessness caused proximately by formal eviction (rent default, lease termination)
2. **Unaffordability-driven** — homelessness from inability to afford rent without formal eviction (cost-burden tipping point; doubled-up to streets)
3. **Institutional-discharge** — homelessness from exit from foster care, prison, mental hospital, etc. without housing plan
4. **Domestic-violence-fled** — homelessness from leaving abusive household
5. **Disaster-displacement-not-recovered** — IDP-channel cases that didn't return to housing

**Predicted orthogonality rate**: ≥ 60% at state-year level (lower than IDP's 92% due to data heterogeneity + counts being smaller).

**H2 (channel-to-mechanism mapping)**: Each channel corresponds to a structural mechanism:
- Eviction-driven → housing-supply + rent-affordability structural conditions
- Unaffordability-driven → wage-vs-housing-cost ratio
- Institutional-discharge → welfare-state design (or lack thereof)
- DV-fled → welfare-state architecture (shelter availability)
- Disaster-not-recovered → climate-attribution + post-disaster reconstruction policy

**H3 (state-level heterogeneity):** States cluster by dominant channel. E.g., CA/NY = eviction-driven + unaffordability-driven; some Southern states = institutional-discharge; states with extreme cost-burden = unaffordability-driven; storm-belt states = disaster-not-recovered.

---

## 2. Pre-locked predictions

### Prediction set A — Orthogonality rate
Among US state-years 2007-2024 with sufficient data (CoC homelessness counts available), ≥ 60% show single-channel dominance.

### Prediction set B — Channel-to-region mapping
| State | Predicted dominant channel |
|---|---|
| CA | Unaffordability-driven (high cost-burden share) |
| NY | Eviction-driven (high eviction rate) |
| MS | Institutional-discharge or DV-fled |
| TX | Disaster-not-recovered (post-Harvey 2017, Beryl 2024) + unaffordability |
| FL | Disaster-not-recovered (post-Helene 2024) + unaffordability |
| LA | Disaster-not-recovered + institutional-discharge |
| MA | Unaffordability-driven (high cost-burden) |
| Detroit/MI | Eviction-driven + institutional-discharge |
| Mid-Atlantic | Mixed |

≥ 6 of 9 states match predicted dominant channel.

### Prediction set C — State residue-class structure
US states cluster into 3-5 homelessness regimes (parallel to Paper 2 disaster regimes). Predicted classes:
- **CA-pattern (severe unaffordability)**: CA + NY + MA + DC + HI
- **TX/FL-pattern (disaster + unaffordability)**: TX + FL + LA
- **MS-pattern (institutional + welfare-thin)**: MS + AL + AR + Southern states
- **WA/OR-pattern (unaffordability + DV-fled)**: WA + OR + CO
- **Rest-of-country**: mixed

---

## 3. Falsifiers

- **F1 (orthogonality fails)**: < 40% of state-years show single-channel dominance → SDP channels not orthogonal; methodology partially doesn't transfer
- **F2 (channel mapping random)**: < 4 of 9 states match predicted dominant channel → channel-to-region mapping not predictable from structural conditions
- **F3 (residue-class structure absent)**: US states don't cluster meaningfully → SDP framework doesn't have residue-class structure parallel to IDP

F1 + F3 firing together = methodology doesn't transfer to SDP fully.

---

## 4. Methodology

### Data acquisition required
- **HUD AHAR PIT counts** 2007-2024 by CoC (Continuum of Care)
- **HUD CoC Long-Term Trends Dataset**
- **Eviction Lab (Princeton)** county-level eviction filings 2000-2024
- **ACS** housing cost-burdened share 2007-2024 by state
- **HUD HMIS** (Homeless Management Information System) for sub-typing where available
- **DV-fled estimates** — NCADV / Mary Kay Foundation / DV shelter data

### Test sequence
1. Build US state-year-channel panel
2. Channel decomposition (where HMIS data allows)
3. Orthogonality test
4. Cluster analysis on states
5. Channel-to-region mapping check

### Acknowledgments at lock time
- Sub-typing channels at HUD level is hard; HUD AHAR aggregates "chronically homeless" / "veterans" / "families" / "youth" — not by structural cause
- Some state-years may lack sufficient HMIS data for channel decomposition; these excluded
- Eviction Lab provides eviction data but NOT homelessness causation linkage; assumption: eviction trends correlate with eviction-driven homelessness rate

## 5. Cross-references
- PRE_REG_004 (IDP channel-orthogonality anchor)
- PRE_REG_025 (SDP framework definitional)
- PRE_REG_022 (Paper 6 residue-class IDP methodology)
- Papers 2 + 4 + 6 methodology

## 6. Provenance
Locked 2026-05-27 before HUD + Eviction Lab + ACS data pulled. First fit fires after Phase 1 data acquisition.
