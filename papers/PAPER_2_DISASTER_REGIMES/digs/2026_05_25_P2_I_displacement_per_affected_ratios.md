# P2-I Dig — Displacement-per-affected ratios (PRE_REG_016 first fit)

**Fired**: 2026-05-25
**Pre-reg**: PRE_REG_016 (locked same day, before run)
**Script**: `D:/IDP/_scripts/paper2_phase1_fire.py`
**Data**: GIDD Disasters 2008-2024 + EM-DAT 2008-2024 — joined on ISO3 × Year × Hazard
**Joined records**: 1,680 country-year-hazard cells

---

## Headline

- **H1 (mechanism-distinct ratios): MIXED**. EQ ≥ 20% confirmed (33.6%) → F1 not fired ✓. But Flood (31.5%) and Storm (28.8%) are within 3pp — F2 not fired but the "Flood = 10-25%" specific prediction was wrong; floods drive much higher displacement-per-affected than predicted.
- **H2 (state-capacity moderation): WALKED BACK**. 0 of 3 contrasts meet the directional + magnitude threshold. ITA > NPL (97% vs 30%) and JPN > HTI (38% vs 31%) are INVERTED (opposite direction from prediction).
- **H3 (PAK > IND): FALSIFIED**. IND (45%) > PAK (30%); steady-high-flood drives HIGHER displacement-per-affected than bimodal-mega-flood. Predicted direction was wrong.
- **Big finding**: Regime 3a (USA, CUB) shows ratio 85% — massively higher than Regime 3b (PHL) at 37%. Predicted opposite direction. **Bimodal mega-storms produce HIGHER displacement-per-affected than perpetual storms.**

---

## Hazard-type medians

| Hazard | N | Median % | P25 % | P75 % | Predicted | Verdict |
|---|---|---|---|---|---|---|
| Earthquake | 166 | **33.6** | 11.4 | 93.2 | ≥30% | ✓ matches |
| Flood | 921 | **31.5** | 10.2 | 80.4 | 10-25% | ABOVE band |
| Storm | 396 | **28.8** | 7.9 | 70.1 | 10-30% | ✓ matches |
| Drought | 22 | **1.3** | 0.05 | 2.8 | <5% | ✓ matches |

**F1 (EQ < 20%)**: NOT FIRED ✓
**F2 (|Storm − Flood| > 15pp)**: NOT FIRED (diff = 2.7pp) ✓

Floods being ABOVE the predicted band is a finding — flood-displacement is more comprehensive than I expected. Possible mechanism: prolonged flood inundation (PAK 2022, BGD perennial) forces high % of affected populations to relocate.

---

## Regime-by-regime median ratios

| Regime | N | Median % | P25 % | P75 % | Countries | Predicted |
|---|---|---|---|---|---|---|
| 1 | 25 | 30.5 | 15.2 | 99.9 | PAK | 20-30% ✓ |
| 2 | 35 | **45.1** | 11.6 | 86.9 | IND | 8-15% — ABOVE |
| 3 (mixed) | 85 | 26.5 | 9.1 | 72.2 | DOM, FJI, MOZ, VNM, VUT | 15-25% (close) |
| **3a** | 33 | **85.1** | 11.0 | 123.4 | CUB, USA | 10-20% — WAY ABOVE |
| 3b | 53 | 37.1 | 19.9 | 68.7 | PHL | 20-30% (above) |
| 4 | 169 | 27.3 | 9.4 | 67.7 | BGD/BRA/IDN/JPN/MEX/PER | 10-20% (above) |
| 6 | 108 | 31.0 | 11.3 | 80.2 | HTI/NPL/CHL/ECU/TUR/ITA | 30-50% ✓ |

**F4 (regimes within 10pp)**: NOT FIRED (spread = 58.6pp) ✓ — regimes ARE separable

**Two stunning findings**:

1. **Regime 3a (85.1%) >>> Regime 3b (37.1%)** — predicted opposite. Bimodal mega-storms produce more displacement per affected than perpetual mega-storms. **Interpretation**: USA Helene/Milton 2024 + CUB cyclone evacuations report high IDP-per-affected because evacuation IS the displacement event; PHL chronic exposure has lower per-event displacement because populations stay in place between events. Counter to my "state-capacity reduces displacement" intuition — in fact, mandatory evacuation infrastructure INCREASES counted displacement.

2. **Regime 2 (IND) 45% vs Regime 1 (PAK) 30%** — predicted PAK > IND. **Interpretation**: India's chronic Brahmaputra/Ganges flooding generates higher IDP-per-affected because affected counts may be more conservatively measured; PAK's mega-floods spread "affected" across enormous denominators (33M affected in 2022).

These flips suggest the displacement-per-affected ratio is more about **how each country COUNTS displacement and affected** than about the physical mechanism. EM-DAT "affected" definitions are heterogeneous: some country reports include impacted-without-displacement; others include only severely-affected.

---

## State-capacity contrasts (H2)

| Contrast | High-capacity | Low-capacity | Predicted | Actual | Meets ≥10pp? |
|---|---|---|---|---|---|
| Regime 3 Storm | USA 33.5% (n=6) | PHL 37.1% (n=17) | USA < PHL | +3.6pp ✓ direction | NO |
| Regime 6 EQ | ITA 97.2% (n=3) | NPL 29.9% (n=4) | ITA < NPL | −67.3pp INVERTED | NO |
| Mixed EQ | JPN 37.8% (n=9) | HTI 31.3% (n=3) | JPN < HTI | −6.5pp INVERTED | NO |

**F3 (< 2 of 3 meet)**: FIRED → **H2 WALKED BACK**

**Why H2 fails**:
- ITA n=3 EQ events: L'Aquila 2009, Amatrice 2016, Marche 2022. Each destroyed historic-center building stock; "affected" was narrowly defined. ITA's 97% ratio = nearly every counted-affected person was displaced.
- JPN n=9 includes Tohoku 2011 (470K displaced from coastal evacuation zone). High-capacity evacuation protocols INCREASE recorded displacement.
- **State capacity may operate inversely on displacement counting**: better infrastructure → better measurement → higher recorded displacement-per-affected.

**Refined understanding**: displacement-per-affected is NOT a pure mechanism signal; it's confounded by reporting practices + evacuation infrastructure. H1 (hazard-type ratios) still survives because EQs are physically distinct from droughts. But H2 (state-capacity moderation) is not detectable in EM-DAT/GIDD data.

---

## Falsifier check (PRE_REG_016)

| Falsifier | Threshold | Result | Fired? |
|---|---|---|---|
| F1 (EQ < 20%) | EQ median fails | EQ = 33.6% | NO ✓ |
| F2 (\|Storm − Flood\| > 15pp) | channels indistinguishable | diff = 2.7pp | NO ✓ |
| F3 (< 2 of 3 state-capacity contrasts) | H2 walked back | 0 of 3 met | **YES → H2 WALKED BACK** |
| F4 (regimes within 10pp) | regimes not separable | spread = 58.6pp | NO ✓ |

**Net**: H1 SUPPORTED with one specific-prediction miss (flood band was wrong); H2 WALKED BACK; H3 implicit prediction (PAK > IND) FALSIFIED.

---

## Reframed claim (post-walk-back)

**New H1 (refined)**: Hazard-types separate ratios at the broad level (EQ ≥ flood ≥ storm >> drought) but the magnitude DIFFERENCES are smaller than predicted (within 5pp for the top 3). The mechanism-distinct claim survives qualitatively.

**Dropped H2**: state-capacity does not moderate displacement-per-affected in the observable data. **Reporting heterogeneity dominates**.

**New finding from data (post-hoc)**: **Bimodal mega-events (Regime 3a) drive higher per-affected displacement than perpetual exposure (Regime 3b)**. This contradicts the "chronic = adapted" intuition. Mechanism candidate: **forced evacuation vs in-place shelter**. Mega-event responses (USA mandatory evacuations) count people as IDPs; chronic-exposure populations (PHL stays in place between typhoons) aren't counted as IDPs unless permanently displaced.

This is a NEW post-hoc hypothesis — needs separate pre-reg if we want to test forward.

---

## Implications for Paper 2

1. **Drop the state-capacity-moderation claim** from the paper. F3 walked back.
2. **Add the bimodal-vs-perpetual displacement-counting finding** — it's a strong unpredicted result. Needs framing as "reporting / evacuation mechanism" rather than physical mechanism.
3. **Keep H1**: hazard-type ratios separate by mechanism. EQ ratio (33.6%) confirms structural-damage mechanism.
4. **Add IND > PAK ratio finding** — explainable by base-rate (PAK mega-floods inflate affected denominator).
5. **The 6 regimes ARE separable by ratio** (F4 not fired) — strengthens the typology.

## Status

**P2-I: CLOSED with PARTIAL SUPPORT + 1 WALK-BACK + 1 POST-HOC FINDING**

- H1 supported (hazard-type ratios mechanism-distinct, qualitatively)
- H2 walked back (state-capacity moderation not detectable)
- H3 (Regime 1 > 2) falsified
- New finding: 3a >> 3b displacement-per-affected
- Regimes well-separated by ratio (F4 not fired)

## Cross-references

- PRE_REG_016 (this dig's first fit)
- PRE_REG_003 (parent regime classification)
- PATTERN_019 (typology — add ratio-separability finding)
- PATTERN_025 (Regime 3 sub-typing — add 3a >> 3b ratio finding)
