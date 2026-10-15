import xml.etree.ElementTree as ET, csv, re
ns={'a':'http://www.w3.org/2005/Atom'}
root=ET.parse('catalog.xml').getroot()
rows=[]
for e in root.findall('a:entry',ns):
    g=lambda t:(e.findtext('a:'+t,'',ns) or '').strip()
    tags=g('tags')
    rows.append(dict(name=g('name'),flavour=g('flavour'),title=g('title'),summary=g('summary'),
        language=g('language'),category=g('category'),tags=';'.join(t for t in tags.split(';') if not t.startswith('_')),
        articles=g('articleCount'),author=(e.findtext('a:author/a:name','',ns) or '').strip(),
        publisher=(e.findtext('a:publisher/a:name','',ns) or '').strip()))
with open('entries.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(len(rows), 'entries;', len({r['name'] for r in rows}),'distinct names')
from collections import Counter
print(Counter(r['category'] for r in rows).most_common())
