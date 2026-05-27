# Pattern 030 — Flood-dominant transitional class (typology gap)

- **ID:** PATTERN_030
- **Status:** candidate-hypothesis (typology refinement; 2 cases)
- **Type:** mechanism (regime-typology gap)
- **Discovered:** 2026-05-25 via Paper 2 Phase 2 P2-G test
- **Severity / interest:** high (exposes structural gap in PRE_REG_003 rules)

## One line

ARG (85.4% flood / 11.1% storm) and KHM (75.7% flood / 23.8% storm) are **flood-dominant but classify as UNCLASSIFIED** under PRE_REG_003 rules. They fit neither Regime 1 (storm <10% required) nor Regime 2 (flood max/median <5× required) nor Regime 4 (flood > 70% disqualifies). **Typology gap surfaced; needs refinement.**

## Numbers

| Country | Flood % | Storm % | EQ % | Total IDP | Current verdict |
|---|---|---|---|---|---|
| ARG | 85.4 | 11.1 | 0.0 | 175,642 | UNCLASSIFIED |
| KHM | 75.7 | 23.8 | 0.0 | 912,686 | UNCLASSIFIED |

Both are predominantly flood-displacement but have meaningful storm-channel exposure (>10%). They cannot be Regime 1 (which requires storm <10% as a discriminator from Regime 2) and they cannot be Regime 2 (which requires steady distribution).

## Why it stands out

PRE_REG_003 H1's rules:
- Regime 1 (Bimodal-mega-flood): flood max/median > 30× AND ≥2 mega-years AND storm <10%
- Regime 2 (Steady-high-flood): flood max/median <5× AND ≥40% mega-years AND flood >50%
- Regime 4 (Mixed): all channels <70%

**Gap**: flood-dominant (>70%) BUT not extreme bimodal (R1) AND not steady (R2). ARG, KHM fall here.

**Possible refinements**:
1. **Regime 2b** — flood-dominant with secondary-storm exposure (could absorb ARG, KHM)
2. **Relax Regime 1** — change storm <10% to storm <25% rule (would absorb KHM, possibly ARG)
3. **Document as boundary** — accept that some flood-dominant countries sit between regimes; useful info, not artifact

**Likely correct refinement**: Add Regime 2b (flood-dominant transitional). Rationale: ARG Río de la Plata basin and KHM Mekong basin both have **secondary cyclone/storm exposure** that distinguishes them structurally from PAK's pure Indus glacial-monsoon system. They are flood-dominant but multi-mechanism, unlike PAK's single-mechanism mega-flood profile.

## Open questions

1. What is ARG's flood max/median ratio? KHM's?
2. Are there other candidates for the transitional class? VNM Mekong delta? IRQ Tigris-Euphrates? COL?
3. Does Regime 2b explain BGD's "between regimes" position in our prior diagnostic (PATTERN_025 dig)?

## Related

- [[PATTERN_019]] master typology — exposes gap
- [[PATTERN_016]] PAK Regime 1 — sister discriminator
- [[PRE_REG_003]] rules — needs refinement
- [[PRE_REG_017]] Phase 2 first fit — surfaced this gap

## Data sources

- `D:/IDP/data/idmc_gidd/IDMC_GIDD_Disasters_Internal_Displacement_Data.xlsx` rows ISO3 in (ARG, KHM)
- Cross-reference: Argentina La Plata basin flood events; Cambodia Mekong + Tonle Sap flooding

## Status

Candidate-hypothesis. Refines PRE_REG_003 by adding Regime 2b. Should be tested by pulling additional flood-dominant candidates (COL, IRQ, VNM Mekong) and seeing if the gap class has more members.
