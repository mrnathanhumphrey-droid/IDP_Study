# Paper 8 — Hunt Plan

## Phase 1 — Coupling census (PRE_REG_033)
**Goal**: separate the coupling minority from the orthogonal majority, formally.
- Compute all-pairs Spearman channel correlations (CF/CD/FD/CS/etc.) for every corpus country-year panel
- Classify: coupling if ≥1 pair |ρ| > 0.5; triple-coupling if all 3 of CF/CD/FD > 0.5
- Test whether coupling-status correlates with a state-fragility scalar (Polity/libdem) or a shock-window-overlap feature
- **Falsifier**: coupling cases share no common feature → idiosyncratic, not a regime

## Phase 2 — ENSO teleconnection (PRE_REG_034)
**Goal**: test the shared-climate-driver mechanism.
- Acquire NOAA ONI (Oceanic Niño Index) monthly 1950-2025
- For each coupling case, align coupled-channel peak-years with ENSO phase (El Niño / La Niña / neutral)
- **Predicted**: coupled channels (esp. drought) peak in La Niña years for Horn (ETH/SOM), El Niño for some
- **Falsifier**: no ENSO alignment → drop teleconnection mechanism

## Phase 3 — Temporal-window / synchronized-shock (PRE_REG_035)
**Goal**: is coupling structural (persistent) or window-transient?
- Split ETH (and SOM/BRA where data allows) into pre-2018 vs 2018-2024
- Bootstrap the coupling correlations with CIs
- **Predicted**: ETH triple-coupling is driven substantially by the 2020-2024 synchronized-shock window (Tigray war + flood + drought); pre-2018 coupling weaker
- **Falsifier**: coupling equally strong in both windows → structural country trait, not window-transient

## Phase 4 — Mechanism synthesis
- Adjudicate ENSO vs synchronized-window vs state-collapse across the coupling cases
- Forward implication: if window-transient, coupling is forecastable from shock-calendar overlap, not country type
