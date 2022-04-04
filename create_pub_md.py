from pybtex.database import parse_file


def format(x):
    return x.replace("{", "").replace("}", "")


def to_md(entry):
    title = format(entry.fields['title'])
    url = entry.fields.get('url')
    if url:
        title = f"[{title}]({url})"
    year = int(entry.fields['year'])
    authors = names(entry.persons['author'])
    md = f'- {authors} ({year}), {title}'
    if entry.type == 'book':
        md += f" {entry.fields['address']}: {entry.fields['publisher']}"
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
for fn in ['cv/books.bib']:
    for entry in get_entries(fn):
        print(entry)
        w.write(entry)
        w.write("\n")
