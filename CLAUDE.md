# CLAUDE.md

Personal academic website for Wouter van Atteveldt (prof. dr., VU Amsterdam), hosted on GitHub Pages at vanatteveldt.com.

## Stack

- **Jekyll** (Ruby) with the Minimal Mistakes theme
- **Liquid** templating, **kramdown** markdown, **SASS** styles
- Deployed via GitHub Pages; custom domain set in `_config.yml`

## Key directories

| Path | Purpose |
|------|---------|
| `_pages/` | Main site pages (about, publications, cv, …) |
| `_layouts/` | Jekyll page templates |
| `_includes/` | Reusable template partials |
| `_data/` | Site data: navigation, authors, UI strings |
| `_publications/` | Individual publication markdown files (generated) |
| `_posts/` | Blog posts |
| `cv/` | LaTeX CV source + BibTeX bibliographies |
| `files/` | Downloadable files (PDFs, etc.) |
| `images/` | Image assets |
| `markdown_generator/` | Python/Jupyter scripts for content generation |

## Publications workflow

Publications are stored as BibTeX in `cv/`:

- `cv/articles.bib` — journal articles
- `cv/books.bib` — books
- `cv/other.bib` — book chapters and misc

**To regenerate the publications page** after editing the BibTeX files:

```bash
python create_pub_md.py
```

This overwrites `_pages/publications.md`. Do not edit that file manually — changes will be lost on the next run.

`markdown_generator/pubsFromBib.py` generates individual per-publication markdown files in `_publications/` (alternate approach, not the primary workflow).

## Local development

```bash
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

`_config.dev.yml` overrides the base URL to `http://localhost:4000` and disables analytics.

## JavaScript

JS is minified with UglifyJS via npm:

```bash
npm run uglify   # rebuild assets/js/main.min.js
npm run watch:js # watch mode
```

## Configuration

- `_config.yml` — main site config (author info, plugins, collections, defaults)
- `_config.dev.yml` — local dev overrides
- `_data/navigation.yml` — top navigation menu
- `Gemfile` — Ruby dependencies

## Dependencies

- Ruby: `jekyll`, `github-pages`, `jekyll-feed`, `jekyll-sitemap`, `hawkins`
- Python: `pybtex` (for publication generation scripts)
- Node: `uglify-js` and jQuery plugins (for JS minification)
