# Paper 9 — Data Sources Manifest (Phase 1)

Live tracking of data sources required by PRE_REG_042. Updated 2026-05-30.

---

## 1. ACS PUMS (anchor dataset) — DONE

- **Dataset**: ACS 5-yr 2024 PUMS (covering 2020-2024 survey years; entry cohorts 2018-2024)
- **Source**: Census Data API `/data/2024/acs/acs5/pums`
- **Auth**: `CENSUS_API_KEY` in `D:/IDP/.env`
- **Script**: [`_scripts/paper9_acs_pums_extract.py`](../../_scripts/paper9_acs_pums_extract.py)
- **Output**: `data/paper9/acs/acs5_2024_pums_origins.csv` (18.1 MB, **289,811 records**)
- **Filter**: 15 origin POBPs (Ukraine 164, Venezuela 373, Cuba 327, Honduras 314, El Salvador 312, Guatemala 313, Haiti 332, Afghanistan 200, Syria 239, Iraq 213, Myanmar 205, DRC 459, Eritrea 417, Somalia 448, Sudan 451)
- **Variables**: POBP, YOEP, CIT, AGEP, PWGTP, ESR, WAGP, SCHL, ENG, FS, HINS4, POVPIP, COW, NATIVITY (+ state from `for=state:XX`)
- **Status**: ✓ extracted; zero NaN in outcome columns; working-age (16-64) N = 218,444
- **Census API quirk discovered**: the comma-list filter `POBP=A,B,C` silently **drops the first and last values**; use repeated `&POBP=A&POBP=B&POBP=C` instead. (Bug confirmed 2026-05-30.)

### Weighted populations by origin (PWGTP-weighted, all cohorts)
| origin | est foreign-born pop |
|---|---:|
| El Salvador | 1,517,646 |
| Cuba | 1,457,080 |
| Guatemala | 1,239,633 |
| Honduras | 895,280 |
| Haiti | 791,783 |
| Venezuela | 730,261 |
| Ukraine | 464,573 |
| Iraq | 245,008 |
| Afghanistan | 194,527 |
| Myanmar | 163,085 |
| Syria | 122,150 |
| Somalia | 99,640 |
| DRC | 67,388 |
| Sudan | 65,520 |
| Eritrea | 52,574 |
| **total** | **8,106,148** |

### Entry-cohort coverage (PWGTP-weighted)
| cohort | weighted N |
|---|---:|
| pre-2018 | 4,962,967 |
| 2018-2019 | 620,792 |
| 2020-2021 | 459,434 |
| 2022-2023 | 489,268 |
| 2024 | 56,673 |

---

## 2. ORR Refugee Resettlement Data — TODO

- **Granularity**: state × origin × Fiscal Year arrivals; precise track identification for the **Refugee** track
- **Primary source**: HHS Office of Refugee Resettlement annual reports — https://www.acf.hhs.gov/orr/policy-guidance/refugee-resettlement-annual-reports-congress (or `https://www.acf.hhs.gov/orr/data/refugees`)
- **Format**: PDFs (older years), CSVs/Excel (recent), and the Refugee Processing Center dashboard at https://www.wrapsnet.org/admissions-and-arrivals/
- **Acquisition strategy**:
  1. Download recent ORR Annual Reports to Congress (FY2018-FY2024) — Table-V style tables list arrivals by state × nationality
  2. Refugee Processing Center (WRAPS) public dashboard for FY-level state × nationality
  3. Cross-check with State Department PRM data if needed
- **Status**: not started

## 3. USCIS TPS Fact Sheets — TODO

- **Granularity**: national populations by origin × designation period; some state-level breakdowns in periodic reports
- **Primary source**: USCIS Temporary Protected Status page — https://www.uscis.gov/humanitarian/temporary-protected-status
- **Per-country pages**: each designated country has its own page with current designation status and population estimates
- **Format**: HTML + PDF Fact Sheets
- **Designations as of 2026-05-30 (to verify)**: Afghanistan, Burma (Myanmar), Cameroon, El Salvador, Ethiopia, Haiti, Honduras, Lebanon, Nepal, Nicaragua, Somalia, South Sudan, Sudan, Syria, Ukraine, Venezuela, Yemen
- **Acquisition strategy**:
  1. Scrape current designation list + extant termination notices
  2. Pull historical TPS populations from DHS reports (annual Yearbook of Immigration Statistics has TPS tables)
  3. For state-level: USCIS publishes occasional reports (FOIA-fulfilled, posted to USCIS reading room)
- **Status**: not started

## 4. EOIR Statistics — TODO

- **Granularity**: immigration court × origin × year × decision (asylum filings, grants, denials)
- **Primary source**: DOJ EOIR Statistics Yearbook + EOIR Statistics page — https://www.justice.gov/eoir/statistics-and-publications
- **Format**: Annual Statistics Yearbook PDFs + downloadable Excel tables on the Adjudication Statistics page (case completions, asylum decisions, etc.)
- **TRAC** has cleaner derivative datasets at https://trac.syr.edu/immigration/ (subscription tier for full granularity; some free)
- **Acquisition strategy**:
  1. EOIR FY Statistics Yearbook (most recent FY2024)
  2. Adjudication Statistics: Asylum Decision Rates by Nationality
  3. Court Hearing Locations file (for crosswalk court → state)
- **Status**: not started

## 5. DOS SIV reports — TODO

- **Granularity**: Annual approvals by origin (Afghan SIV + Iraqi SIV programs)
- **Primary source**: US Department of State, Bureau of Consular Affairs — https://travel.state.gov/content/travel/en/us-visas/immigrate/special-immg-visa-afghans-employed-us-gov.html (Afghan SIV) and the analogous Iraqi SIV page
- **Quarterly reports to Congress**: required by statute; posted on State Department's website
- **Format**: PDF reports; spreadsheet annexes
- **Acquisition strategy**: pull quarterly reports FY2018-FY2024
- **Status**: not started

## 6. CHNV/UFU Parole Reports — TODO

- **Granularity**: monthly/quarterly parole-program enrollments by origin (Cuba/Haiti/Nicaragua/Venezuela for CHNV; Ukraine for UFU); national-level
- **Primary source**: USCIS parole-program data on https://www.uscis.gov/humanitarian/uniting-for-ukraine-data and https://www.uscis.gov/CHNV
- **Format**: HTML tables + PDF reports
- **Acquisition strategy**: scrape current totals + historical monthly reports; cross-check with DHS press releases on enrollment caps and pauses
- **Status**: not started
- **Caveat**: CHNV was paused at various points (litigation, eligibility changes); document program timing carefully for cohort assignment

## 7. MPI Undocumented Estimates — TODO

- **Granularity**: state × origin estimates
- **Primary source**: Migration Policy Institute Data Hub — https://www.migrationpolicy.org/programs/us-immigration-policy-program-data-hub/unauthorized-immigrant-population-profiles
- **Format**: per-state interactive profiles + downloadable datasets
- **Estimates also from**: Pew Research Hispanic Trends + DHS's own Estimates of the Unauthorized Immigrant Population Residing in the United States (annual)
- **Status**: not started

---

## Cross-walk construction (after all sources acquired)

For each (state × origin × entry-cohort) cell in ACS, build a 7-dimensional probability vector over tracks: {Refugee, TPS, Asylum-pending, Asylum-granted, SIV, Parole-with-EAD, Undocumented}.

**Allocation rules (per PRE_REG_042 §3)**:
1. Where admin source gives state × origin × cohort directly (e.g., ORR refugee arrivals), use it as the count.
2. Where admin gives national × origin × period (e.g., USCIS TPS), allocate to states proportionally to ACS foreign-born of that origin in each state.
3. Residual = (ACS foreign-born from origin × cohort × state) − (sum across tracks 1-6) → assigned to {Undocumented, LPR-other}.
4. Use MPI undocumented estimates as upper-bound check on the undocumented residual.

**Robustness**: report results under (i) strict cross-walk and (ii) weakest-link assumptions (uniform allocation where granularity is missing).

---

## Phase 1 fire sequence (after manifest items 2-7 complete)

1. Build the (state × origin × cohort) → 7-track probability matrix from admin sources.
2. Join to ACS PUMS at the cell level.
3. Compute outcome aggregates per cell (LFP rate, formal-employment rate, mean WAGP, SNAP takeup, Medicaid takeup, English-prof rate, mean education).
4. Variance decomposition (mixed-effects): track partial-R² vs origin partial-R² per outcome.
5. **Differential test** (the load-bearing claim): track > origin on work-auth-dep outcomes; origin > track on human-capital outcomes.
6. Sensitivity: probabilistic individual-level via multiple imputation.

---

## Status snapshot

| Source | acquired | parsed | crosswalked |
|---|:---:|:---:|:---:|
| ACS PUMS (anchor) | ✓ | ✓ | n/a (substrate) |
| ORR Refugee | ✗ | ✗ | ✗ |
| USCIS TPS | ✗ | ✗ | ✗ |
| EOIR Asylum | ✗ | ✗ | ✗ |
| DOS SIV | ✗ | ✗ | ✗ |
| CHNV/UFU Parole | ✗ | ✗ | ✗ |
| MPI Undocumented | ✗ | ✗ | ✗ |

**Next session**: pull ORR + USCIS TPS first (the two largest tracks); build initial cross-walk; descriptive joint table; identify gaps in EOIR/SIV/CHNV/MPI that need session 3.
