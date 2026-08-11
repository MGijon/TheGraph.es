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

| Command             | Action                                      |
| :------------------- | :------------------------------------------ |
| `npm install`         | Install dependencies                        |
| `npm run dev`          | Start local dev server at `localhost:4321`  |
| `npm run build`        | Build the production site to `./dist/`      |
| `npm run preview`      | Preview the build locally                   |
| `npm run astro check`  | Type-check the project                      |

## Adding content

Drop a `.md` or `.mdx` file into `src/content/writing/`, `projects/`, or
`research/` with the collection's frontmatter (see
`src/content.config.ts` for the schema). Math is written with KaTeX
(`$inline$` / `$$block$$` via `remark-math`), and fenced code blocks are
highlighted with Shiki.
