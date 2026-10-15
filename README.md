# content-classification-system
Data and tools about content (ZIMs) classification

This is a WIP effort to develop a standard, datasets, procedures and tools regarding the classsification of ZIMs.

Late 2024 @doubletkovacs delivered a [foundational document](./KCCS-Jan2025.md) laying-out this effort. This is going to be transformed into an globaly approved standard at organization level (some wording or practices might change), and then datasets, procedures and tools.

# ZIM Classification v1

As a first step, we have agreed on a simplified taxonomy (v1) of 17 flat categories, built from the actual content of the Kiwix catalog. It is deliberately smaller than the foundational document so that it can be applied to the whole catalog right away and refined later.

## Terminology

What the foundational document calls a *classification tag* is what we name a **category**, and we keep using this word.

## Categories vs content source

So far, the single `category` of a ZIM in the catalog (e.g. `wikipedia`, `wiktionary`, `stack_exchange`, `gutenberg`, `phet`, ...) described where the content comes from, not what it is about. This information is not a category anymore: it belongs to the `Source` ZIM metadata (exact format still to be specified), and readers should make it available to users searching for a ZIM (e.g. as a filter alongside categories).

Categories, as defined below, describe the subject, audience or format of the content, and a ZIM can now have more than one.

## Categories

| Identifier | Label |
|---|---|
| `for-children` | For Children |
| `encyclopedias-general-reference` | Encyclopedias & General Reference |
| `languages-dictionaries` | Languages & Dictionaries |
| `books-literature` | Books & Literature |
| `school-courses` | School & Courses |
| `science-mathematics` | Science & Mathematics |
| `computers-technology` | Computers & Technology |
| `health-medicine` | Health & Medicine |
| `history` | History |
| `geography-maps-travel` | Geography, Maps & Travel |
| `society-politics-economy` | Society, Politics & Economy |
| `religion-philosophy` | Religion & Philosophy |
| `arts-music-film` | Arts, Music & Film |
| `games-fandom-humor` | Games, Fandom & Humor |
| `sports-outdoors` | Sports & Outdoors |
| `home-food-diy` | Home, Food & DIY |
| `survival-preparedness` | Survival & Preparedness |

The source of this list is [`zim-taxonomy/rules.py`](./zim-taxonomy/rules.py) (`TAXONOMY`).

## Classification rules

We aim for **one category per ZIM**. A second category is tolerated when required (see rules below). Three or more categories are discouraged and must be clearly justified.

1. Pick the **subject** of the ZIM. *Encyclopedias & General Reference* is only for content spanning all topics.
2. If the content is a **learning path** (textbook, course, lessons, exercises, exam prep), add *School & Courses*. Multi-subject curricula get *School & Courses* alone.
3. If the content is **made for kids**, add *For Children* as second category, never a third: children's school material is *For Children* + *School & Courses*, without its subject.
4. Otherwise add a second category only when the content **truly** belongs to both (e.g. Gutenberg history books: *Books & Literature* + *History*).

ZIMs are grouped into **families**: a family is a ZIM name with its language code replaced by `*` (e.g. `wikipedia_en_chemistry`, `wikipedia_fr_chemistry`, ... all belong to the `wikipedia_*_chemistry` family). Every ZIM of a given family is expected to have the same category(ies), whatever its language (and flavour).

## Identifiers

- Each category is identified by a stable HTTP URI: `https://id.openzim.org/categories/<slug>`, e.g. `https://id.openzim.org/categories/health-medicine`.
- The slug is semantic (the identifiers in the table above), with no number or language embedded, and is never changed once published. Labels may evolve and be translated, identifiers do not.
- OIDs have been considered and abandoned: too much friction for a use case that's mainly meant to be consulted outside the organization, without a real need for strict protocol-level interoperability.

## Taxonomy modeling

- Categories are stored in **SKOS** ([W3C reference](https://www.w3.org/TR/skos-reference/), [Wikipedia](https://en.wikipedia.org/wiki/Simple_Knowledge_Organization_System)), a standard designed to represent classifications, thesauri, and controlled vocabularies (concepts, hierarchical relations, multilingual labels).
- Each category is a `skos:Concept` of a single `skos:ConceptScheme`, with its translations as `skos:prefLabel` (one per language) and optionally `skos:definition` / `skos:scopeNote` to help editors.
- The SKOS file is the taxonomy's source of truth (including multilingual labels). It is published at `https://id.openzim.org/categories/` in Turtle, JSON-LD and HTML (human-readable).
- v1 is flat: all categories are top concepts. Future versions may introduce relations between categories (`skos:broader` / `skos:narrower` / `skos:related`), and polyhierarchy is embraced: a concept may have several parents (e.g. "Medical & Health Technologies" attached to both "Applied Sciences" and "Medical Knowledge") instead of being forced into a single branch.
- Positional numbering (1.1, 1.2, 1.2.1...) is not used: once a concept can have several parents, a single positional number no longer makes sense, and would give a false impression of strict hierarchy. Neighborhood and hierarchy are carried solely by SKOS relations.

Example:

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix cat:  <https://id.openzim.org/categories/> .

cat:health-medicine a skos:Concept ;
    skos:inScheme cat: ;
    skos:topConceptOf cat: ;
    skos:prefLabel "Health & Medicine"@en, "Santé & Médecine"@fr .
```

# Tooling

The [`zim-taxonomy`](./zim-taxonomy) folder contains the scripts used to build v1 and the initial classification of the catalog. Scripts are run from within that folder:

| File | Purpose |
|---|---|
| `catalog.xml` | Snapshot of the Kiwix OPDS catalog used as input |
| `parse.py` | Extracts catalog entries into `entries.csv` |
| `rules.py` | Taxonomy definition and classification rules (by family, series or site) |
| `classify.py` | Applies the rules, writes `classified.csv` and prints per-category stats and unclassified ZIMs |
| `report.py` | Prints, per category, the families assigned (used to produce `report.md`) |
| `build_page.py` | Builds `taxonomy.html`, a review page for editors, from `classified.csv` and `page_template.html` |

```sh
cd zim-taxonomy
python3 parse.py
python3 classify.py
python3 report.py > report.md
python3 build_page.py
```
