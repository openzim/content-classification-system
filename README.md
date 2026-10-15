# content-classification-system
Data and tools about content (ZIMs) classification

This is a WIP effort to develop a standard, datasets, procedures and tools regarding the classsification of ZIMs.

Late 2024 @doubletkovacs delivered a [foundational document](./KCCS-Jan2025.md) laying-out this effort. This is going to be transformed into an globaly approved standard at organization level (some wording or practices might change), and then datasets, procedures and tools.

# ZIM Classification v1

As a first step, we have agreed on a simplified taxonomy (v1) of 18 flat categories, built from the actual content of the Kiwix catalog. It is deliberately smaller than the foundational document so that it can be applied to the whole catalog right away and refined later.

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
| `other` | Other |

The source of this list is the [reference data](#reference-data-and-translations).

## Classification rules

We aim for **one category per ZIM**. A second category is tolerated when required (see rules below). Three or more categories are discouraged and must be clearly justified.

1. Pick the **subject** of the ZIM. *Encyclopedias & General Reference* is only for content spanning all topics.
2. If the content is a **learning path** (textbook, course, lessons, exercises, exam prep), add *School & Courses*. Multi-subject curricula get *School & Courses* alone.
3. If the content is **made for kids**, add *For Children* as second category, never a third: children's school material is *For Children* + *School & Courses*, without its subject.
4. Otherwise add a second category only when the content **truly** belongs to both (e.g. Gutenberg history books: *Books & Literature* + *History*).
5. *Other* is only for ZIMs which really fit no other category, and is never combined with another category. It should stay exceptional: many ZIMs in *Other* is a sign that the taxonomy needs a new category.

ZIMs are grouped into **families**: a family is a ZIM name with its language code replaced by `*` (e.g. `wikipedia_en_chemistry`, `wikipedia_fr_chemistry`, ... all belong to the `wikipedia_*_chemistry` family). Every ZIM of a given family is expected to have the same category(ies), whatever its language (and flavour).

## Identifiers

- Each category is identified by a stable HTTP URI: `https://id.openzim.org/categories/<slug>`, e.g. `https://id.openzim.org/categories/health-medicine`.
- The slug is semantic (the identifiers in the table above), with no number or language embedded, and is never changed once published. Labels may evolve and be translated, identifiers do not.
- OIDs have been considered and abandoned: too much friction for a use case that's mainly meant to be consulted outside the organization, without a real need for strict protocol-level interoperability.

## Storing categories in ZIMs

- Categories are stored in the `Tags` ZIM metadata, using the special `_category` tag (see [openZIM Tags](https://wiki.openzim.org/wiki/Tags)) with the category URI **without its `https://` scheme** as value, e.g. `_category:id.openzim.org/categories/health-medicine`. The canonical identifier is obtained by prepending `https://`.
- The scheme is dropped so that the value contains no `:`, which some readers and tools use to split special tags.
- When a ZIM has several categories, the `_category` tag is repeated, e.g. `_category:id.openzim.org/categories/science-mathematics;_category:id.openzim.org/categories/school-courses`.
- Using the host and path (rather than the bare slug or a label) keeps the value stable across time and unambiguous: an old ZIM can always be resolved to its category, and translated labels are obtained from the SKOS taxonomy.
- Existing ZIMs use `_category` for their content source (e.g. `_category:wikipedia`, see [Categories vs content source](#categories-vs-content-source)). Any `_category` value that does not start with `id.openzim.org/categories/` is such a legacy value and must not be interpreted as a category.
- Transition: current readers only consider the first `_category` tag, and rely on its legacy value. Until readers are updated, ZIMs should keep their legacy `_category` value first, followed by their categories, e.g. `_category:wikipedia;_category:id.openzim.org/categories/encyclopedias-general-reference`.
- Informal / community tags (as described in the foundational document) are not part of this classification system: regular (non-special) ZIM tags already allow this.

## Transition in readers

Readers have to keep supporting old ZIMs, which have no category but a legacy `_category` value (see [Storing categories in ZIMs](#storing-categories-in-zims)):

- The categories of a ZIM are all its `_category` values starting with `id.openzim.org/categories/`. Other `_category` values are ignored for classification.
- A ZIM without any category (old ZIM, third-party ZIM, ZIM not classified yet) is displayed under *Other*, like ZIMs explicitly classified as *Other*. Readers therefore always have an *Other* category.
- Category labels are taken from the SKOS taxonomy, in the user's language, so *Other* is translated like any other category.

### Option to study: categories provided by the catalog

With the rules above, once readers are updated, every old ZIM ends up in *Other*, since it has no category in its metadata. This would be the case for most of the library for a long time, since ZIMs are not all re-created frequently.

Since classification is done per family, categories are known for old ZIMs as well (see [`classified.csv`](./zim-taxonomy/classified.csv)). The catalog (library.kiwix.org) could therefore provide categories for every ZIM it lists, whatever the content of the ZIM metadata, and readers would use them, at least when the ZIM has no category of its own.

Points to study:

- How categories are exposed in the catalog (OPDS `<category>` elements, `library.xml`) and maintained (where the family ↔ categories mapping lives and who updates it).
- Precedence when both are available: categories from the ZIM, from the catalog, or the catalog only as a fallback.
- Readers using ZIMs which are not (or no longer) in the catalog, e.g. ZIMs side-loaded or kept offline, which would still fall into *Other*.

## Taxonomy modeling

- Categories are stored in **SKOS** ([W3C reference](https://www.w3.org/TR/skos-reference/), [Wikipedia](https://en.wikipedia.org/wiki/Simple_Knowledge_Organization_System)), a standard designed to represent classifications, thesauri, and controlled vocabularies (concepts, hierarchical relations, multilingual labels).
- Each category is a `skos:Concept` of a single `skos:ConceptScheme`, with its translations as `skos:prefLabel` (one per language) and optionally `skos:definition` / `skos:scopeNote` to help editors.
- The SKOS files are generated from the [reference data](#reference-data-and-translations), which is the taxonomy's source of truth (including multilingual labels), and [published](#publication) at `https://id.openzim.org/categories/` in Turtle, JSON-LD and HTML (human-readable).
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

## Reference data and translations

The [`categories`](./categories) folder holds the reference data:

- [`categories.json`](./categories/categories.json): the concept scheme URI and the ordered list of category identifiers. Future non-translatable data (e.g. relations between categories) belongs here.
- [`i18n/en.json`](./categories/i18n/en.json): English labels, in the [banana](https://github.com/wikimedia/banana-i18n) JSON format used by other Kiwix projects, with keys `scheme-label` and `category-<id>`.
- [`i18n/qqq.json`](./categories/i18n/qqq.json): documentation of each message for translators, with examples of content in each category.
- `i18n/<lang>.json`: translations, contributed through [TranslateWiki](https://translatewiki.net/) like for other Kiwix projects. They must not be edited by hand in this repository.

Adding a category means adding its identifier to `categories.json`, and its English label and translator documentation to `en.json` and `qqq.json`. Identifiers are never changed nor removed once published.

TranslateWiki setup: the project has to be registered on translatewiki.net (as other Kiwix projects are), pointing to `categories/i18n/` with `en.json` as source language and `qqq.json` as message documentation. TranslateWiki then regularly commits translations to this repository.

## Publication

[`categories/build.py`](./categories/build.py) generates the files to publish at `https://id.openzim.org/` from the reference data, in a `dist` folder:

```
dist/categories/index.{ttl,jsonld,html}        concept scheme, with all categories
dist/categories/<id>/index.{ttl,jsonld,html}   one category
```

```sh
python3 categories/build.py --output dist
```

The web server should serve these files so that each URI (e.g. `https://id.openzim.org/categories/health-medicine`) returns HTML by default, and Turtle or JSON-LD when requested through the `Accept` header (`text/turtle`, `application/ld+json`). Each format is also directly reachable (e.g. `https://id.openzim.org/categories/health-medicine/index.ttl`).

# Tooling

See [Reference data and translations](#reference-data-and-translations) and [Publication](#publication) for the `categories` folder.

The [`zim-taxonomy`](./zim-taxonomy) folder contains the scripts used to build v1 and the initial classification of the catalog. Scripts are run from within that folder:

| File | Purpose |
|---|---|
| `catalog.xml` | Snapshot of the Kiwix OPDS catalog used as input |
| `parse.py` | Extracts catalog entries into `entries.csv` |
| `rules.py` | Classification rules (by family, series or site), categories are loaded from the reference data |
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
