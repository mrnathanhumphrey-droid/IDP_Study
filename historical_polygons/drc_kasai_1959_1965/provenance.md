# DRC Stage-A Polygon: Kasai 1959–1965 Luba Expulsion Zone

**Status:** LOCKED interpretation per pre-reg redline Entry 002 (2026-05-17).

**Framing (per Entry 002 substrate-9 long-term-displacement clarification):**
The polygon marks the founding multi-generational IDP geography in DRC's
Kasai region. The Luba expulsion from Katanga + Lulua-Luba ethnic violence
in Kasai (1959-1965) created ~250,000 internally-displaced ethnic-Luba
returnees who settled in Kasai-Occidental + Kasai-Oriental. That
chronic displacement geography persisted through Mobutu, the Congo Wars,
and was reactivated by the 2016-2018 Kamuina Nsapu militia conflict that
displaced ~1.5 million in the same provinces. The polygon is the
historical substrate; modern shocks (Kamuina Nsapu, RDF cross-border
pressure) compound on it.

**Period:** 1959-1965 (Katangan secession era through immediate post-
secession aftermath). Lulua-Luba ethnic violence in Kasai documented from
1959; mass Luba expulsion from Katanga peaks 1960-1962; Kasai resettlement
1962-1965.

**Estimated displacement:** ~250,000 ethnic-Luba forcibly returned to
Kasai from Katanga; ~hundreds-of-thousands additional displaced within
Kasai by Lulua-Luba violence.

## Geographic extent

Modern province equivalents (post-2015 DRC administrative reorganization
that subdivided Kasai-Occidental + Kasai-Oriental into 5 provinces):

- **Kasai** (former part of Kasai-Occidental)
- **Kasai-Central** (former part of Kasai-Occidental)
- **Kasai-Oriental**
- **Lomami** (former part of Kasai-Oriental)
- **Sankuru** (former part of Kasai-Oriental)

Territoires within these provinces where Luba returnee resettlement
concentrated:

- Mwene-Ditu, Kabinda, Lubao (Lomami)
- Mbuji-Mayi area territoires (Kasai-Oriental)
- Demba, Dimbelenge, Luiza (Kasai-Central)
- Tshikapa, Kamonia, Ilebo (Kasai)
- Lusambo, Lubefu (Sankuru)

Polygon excludes Katanga (modern Haut-Katanga, Lualaba, Tanganyika,
Haut-Lomami) — that's the EXPULSION SOURCE not the displacement
destination. Stage-A polygon is the chronic-IDP destination geography.

## Source materials

**No UCDP / EOSV coverage:** both data sources begin in 1989; Kasai
expulsion 1959-1965 is pre-data-era. `historical_atrocity_count` for DRC
operationalizes via manual coding from academic-history sources listed
below. This is the v1 → v2 source-list amendment locked in redline
Entry 002 §3.2.

1. **Young, C., & Turner, T. (1985).** *The Rise and Decline of the
   Zairian State.* University of Wisconsin Press. Chapter on early
   Mobutu period documents Luba expulsion + Kasai resettlement geography.
2. **Lemarchand, R. (1964).** *Political Awakening in the Belgian Congo.*
   University of California Press. Primary contemporary academic source
   on the 1959-1962 ethnic-conflict pattern.
3. **CRDA UCL Louvain Belgian colonial archives** — original colonial
   ethnic-population census records + missionary reports.
4. **De Villers, G. (2002).** *Tribu et État au Zaïre, République
   Démocratique du Congo.* Cahiers Africains 50. Detailed retrospective
   on Mobutu-era ethnic geography.
5. **Stearns, J. (2011).** *Dancing in the Glory of Monsters: The Collapse
   of the Congo and the Great War of Africa.* PublicAffairs. Modern
   trailing-effect analysis for the same geography.
6. **CRG (Congo Research Group) / NYU 2017 reports on Kamuina Nsapu** —
   recent (2016-2018) Kasai conflict event-level data; cross-reference
   for confirming the same geography reactivated 50+ years later.

## historical_atrocity_count source (DRC-specific operationalization)

Per Entry 002 §3.2 amendment: DRC uses **manual coding from Young &
Turner + Lemarchand + Stearns** of Luba expulsion + ethnic-violence
events per territoire (modern admin-2 equivalent) for the 1959-1965
window. Output: `data/atrocity_counts/drc_kasai_atrocity_count.csv`
with columns `territoire_gid, n_events_1959_1965, n_displaced_estimate`.

This is methodologically different from the UCDP/EOSV event-database
extraction used for Colombia / Sudan / Yemen. The DRC count is academic-
secondary-source coded, not primary-source event-database extraction.
The methodological asymmetry is documented in the §6 disposition
reading as a per-country limitation.

## Why Kasai (PI selection rationale)

Per redline Entry 002, Kasai chosen over the two alternatives because:

- **vs Eastern Kivu pre-1996:** the post-1996 Kivu story is well-covered
  by event-database extraction (UCDP-GED 1989-present), so the
  shock-amplification test would be testing against a polygon that's
  almost contemporaneous with the contemporary panel. Kasai 1959-1965
  is a deeper historical layer — better fit for the
  protracted-displacement framing.
- **vs Ituri pre-1999 Hema-Lendu:** narrower geography; smaller
  population at risk; less of a multi-generational story.

The Kasai choice is consistent with the substrate-9 framing that the
historical polygon should mark *founding* protracted-displacement
geography, not just any prior-conflict geography.

## Digitization plan

1. Acquire Young & Turner (1985) administrative map of post-1965 Kasai.
2. Cross-check against Stearns (2011) Map 4 (Kamuina Nsapu zone, modern
   geography) — confirms same territoires reactivated by 2016-2018
   conflict.
3. Georeference against modern DRC GADM admin-2 (Territoire).
4. Digitize as union of territoires in the 5 modern provinces (Kasai +
   Kasai-Central + Kasai-Oriental + Lomami + Sankuru).
5. Export as GeoJSON in EPSG:4326.

## Digitization output (when complete)

- `drc_kasai_1959_1965.geojson` — primary polygon
- `drc_kasai_1959_1965_buffer_plus_10km.geojson` — Axis 4
- `drc_kasai_1959_1965_buffer_minus_10km.geojson` — Axis 4
- `provenance.md` (this file, updated with RMS + SHA-256)

## DRC population denominator (locked)

Per PI confirmation 2026-05-17: 2024 INS estimates as the population
denominator for DRC admin-2 units. The 1984 census is 40 years stale;
the staleness is flagged in `data/dtm/_population_provenance.md` (Phase 2
output) and reported in the §6 disposition reading as a per-country
caveat.
