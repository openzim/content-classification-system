"""Build taxonomy.html (review page for editors) from classified.csv and rules.py."""
import csv, json, html
from collections import defaultdict
import rules

VERSION = "v2"
RULES = [
    "Aim for <b>one category per ZIM</b>. A second category is tolerated when required (see below). "
    "Three or more categories are discouraged and must be clearly justified.",
    "Pick the <b>subject</b> of the ZIM. <i>Encyclopedias &amp; General Reference</i> is only for content spanning all topics.",
    "If the content is a <b>learning path</b> (textbook, course, lessons, exercises, exam prep), "
    "at any level from primary school to university, add <i>Courses &amp; Textbooks</i>. "
    "Multi-subject curricula get <i>Courses &amp; Textbooks</i> alone.",
    "If the content is <b>made for kids</b>, add <i>For Children</i> as second category, never a third: "
    "children's school material is <i>For Children</i> + <i>Courses &amp; Textbooks</i>, without its subject.",
    "Otherwise add a second category only when the content truly belongs to both (e.g. Gutenberg history books: "
    "<i>Books</i> + <i>History</i>).",
    "<i>Other</i> is only for ZIMs which really fit no other category, and is never combined with another category. "
    "It should stay exceptional: many ZIMs in <i>Other</i> is a sign that the taxonomy needs a new category.",
]
OPEN = [
    ("History is the thinnest category (23 families)",
     "Keep it (clear to readers and editors), or merge into <i>History, Religion &amp; Philosophy</i>?"),
    ("PhET simulations", "Science only for now; should it also be Courses &amp; Textbooks?"),
    ("TED all / TEDx / TED conference", "General Reference for now, since they span every topic."),
    ("Privacy guides (OpSec Bible, Anonymous Planet)", "Computers + Survival."),
    ("Psiram, RationalWiki, Skeptics", "Religion &amp; Philosophy (belief and skepticism)."),
    ("ScoutWiki", "Sports &amp; Outdoors."),
    ("Gutenberg LCC T (Technology)", "Books + Science rather than Computers: mostly engineering and industry."),
]

rows = list(csv.DictReader(open("classified.csv")))
fam = defaultdict(lambda: {"n": 0, "langs": set(), "title": "", "cats": []})
for r in rows:
    f = fam[r["family"]]
    f["n"] += 1
    f["langs"].add(r["language"])
    if not f["title"] or r["language"] == "eng":
        f["title"] = r["title"]
    f["cats"] = [c for c in r["categories"].split(";") if c]
data = [{"k": k, "t": v["title"], "n": v["n"], "l": sorted(v["langs"]), "c": v["cats"]}
        for k, v in sorted(fam.items())]

payload = json.dumps({"tax": rules.TAXONOMY, "fam": data}, ensure_ascii=False).replace("</", "<\\/")
rules_html = "".join(f"<li>{r}</li>" for r in RULES)
open_html = "".join(f"<li><b>{html.escape(a) if '&' not in a else a}</b><span>{b}</span></li>" for a, b in OPEN)
total_names = len({r["name"] for r in rows})
two = sum(1 for d in data if len(d["c"]) == 2)

page = open("page_template.html").read()
for k, v in {"__DATA__": payload, "__RULES__": rules_html, "__OPEN__": open_html,
             "__VERSION__": VERSION, "__NAMES__": str(total_names), "__FAMS__": str(len(data)),
             "__TWO__": str(two), "__CATS__": str(len(rules.TAXONOMY))}.items():
    page = page.replace(k, v)
open("taxonomy.html", "w").write(page)
print("wrote taxonomy.html", len(page) // 1024, "KB")
