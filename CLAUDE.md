# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static marketing site for "Jaden Does AI" — an AI tutoring and consulting business in the Mad River Valley, Vermont. Deployed on Vercel.

## Architecture

- **Pure static site** — no build step, no framework, no JavaScript bundler
- `index.html` is the main marketing page with all CSS inlined in a `<style>` tag
- Additional standalone HTML pages exist at `/links/`, `/rice-mountain/`, and `/warren-public-buildings-report/` (the latter two are disallowed in robots.txt)
- `files/` contains utility scripts and standalone HTML files (not part of the main site)

## Development

No build or test commands. Open `index.html` in a browser or use any local HTTP server:

```
python3 -m http.server
```

## Deployment

Hosted on Vercel. Pushes to `main` trigger automatic deployment.
