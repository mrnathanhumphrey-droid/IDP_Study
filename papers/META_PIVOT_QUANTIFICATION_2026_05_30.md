# Meta-Pivot Quantification — Naming the Colors (2026-05-30)

**Purpose**: Quantify the pivot-dimensions matrix from [RIGHT_UNIT_TABLE_2026_05_30.md](RIGHT_UNIT_TABLE_2026_05_30.md). The matrix shows visual structure ("colors") — this doc operationalizes that structure with frequency, co-occurrence, clustering, mutual information, and rarity-weighted novelty metrics. Computed by `_scripts/meta_pivot_quantification.py`; raw values in `analysis/meta_pivot_quantification_2026_05_30.json`.

---

## 0. The starting matrix (recap)

| paper | (a) finer | (b) downstream | (c) typed | (d) relational | (e) mediator | total |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | | | ✓ | ✓ | | 2 |
| P2 | ✓ | | ✓ | | | 2 |
| P3 | ✓ | | | ✓ | | 2 |
| P4 | ✓ | | ✓ | ✓ | | 3 |
| P5 | | | ✓ | ✓ | | 2 |
| P6 | | | ✓ | ✓ | | 2 |
| P7 | ✓ | ✓ | | | ✓ | 3 |
| P8 | ✓ | ✓ | | ✓ | ✓ | 4 |

---

## 1. Pivot frequency — what's common, what's rare

| pivot | papers using it | freq | rarity |
|---|:---:|:---:|---|
| (d) relational / structural | 6/8 | 0.75 | **most common** |
| (a) finer resolution | 5/8 | 0.625 | common |
| (c) typed / configured | 5/8 | 0.625 | common |
| (b) downstream of cause | 2/8 | 0.25 | **rare** |
| (e) mediator / destination channel | 2/8 | 0.25 | **rare** |

Three common pivots (relational, finer-resolution, typed) — 5-6 papers each. Two rare pivots (downstream, mediator) — both at exactly 2/8. The frequencies cluster: there's no pivot at 3 or 4. The corpus is **bimodal in pivot frequency**: things either show up nearly everywhere or barely at all.

---

## 2. Pivot co-occurrence + mutual information — the structural backbone

**Pairwise co-occurrence** (number of papers exhibiting both):

| pair | n | reading |
|---|:---:|---|
| (c) typed × (d) relational | **4** | the program's signature pairing |
| (a) finer × (d) relational | 3 | sub-national structural |
| (a) finer × (b) downstream | 2 | |
| (a) finer × (c) typed | 2 | |
| (a) finer × (e) mediator | 2 | |
| (b) downstream × (e) mediator | **2** | **perfect** (always together) |
| (b) downstream × (d) relational | 1 | (P8 only) |
| (d) relational × (e) mediator | 1 | (P8 only) |
| **(b) downstream × (c) typed** | **0** | **mutually exclusive** |
| **(c) typed × (e) mediator** | **0** | **mutually exclusive** |

**Pairwise mutual information (bits)** — bold = highest signal:

|  | a | b | c | d | e |
|---|:---:|:---:|:---:|:---:|:---:|
| **a** finer | 0.954 | 0.204 | 0.348 | 0.204 | 0.204 |
| **b** downstream | 0.204 | 0.811 | **0.467** | 0.074 | **0.811** |
| **c** typed | 0.348 | **0.467** | 0.954 | 0.016 | **0.467** |
| **d** relational | 0.204 | 0.074 | 0.016 | 0.811 | 0.074 |
| **e** mediator | 0.204 | **0.811** | **0.467** | 0.074 | 0.811 |

Two structural constraints emerge — both qualify as "high MI" but they encode opposite relationships:

### Constraint 1: (b) and (e) are perfectly correlated
**MI(b, e) = 0.811** — equal to either's own entropy. In information-theoretic terms, **downstream and mediator carry identical information about which papers use them**. The two pivots are not independent; they are one combined "channel" pivot that has been factored into two facets (the direction = downstream; the unit = the mediating channel). P7 and P8 are the only papers where this combined pivot fires.

### Constraint 2: (c) is mutually exclusive with both (b) and (e)
MI(b, c) = MI(c, e) = 0.467 — high precisely *because* they co-occur **zero times**. The typed pivot and the channel pivot **never coexist in the same paper**. This is not weak independence — it is a hard structural constraint in the corpus.

### What constraints 1 + 2 jointly say
The program operates in two **mutually exclusive epistemic modes**:

- **TYPED mode**: classify entities into discrete buckets (pivot c, almost always with d, sometimes with a). Question: *"what kind is this?"*
- **CHANNEL mode**: find the downstream funnel (pivots b + e together, with a, sometimes with d). Question: *"what mediator do distinct causes flow through?"*

These are not just different — they are **antagonistic**: no paper does both. They demand different tools, different units, different framings. Choosing one excludes the other.

A paper in TYPED mode (P1, P2, P4, P5, P6) builds a typology and identifies which type a country-period belongs to. A paper in CHANNEL mode (P7, P8) finds a single downstream variable through which multiple upstream causes converge. The two modes are coordinated with different research questions and produce different kinds of findings — the empirical signature in the MI matrix is that they don't mix.

---

## 3. Paper similarity — three archetypes by hierarchical clustering

Jaccard similarity matrix (rows/cols = papers):

|  | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 1.00 | .33 | .33 | .67 | **1.00** | **1.00** | .00 | .20 |
| P2 | .33 | 1.00 | .33 | .67 | .33 | .33 | .25 | .20 |
| P3 | .33 | .33 | 1.00 | .67 | .33 | .33 | .25 | **.50** |
| P4 | .67 | .67 | .67 | 1.00 | .67 | .67 | .20 | .40 |
| P5 | **1.00** | .33 | .33 | .67 | 1.00 | **1.00** | .00 | .20 |
| P6 | **1.00** | .33 | .33 | .67 | **1.00** | 1.00 | .00 | .20 |
| P7 | .00 | .25 | .25 | .20 | .00 | .00 | 1.00 | **.75** |
| P8 | .20 | .20 | .50 | .40 | .20 | .20 | **.75** | 1.00 |

Three observations:
- **P1 = P5 = P6 exactly** (Jaccard 1.0, identical vectors): pure configuration mode.
- **P7 and P8 are isolated** from P1/P5/P6 (Jaccard = 0.00): the two modes don't overlap at all.
- **P4 is the centroid of the typology group** — average similarity 0.667 with the other sub-national-typology papers.

Hierarchical clustering (average linkage on Jaccard distance) at k=3:

| cluster | papers | shared signature | archetype name |
|---|---|---|---|
| 1 | **P1, P5, P6** | (0,0,1,1,0) — typed + relational, no finer | **CONFIGURATION** |
| 2 | **P2, P3, P4** | (1,0,*,*,0) — finer + typed and/or relational | **SUB-NATIONAL CLASSIFICATION** |
| 3 | **P7, P8** | (1,1,0,*,1) — finer + downstream + mediator | **CHANNEL** |

At k=2, the program splits cleanly into **{P7, P8} vs {everything else}** — the channel-mode papers are far more distinct from the rest than the rest are from each other. The single most informative bisection of the corpus is "channel-mode papers" vs "typology/configuration papers."

---

## 4. Rarity-weighted novelty per paper

For each paper, score = Σ (inverse frequency of each pivot used). This is essentially TF-IDF for pivots — high score = uses pivot dimensions that are rare in the corpus = doing something distinctive.

Inverse-frequency weights:
- (a) finer = 1.60 · (b) downstream = **4.00** · (c) typed = 1.60 · (d) relational = 1.33 · (e) mediator = **4.00**

Ranked novelty scores:

| paper | rarity-weighted score | which rare pivots used |
|---|:---:|---|
| **P8 Compound-crisis coupling** | **10.93** | both rare (b + e) |
| **P7 SDP / homelessness** | **9.60** | both rare (b + e) |
| P4 Conflict typology | 4.53 | none (just more pivots) |
| P2 Disaster regimes | 3.20 | none |
| P1 Exec aggrandizement | 2.93 | none |
| P3 Strife epicenter | 2.93 | none |
| P5 Democratic resilience | 2.93 | none |
| P6 Methodology | 2.93 | none |

The separation is stark: **P7 and P8 score >9; everything else clusters at ~3** — a 3× gap between channel-mode and typology-mode papers.

The reason: both rare pivots (b downstream, e mediator) are weighted 4.00 each, vs 1.33–1.60 for the common pivots. Using *one* rare pivot is worth more than three common ones; using *both* (P7 and P8) doubles that advantage.

**This is what the visual "color" was**: when you look at the pivot matrix, P7 and P8 *look* different because their ✓s land on columns that are mostly empty elsewhere. The eye reads rarity. The TF-IDF score names it.

---

## 5. The colors named

| color (visual reading) | quantification | interpretation |
|---|---|---|
| "P1, P5, P6 look identical" | Jaccard sim = 1.000; identical (0,0,1,1,0) vectors | the CONFIGURATION archetype — three independent papers, one analytical mode |
| "P7 and P8 stand apart" | k=2 clustering splits {P7,P8} vs rest; novelty score 9.6 / 10.93 vs ~3 | CHANNEL archetype; the program's two mechanism-via-mediator papers |
| "The two columns at the right are mostly empty" | (b) and (e) at 2/8 frequency; perfect MI(b,e)=0.811 | rare pivots that always travel together |
| "P2/P3/P4 share something but aren't the same" | finer-resolution column ✓ for all 3, varying (c)/(d) | SUB-NATIONAL CLASSIFICATION archetype (variations on a theme) |
| "Some cells never light up together" | MI(b,c) = MI(c,e) = 0.467 from zero co-occurrence | TYPED and CHANNEL modes are mutually exclusive in the corpus |

---

## 6. The deeper structural finding — *two modes, three archetypes*

The quantification surfaces a structural property of the IDP program that wasn't visible in any single paper:

### The two modes (mutually exclusive)
- **TYPED mode** (c often with d, sometimes with a): builds a typology, classifies entities, characterizes structure.
- **CHANNEL mode** (b + e always together, with a): finds the downstream funnel through which distinct upstream causes converge to a shared outcome.

These two modes are not just different methodological choices — they are **statistically antagonistic across the corpus** (MI evidence: zero co-occurrence). A paper choosing one excludes the other.

### The three archetypes (paper-level clusters)
- **CONFIGURATION** (P1, P5, P6): TYPED mode without sub-national resolution. Classifies system *configurations* (lever patterns, residue classes when generalized).
- **SUB-NATIONAL CLASSIFICATION** (P2, P3, P4): TYPED mode plus sub-national / structural relational refinement. Classifies entities at finer resolution.
- **CHANNEL** (P7, P8): CHANNEL mode — distinct upstream causes → shared mediator → outcome. Distinctive use of rare pivots; high TF-IDF novelty.

### What this implies
**The CHANNEL archetype is where the program's most novel mechanism findings live** — and it's also where the rarest pivots are. P7's rent funnel and P8's destination convergence are the program's two genuinely novel mechanistic stories; the other six papers are *characterizations* (typologies, configurations, recovery axes). This is not a criticism of the characterization papers — typologies are foundational; P6 (Stan validation) is what makes the typological work irreducible. But the empirical signature is clear: **distinctive mechanism findings show up where rare pivots are deployed.**

The strongest manuscript-framing implication: if a future paper aims for novel mechanism rather than refined typology, **the right move is to deploy the rare pivot pair (b + e)** — find the downstream channel where distinct upstream causes converge. That move predicts P7- and P8-style breakthroughs.

---

## 7. Synthesis — what's quantified

1. **Pivot frequency is bimodal** — 5/8 or 6/8 vs 2/8, nothing in between. The corpus has "common pivots" and "rare pivots" with a frequency gap.
2. **Two rare pivots are perfectly correlated** — downstream and mediator are effectively one pivot, factored into direction (downstream) and unit (mediator/destination channel). MI = 0.811, maximum possible at their marginal frequency.
3. **TYPED and CHANNEL modes are mutually exclusive** — zero co-occurrence; high MI by exclusion. The program operates in *one or the other*, never both within a single paper.
4. **Three paper archetypes emerge from clustering** — CONFIGURATION (P1/P5/P6, identical vectors), SUB-NATIONAL CLASSIFICATION (P2/P3/P4), CHANNEL (P7/P8). The k=2 split isolates CHANNEL from everything else.
5. **Rarity-weighted novelty isolates P7 and P8 by 3×** — 9.60 and 10.93 vs the ~2.93–4.53 cluster. The visual "colors" in the matrix are TF-IDF.
6. **Novel mechanism findings cluster in CHANNEL mode** — rent funnel, destination convergence. This is not a coincidence; it is a structural feature of the corpus.

**Refined meta-claim from this quantification**: *the IDP program operates in two mutually exclusive epistemic modes (TYPED and CHANNEL), produces three paper archetypes (CONFIGURATION, SUB-NATIONAL CLASSIFICATION, CHANNEL), and the rarest pivot pair (downstream + mediator) is precisely where the program's most novel mechanism findings live.* This is a quantified version of "the colors" — and it suggests that future analytical effort aimed at novel mechanism (rather than refined typology) should specifically deploy the CHANNEL-mode pivots.
