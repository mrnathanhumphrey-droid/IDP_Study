# Pre-Registration Redline Trail v1 → v2

This file tracks every documented deviation from the locked pre-registration
v1 (`notes/displacement_research_design.md` v1, committed at the initial
git commit `dd3f0ec`). Each entry has:

- The locked v1 specification being modified
- The reason for modification
- The replacement specification
- The commit hash at which the deviation is locked into v2
- The PI sign-off (or "automatic" for environment-forced deviations)

---

## Entry 001 — 2026-05-17 — ACLED replaced by GDELT for cross-source validation

**Locked v1 spec:** `notes/displacement_research_design.md` §3.3 + §5 (Axis 1)
+ §7 (Pre-cond 2 + Pre-cond 4) + §8 (data sources) named **ACLED** as the
cross-source conflict-event validator against UCDP-GED.

**Reason for modification:** ACLED access tightened post-2024 to require
institutional email + manual academic approval. Principal investigator
(Nathan Humphrey) is not institutionally affiliated; ACLED registration
returned access denial. The pre-cond 2 cross-source agreement check and
pre-cond 4 Yemen post-2022 coverage check both depended on ACLED.

**Replacement spec (locked at this commit):** **GDELT 2.0 Event Database**
substitutes for ACLED in:
  - §3.3 covariate `acled_event_count` → `gdelt_event_count` (event count
    from GDELT 2.0 ActionGeo-filtered to admin-2 × year)
  - §5 Robustness Axis 1: "Cross-source GDELT vs UCDP-GED" (was "Cross-source
    ACLED vs UCDP-GED")
  - §7 Pre-cond 2: Spearman ≥ 0.6 GDELT-vs-UCDP-GED per admin-2 × year
    (same threshold as locked v1; only the source substituted)
  - §7 Pre-cond 4: Yemen post-2022 coverage check uses GDELT
    ActionGeo_CountryCode = YM filtered to Houthi-controlled governorates
    (governorate list per the locked precond_4 script). Same ≥ 30%
    threshold as v1; only the source substituted.

**Rationale + tradeoffs:**

  - **GDELT is public + no auth + reproducible.** Free under Creative
    Commons. URL: https://www.gdeltproject.org/. Anyone can verify the
    fetched data without institutional access barriers — this is closer
    to the open-science discipline of the methodology corpus.
  - **GDELT is machine-coded from news, not human-coded.** Higher
    false-positive rate than ACLED's hand-coded data. Mitigated by the
    admin-2 × year aggregation (locked aggregation level is unchanged):
    noise smooths out at the aggregate scale used in pre-cond 2 + 4.
  - **GDELT event coding (CAMEO codes) differs from ACLED event types.**
    The shock indicator (UCDP-GED fatality 80th percentile within country)
    remains unchanged — GDELT is only the cross-source validator, not
    the primary shock indicator.
  - **Cross-source agreement threshold (Spearman ≥ 0.6) is unchanged.**
    The locked threshold is unchanged; the question is whether GDELT and
    UCDP-GED agree at the admin-2 × year aggregate, regardless of which
    source is "ground truth."
  - **Three-way cross-source possibility:** UCDP + GDELT + ICEWS (Harvard
    Dataverse, free, no auth) could be a tertiary check if GDELT alone
    is too noisy. Locked here: GDELT is the primary cross-source
    validator; ICEWS is reserved as Phase 1+ tertiary if Spearman corr
    is borderline (0.5-0.7 range).

**What stays unchanged from v1:**

  - All 4 hypotheses (H_SHOCK_AMPLIFICATION, H_HISTORICAL_INTENSITY,
    H_TERRAIN, H_CROSS_COUNTRY_PORTABILITY)
  - All 4 hypotheses' falsifier thresholds + confirmation CIs
  - Locked "associated with" framing in shock_amplification_specification.md
  - Stage-A historical polygon definitions (4 polygons unchanged)
  - UCDP-GED as primary shock indicator
  - DTM as primary outcome source
  - Stan model class + priors
  - 5 axes of pre-cond → 4 of which use GDELT now (axis 1 + pre-cond 2 + pre-cond 4)

**PI sign-off:** automatic — environment-forced deviation. ACLED access
denied to non-institutional PI; substrate-9 pre-reg cannot otherwise
proceed without dropping cross-source validation entirely. Documented in
this redline before any GDELT fetch is run.

**Files affected by this redline (to be updated in next commit):**

  - `_scripts/fetch_acled.py` — retained as FETCH_INSTRUCTIONS stub for
    future institutional access; not used in Phase 0+
  - `_scripts/fetch_gdelt.py` — NEW; replaces ACLED fetch
  - `_scripts/precond_2_conflict_source_agreement.py` — updated to read
    GDELT instead of ACLED
  - `_scripts/precond_4_yemen_post2022_coverage.py` — updated to use
    GDELT for the Yemen post-2022 coverage check
  - `notes/displacement_research_design.md` — v2 update reflecting the
    redline (header should reflect "v2" with link to this redline file)
  - `provenance/data_sources.md` — GDELT added; ACLED retained with
    note about access denial
