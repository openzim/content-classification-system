# content-classification-system
Data and tools about content (ZIMs) classification

This is a WIP effort to develop a standard, datasets, procedures and tools regarding the classsification of ZIMs.

Late 2024 @doubletkovacs delivered a [foundational document](./KCCS-Jan2025.md) laying-out this effort. This is going to be transformed into an globaly approved standard at organization level (some wording or practices might change), and then datasets, procedures and tools.

# ZIM Classification

## 1. Identifiers

- Chosen approach: stable HTTP URIs under a prefix we own, e.g. `https://id.yourorg.org/<slug>`.
- The slug is semantic (e.g. `medical-health-technologies`), with no number or language embedded, and is never changed once published.
- Other alternatives abandonned:
    - No OIDs: too much friction for a use case that's mainly meant to be consulted outside the organization, without a real need for strict protocol-level interoperability.

## 2. Taxonomy modeling

- Goal: document the taxonomy, i.e. relations between our categories
- Format: **SKOS** ([W3C reference](https://www.w3.org/TR/skos-reference/), [Wikipedia](https://en.wikipedia.org/wiki/Simple_Knowledge_Organization_System)), a standard designed to represent classifications, thesauri, and controlled vocabularies (concepts, hierarchical relations, multilingual labels).
- Polyhierarchy is embraced: a concept can have several parents (e.g. "Medical & Health Technologies" attached to both "Applied Sciences" and "Medical Knowledge") instead of being forced into a single branch.
- Publication: Taxonomy is published as Turtle/JSON-LD, this is the taxonomy's source of truth (includes multilingual labels).
- Numbering (1.1, 1.2, 1.2.1...) is dropped entirely, not just demoted to metadata: once a concept can have several parents, a single positional number no longer makes sense (it would need one number per parent relation, i.e. several numbers for the same concept). Keeping it would give a false impression of strict hierarchy to anyone consulting it. Neighborhood and hierarchy are therefore carried solely by SKOS relations (`broader`/`narrower`/`related`), not by a parallel numbering system.

## 3. Storage and querying

- No need for a complex querying mechanism like a triplestore: at our scale (3-20k ZIMs, ~150 concepts), a standard relational database (Postgres) is more than sufficient.
- A precomputed hierarchical closure table ("all ancestors of each concept") greatly simplifies filtering queries (e.g. "all ZIMs under Technology, including its subcategories").

## 4. Distribution to readers (C++, JS, etc.)

- No need for a shared cross-platform library: the required queries are simple enough to be documented as a common reference and reimplemented natively by each team.
- **OPDS** remains our single protocol for catalog distribution/discovery. Each entry exposes its categories (URI + label) via the standard `<category>` element.
- The full taxonomy (concepts + hierarchy) can be distributed separately, as a lightweight, optional file — useful only to readers that want a rich hierarchical navigation UI.

## 5. Two ways of consuming the catalog, both to be supported

- **"Local sync" readers**: fetch the full feed (and optionally the taxonomy), then filter locally. No behavioral difference between online and offline modes.
- **"On-demand" readers**: query the server on every user action, with no local copy. The OPDS server therefore needs to keep supporting filtering by category (including subcategories), without necessarily requiring a full faceted system with counts for now.

## 6. Open questions for later

- Precise specification of the category filtering parameter in OPDS (whether subcategories are included by default, handling multiple categories, pagination).
- Facets and counts on the OPDS server side, if usage justifies it.
