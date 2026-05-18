# Yemen Stage-A Polygon: Pre-2014 Houthi / Zaydi Heartland

**Status:** SCAFFOLD. Digitization not yet executed. Budgeted ~1-2 days
(simpler than Sudan/DRC since the Six Wars are well-documented).

**PI confirmation required (v2 redline flag #3):** The author's
inference of "pre-2014 Houthi conflict zones (Sa'dah / Hajjah / Amran)"
as the Yemen Stage-A polygon is a placeholder. Candidate interpretations:

  (a) Six Wars (2004-2010) territorial extent: Sa'dah, Hajjah, Amran +
      northern Sana'a *(primary placeholder)*
  (b) Zaydi-religion heartland (broader: Sa'dah, Hajjah, Amran, Sana'a
      city + governorate, Dhamar, Mahwit, Raymah — areas of historical
      Zaydi-imamate authority pre-1962 revolution)
  (c) Other

The (a) "Six Wars territorial extent" focuses on the operational
Houthi-government conflict zones; (b) "Zaydi heartland" is broader and
predates the Houthi movement, capturing the deeper historical
ethno-religious geography. PI should choose between operational-conflict
(narrower) vs religious-heritage (broader) framing.

Until PI confirms, the digitization is paused.

## Source materials (for primary placeholder, option a)

1. **Salisbury, P. (2015).** "Yemen and the Saudi-Iranian 'Cold War'."
   Chatham House Research Paper. Maps the Six Wars (2004-2010)
   geographic progression.
2. **International Crisis Group (ICG) reports 2007-2014:** detailed
   battle-by-battle maps for each of the Six Wars (1: 2004; 2: 2005; 3:
   2005-2006; 4: 2007; 5: 2008-2009; 6: 2009-2010).
3. **Yemen Polling Center conflict atlas (2012):** independent Yemeni
   civil-society polygon mapping of the Sa'dah war zones.
4. **ACLED back-cast 2010-2014:** ACLED events with location_subtype =
   "Battle - No change of territory" or "Riots/Protests" filtered to
   pre-Houthi-takeover 2014 — secondary-source bounding of the polygon.

## Six Wars geographic core (option a primary placeholder)

The pre-2014 Houthi conflict zones, per ICG and Salisbury 2015:
- **Sa'dah governorate** — entire governorate, the Houthi heartland
- **Northern Hajjah governorate** — Houthi-government incursions
- **Western Amran governorate** — Houthi-government incursions
- **Northern Sana'a governorate** (NOT Sana'a city) — Houthi-government
  staging grounds

The polygon should EXCLUDE Sana'a city (capital) — Houthi capture of the
capital occurred in September 2014, AFTER the locked pre-2014 cutoff.

## Pre-cond 4 cross-reference

Per locked Phase 0 constraint:

  *"Yemen post-2022 ACLED coverage is degraded in Houthi-controlled
  areas. Pre-cond 4 may force Yemen drop to Stage B only. Document,
  don't fight it."*

Pre-cond 4 checks Yemen ACLED post-2022 coverage in Houthi-controlled
governorates (different from this Stage-A polygon — Houthi-controlled
governorates after 2014 include Sa'dah, Hajjah, Amran, Sana'a city +
governorate, Dhamar, Ibb, Hodeidah, Mahwit, Raymah — see
`_scripts/precond_4_yemen_post2022_coverage.py` for the locked list).

This Stage-A polygon is the PRE-2014 Houthi conflict zone, NOT the
post-2014 Houthi-controlled territory. They overlap but are not
identical.

## Digitization plan

1. Acquire ICG Crisis Group 2010 Yemen Map (post-Six-Wars boundary
   reproduction) or Salisbury 2015 map.
2. Georeference scanned map against modern Yemen GADM admin-2
   (Mudīriyah / district).
3. Digitize polygon vertices in QGIS.
4. Export as GeoJSON in EPSG:4326.

## Digitization output (when complete)

- `yemen_houthi_zaydi_pre2014.geojson`
- `yemen_houthi_zaydi_pre2014_buffer_plus_10km.geojson` — Axis 4
- `yemen_houthi_zaydi_pre2014_buffer_minus_10km.geojson` — Axis 4
- `provenance.md` (this file, updated)

## Hash chain

SHA-256 of this file at Phase 0 lock recorded in `manifest.json`.
