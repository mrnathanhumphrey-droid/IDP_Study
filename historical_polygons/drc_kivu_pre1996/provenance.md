# DRC Stage-A Polygon: Eastern Kivu Pre-1996 Ethnic-Targeting Zones

**Status:** SCAFFOLD. Digitization not yet executed. Budgeted 2-3 days.

**PI confirmation required (v2 redline flag #2):** The author's
inference of "Kivu pre-1996 ethnic-targeting zones" as the DRC Stage-A
polygon is a placeholder pending PI confirmation. See §12 of
`notes/displacement_research_design.md`. Candidate interpretations:

  (a) Eastern Kivu (North Kivu + South Kivu) historical
      Banyamulenge/Hutu/Tutsi ethnic-targeting zones pre-1996 *(primary
      placeholder)*
  (b) Kasai historical ethnic-cleansing zones (1959-1965 Luba expulsion)
  (c) Ituri pre-1999 Hema-Lendu conflict zone
  (d) Other

Until PI confirms, digitization is paused.

## Source materials (for primary placeholder)

1. **de Villers, G. (2002). *Tribu et État au Zaïre, République
   Démocratique du Congo*.** Cahiers Africains 50. Detailed ethnic
   geography of pre-Mobutu and Mobutu-era eastern Zaire.
2. **Centre de Recherches et de Documentation sur l'Afrique (CRDA, UCL
   Louvain):** holds Belgian colonial-era ethnic-mapping records and
   pre-1996 conflict-zone reports.
3. **Reyntjens, F. (2009). *The Great African War: Congo and Regional
   Geopolitics 1996-2006*.** Cambridge University Press. Maps the
   1996-1997 AFDL invasion and identifies pre-1996 ethnic-targeting
   geography.
4. **UCDP-GED pre-1996 events filtered to eastern DRC** as
   secondary-source validation (events have lat/long; can be used to
   bound the polygon empirically).

## Why pre-1996?

The 1996 Rwandan-genocide spillover (AFDL invasion + First Congo War)
restructured eastern DRC's ethnic-violence geography. Pre-1996 zones
reflect the underlying ethnic-targeting pattern that the post-1996
conflict ESCALATED but did not create. The pre-1996 polygon isolates
the historical-atrocity baseline that the substrate-9 hypothesis tests
against contemporary shocks.

## Digitization plan

1. Acquire de Villers 2002 or Reyntjens 2009 ethnic-targeting map as
   primary reference.
2. Cross-check against pre-1996 UCDP-GED events filtered to DRC
   territoires.
3. Georeference scanned map against modern DRC GADM admin-2 (Territoire).
4. Digitize polygon vertices in QGIS.
5. Export as GeoJSON in EPSG:4326.

## DRC-specific staleness flag (locked constraint)

Per locked Phase 0 constraint:

  *"DRC 1984 census is 40 years stale. Note the limitation; use 2024 INS
  estimates for present-day population offsets but flag the uncertainty."*

The population denominator for DRC admin-2 units is 2024 INS estimate
based on 1984 census rolled forward with growth rates. This is the
weakest population denominator across the 4 countries. The
DRC-specific uncertainty is documented in
`data/dtm/_population_provenance.md` (Phase 2 output) and flagged in
the §6 disposition reading.

## Digitization output (when complete)

- `drc_kivu_pre1996_polygon.geojson`
- `drc_kivu_pre1996_buffer_plus_10km.geojson` — Axis 4 sensitivity
- `drc_kivu_pre1996_buffer_minus_10km.geojson` — Axis 4 sensitivity
- `provenance.md` (this file, updated)

## Hash chain

SHA-256 of this file at Phase 0 lock recorded in `manifest.json`.
