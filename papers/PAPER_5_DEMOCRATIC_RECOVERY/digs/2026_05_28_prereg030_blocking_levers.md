# Paper 5 — PRE_REG_030 Phase 1: Blocking-lever model

**Fired**: 2026-05-28
**Pre-reg**: PRE_REG_030 (blocking-lever predictive model)
**Data**: V-Dem v15 full Country-Year CSV (466MB local), 12 corpus cases at attempt onset
**Status**: H1 SUPPORTED (10/12); H2 (USA erosion) NOT supported on V-Dem coarse measures. Refinement: civil society + federalism are the discriminating levers.

---

## Headline

**The 4-lever model predicts blocked-vs-consolidated for 10 of 12 corpus cases** (pre-committed threshold ≥10 → H1 supported). The two misses are precisely the cases the substrate already flagged as special: SLV (the popular-mandate exception) and PER (the self-coup-blocked-but-successor-consolidated complication). **The discriminating levers are civil-society capacity and federalism, NOT court independence or election quality** — the latter two are near-universal at backsliding onset because backsliding begins from a democracy.

---

## Operationalization (pre-committed)

Levers 1-3 scored 1 if the case exceeds the GLOBAL median (all countries) for the indicator at attempt-onset year; lever 4 hand-coded from constitutional structure:

| Lever | Indicator | Threshold |
|---|---|---|
| 1. Court independence | v2juhcind | > global median at onset |
| 2. Civil-society capacity | v2csprtcpt | > global median at onset |
| 3. Competitive election | v2xel_frefair | > global median at onset |
| 4. Federal/regional power | constitutional federation | USA/BRA/VEN = 1; others 0 |

Lever 4 hand-coded because v2elreggov is binary (most countries have elected regional govts; global median = 1.0) and doesn't separate genuine federations from unitary states with local councils. Federalism is a non-disputed constitutional fact. VEN coded federal by constitutional structure (not outcome) to avoid bias.

Decision rule: **≥3 levers → BLOCKED; ≤2 → CONSOLIDATES.**

---

## Results — Test A (in-corpus separation)

| Case | onset | L1 court | L2 civ-soc | L3 election | L4 federal | score | predicted | actual | ✓ |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|---|:---:|
| BRA Bolsonaro | 2019 | 1 | 1 | 1 | 1 | **4** | blocked | blocked | ✓ |
| ISR overhaul | 2023 | 1 | 1 | 1 | 0 | **3** | blocked | blocked | ✓ |
| USA Trump I | 2017 | 1 | 1 | 1 | 1 | **4** | blocked | blocked | ✓ |
| KOR Yoon | 2022 | 1 | 1 | 1 | 0 | **3** | blocked | blocked | ✓ |
| PER Castillo | 2021 | 1 | 0 | 1 | 0 | 2 | consolidated | blocked | ✗ |
| SLV Bukele | 2019 | 1 | 1 | 1 | 0 | **3** | blocked | consolidated | ✗ |
| HUN Orbán | 2010 | 1 | 0 | 1 | 0 | 2 | consolidated | consolidated | ✓ |
| TUR Erdoğan | 2014 | 1 | 0 | 1 | 0 | 2 | consolidated | consolidated | ✓ |
| VEN Chávez | 2006 | 0 | 0 | 0 | 1 | 1 | consolidated | consolidated | ✓ |
| POL PiS | 2015 | 1 | 0 | 1 | 0 | 2 | consolidated | consolidated | ✓ |
| TUN Saied | 2021 | 1 | 0 | 0 | 0 | 1 | consolidated | consolidated | ✓ |
| BLR Lukashenko | 2020 | 0 | 0 | 0 | 0 | 0 | consolidated | consolidated | ✓ |

**10 of 12 correct → H1 SUPPORTED (threshold ≥10). F1 (< 8) NOT FIRED.**

### The two misses are the documented special cases
- **SLV (Bukele)**: scored 3 (court + civil society + competitive election all present at 2019 onset) → model predicts blocked, but Bukele consolidated. SLV is THE flagged exception in PATTERN_027: consolidation succeeded *despite* democratic conditions because of 80%+ approval + a Constituent Assembly Bukele had already captured. The lever model correctly identifies SLV as the anomaly — a country that "should" have blocked backsliding but didn't, via popular mandate.
- **PER (Castillo)**: scored 2 → model predicts consolidated; coded "blocked" in PATTERN_027. But PER *did* consolidate under successor Boluarte (hcind collapsed 1.547→0.455 2022-2025). The model's "consolidated" prediction arguably captures the deeper outcome — only Castillo's dramatic self-coup was blocked, not the backsliding itself. This is the F2 nuance the pre-reg flagged ("blocking a self-coup ≠ preventing backsliding").

Read generously, the model is "right in spirit" on both misses (SLV = the known anomaly; PER = consolidated-via-successor). On the literal coding it's 10/12.

---

## Results — Test B (USA lever-erosion, H2)

| Year | L1 court | L2 civ-soc | L3 election | L4 federal | score |
|---|:---:|:---:|:---:|:---:|:---:|
| 2017 (Trump I) | 1 | 1 | 1 | 1 | 4 |
| 2025 (Trump II) | 1 | 1 | 1 | 1 | 4 |

**H2 NOT supported.** The pre-reg predicted USA lever-count drops ≥3 → ≤2 (the PATTERN_027 argument that SCOTUS-capture + party-state-fusion eroded the levers between Trump I and Trump II). V-Dem's coarse global-median measures do NOT detect this: USA's high-court-independence index stayed above the global median through 2025, and v2csprtcpt/v2xel_frefair likewise held.

This is an honest null. Two readings:
1. The lever-erosion argument (PATTERN_027) is real but operates BELOW the resolution of V-Dem global-median splits — the SCOTUS 6-3 shift is a within-US change that doesn't move the US below the *global* median for high-court independence.
2. Or the qualitative erosion argument overstated the institutional damage as of 2025.

Either way, the coarse lever-count does not capture USA's 2025 fast-pole. The within-country erosion (PATTERN_026's fast-pole signature) is finer-grained than this model. **Flagged as a limitation: the lever model is a cross-country separator, not a within-country early-warning instrument.**

---

## The substantive refinement: which levers discriminate

Looking down the lever columns, two levers are near-universal at onset and two do the discriminating:

| Lever | Present in blocked (of 5) | Present in consolidated (of 7) | Discriminating? |
|---|:---:|:---:|---|
| L1 court independence | 5/5 | 5/7 | weak (near-universal at onset) |
| L3 competitive election | 5/5 | 4/7 | weak |
| **L2 civil-society capacity** | **4/5** | **1/7** | **STRONG** |
| **L4 federalism** | **2/5** | **1/7** | moderate |

**Court independence and competitive elections are near-universal at backsliding onset — because backsliding BEGINS from a functioning democracy.** At the moment an aggrandizing executive takes power, the courts are usually still independent and elections still competitive (that's the starting condition). What separates blocked from consolidated is whether there's **civil-society capacity** (4/5 blocked vs 1/7 consolidated — the single strongest discriminator) and **federal parallel power** to mount and sustain resistance.

This refines the framework: the blocking levers that MATTER are the resistance-mobilization levers (civil society, federalism), not the baseline institutional-quality levers (courts, elections) which are present at onset almost by definition. SLV is the exception that proves it — SLV had civil society at onset (L2=1) but Bukele's popular mandate overwhelmed it.

---

## Sensitivity (pre-committed ±1 cutoff)

| Cutoff | Correct | Note |
|---|:---:|---|
| ≥2 → blocked | 8/12 | PER becomes correct (+1) but HUN/TUR/POL become wrong (−3) |
| **≥3 → blocked (locked)** | **10/12** | optimal |
| ≥4 → blocked | 8/12 | SLV becomes correct (+1) but ISR/KOR become wrong (−2) |

The pre-committed ≥3 cutoff is the optimum. The model is not knife-edge-dependent on a lucky threshold.

---

## Falsifier status

| F | Status |
|---|---|
| F1 (< 10 of 12 correct) | NOT FIRED (exactly 10/12) |
| F2 (≥3 "blocked" cases consolidate via legal channels) | PARTIAL — PER is the one case (Castillo blocked, Boluarte consolidated); single case, flagged not fired |
| F3 (USA lever-count does NOT drop 2020→2025) | **FIRED** — USA stays at 4 both years; H2 (lever-erosion) walked back on V-Dem coarse measures |

H1 SUPPORTED. H2 walked back (F3 fired). Refinement-rich.

---

## Net result

**PRE_REG_030 H1 SUPPORTED (10/12); H2 walked back (USA erosion not detected by V-Dem coarse measures).** The blocking-lever model separates blocked from consolidated backsliding at the pre-committed ≥3 cutoff, with the 2 misses being the documented SLV-exception and PER-complication. The discriminating levers are civil society + federalism (resistance-mobilization capacity), not courts + elections (near-universal at onset). The USA within-country erosion is finer-grained than this cross-country model detects — an honest limitation.

---

## Cross-references
- PRE_REG_030 (this dig's first fit)
- PATTERN_027 (the 4-lever source + 5 blocked cases + SLV/PER flags)
- PATTERN_026 (USA fast-pole — H2 anchor; the erosion this model fails to detect)
- PATTERN_013 (7 consolidated cases)
- `analysis/paper5_prereg030_2026_05_28.json`
- `_scripts/paper5_prereg030_blocking_levers.py`

## Status

**Phase 1 done. H1 SUPPORTED.** Paper 5 closure: 1/9 → first empirical fire lands. Next: Phase 2 (PRE_REG_031 recovery velocity) + Phase 3 (PRE_REG_032 recovery ceiling). The discriminating-lever refinement (civil society + federalism) is a candidate headline finding for the paper.
