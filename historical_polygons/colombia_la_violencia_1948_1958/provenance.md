# Colombia Stage-A Polygon: La Violencia 1948–1958 Mortality Concentration Zones

**Status:** LOCKED interpretation per pre-reg redline Entry 002 (2026-05-17).

**Framing (per Entry 002 substrate-9 long-term-displacement clarification):**
The polygon marks where Colombia's *protracted, multi-generational IDP burden*
was first established. Modern IDP is not new-onset displacement; it's the
chronic legacy of historical atrocity geographies, periodically compounded
by contemporary shocks. La Violencia 1948-1958 is Colombia's founding modern
displacement-atrocity event — ~2 million internally displaced, mortality
~200-300k. Its geography became the platform that FARC, paramilitary, and
post-1985 displacement waves all subsequently overlaid.

**Period:** April 1948 (Bogotazo / Gaitán assassination) through ~1958
(National Front pact). Some scholars extend to 1964 (FARC founding).

**Estimated mortality:** 200,000-300,000 killed.
**Estimated displacement (chronic):** ~2 million IDPs, persisting into
subsequent decades.

## Geographic extent (per Centro de Memoria Histórica + CINEP)

Departments where La Violencia mortality concentration was ≥ 10 documented
events per municipio:

- **Tolima** — central-mountain coffee zone (Líbano, Chaparral, Rovira,
  Rioblanco)
- **Caldas** (within 1950s borders; modern Caldas + Quindío + Risaralda)
- **Cundinamarca** — west of Bogotá in coffee municipios
- **Valle del Cauca** — northern Valle (Sevilla, Caicedonia)
- **Antioquia** — southwest + far northern Antioquia
- **Boyacá** — Tundama + Sugamuxi provinces
- **Norte de Santander** — eastern Pamplona / Cúcuta area

Spillover zones (lower density): Huila, Cauca, Nariño. ±10km buffer
variant (Axis 4) tests whether including spillover changes results.

## Source materials

1. **Guzmán Campos, G., Fals Borda, O., & Umaña Luna (1962).**
   *La Violencia en Colombia: Estudio de un proceso social.* Canonical
   contemporary academic source — per-municipio mortality + violence maps.
2. **CINEP Noche y Niebla** (https://www.nocheyniebla.org/) — modern
   archive of Colombian historical violence, coverage extends back to
   1948. Per-municipio event-level records, usable for
   `historical_atrocity_count`.
3. **Centro Nacional de Memoria Histórica.** *¡Basta Ya! Colombia:
   Memorias de Guerra y Dignidad* (2013). Map 2 (p. 41): La Violencia
   mortality density per municipio — primary digitization reference.
4. **Sánchez, G., & Meertens, D. (2001).** *Bandits, Peasants, and Politics:
   The Case of "La Violencia" in Colombia.* Cambridge UP.
5. **Roldán, M. (2002).** *Blood and Fire: La Violencia in Antioquia,
   Colombia, 1946-1953.* Duke UP. Antioquia-specific cross-check.

## Why La Violencia (PI selection rationale)

Per redline Entry 002, La Violencia chosen over Comisarías Especiales (1922
admin boundary, not atrocity) and FARC pre-Caguán foothold (overlaps too
much with modern displacement — confounds historical with current). La
Violencia geography is distinct from modern FARC-era displacement (Pacific
coast, Caquetá, Norte de Santander) — captures a non-overlapping historical
substrate that protracted-displacement framing requires.

## historical_atrocity_count source for Colombia

CINEP Noche y Niebla per-municipio event counts, 1948-1965 window
(extending 7 years past strict 1958 endpoint to capture trailing Violencia
events documented in CNMH ¡Basta Ya!). Available without institutional
access.

## Digitization plan

1. Acquire CNMH ¡Basta Ya! (2013) Map 2 scan as primary reference.
2. Cross-check against Sánchez & Meertens (2001) + Guzmán Campos et al.
   (1962).
3. Georeference against modern GADM admin-2 (Municipio).
4. Digitize union of municipios with ≥ 10 La Violencia events per
   consolidated record.
5. Export as GeoJSON in EPSG:4326.

## Digitization output (when complete)

- `colombia_la_violencia_1948_1958.geojson` — primary polygon
- `colombia_la_violencia_1948_1958_buffer_plus_10km.geojson` — Axis 4
- `colombia_la_violencia_1948_1958_buffer_minus_10km.geojson` — Axis 4
- `provenance.md` (this file, updated with georef RMS + SHA-256)
