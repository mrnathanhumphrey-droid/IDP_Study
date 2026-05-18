# ACLED Manual Fetch Instructions

The ACLED API requires registration. To execute the Phase 0 ACLED fetch:

1. Register at https://acleddata.com/register-for-an-acled-access/
2. Receive email confirmation + API key.
3. Set environment variables:

   ```
   $env:ACLED_EMAIL = "your@email"
   $env:ACLED_API_KEY = "your_key"
   ```

4. Re-run `python _scripts/fetch_acled.py`.

ALTERNATIVELY, use the Data Export Tool (browser): https://acleddata.com/data-export-tool/

Per-country export parameters (locked here):

| Country | ISO3 | Date range | Export filename |
|---|---|---|---|
| Colombia | COL | 2014-01-01 to 2024-12-31 | `acled-colombia.csv` |
| Sudan    | SDN | 2014-01-01 to 2024-12-31 | `acled-sudan.csv` |
| DRC      | COD | 2014-01-01 to 2024-12-31 | `acled-drc.csv` |
| Yemen    | YEM | 2014-01-01 to 2024-12-31 | `acled-yemen.csv` |
| Yemen pre-2014 | YEM | 2010-01-01 to 2013-12-31 | `acled-yemen-pre2014.csv` |

Save the CSVs to `data/acled/` then re-run any downstream scripts that read
ACLED. The harmonization layer + pre-cond 2 + pre-cond 4 will use whichever
files are present.

The Yemen pre-2014 file is required for pre-cond 4 (Yemen post-2022 coverage
degradation check).
