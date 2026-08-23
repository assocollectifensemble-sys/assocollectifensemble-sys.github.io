# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Static site for **« Une 2CV, mille histoires »** (`une2cvmillehistoires.re`) — a wedding-car / sunset-ride / photoshoot rental business built around two vintage Citroën 2CVs ("Rosalie" et "Soizig") with a licensed VTC driver, on Réunion Island. The site is a project of the association **Collectif Ensemble** (Saint-Leu, La Réunion), which is the legal operator (SIRET on file in `mentions-legales.html`).

Hosted on GitHub Pages, French-only, no backend — leads are captured via WhatsApp deep links (`wa.me/262693828108?text=...`) and a static contact form.

## Commands

Build (regenerates every `.html` file, `robots.txt`, and `sitemap.xml` from `build.py`):

```
python3 build.py
```

There is no other tooling — no package.json, no linter, no test suite. `build.py` prints `OK <filename> <bytes>` per page and `Terminé.` when done; a non-zero exit or a Python traceback is the only failure signal.

To preview locally, serve the repo root with any static file server (e.g. `python3 -m http.server`) after running the build.

## Architecture

**Every `.html` file in the repo root is generated output.** Never hand-edit `index.html`, `mariage.html`, `balades.html`, `shooting-evenements.html`, `rosalie-et-soizig.html`, `faq.html`, `contact.html`, `merci.html`, or `mentions-legales.html` — edits will be silently overwritten the next time someone runs `build.py`. All content, copy, and markup changes belong in `build.py`. Same for `robots.txt` and `sitemap.xml`.

`build.py` is a single ~800-line script structured as:
- **Shared constants** at the top: `DOMAIN`, WhatsApp deep-link URLs per intent (`WA`, `WA_MARIAGE`, `WA_BALADE`, `WA_SHOOT`), the `IMG` dict mapping semantic image keys to Google Drive file IDs (rendered via the `D(id, width)` helper into `lh3.googleusercontent.com` URLs), social links (`INSTA`, `FB`).
- **Layout helpers**: `head()` (doctype/meta/OG tags/JSON-LD/`<link>`s, takes per-page `title`/`desc`/`path`/optional `jsonld`/`noindex`), `navbar()`, `footer()`, plus small builders like `btn_wa()`, `page_hero()`, `cta_band()`, `bloc_balade()`.
- **One section per page**, in page order, each building an HTML string and assigning it into the `pages` dict, e.g. `pages["mariage.html"] = head(...) + body + footer()`.
- **Emission loop** at the bottom writes `robots.txt`, `sitemap.xml`, then every entry of `pages` to disk.

Adding a page means: write a new section following the existing pattern, add it to `pages{}`, add its route to `navbar()` if it should appear in the nav, and add its URL to the `urls` list feeding `sitemap.xml`.

Images are never stored in the repo — they're hosted on Google Drive and referenced by ID through `IMG`/`D()`. Adding an image means adding a new `IMG` entry with its Drive file ID.

`assets/style.css` defines the visual system as CSS custom properties on `:root` (`--terre`, `--brun`, `--encre`, `--sauge`, `--wa`, etc.) plus the `Playfair Display` / `Jost` / `Pinyon Script` font trio (script accents use `.script`). `assets/site.js` is a small vanilla-JS file handling scroll-based nav opacity, reveal-on-scroll animations, and the background music toggle on the homepage — it's static and referenced identically by every generated page.

## Content/business notes worth knowing when editing copy

- Primary contact channel is WhatsApp (+262 693 82 81 08), with a distinct pre-filled message per funnel (general / mariage / balade / shooting) — keep new CTAs consistent with this pattern rather than adding a generic "contact us" link.
- The site has three offer pillars: **Mariage** (weddings/EVJF-EVJG/elopements), **Balades** (sunset rides, brunch, island tours), **Shootings & évènements** (photo/film/events) — reflected in `mariage.html`, `balades.html`, `shooting-evenements.html`.
- SEO/structured data: `LocalBusiness` JSON-LD lives in the index section of `build.py` (`biz_jsonld`) — update it there if pricing, offers, or address change.
