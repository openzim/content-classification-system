"""Classify catalog entries using rules.py; write classified.csv and print stats."""
import csv, sys
from collections import defaultdict, Counter
import rules

def famkey(n):
    p = n.split('_')
    return '_'.join([p[0], '*'] + p[2:]) if len(p) >= 3 else n

def classify(name):
    c = list(_primary(name) or [])
    if not c: return None
    k = famkey(name); tok = name.split('_')[0]
    extra = rules.ADD_FAMILY.get(k, []) + [x for x in rules.ADD_SITE.get(tok, [])
             if not (x == 'school-courses' and k in rules.NO_EDU)]
    for x in extra:
        if x not in c: c.append(x)
    return rules.finalize(k, c)

def _primary(name):
    k = famkey(name); p = name.split('_'); tok = p[0]
    if k in rules.FAMILY: return rules.FAMILY[k]
    if tok in rules.SERIES and len(p) >= 3:
        c = rules.SERIES[tok]('_'.join(p[2:]))
        if c: return c
    return rules.SITE.get(tok)

rows = list(csv.DictReader(open('entries.csv')))
names = {}
for r in rows: names.setdefault(r['name'], r)
out, unk = [], []
fam_cats = {}
for n, r in sorted(names.items()):
    c = classify(n)
    if not c: unk.append(n); c = []
    fam_cats[famkey(n)] = c
    out.append(dict(name=n, family=famkey(n), title=r['title'], language=r['language'],
                    categories=';'.join(c)))
with open('classified.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)

fam_n, name_n, ent_n = Counter(), Counter(), Counter()
for k, c in fam_cats.items():
    for x in c: fam_n[x] += 1
for o in out:
    for x in o['categories'].split(';'):
        if x: name_n[x] += 1
for r in rows:
    for x in classify(r['name']) or []: ent_n[x] += 1
multi = Counter(len(c) for c in fam_cats.values())
print(f"{'category':<40}{'families':>9}{'names':>7}{'entries':>9}")
for c, label in rules.TAXONOMY.items():
    print(f"{label:<40}{fam_n[c]:>9}{name_n[c]:>7}{ent_n[c]:>9}")
print("categories per family:", dict(sorted(multi.items())))
print("3+ categories:", sorted({k for k,c in fam_cats.items() if len(c)>=3}))
print("unclassified:", len(unk)); print('\n'.join(unk[:80]))
