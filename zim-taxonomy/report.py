"""Print, per category, the families assigned (with name counts) for review."""
import csv, rules
from collections import defaultdict
rows=list(csv.DictReader(open('classified.csv')))
fam=defaultdict(lambda:[0,'',''])
for r in rows:
    f=fam[r['family']]; f[0]+=1; f[1]=f[1] or r['title']; f[2]=r['categories']
for c,label in rules.TAXONOMY.items():
    items=[(k,v) for k,v in sorted(fam.items()) if c in v[2].split(';')]
    print(f"\n## {label} `{c}` ({len(items)} families)")
    for k,(n,t,cats) in items:
        other=[x for x in cats.split(';') if x!=c]
        print(f"- {k} ({n}) {t[:40]}" + (f"  +{','.join(other)}" if other else ''))
