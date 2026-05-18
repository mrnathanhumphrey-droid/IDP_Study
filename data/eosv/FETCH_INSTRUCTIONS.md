# EOSV Manual Fetch Instructions

UCDP EOSV (Ethnic One-Sided Violence) dataset, Eck & Hultman variant.

**Time coverage:** 1989-2013. Per locked constraint: do NOT extend post-2013
into the EOSV atrocity-count covariate. Post-2013 ethnic-targeting events
fold into current_conflict_intensity instead.

## Manual download

1. Visit https://ucdp.uu.se/downloads/eosv/
2. Download the latest EOSV release (typically .zip or .xlsx).
3. Save as `data/eosv/eosv-1989-2013.xlsx` or `.csv`.
4. Re-run dependent scripts.

Alternative: UCDP One-Sided Violence dataset (annualized country-level)
at https://ucdp.uu.se/downloads/index.html#onesided. The georeferenced
event-level data is in UCDP-GED with `type_of_violence = 3` (one-sided).
The locked design doc uses UCDP-GED filtered by type_of_violence=3 as
the operational substitute for EOSV when geocoded events are needed; EOSV
proper is used for ethnic-target coding.
