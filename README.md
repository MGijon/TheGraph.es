# thegraph.es

Personal site — writing, projects, and research notes.

Built with [Astro](https://astro.build), React, Tailwind CSS, MDX, Shiki,
KaTeX, and `astro-seo`.

## Structure

```text
src/
├── components/       Header, Footer, ProjectCard, ThemeToggle, ...
├── content/
│   ├── writing/      articles (.md / .mdx)
│   ├── projects/
│   └── research/
├── content.config.ts content collection schemas
├── layouts/
│   ├── BaseLayout.astro     head/SEO, header, footer
│   └── ArticleLayout.astro  article chrome (title, date, tags)
└── pages/
    ├── index.astro
    ├── writing/
    ├── projects/
    ├── research/
    └── about.astro
```

## Commands

| Command                | Action                                        |
| :--------------------- | :-------------------------------------------- |
| `npm install`          | Install dependencies                          |
| `npm run dev`          | Start local dev server at `localhost:4321`    |
| `npm run build`        | Build the production site to `./dist/`        |
| `npm run preview`      | Preview the build locally                     |
| `npm run astro check`  | Type-check the project                        |
| `npm run format`       | Format the codebase with Prettier             |
| `npm run format:check` | Check formatting without writing (used in CI) |

## Adding content

Drop a `.md` or `.mdx` file into `src/content/writing/`, `projects/`, or
`research/` with the collection's frontmatter (see
`src/content.config.ts` for the schema). Math is written with KaTeX
(`$inline$` / `$$block$$` via `remark-math`), and fenced code blocks are
highlighted with Shiki.

## Deploying

Deploys are tag-triggered: pushing a tag matching `v*.*.*` runs
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml), which builds
the static site and uploads `dist/` to the Hostalia server over FTPS. There's
no manual deploy step — the tag push _is_ the deploy.

1. Get your change onto `master`:
   - Push your branch and open a PR against `master`. CI
     ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)) runs
     `npm run format:check` on the PR — fix formatting with `npm run format`
     if it fails.
   - Merge the PR (or push directly to `master`).
2. From an up-to-date `master`, tag the release:
   ```sh
   git checkout master
   git pull
   git tag -a vX.Y.Z -m "vX.Y.Z"
   git push origin vX.Y.Z
   ```
3. Watch the **Deploy to production** run under the repo's Actions tab. It
   builds with `npm ci && npm run build`, then syncs `dist/` to
   `REMOTE_TARGET_DIR` on the server with
   `dangerous-clean-slate: true` — anything in that remote folder not part of
   the new build gets deleted, so it should only ever contain this site's
   output.

### Required repository secrets

Set these under **Settings → Secrets and variables → Actions**:

| Secret              | Value                                                                      |
| :------------------ | :------------------------------------------------------------------------- |
| `FTP_SERVER`        | FTP hostname/IP from Hostalia                                              |
| `FTP_USERNAME`      | Hostalia FTP username                                                      |
| `FTP_PASSWORD`      | Hostalia FTP password                                                      |
| `FTP_PORT`          | Only needed if not 21                                                      |
| `REMOTE_TARGET_DIR` | Path to the site's public folder on the server (no leading/trailing slash) |

### Rolling back

Re-tag and re-push an older commit (or revert on `master` and cut a new
tag) — there's no separate rollback mechanism, a deploy is just whatever
`dist/` looked like at the tagged commit.
