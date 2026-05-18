"""Pre-cond 2 — Conflict-source agreement (ACLED vs UCDP-GED).

Locked check (§7 of design doc):
  ACLED and UCDP-GED event counts per admin-2 x year correlate >= 0.6
  across the panel (Spearman). Cross-source validity check.

Pass: all countries clear.
Fail: reframe shock indicator as source-specific; rerun §5 Axis 1 as
      primary instead of robustness.

Phase 0 status: runs against fetched UCDP + ACLED data spatial-joined to
GADM admin-2 polygons. In Phase 0, if either data source not present,
emits STUB.
"""
import pathlib, sys, json, time, io
import warnings; warnings.filterwarnings("ignore")
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)
except Exception:
    pass
import numpy as np
import pandas as pd

ROOT = pathlib.Path(r"D:/IDP")
UCDP_DIR = ROOT / "data" / "ucdp"
ACLED_DIR = ROOT / "data" / "acled"
GADM_DIR = ROOT / "data" / "gadm"
NOTES = ROOT / "notes"
REPORT = NOTES / "precond_2_report.md"

COUNTRIES = ["colombia", "sudan", "drc", "yemen"]
LOCKED_CORR_THRESHOLD = 0.6


def stub_result(country, reason):
    return {
        "country": country,
        "verdict": "PHASE0_STUB",
        "reason": reason,
        "spearman_correlation": None,
    }


def check_country(country):
    ucdp_path = UCDP_DIR / f"ucdp-ged-{country}.csv"
    acled_path = ACLED_DIR / f"acled-{country}.csv"
    gadm_path = GADM_DIR / f"gadm41_{country}.gpkg"
    missing = []
    for p, name in [(ucdp_path, "UCDP"), (acled_path, "ACLED"), (gadm_path, "GADM")]:
        if not p.exists(): missing.append(name)
    if missing:
        return stub_result(country, f"Missing data: {missing}")

    try:
        import geopandas as gpd
        import fiona
    except ImportError:
        return stub_result(country, "geopandas/fiona not available")

    # Load admin-2 polygons
    try:
        layers = fiona.listlayers(gadm_path)
        adm2_layer = next((l for l in layers if "_2" in l or "ADM_2" in l.upper()), layers[-1])
        adm2 = gpd.read_file(gadm_path, layer=adm2_layer)
    except Exception as e:
        return stub_result(country, f"GADM read failed: {e}")

    if "GID_2" in adm2.columns:
        adm2_id_col = "GID_2"
    elif "ID_2" in adm2.columns:
        adm2_id_col = "ID_2"
    else:
        adm2_id_col = adm2.columns[0]

    # Load + filter event tables to year + admin-2 join
    try:
        ucdp = pd.read_csv(ucdp_path, low_memory=False)
        acled = pd.read_csv(acled_path, low_memory=False)
    except Exception as e:
        return stub_result(country, f"event table read failed: {e}")

    def to_year(df, col_candidates):
        for c in col_candidates:
            if c in df.columns:
                try: return pd.to_datetime(df[c], errors="coerce").dt.year
                except: pass
                try: return pd.to_numeric(df[c], errors="coerce")
                except: pass
        return None

    ucdp_year = to_year(ucdp, ["year","date_start","Year"])
    acled_year = to_year(acled, ["year","event_date","Year"])
    if ucdp_year is None or acled_year is None:
        return stub_result(country, "year column not identified in events")
    ucdp = ucdp.assign(_year=ucdp_year)
    acled = acled.assign(_year=acled_year)

    # Filter to panel years 2014-2024
    ucdp = ucdp[(ucdp["_year"] >= 2014) & (ucdp["_year"] <= 2024)]
    acled = acled[(acled["_year"] >= 2014) & (acled["_year"] <= 2024)]

    # Spatial join each event table to admin-2
    def make_gdf(df, lat_cols, lon_cols):
        for lat, lon in zip(lat_cols, lon_cols):
            if lat in df.columns and lon in df.columns:
                return gpd.GeoDataFrame(df.copy(),
                    geometry=gpd.points_from_xy(df[lon], df[lat]), crs="EPSG:4326")
        return None
    u_g = make_gdf(ucdp, ["latitude","lat"], ["longitude","lon"])
    a_g = make_gdf(acled, ["latitude","lat"], ["longitude","lon"])
    if u_g is None or a_g is None:
        return stub_result(country, "lat/lon columns not identified")
    if adm2.crs is None or str(adm2.crs).lower() != "epsg:4326":
        adm2 = adm2.to_crs("EPSG:4326")
    u_join = gpd.sjoin(u_g, adm2[[adm2_id_col,"geometry"]], how="left", predicate="within")
    a_join = gpd.sjoin(a_g, adm2[[adm2_id_col,"geometry"]], how="left", predicate="within")

    # Per-admin2 × year counts
    u_count = (u_join.dropna(subset=[adm2_id_col])
                     .groupby([adm2_id_col,"_year"]).size().rename("ucdp_events"))
    a_count = (a_join.dropna(subset=[adm2_id_col])
                     .groupby([adm2_id_col,"_year"]).size().rename("acled_events"))
    panel = pd.concat([u_count, a_count], axis=1).fillna(0).reset_index()
    if len(panel) < 30:
        return stub_result(country, f"only {len(panel)} cells — too few for correlation")

    rho = panel["ucdp_events"].corr(panel["acled_events"], method="spearman")
    verdict = "PASS" if rho >= LOCKED_CORR_THRESHOLD else "FAIL"
    return {
        "country": country,
        "verdict": verdict,
        "spearman_correlation": float(rho),
        "n_admin2_year_cells": int(len(panel)),
        "threshold": LOCKED_CORR_THRESHOLD,
    }


def main():
    print(f"=== Pre-cond 2: ACLED vs UCDP source agreement ===")
    print(f"  Locked threshold: Spearman corr >= {LOCKED_CORR_THRESHOLD}")
    results = [check_country(c) for c in COUNTRIES]
    for r in results:
        print(f"  [{r['country']}] {r['verdict']}  corr={r.get('spearman_correlation')}")

    overall = ("PASS" if all(r["verdict"] == "PASS" for r in results)
               else "PHASE0_STUB" if all(r["verdict"] == "PHASE0_STUB" for r in results)
               else "FAIL_OR_MIXED")

    md = []
    md.append("# Pre-cond 2 Report — Conflict-Source Agreement (ACLED vs UCDP-GED)\n")
    md.append(f"**Run at:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    md.append(f"**Locked check:** Spearman corr >= {LOCKED_CORR_THRESHOLD} between ACLED and UCDP-GED event counts per admin-2 x year.\n")
    md.append(f"**Overall verdict:** **{overall}**\n")
    md.append("\n## Per-country results\n")
    md.append("| Country | Spearman corr | N cells | Verdict |")
    md.append("|---|---|---|---|")
    for r in results:
        corr = r.get('spearman_correlation')
        corr_s = f"{corr:.3f}" if corr is not None else "—"
        md.append(f"| {r['country']} | {corr_s} | {r.get('n_admin2_year_cells','—')} | {r['verdict']} |")
    md.append("\n## Failure handling (locked walk-back §7)\n")
    md.append("- FAIL: reframe shock indicator as source-specific; promote §5 Axis 1 to primary.\n")
    md.append("- PHASE0_STUB: Phase 2 re-runs after data fetched.\n")
    REPORT.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"\n=== Report: {REPORT} ===")
    (NOTES / "precond_2_results.json").write_text(json.dumps({"overall": overall, "results": results}, indent=2))


if __name__ == "__main__":
    main()
