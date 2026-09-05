# AIjuggernauts

AI tools, resources, and hands-on training — built with Jekyll, hosted on GitHub Pages.

## Structure
- `_posts/` — Articles (Markdown, dated filenames: `YYYY-MM-DD-title.md`)
- `_case_studies/` — Case studies (Markdown)
- `_simulations/` — Interactive text-based simulations (Markdown + inline JS)
- `_layouts/` — Page templates (`default`, `article`, `page`)
- `assets/` — CSS and JS
- `_config.yml` — Site settings and top nav (the "tabs")

## Adding new content
- New article: add a file to `_posts/` named `YYYY-MM-DD-slug.md` with front matter (title, date, category, tags, description).
- New case study: add a file to `_case_studies/`.
- New simulation: add a file to `_simulations/`, following the pattern in `prompt-engineering-basics.md`.

## Local preview (optional)
```
bundle install
bundle exec jekyll serve
```
Then visit http://localhost:4000

## Deploying
Push to the `main` branch of this repo. GitHub Pages will build and publish automatically (enable it under Settings → Pages → Source: `main` branch).

The `CNAME` file points the site at aijuggernauts.com — configure GoDaddy DNS to match (see project notes).
