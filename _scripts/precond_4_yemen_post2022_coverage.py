"""Pre-cond 4 — Yemen post-2022 ACLED coverage check.

Locked check (§7 of design doc):
  ACLED post-2022 events in Houthi-controlled governorates as a fraction of
  pre-2022 coverage. Drop threshold: < 30% of pre-2022 level -> Yemen
  post-2022 Stage A is unreliable.

Pass: coverage >= 30% -> Yemen panel intact.
Fail: drop Yemen post-2022 from Stage B; keep Stage A historical polygon
      analysis only. **Document, don't fight it** (locked constraint).

Houthi-controlled governorates (locked list per ICG / Salisbury 2015):
  Sa'dah, Hajjah, Amran, Sana'a (capital + governorate), Dhamar, Ibb,
  Hodeidah, Mahwit, Raymah

Phase 0 status: requires fetched ACLED Yemen data (post-2014 + pre-2014
reference). Emits STUB if either missing.
"""
import pathlib, sys, json, time, io
import warnings; warnings.filterwarnings("ignore")
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)
except Exception:
    pass

ROOT = pathlib.Path(r"D:/IDP")
ACLED_DIR = ROOT / "data" / "acled"
NOTES = ROOT / "notes"
REPORT = NOTES / "precond_4_report.md"

YEMEN_FILE_RECENT = ACLED_DIR / "acled-yemen.csv"
YEMEN_FILE_PRE2014 = ACLED_DIR / "acled-yemen-pre2014.csv"

HOUTHI_CONTROLLED_GOVS = {
    # As of locked specification (2025-state, per ICG / Salisbury 2015 baselining)
    # ACLED uses governorate names in `admin1` field; normalization needed
    "Sa'dah","Saada","Sadah",
    "Hajjah",
    "Amran","'Amran","Amaran",
    "Sana'a","Sanaa","Sanaa City","Amanat Al Asimah",
    "Dhamar",
    "Ibb",
    "Hodeidah","Al Hudaydah","Hudaydah",
    "Mahwit","Al Mahwit","Almahwit",
    "Raymah","Raima",
}
LOCKED_DROP_THRESHOLD = 0.30   # < 30% of pre-2022 level => drop


def stub_result(reason):
    return {"verdict": "PHASE0_STUB", "reason": reason}


def main():
    print(f"=== Pre-cond 4: Yemen post-2022 ACLED coverage ===")
    print(f"  Locked threshold: post-2022 events in Houthi-controlled govs >= {LOCKED_DROP_THRESHOLD*100:.0f}% of pre-2022 baseline")
    if not YEMEN_FILE_RECENT.exists():
        print(f"  STUB: {YEMEN_FILE_RECENT.relative_to(ROOT)} not yet fetched")
        result = stub_result(f"{YEMEN_FILE_RECENT.relative_to(ROOT)} missing")
    elif not YEMEN_FILE_PRE2014.exists():
        print(f"  STUB: {YEMEN_FILE_PRE2014.relative_to(ROOT)} not yet fetched (Yemen 2010-2013 reference window)")
        result = stub_result(f"{YEMEN_FILE_PRE2014.relative_to(ROOT)} missing")
    else:
        import pandas as pd
        recent = pd.read_csv(YEMEN_FILE_RECENT, low_memory=False)
        pre = pd.read_csv(YEMEN_FILE_PRE2014, low_memory=False)
        gov_col = "admin1" if "admin1" in recent.columns else ("Admin1" if "Admin1" in recent.columns else None)
        if gov_col is None:
            result = stub_result(f"admin1 column not found in {YEMEN_FILE_RECENT.name}")
        else:
            yr_col = "year" if "year" in recent.columns else None
            if yr_col is None and "event_date" in recent.columns:
                recent["_year"] = pd.to_datetime(recent["event_date"], errors="coerce").dt.year
                pre["_year"] = pd.to_datetime(pre["event_date"], errors="coerce").dt.year
                yr_col = "_year"
            if yr_col is None:
                result = stub_result("year column not found")
            else:
                # Pre-2022 baseline within Houthi-controlled govs (use 2014-2021 window for stable comparison)
                pre_window = recent[(recent[yr_col] >= 2014) & (recent[yr_col] <= 2021)
                                    & recent[gov_col].isin(HOUTHI_CONTROLLED_GOVS)]
                # Post-2022
                post_window = recent[(recent[yr_col] >= 2022) & (recent[yr_col] <= 2024)
                                     & recent[gov_col].isin(HOUTHI_CONTROLLED_GOVS)]
                pre_per_year = len(pre_window) / max(8, 1)   # 2014-2021 = 8 years
                post_per_year = len(post_window) / max(3, 1) # 2022-2024 = 3 years
                ratio = post_per_year / pre_per_year if pre_per_year > 0 else None
                verdict = "PASS" if (ratio is not None and ratio >= LOCKED_DROP_THRESHOLD) else "FAIL"
                result = {
                    "verdict": verdict,
                    "n_pre_events_houthi_govs_2014_2021": int(len(pre_window)),
                    "n_post_events_houthi_govs_2022_2024": int(len(post_window)),
                    "events_per_year_pre": float(pre_per_year),
                    "events_per_year_post": float(post_per_year),
                    "ratio_post_to_pre": float(ratio) if ratio is not None else None,
                    "threshold": LOCKED_DROP_THRESHOLD,
                }
                print(f"  Pre-2022 (2014-21) Houthi-gov events: {len(pre_window):,} ({pre_per_year:.0f}/yr)")
                print(f"  Post-2022 (2022-24) Houthi-gov events: {len(post_window):,} ({post_per_year:.0f}/yr)")
                print(f"  ratio = {ratio:.3f}  verdict: {verdict}")

    md = []
    md.append("# Pre-cond 4 Report — Yemen Post-2022 ACLED Coverage\n")
    md.append(f"**Run at:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    md.append(f"**Locked check:** Yemen post-2022 events in Houthi-controlled governorates >= {LOCKED_DROP_THRESHOLD*100:.0f}% of pre-2022 (2014-2021) per-year rate.\n")
    md.append(f"**Verdict:** **{result['verdict']}**\n")
    md.append("\n## Houthi-controlled governorate list (locked)\n")
    md.append(", ".join(sorted(HOUTHI_CONTROLLED_GOVS)) + "\n")
    if result["verdict"] not in ("PHASE0_STUB",):
        md.append("\n## Coverage statistics\n")
        for k, v in result.items():
            if k == "verdict": continue
            md.append(f"- **{k}**: {v}")
    md.append("\n## Failure handling (locked constraint)\n")
    md.append("- FAIL: drop Yemen post-2022 from Stage B; keep Stage A historical polygon analysis only. ")
    md.append("Document, don't fight it. Yemen post-2022 will appear as a Stage-B sample-size caveat in §6 disposition reading.\n")
    REPORT.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"\n=== Report: {REPORT} ===")
    (NOTES / "precond_4_results.json").write_text(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
