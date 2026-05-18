# Sudan Stage-A Polygon: Pre-1994 Fur Dar (Dar Fur)

**Status:** SCAFFOLD. Digitization not yet executed. Budgeted 2-3 days per
locked Phase 0 constraint: *"Better slow and right than fast and wrong."*

**Polygon meaning (unambiguous):** the territorial extent of the
historical Dar Fur (Fur Sultanate / Fur dar) prior to its 1994
administrative subdivision under the Bashir regime. Per Daly 2007
*Darfur's Sorrow* and Sudan-Open-Archive colonial records, the Fur dar
covers what is approximately modern Sudan's North Darfur, West Darfur,
South Darfur, and Central Darfur states — but the precise pre-1994
boundary follows colonial-era Anglo-Egyptian Sudan Survey demarcations
(1928 Anglo-Egyptian Sudan map series), NOT modern state lines.

This is the canonical Stage-A site for substrate 9.

## Source materials

1. **Colonial Sudan Anglo-Egyptian Survey maps (1920s–1950s):** held by
   the UK National Archives at Kew (CO/MFQ series). Reproduced in:
   - Daly, M. W. (2007). *Darfur's Sorrow: A History of Destruction and
     Genocide*. Cambridge University Press. Map plates II + III show the
     traditional Fur dar boundary at the eve of British administration.
2. **Sudan Open Archive:** https://www.sudanarchive.net/. Holds
   digitized colonial cartography and Anglo-Egyptian Survey
   administrative records.
3. **UCLA Sudan Archive (W.P. Pakenham-Walsh collection):** physical maps
   not online but referenced in Daly 2007 endnotes.
4. **De Waal, A. (2005).** *Famine That Kills: Darfur, Sudan*. Oxford
   University Press. Map A1 reproduces the 1916 Fur Sultanate boundary at
   point of British annexation.

## Digitization plan

1. Acquire scanned Daly 2007 Plate II or De Waal 2005 Map A1 as primary
   reference (best-available reproduction of the pre-1994 Fur dar).
2. Georeference scanned map against modern Sudan GADM admin-2 (Locality /
   mahaliya) boundaries.
3. Digitize polygon vertices in QGIS.
4. Export as GeoJSON in EPSG:4326.
5. Save to this directory as `sudan_fur_dar_pre1994.geojson`.
6. Cross-check against modern Darfur states administrative boundaries:
   the polygon should approximately contain modern N/W/S/Central Darfur
   but EXTEND slightly into modern Chad (the Fur dar historically
   straddled what is now the Chad-Sudan border) and into modern
   Kordofan provinces along the eastern edge.

## EOSV historical-atrocity-count cross-reference (locked constraint)

Per `displacement_research_design.md` §3.2 and locked Phase 0 constraints:

  **Sudan EOSV window: 2003–2010** (cleanly within EOSV coverage; EOSV
  ends 2013). Post-2013 ethnic-targeting events fold into
  `current_conflict_intensity`, NOT into `historical_atrocity_count`.

The Fur-dar polygon is the geographic scope; the 2003-2010 EOSV events
filtered to within the polygon constitute the historical-atrocity-count
covariate for Sudan.

## Sensitivity to polygon boundary choice (Axis 4 in §5)

The exact pre-1994 boundary has some interpretive variation across
Daly 2007 vs De Waal 2005 vs Anglo-Egyptian Survey 1928. Axis 4 (polygon
boundary sensitivity) fits the v0_2 model under:
  - Daly 2007 reproduction (primary)
  - +10km buffer expansion
  - -10km buffer erosion

## Digitization output (when complete)

- `sudan_fur_dar_pre1994.geojson` — primary polygon
- `sudan_fur_dar_pre1994_buffer_plus_10km.geojson` — Axis 4 sensitivity
- `sudan_fur_dar_pre1994_buffer_minus_10km.geojson` — Axis 4 sensitivity
- `provenance.md` (this file, updated with georeferencing RMS + SHA-256)

## Hash chain

This provenance.md file's SHA-256 at Phase 0 lock will be recorded in
`manifest.json`.
