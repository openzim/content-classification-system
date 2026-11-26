"""Build the taxonomy (JSON-LD, HTML) to publish at https://id.openzim.org/.

Categories are modeled with a hybrid of schema.org (data and metadata, including illustrations)
and SKOS (relations between categories), serialized as JSON-LD, with a shared external context.

Reads categories.json and i18n/*.json, writes to the output directory (default: dist):

    categories/context.jsonld                the shared JSON-LD context
    categories/index.{jsonld,html}           the concept scheme, with all categories
    categories/<id>/index.{jsonld,html}      one category
    images/<file>                            category illustrations (copied from categories/images)
"""
import argparse
import html
import json
import shutil
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
SCHEMA = "http://schema.org/"
SKOS = "http://www.w3.org/2004/02/skos/core#"
OPENZIM = "https://id.openzim.org/vocab#"
IMAGE_BASE = "https://id.openzim.org/images/"
IMAGE_LICENSE = "https://creativecommons.org/licenses/by-sa/4.0/"
CONTEXT_URL = "https://id.openzim.org/categories/context.jsonld"
ENCODING_FORMATS = {".png": "image/png", ".svg": "image/svg+xml", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}

# @vocab covers schema.org terms (name, description, image, termCode, inDefinedTermSet, ImageObject,
# contentUrl, encodingFormat, caption, license, ...); SKOS relations are mapped explicitly as @id-valued.
# `scale` (device pixel ratio) has no schema.org equivalent, so it's minted under our own `openzim:` namespace
# instead of silently falling through to a non-existent schema.org term.
CONTEXT = {
    "@vocab": SCHEMA,
    "skos": SKOS,
    "openzim": OPENZIM,
    "scale": "openzim:scale",
    "broader": {"@id": "skos:broader", "@type": "@id"},
    "narrower": {"@id": "skos:narrower", "@type": "@id"},
    "related": {"@id": "skos:related", "@type": "@id"},
    "inScheme": {"@id": "skos:inScheme", "@type": "@id"},
    "topConceptOf": {"@id": "skos:topConceptOf", "@type": "@id"},
    "hasTopConcept": {"@id": "skos:hasTopConcept", "@type": "@id"},
    "inDefinedTermSet": {"@type": "@id"},
    "contentUrl": {"@type": "@id"},
    "license": {"@type": "@id"},
}


def load():
    ref = json.loads((HERE / "categories.json").read_text())
    messages = {}
    for f in sorted((HERE / "i18n").glob("*.json")):
        if f.stem == "qqq":
            continue
        messages[f.stem] = {k: v for k, v in json.loads(f.read_text()).items() if k != "@metadata"}
    scheme = ref["scheme"]

    def lang_values(key):
        # English first, then other languages alphabetically
        langs = sorted(messages, key=lambda lang: (lang != "en", lang))
        return [{"@value": messages[lang][key], "@language": lang} for lang in langs if messages[lang].get(key)]

    for c in ref["categories"]:
        if not messages["en"].get(f"category-{c['id']}"):
            raise SystemExit(f"missing English label for {c['id']}")

    def image_objects(c, label):
        objects = []
        for img in c.get("images", []):
            url = IMAGE_BASE + img["file"]
            ext = Path(img["file"]).suffix
            if ext not in ENCODING_FORMATS:
                raise SystemExit(f"unknown image format for {img['file']}")
            objects.append({
                "@id": url,
                "@type": "ImageObject",
                "contentUrl": url,
                "encodingFormat": ENCODING_FORMATS[ext],
                "width": img["width"],
                "height": img["height"],
                "scale": img["scale"],
                "caption": [{"@value": f"{label} category icon", "@language": "en"}],
                "license": IMAGE_LICENSE,
            })
        return objects

    concepts = []
    for c in ref["categories"]:
        label = messages["en"][f"category-{c['id']}"]
        concepts.append({"id": c["id"], "uri": scheme + c["id"],
                          "names": lang_values(f"category-{c['id']}"),
                          "images": image_objects(c, label)})
    return {"uri": scheme, "names": lang_values("scheme-label"), "concepts": concepts}


def node_concept(scheme, c):
    node = {
        "@id": c["uri"],
        "@type": ["CategoryCode", "skos:Concept"],
        "termCode": c["id"],
        "name": c["names"],
        "inDefinedTermSet": scheme["uri"],
        "inScheme": scheme["uri"],
        "topConceptOf": scheme["uri"],
    }
    if c["images"]:
        node["image"] = c["images"]
    return node


def node_scheme(scheme, concepts):
    return {
        "@id": scheme["uri"],
        "@type": ["CategoryCodeSet", "skos:ConceptScheme"],
        "name": scheme["names"],
        "hasTopConcept": [c["uri"] for c in concepts],
    }


def jsonld(scheme, concepts, with_scheme):
    graph = ([node_scheme(scheme, concepts)] if with_scheme else []) + [node_concept(scheme, c) for c in concepts]
    doc = {"@context": CONTEXT_URL, "@graph": graph}
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def context_jsonld():
    return json.dumps({"@context": CONTEXT}, indent=2, ensure_ascii=False) + "\n"


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="alternate" type="application/ld+json" href="{path}index.jsonld">
<link rel="http://www.w3.org/ns/json-ld#context" type="application/ld+json" href="{context}">
<style>
body {{ font-family: system-ui, sans-serif; max-width: 50rem; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ text-align: left; padding: .3rem .6rem; border-bottom: 1px solid #ddd; vertical-align: top; }}
code {{ font-size: .9em; }}
img.icon {{ width: 1.5em; height: 1.5em; vertical-align: middle; }}
</style>
</head>
<body>
{body}
<p>Also available as JSON-LD: request <code>{uri}</code> with an <code>Accept</code> header of <code>application/ld+json</code>.
Direct link (<a href="{path}index.jsonld">JSON-LD</a>) is provided for convenience only and may change: always use the URI above with content negotiation.
All JSON-LD files share the context at <a href="{context}">{context}</a>.</p>
</body>
</html>
"""


def path(uri):
    # links are relative to the site root, so that pages work whatever the host and with or without trailing /
    return urlparse(uri).path


def identifier(uri):
    # identifiers are displayed as stored in ZIMs, without the https:// scheme
    return uri.removeprefix("https://")


def folder(uri):
    return path(uri).rstrip("/") + "/"


def label_en(names):
    return next(n["@value"] for n in names if n["@language"] == "en")


def icon_img(c):
    if not c["images"]:
        return ""
    base = next((img for img in c["images"] if img["scale"] == 1), c["images"][0])
    srcset = ", ".join(f'{path(img["contentUrl"])} {img["scale"]}x' for img in c["images"])
    return (f'<img class="icon" src="{html.escape(path(base["contentUrl"]))}" '
            f'srcset="{html.escape(srcset)}" alt="">')


def html_scheme(scheme):
    e = html.escape
    rows = "".join(f'<tr><td>{icon_img(c)}</td><td><a href="{e(path(c["uri"]))}">{e(label_en(c["names"]))}</a></td>'
                   f'<td><code>{e(identifier(c["uri"]))}</code></td><td>{len(c["names"])}</td></tr>\n'
                   for c in scheme["concepts"])
    title = label_en(scheme["names"])
    body = (f"<h1>{e(title)}</h1>\n<p><code>{e(identifier(scheme['uri']))}</code></p>\n"
            f"<table>\n<tr><th></th><th>Category</th><th>Identifier</th><th>Languages</th></tr>\n{rows}</table>")
    return PAGE.format(title=e(title), body=body, path=e(folder(scheme["uri"])), uri=e(scheme["uri"]),
                        context=e(CONTEXT_URL))


def html_concept(scheme, c):
    e = html.escape
    rows = "".join(f'<tr><td><code>{e(n["@language"])}</code></td><td lang="{e(n["@language"])}">{e(n["@value"])}</td></tr>\n'
                   for n in c["names"])
    title = label_en(c["names"])
    body = (f"<h1>{icon_img(c)} {e(title)}</h1>\n"
            f"<p>Identifier: <code>{e(identifier(c['uri']))}</code><br>\n"
            f"ZIM tag: <code>_category:{e(identifier(c['uri']))}</code></p>\n"
            f'<p>Category of <a href="{e(path(scheme["uri"]))}">{e(label_en(scheme["names"]))}</a></p>\n'
            f"<table>\n<tr><th>Language</th><th>Label</th></tr>\n{rows}</table>")
    return PAGE.format(title=e(title), body=body, path=e(folder(c["uri"])), uri=e(c["uri"]),
                        context=e(CONTEXT_URL))


def write(folder, jsonld_text, html_text):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.jsonld").write_text(jsonld_text)
    (folder / "index.html").write_text(html_text)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args()
    scheme = load()
    root = args.output / "categories"
    concepts = scheme["concepts"]
    (root).mkdir(parents=True, exist_ok=True)
    (root / "context.jsonld").write_text(context_jsonld())
    write(root, jsonld(scheme, concepts, True), html_scheme(scheme))
    for c in concepts:
        write(root / c["id"], jsonld(scheme, [c], False), html_concept(scheme, c))

    images_dir = args.output / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    for f in sorted((HERE / "images").glob("*")):
        shutil.copyfile(f, images_dir / f.name)

    print(f"wrote {len(scheme['concepts'])} categories to {root}")


if __name__ == "__main__":
    main()
