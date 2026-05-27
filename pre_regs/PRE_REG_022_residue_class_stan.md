# Pre-Registration 022 — Residue-Class Stan Model Outperforms Classical Hierarchical Baseline

**ID:** PRE_REG_022
**Locked:** 2026-05-27
**Substrate:** Papers 2 + 4 typology assignments + PATTERN_001 channel-orthogonality + PRE_REG_004 92% orthogonality
**Status:** LOCKED — predictions and falsifiers pre-committed; first fit fires on country-year-channel panel

---

## 1. Hypothesis

**H1 (load-bearing — methodology contribution):** A hierarchical Stan model with **residue-class** partial-pooling (pooling by discrete-type membership from Papers 2 + 4) **outperforms** a classical hierarchical baseline (pooling by continuous covariates only) on out-of-sample predictive performance.

**Metric**: ΔLOO-CV (leave-one-out cross-validation expected log predictive density). Predicted: **ΔLOO ≥ 5** (residue-class better). LOO-CV is the gold-standard out-of-sample metric in Bayesian model comparison (Vehtari, Gelman & Gabry 2017).

**H2 (mechanism):** Residue-class wins because Papers 2 + 4 typology captures discrete generative-process membership (disaster regime / conflict type) that continuous covariates can't recover. Modeling without residue-classes systematically under-fits when the data-generating process is typological.

**H3 (channel-level):** The improvement is largest for channels where Papers 2 + 4 typology is sharpest:
- Storm channel (Regime 3a/3b sub-typing in Paper 2)
- EQ channel (Regime 6 event-latency from Paper 2)
- Conflict channel (Types A/B/D well-anchored from Paper 4)

Smaller improvement expected for:
- Flood channel (Regime 1/2/4 with typology gap; Paper 2 finds heterogeneity)
- Drought channel (sub-channel within Regime 4; less discriminating)

---

## 2. Model specifications (locked BEFORE fit)

### Baseline model (classical hierarchical, no typology)
```
y_{c,t,h} ~ NegBinomial(mu_{c,t,h}, phi)
log(mu_{c,t,h}) = alpha + beta_c + gamma_t + delta_h
                  + b1 * libdem_{c,t} + b2 * log_population_{c,t} + b3 * log_gdp_{c,t}
beta_c ~ Normal(0, sigma_country)
gamma_t ~ Normal(0, sigma_year)
delta_h ~ Normal(0, sigma_hazard)
```

Where:
- y_{c,t,h} = displacement events for country c, year t, hazard channel h
- alpha = global intercept
- beta_c = country random effect
- gamma_t = year random effect
- delta_h = hazard random effect
- Covariates: V-Dem libdem, log-population, log-GDP

### Residue-class model (proposed; same data, adds typology)
```
y_{c,t,h} ~ NegBinomial(mu_{c,t,h}, phi)
log(mu_{c,t,h}) = alpha + beta_c + gamma_t + delta_h
                  + zeta_{class(c,h)} * intercept_addition
                  + b1 * libdem_{c,t} + b2 * log_population_{c,t} + b3 * log_gdp_{c,t}
zeta_{class(c,h)} ~ Normal(0, sigma_class)
class(c,h) = {disaster regime for h in disaster channels, conflict type for h in conflict channel}
```

Where:
- class(c,h) maps each country×channel to a residue-class from Papers 2 + 4
- Disaster channels (flood, storm, EQ, drought, wildfire) → Paper 2 regime (1/2/3/3a/3b/4/6)
- Conflict channel → Paper 4 type (A/B/C/D/E)
- zeta = class-level effect

### Data
- Country-year-hazard panel 2008-2024 (matches Papers 2/4 substrate window)
- Sample: 30+ countries with confirmed regime/type assignments (Papers 2 + 4)
- ~30 countries × 17 years × 5 main channels = ~2,550 observations
- y = log-transformed where appropriate; NegBinomial likelihood handles overdispersion

### Inference
- Stan via PyMC or cmdstanpy interface
- 4 chains × 2000 warmup × 2000 samples
- LOO-CV via the `loo` R package or equivalent Python implementation (`arviz.loo`)
- Compare ΔLOO between models

---

## 3. Pre-locked predictions

### Prediction set A — Headline: residue-class outperforms baseline
**Predicted**: ΔLOO ≥ 5 (residue-class better) with se_diff ≤ 2 → **clear improvement, not marginal**.

### Prediction set B — Channel-specific improvement gradient
ΔLOO per channel:
- Storm channel: ≥ 3 (sub-typing helps)
- EQ channel: ≥ 4 (event-latency captured by residue-class)
- Conflict channel: ≥ 4 (clean A/B/D types)
- Flood channel: 0-3 (typology gap absorbs some signal)
- Drought channel: 0-2 (sub-channel, less discriminating)

### Prediction set C — Within-type heterogeneity test
Posterior predictive checks: residue-class model's posterior interval for each type should be NARROWER than baseline's posterior interval for the same observation. **Predicted**: ≥ 70% of test observations show narrower residue-class interval.

### Prediction set D — Specific case anchor
USA 2024 (the 11.0M storm + 1.96M baseline-max anchor): residue-class model should predict the magnitude correctly (within 50% of observed); baseline should under-predict by 5× or more.

---

## 4. Falsifiers

- **F1 (H1 walks back)**: ΔLOO < 5 OR se_diff > 2 → residue-class doesn't meaningfully outperform baseline
- **F2 (channel improvement absent)**: No channel shows ΔLOO ≥ 3 → mechanism-distinct effect of typology fails
- **F3 (posterior interval test fails)**: < 50% of test observations show narrower residue-class interval → no within-type tightening
- **F4 (USA 2024 anchor missed)**: BOTH models under-predict USA 2024 → models miss the climate-attribution intensification signal entirely; typology and methodology both fail for this case

F1 firing = H1 walks back; methodology contribution diluted. Paper 6 reframes as "typology aware but no clear performance gain."
F1 + F2 firing together = methodology doesn't transfer to predictive setting. Paper 6 walks back substantively.

---

## 5. Methodology details

### Channel definitions (matches Papers 2 + 4)
- Conflict channel: GIDD `Conflict Stock Displacement` aggregated yearly
- Flood channel: GIDD `Disaster Internal Displacements` filtered hazard = Flood
- Storm channel: same filtered hazard = Storm
- EQ channel: same filtered hazard = Earthquake
- Drought channel: same filtered hazard = Drought
- Wildfire channel: same filtered hazard = Wildfire (when meaningful)

### Class assignments
- Use PRE_REG_018 v2 conflict-type assignments (5 types A/B/C/D/E)
- Use PATTERN_019 + 020 + 025 disaster regime assignments (1/2/3/3a/3b/4/6)
- Countries without confirmed type/regime → excluded from the residue-class model OR assigned to "other" class

### Numerical stability
- Use non-centered parameterization for all hierarchical levels (per `feedback_non_centered_for_sparse_funnels`)
- log-transform displacement counts with offset
- standardize continuous covariates

---

## 6. Cross-references
- Papers 2 + 4 (typology source)
- PATTERN_001 (channel-orthogonality)
- PRE_REG_004 (92% orthogonality)
- PRE_REG_023 (forthcoming — admin-1 sub-national orthogonality)
- PRE_REG_024 (forthcoming — forward-prediction validation)

---

## 7. Provenance
Locked 2026-05-27 before Stan fit. Will be hashed and committed to git.
