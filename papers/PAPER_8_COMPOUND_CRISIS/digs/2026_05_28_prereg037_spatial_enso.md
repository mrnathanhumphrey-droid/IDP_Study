# Paper 8 — PRE_REG_037: spatially-resolved (area-fraction) SPEI ENSO test (P8-F2)

**Fired**: 2026-05-28
**Pre-reg**: PRE_REG_037 (locked + committed before the GEE area-fraction pull, HEAD 89dcf1e)
**Data**: SPEIbase v2.10 via GEE `CSIC/SPEI/2_10`; area-fraction of land with SPEI ≤ −1.0 over ETH/SOM/BRA boxes, Dec, 1950-2023 + OND ONI.
**Status**: **Set A F1 (harder than box-mean); the dilution alternative is RULED OUT.** The spatially-resolved metric confirms ENSO is genuinely weak for Horn drought. F2 does NOT fire (metric registers recent droughts). Set B holds on OND band. Tempers PRE_REG_036's small-n tail finding.

---

## Headline

PRE_REG_036 fired F1 (Horn box-mean drought ~50% La Niña, not ≥60%) but flagged a real measurement pathology — the country-box MEAN diluted the spatially-concentrated 2020-22 Horn drought to invisibility. PRE_REG_037 re-ran the test with **area-fraction-in-drought** (% of region land area with SPEI ≤ −1.0; drought-year = ≥30%), which is not diluted by averaging across climate zones.

**Result: the spatial metric does NOT rescue the La Niña signal — it shows it is even weaker (41.2% La Niña, +6.1pp) than the box-mean (50%, +14.9pp).** Since the spatially-resolved metric gives a *lower* La Niña share than the box-mean, **the box-mean was not hiding a diluted signal** (Set C-exceed NO). And the metric is not blind — SOM 2022 now registers (36.5% of land in drought), so F2 does not fire (Set C-reg YES). The weak Horn drought–La Niña association is **real and robust to spatial resolution**, not an aggregation artifact.

This triangulates with displacement (PRE_REG_034: 50%) and box-mean SPEI (PRE_REG_036: 50%): across three independent instruments, Horn drought–La Niña is ~40-50% — **single-year ENSO does not drive Horn compound-crisis coupling.**

---

## Set A — Horn La Niña enrichment (area-fraction): NOT SUPPORTED (F1)

Locked primary: area-fraction ≥ 0.30 (≥30% of land in SPEI ≤ −1.0), annual SPEI_12, 1950-2023, baseline La Niña 35.1%.

| cutoff | band | Horn drought-years (n) | La Niña % | enrichment |
|---|---|:---:|:---:|:---:|
| ≥0.20 | annual | 37 | 35.1% | +0.0pp |
| **≥0.30** | **annual** | **17** | **41.2%** (7LN/6EN) | **+6.1pp** |
| ≥0.40 | annual | 11 | 45.5% (5LN/4EN) | +10.4pp |
| ≥0.30 | OND | 24 | 41.7% | +6.6pp |
| ≥0.40 | OND | 17 | 47.1% (8LN/3EN) | +12.0pp |

Predicted ≥60% AND enrichment ≥15pp. Observed 41.2% / +6.1pp (primary). **F1 FIRED** — and the enrichment is *weaker* than the box-mean's +14.9pp. There is a gentle severity gradient (35→41→45% as the drought becomes more widespread) but it never approaches 60%.

## Set C — the dilution question, resolved

- **Set C-reg (does the metric register the 2020-22 drought?): YES.** SOM 2022 = 36.5% of land in moderate+ drought → registers at the 0.30 cutoff (it was invisible at box-mean, SPEI −0.30). At the 0.20 cutoff, 2021+2022+2023 all register. **F2 does NOT fire — the metric is not blind; it sees recent Horn droughts.**
- **Set C-exceed (does spatial > box-mean by ≥15pp?): NO.** Spatial 41.2% < box-mean 50%. **The box-mean was NOT diluting a hidden La Niña signal** — if anything the area metric, by including more (ENSO-mixed) widespread-drought years, shows even less enrichment. The dilution concern from PRE_REG_036 is resolved: it affected *visibility of specific events* but not the *La Niña enrichment conclusion*.

So both branches point the same way: the metric works (registers 2022), and even working it shows ~41% La Niña. The weak signal is genuine.

## Set B — Amazon opposite phase: holds on OND band

| cutoff | band | BRA drought-years | La Niña % | El Niño % |
|---|---|---|:---:|:---:|
| ≥0.30 | annual | 15 | 40.0% | 33.3% |
| ≥0.30 | OND | 17 | **17.6%** | **52.9%** |
| ≥0.40 | OND | 10 | **0.0%** | **60.0%** |

The contemporaneous **OND band shows BRA Amazon drought is El-Niño-aligned (17.6% / 0% La Niña), opposite the Horn** — two-family split survives. The annual band smears it (40% La Niña) via the same year-labeling timing artifact as PRE_REG_036/034. Instrument-timing lesson reconfirmed for a third time.

## Tempering PRE_REG_036's tail finding (honest revision)

PRE_REG_036 reported a clean secondary: "extreme Horn droughts (SPEI ≤ −1.5) are 100% La Niña." That was **n=2** (1955, 1984). PRE_REG_037's area-fraction metric, which captures more widespread-drought years at the strict end, shows the most-widespread Horn droughts (≥40% area) at only **45-47% La Niña** — a gentle gradient, not a tail-lock. **The "100% La Niña tail" was a small-n artifact; the honest statement is a weak severity gradient toward ~45%.** Logged as a downward revision.

---

## Falsifier status

| F | Status |
|---|---|
| F1 (Horn area-frac drought < 60% La Niña) | **FIRED** (41.2% annual / 41.7% OND; weaker than box-mean) |
| F2 (metric still blind to 2020-22) | **NOT fired** — SOM 2022 registers (36.5% area); metric works |
| F3 (Amazon also La-Niña-aligned) | NOT fired — BRA OND 17.6%/0% La Niña (opposite Horn) |

The decisive pattern: F1 fires AND F2 does not → the metric is capable but the signal is genuinely ~41%. Combined with Set C-exceed NO → **box-mean dilution was not masking a real La Niña signal.**

---

## Net result — climate mechanism for Paper 8 is now settled (triangulated)

Across **three independent instruments**:
| instrument | Horn drought La Niña % | verdict |
|---|:---:|---|
| GIDD displacement (PRE_REG_034) | 50% | F1 |
| box-mean SPEI v2.10 (PRE_REG_036) | 50% | F1 + F2 (not instrument artifact) |
| area-fraction SPEI v2.10 (PRE_REG_037) | 41% | F1 (not dilution artifact) |

**The Horn drought–La Niña association is consistently ~40-50% — weak, real, robust to instrument AND spatial aggregation. Single-year ENSO is NOT the driver of Horn compound-crisis coupling.** ENSO is at most a weak modulator (gentle severity gradient). The Amazon stays El-Niño-aligned (opposite phase), so the two-family climate-signature split is real even though neither family's coupling is ENSO-driven year-to-year.

**Paper 8 final mechanism statement** (PRE_REG_033/034/035/036/037): compound-crisis coupling is **rare (8%), structural not window-transient, predicted by chronic shock-overlap (not state-fragility), with family-specific climate signatures (Horn La-Niña-leaning / Amazon El-Niño, opposite phases) — but NOT explained by single-year ENSO phase at country scale, robust across displacement, box-mean, and area-fraction instruments.** The climate driver is a weak tail-modulator, not the coupling mechanism. The coupling mechanism is chronic multi-hazard shock-synchrony. This is a thoroughly triangulated, honest negative on the ENSO hypothesis — the climate question is closed.

---

## Cross-references
- PRE_REG_037 (this dig); PRE_REG_036 (box-mean — dilution limitation resolved here); PRE_REG_034 (displacement); PRE_REG_033/035.
- `analysis/paper8_prereg037_spatial_enso_2026_05_28.json`; `_scripts/paper8_gee_spei210_spatial_pull.py`; `_scripts/paper8_prereg037_fire_spatial.py`; `data/spei/spei210_spatial_ETH_SOM_BRA_1950_2023.csv`.
- [[reference-google-earth-engine-access]]; `data/oni.txt`.

## Status
**PRE_REG_037 fired: F1 (Horn area-fraction 41% La Niña, weaker than box-mean → ENSO genuinely weak); F2 NOT fired (metric registers SOM 2022 → not blind); Set C-exceed NO (box-mean not diluting a signal); Set B holds on OND (Amazon El Niño opposite).** Tempers 036's small-n tail finding to a gentle gradient. The Horn ENSO hypothesis is now triangulated-negative across three instruments — climate-mechanism question closed for Paper 8.
