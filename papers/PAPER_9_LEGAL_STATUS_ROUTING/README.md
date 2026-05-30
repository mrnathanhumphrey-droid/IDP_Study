# Paper 9 — Legal-Status Routing (Active CHANNEL paper)

**Working title**: *Routing as Mechanism: Legal-Status Classification as an Active Channel in US Displacement Outcomes*

**Status**: launched 2026-05-30; scope locked; PRE_REG_042 locked.

**Selected via**: [META_PIVOT_QUANTIFICATION](../META_PIVOT_QUANTIFICATION_2026_05_30.md). First **ACTIVE CHANNEL** paper in the program (P7=passive market-price channel; P8=passive spatial-receiver channel; P9=active administrative-routing channel with institutional actor).

## Core flip
**Conventional**: study Ukrainian / Venezuelan / Cuban / Syrian / Afghan displacement *separately*.
**Right unit**: pool across origins, split by **legal-track × jurisdiction × cohort** (TPS / Asylum / Refugee / SIV / Parole / Undocumented / LPR).

## Core claim
The US receiving-state apparatus routes heterogeneous upstream displacement events into a small number of downstream legal categories. Each category attaches a distinct rights-bundle. **Variation in outcomes is dominated by track, not origin** — for outcomes whose mechanism runs through legal authorization.

## Scope + plan
See [PAPER_9_SCOPE.md](../PAPER_9_SCOPE.md) for full architecture.
See [HUNT_PLAN.md](HUNT_PLAN.md) for phased pre-reg roster.

## Substrate elements
- `digs/` — analysis digs (one per fired pre-reg)
- `HUNT_PLAN.md` — phased pre-reg schedule
- (when relevant) `analysis/`, `_scripts/`, `data/paper9/` parallel folders elsewhere in the repo

## Connection to the rest of the program
| paper | shared with P9 | difference |
|---|---|---|
| P7 (SDP rent funnel) | CHANNEL archetype | P7 passive (market price); P9 active (admin decision) |
| P8 (destination convergence) | CHANNEL archetype | P8 passive (spatial receiver); P9 active (institutional routing) |
| P1/P5 (lever configs) | configuration-of-rights framing | P9 rights-bundle per track ≈ P1/P5 lever-config per case |
| Migration project (D:/Migration) | US receiving-side | P9 routes-then-outcomes; migration project clusters-then-routes |

## Risks (per scope)
1. data cross-walk uncertainty (ACS doesn't directly identify track)
2. selection into track (non-random; eligibility-window timing as quasi-exogenous)
3. political sensitivity (pre-reg discipline is the safeguard)
4. coordination with parallel agent on P7 territory
5. TPS terminations 2025-2026 affecting cohort definitions

## Next
Phase 1 fires on next session — data acquisition (ACS extract, ORR refugee data, USCIS TPS, EOIR, DOS SIV, MPI undoc) + cross-walk construction + variance decomposition + differential outcome prediction (PRE_REG_042).
