# Yemen Stage-A Polygon: Six Wars (2004–2010) Operational Extent

**Status:** LOCKED interpretation per pre-reg redline Entry 002 (2026-05-17).
PI confirmed selection: Six Wars operational-conflict-narrow framing
(vs broader Zaydi-imamate heartland).

**Framing (per Entry 002 substrate-9 long-term-displacement clarification):**
Yemen's Six Wars (2004-2010) are this substrate's *youngest* historical
polygon — only ~4-10 years before the contemporary panel starts (2014).
This is the methodological asymmetry across the 4 countries: Colombia
(80yr-old polygon), Sudan (pre-1994 / centuries-old Fur Sultanate), DRC
(65yr-old Kasai), Yemen (15-20yr-old Six Wars). The Yemen historical
polygon is closer to contemporaneous than truly historical.

That asymmetry is locked in the design doc §6 H_CROSS_COUNTRY_PORTABILITY
test — direction must hold in all 4 countries; if it holds only in the
older-polygon countries (Colombia/Sudan/DRC), that's a temporal-distance
finding distinct from the cross-country claim. Documented in walk-back
§9.

**Period:** 2004 (Sa'dah Houthi insurgency outbreak) through ~2010
(Sixth War end). Six discrete wars per ICG numbering: War 1 (2004),
War 2 (2005), War 3 (2005-2006), War 4 (2007), War 5 (2008-2009),
War 6 (2009-2010).

**Estimated displacement (cumulative Six Wars):** ~300,000-400,000 IDPs
peak during War 5 + War 6 (per OCHA + IOM 2010 estimates), most
returning intermittently between wars. Modern Yemen civil war (2014-present)
overlaid on this same geography produces an order-of-magnitude larger
chronic IDP population (~4 million as of 2024).

## Geographic extent (per ICG / Salisbury 2015 / Yemen Polling Center 2012)

The Six Wars operational extent — admin-2 mudiriyah units where battle
events were documented across the six wars:

- **Sa'dah governorate** — entirety (Houthi heartland; all six wars fought here)
- **Northern Hajjah governorate** — Khayran al Muharraq, Kushar, Mustaba
  mudiriyahs (War 3, War 5, War 6)
- **Western Amran governorate** — Harf Sufyan, Suwayr, Huth mudiriyahs
  (War 4, War 5, War 6)
- **Northern Sana'a governorate** — Bani Matar, Bani Hushaysh fringe
  (War 5, War 6 only)

**EXCLUDED from primary polygon:** Sana'a city (capital). Houthi capture
of the capital occurred September 2014, AFTER the locked pre-2014 cutoff.
Sana'a city becomes part of the contemporary-shock geography, not the
historical-polygon geography. This is a critical boundary distinction
per locked Phase 0 constraints.

The locked Axis 4 polygon-boundary sensitivity (±10km buffer) tests
whether including/excluding the Sana'a city fringe changes the
substrate-9 finding.

## Source materials

1. **International Crisis Group reports per war:**
   - "Yemen: Defusing the Saada Time Bomb" (ICG Middle East Report N°86,
     2009; covers Wars 1-5)
   - "Breaking Point? Yemen's Southern Question" (ICG Middle East
     Report N°114, 2011; covers War 6 + aftermath)
   - Each report includes battle-by-battle maps with mudiriyah-level
     identification
2. **Salisbury, P. (2015).** "Yemen and the Saudi-Iranian 'Cold War'."
   Chatham House Research Paper. Comprehensive Six Wars geographic
   progression map (Figure 2).
3. **Yemen Polling Center (2012).** Independent Yemeni civil-society
   conflict atlas. Sa'dah war zones at mudiriyah granularity.
4. **UCDP-GED Yemen events 2004-2010** filtered to
   side_a=Houthi/Government dyad (UCDP conflict_new_id for Yemen-Houthi
   conflict). Already in `data/ucdp/ucdp-ged-yemen.csv` (5,445 total Yemen
   events 1989-2024; subset to 2004-2010 yields the operational
   atrocity-count for this polygon).
5. **EOSV 2003-2010 (per locked Sudan constraint also applies to Yemen
   one-sided violence subset).** Use type_of_violence=3 from UCDP-GED as
   functional EOSV substitute since UCDP one-sided events are
   ethnicity-coded post-2003.

## historical_atrocity_count source for Yemen

UCDP-GED Yemen events filtered to:
- year between 2004 and 2010
- side_a OR side_b contains "Houthi" or "Government of Yemen"
- type_of_violence in {1 (state-based), 3 (one-sided)}

Per mudiriyah event count via ActionGeo lat/long spatial join to GADM
admin-2 polygons. Available from the already-fetched
`data/ucdp/ucdp-ged-yemen.csv`.

## Why Six Wars narrow (PI selection rationale)

Per redline Entry 002, narrow Six Wars chosen over broader Zaydi heartland:

- **vs Zaydi-imamate heartland (broad):** the broader option would
  include Sana'a city + governorate + Dhamar + Mahwit + Raymah, capturing
  pre-1962 imamate authority geography. That's ~9 governorates rather
  than 4. Substantively appealing as a "deep historical layer" framing,
  but the contemporary contrast becomes harder — most of Yemen's
  population lives in the broad-Zaydi geography, so non-polygon admin-2
  units would be a thin tail. Narrow Six Wars has cleaner empirical
  contrast: a defined operational-conflict zone vs the rest of Yemen.
- **Operational-conflict-narrow has better data coverage:** UCDP-GED
  + ICG documentation covers Six Wars at mudiriyah granularity. The
  broader Zaydi heartland would require historical-religious-geography
  sources outside the locked data sources.

## Digitization plan

1. Acquire ICG MER N°86 (2009) Figure 1 + Salisbury 2015 Figure 2 as
   primary references.
2. Cross-check with UCDP-GED Yemen events 2004-2010 spatial distribution.
3. Georeference against modern Yemen GADM admin-2 (Mudīriyah).
4. Digitize as union of mudiriyahs with ≥ 5 documented Six Wars events.
5. Export as GeoJSON in EPSG:4326.

## Digitization output (when complete)

- `yemen_six_wars_2004_2010.geojson` — primary polygon
- `yemen_six_wars_2004_2010_buffer_plus_10km.geojson` — Axis 4
- `yemen_six_wars_2004_2010_buffer_minus_10km.geojson` — Axis 4
- `provenance.md` (this file, updated with RMS + SHA-256)
