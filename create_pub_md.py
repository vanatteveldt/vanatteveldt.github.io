from pybtex.database import parse_file


def format(x):
    return x.replace("{", "").replace("}", "").replace("\\&", "&")


def to_md(entry):
    title = format(entry.fields['title']).strip(".")
    url = entry.fields.get('url')
    if url:
        title = f"[{title}]({url})"
    year = int(entry.fields['year'])
    authors = names(entry.persons['author'])
    fields = [f'{authors} ({year})', title]
    if entry.type == 'book':
        fields += [f"{entry.fields['address']}: {entry.fields['publisher']}"]
    elif entry.type == 'article':
        fields += [f"*{entry.fields['journal']}*"]
        if 'volume' in entry.fields:
            vol = entry.fields['volume']
            if 'number' in entry.fields:
                vol = f"{vol} ({entry.fields['number']})"
            fields += [vol]
        if 'pages' in entry.fields:
            fields += [f"{entry.fields['pages']}"]
    if doi := entry.fields.get('doi'):
        fields += [f"[doi.org/{doi}](https://doi.org/{doi})"]
    md = f'- {", ".join(fields)}'
    return -year, md


def names(persons):
    names = [format(name(person)) for person in persons]
    if len(names) == 1:
        return names[0]
    else:
        return " & ".join([", ".join(names[:-1]), names[-1]])


def name(person):
    fn = " ".join(person.first_names)
    ln = " ".join(person.last_names)
    return f'{fn} {ln}'


def get_entries(fn):
    entries = sorted(to_md(x) for x in parse_file(fn).entries.values())
    return (entry for (sortkey, entry) in entries)


w = open("_pages/publications.md", "w")
print("""---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
""", file=w)
for section, fn in [("Books", 'cv/books.bib'),
                    ("Journal Articles", 'cv/articles.bib')]:
    w.write(f"## {section}\n\n")
    for entry in get_entries(fn):
        print(entry)
        w.write(entry)
        w.write("\n")
