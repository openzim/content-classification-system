"""Build the SKOS taxonomy (Turtle, JSON-LD, HTML) to publish at https://id.openzim.org/.

Reads categories.json and i18n/*.json, writes to the output directory (default: dist):

    categories/index.{ttl,jsonld,html}          the concept scheme, with all categories
    categories/<id>/index.{ttl,jsonld,html}     one category
"""
import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
SKOS = "http://www.w3.org/2004/02/skos/core#"


def load():
    ref = json.loads((HERE / "categories.json").read_text())
    messages = {}
    for f in sorted((HERE / "i18n").glob("*.json")):
        if f.stem == "qqq":
            continue
        messages[f.stem] = {k: v for k, v in json.loads(f.read_text()).items() if k != "@metadata"}
    scheme = ref["scheme"]

    def labels(key):
        # English first, then other languages alphabetically
        langs = sorted(messages, key=lambda lang: (lang != "en", lang))
        return {lang: messages[lang][key] for lang in langs if messages[lang].get(key)}

    for c in ref["categories"]:
        if not messages["en"].get(f"category-{c['id']}"):
            raise SystemExit(f"missing English label for {c['id']}")
    concepts = [{"id": c["id"], "uri": scheme + c["id"], "labels": labels(f"category-{c['id']}")}
                for c in ref["categories"]]
    return {"uri": scheme, "labels": labels("scheme-label"), "concepts": concepts}


def ttl_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def ttl_labels(labels):
    return ", ".join(f"{ttl_str(v)}@{k}" for k, v in labels.items())


def ttl_concept(scheme, c):
    return (f"<{c['uri']}> a skos:Concept ;\n"
            f"    skos:inScheme <{scheme['uri']}> ;\n"
            f"    skos:topConceptOf <{scheme['uri']}> ;\n"
            f"    skos:prefLabel {ttl_labels(c['labels'])} .\n")


def ttl(scheme, concepts, with_scheme):
    out = [f"@prefix skos: <{SKOS}> .\n"]
    if with_scheme:
        top = ",\n        ".join(f"<{c['uri']}>" for c in concepts)
        out.append(f"<{scheme['uri']}> a skos:ConceptScheme ;\n"
                   f"    skos:prefLabel {ttl_labels(scheme['labels'])} ;\n"
                   f"    skos:hasTopConcept {top} .\n")
    out += [ttl_concept(scheme, c) for c in concepts]
    return "\n".join(out)


def jsonld(scheme, concepts, with_scheme):
    graph = []
    if with_scheme:
        graph.append({"@id": scheme["uri"], "@type": "skos:ConceptScheme",
                      "skos:prefLabel": scheme["labels"],
                      "skos:hasTopConcept": [{"@id": c["uri"]} for c in concepts]})
    graph += [{"@id": c["uri"], "@type": "skos:Concept",
               "skos:inScheme": {"@id": scheme["uri"]},
               "skos:topConceptOf": {"@id": scheme["uri"]},
               "skos:prefLabel": c["labels"]} for c in concepts]
    doc = {"@context": {"skos": SKOS,
                        "skos:prefLabel": {"@container": "@language"}},
           "@graph": graph}
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="alternate" type="text/turtle" href="{path}index.ttl">
<link rel="alternate" type="application/ld+json" href="{path}index.jsonld">
<style>
body {{ font-family: system-ui, sans-serif; max-width: 50rem; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ text-align: left; padding: .3rem .6rem; border-bottom: 1px solid #ddd; vertical-align: top; }}
code {{ font-size: .9em; }}
</style>
</head>
<body>
{body}
<p>Also available as Turtle and JSON-LD: request <code>{uri}</code> with an <code>Accept</code> header of <code>text/turtle</code> or <code>application/ld+json</code>.
Direct links (<a href="{path}index.ttl">Turtle</a>, <a href="{path}index.jsonld">JSON-LD</a>) are provided for convenience only and may change: always use the URI above with content negotiation.</p>
</body>
</html>
"""


def path(uri):
    # links are relative to the site root, so that pages work whatever the host and with or without trailing /
    return urlparse(uri).path


def folder(uri):
    return path(uri).rstrip("/") + "/"


def html_scheme(scheme):
    e = html.escape
    rows = "".join(f'<tr><td><a href="{e(path(c["uri"]))}">{e(c["labels"]["en"])}</a></td>'
                   f'<td><code>{e(c["uri"])}</code></td><td>{len(c["labels"])}</td></tr>\n'
                   for c in scheme["concepts"])
    title = scheme["labels"]["en"]
    body = (f"<h1>{e(title)}</h1>\n<p><code>{e(scheme['uri'])}</code></p>\n"
            f"<table>\n<tr><th>Category</th><th>Identifier</th><th>Languages</th></tr>\n{rows}</table>")
    return PAGE.format(title=e(title), body=body, path=e(folder(scheme["uri"])), uri=e(scheme["uri"]))


def html_concept(scheme, c):
    e = html.escape
    rows = "".join(f'<tr><td><code>{e(k)}</code></td><td lang="{e(k)}">{e(v)}</td></tr>\n'
                   for k, v in c["labels"].items())
    body = (f"<h1>{e(c['labels']['en'])}</h1>\n<p><code>{e(c['uri'])}</code></p>\n"
            f'<p>Category of <a href="{e(path(scheme["uri"]))}">{e(scheme["labels"]["en"])}</a></p>\n'
            f"<table>\n<tr><th>Language</th><th>Label</th></tr>\n{rows}</table>")
    return PAGE.format(title=e(c["labels"]["en"]), body=body, path=e(folder(c["uri"])), uri=e(c["uri"]))


def write(folder, ttl_text, jsonld_text, html_text):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.ttl").write_text(ttl_text)
    (folder / "index.jsonld").write_text(jsonld_text)
    (folder / "index.html").write_text(html_text)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args()
    scheme = load()
    root = args.output / "categories"
    concepts = scheme["concepts"]
    write(root, ttl(scheme, concepts, True), jsonld(scheme, concepts, True), html_scheme(scheme))
    for c in concepts:
        write(root / c["id"], ttl(scheme, [c], False), jsonld(scheme, [c], False), html_concept(scheme, c))
    print(f"wrote {len(scheme['concepts'])} categories to {root}")


if __name__ == "__main__":
    main()
