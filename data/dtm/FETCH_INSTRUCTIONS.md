# IOM DTM (Displacement Tracking Matrix) Fetch Instructions

**Phase 0 status:** SCAFFOLDED (not yet executed). Phase 2 will execute
country-by-country with the defensive harmonization layer in
`build_longitudinal_panel.py`.

**Critical constraint (Phase 0 lock):** DTM schema drift is real. Different
rounds have different columns. The harmonization layer must be defensive:
log every column rename, every type coercion, every missing-value fill.
Output `data/dtm/_harmonization_log.json` per country.

## Per-country data sources

### Colombia
DTM presence is minimal. Primary IDP data:
- **Unidad para las Víctimas (RUV)** — Registro Único de Víctimas. Census
  of victims of armed conflict including IDPs. URL:
  https://www.unidadvictimas.gov.co/es/registro-unico-de-victimas-ruv/37394
- Provides annual displacement statistics per municipio.
- Alternative: **JIPS-Colombia** (Joint IDP Profiling Service) reports.

### Sudan
DTM Sudan: https://dtm.iom.int/sudan
- Round-by-Round mobility tracking matrices. ~quarterly cadence.
- Published as Excel files. Per-round columns vary.
- Typical columns (some optional per round): admin1 / admin2 / state /
  locality / idp_individuals / arrival_period / location_type.
- **Schema drift to expect:** column renames between rounds (e.g.
  "Locality" -> "Admin 2 Name"); presence of `ssid` / `assessment_round`
  fields varies; population denominators absent in some rounds.

### DRC
DTM DRC: https://dtm.iom.int/democratic-republic-congo
- Monthly provincial reports. PDF + Excel + Tableau.
- Per-territoire (admin-2 equivalent) IDP counts.
- **Schema drift to expect:** PDF tables OCR'd inconsistently across
  reports; CSV exports only available from 2018 forward; pre-2018 data
  is PDF-extract.

### Yemen
DTM Yemen: https://dtm.iom.int/yemen
- Master List + Area Assessments + Mobility Tracking.
- Per-mudiriyah (admin-2) IDP counts + flow.
- **Schema drift to expect:** governorate-level vs district-level
  resolution varies by round; the "Master List" granularity is district;
  Area Assessments are governorate.

## Fetch sequence (Phase 2 execution)

For each country:
  1. Visit DTM country page; download all available round files.
  2. Save raw round files to `data/dtm/<country>/round_NN_raw.xlsx`.
  3. Run `_scripts/build_longitudinal_panel.py <country>` to harmonize.
  4. Inspect `data/dtm/<country>/_harmonization_log.json` for drift warnings.
  5. Output: `data/dtm/<country>/panel_admin2_annual.csv`.

## Pre-cond 1 dependency

Pre-cond 1 (country sample availability) requires that each of the 4
countries has >= 5 years of DTM data with >= 50 admin-2 units per year.
If a country fails pre-cond 1, drop it from primary panel per locked
walk-back protocol (§7).

## Pre-cond 4 dependency (Yemen)

Pre-cond 4 requires Yemen ACLED post-2022 coverage in Houthi-controlled
governorates to be >= 30% of pre-2022 level. If fail, drop Yemen post-2022
from Stage B; keep Stage A historical polygon analysis only. Document;
do not fight it.

## Scaffold last updated

2026-05-17 19:34:42
