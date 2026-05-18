# Colombia Stage-A Polygon: "CDO 1922"

**Status:** SCAFFOLD. Digitization not yet executed. Budgeted 2-3 days per
locked Phase 0 constraint: *"Better slow and right than fast and wrong."*

**PI confirmation required (v2 redline flag #1):** The author's
interpretation of "CDO 1922" is a placeholder pending PI confirmation. See
§12 of `notes/displacement_research_design.md`. Candidate interpretations:

  (a) 1922 Colombian colonial Comisarías administrative boundaries
      (Comisaría Especial — *primary placeholder*)
  (b) La Violencia 1948-1958 mortality concentration zones
  (c) FARC-pre-Caguán historical foothold (Caquetá, Putumayo, Cauca
      south)
  (d) Other

Until PI confirms, the digitization process is paused.

## Source materials (placeholder)

Per locked design doc §1.1:

1. **Historical Colombian gov't gazettes (1920s):** the 1922 ley creating
   Colombian Comisarías Especiales — source archive at Archivo General
   de la Nación de Colombia (AGN). URL: https://www.archivogeneral.gov.co/

2. **IGAC archive (Instituto Geográfico Agustín Codazzi):** authoritative
   Colombian cartography. URL: https://www.igac.gov.co/. Historical
   administrative-division maps available in the Mapoteca section.

3. **CINEP archive of La Violencia 1948-1958 mortality:** Centro de
   Investigación y Educación Popular. URL: https://www.cinep.org.co/. The
   *Noche y Niebla* database has documented violence events back to 1948.

## Digitization plan (when unlocked by PI)

1. Acquire scanned historical reference map per the confirmed
   interpretation (a-d above).
2. Georeference scanned map against modern Colombian admin boundaries
   (GADM admin-2 = Municipio).
3. Digitize polygon vertices in QGIS or web GIS.
4. Export as GeoJSON in EPSG:4326.
5. Save to this directory as `colombia_stage_a_polygon.geojson`.
6. Update `provenance.md` with:
   - Source map citation (publisher, date, sheet number)
   - Georeferencing method + RMS error
   - Digitization operator + date
   - SHA-256 of output GeoJSON

7. Run `precond_3_polygon_coverage.py` to confirm >= 5 admin-2 inside.

## Cross-substrate methodology touch

The 1930s HOLC redlining polygons used in gun-violence substrate 6 set the
provenance standard: each polygon comes with explicit source citation,
georeferencing method, RMS error, and SHA-256. Colombia "CDO 1922"
follows that pattern.

## Digitization output (when complete)

- `colombia_stage_a_polygon.geojson` — single polygon or multi-polygon
- `colombia_stage_a_polygon.png` — visual reference for the digitization
  (optional)
- `provenance.md` (this file, updated)

## Hash chain

This provenance.md file's SHA-256 at Phase 0 lock will be recorded in the
top-level `manifest.json` so the rule book is auditable.
