import { defineCollection, reference, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Links to entries in other sections, as "<collection>/<id>", e.g.
// "writing/building-a-time-series-engine-in-rust" or "projects/temporalseries".
// Links show up on both pages, so each pair only needs to be declared once.
const related = z
  .array(
    z
      .string()
      .regex(
        /^(writing|research|speak|projects)\/.+$/,
        'Use "<writing|research|speak|projects>/<id>"'
      )
  )
  .default([]);

// Link to the source code behind an entry (repository, notebook, gist…), shown as "Code →".
const codeUrl = z.string().url().optional();

const series = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/series' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
  }),
});

const writing = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/writing' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    description: z.string(),
    series: reference('series').optional(),
    seriesOrder: z.number().int().positive().optional(),
    codeUrl,
    related,
    draft: z.boolean().default(false),
  }),
});

const speak = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/speak' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    kind: z.enum(['talk', 'workshop', 'panel', 'podcast', 'interview', 'other']).default('talk'),
    event: z.string(),
    location: z.string().optional(),
    eventUrl: z.string().url().optional(),
    slidesUrl: z.string().url().optional(),
    videoUrl: z.string().url().optional(),
    codeUrl,
    // Path under /public, e.g. "/images/<slug>/photo.webp". Used as the social preview image.
    image: z.string().optional(),
    tags: z.array(z.string()).default([]),
    description: z.string(),
    related,
    draft: z.boolean().default(false),
  }),
});

const projects = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    description: z.string(),
    category: z.enum(['engineering', 'venture']).default('engineering'),
    repoUrl: z.string().url().optional(),
    liveUrl: z.string().url().optional(),
    related,
    draft: z.boolean().default(false),
  }),
});

const research = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/research' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    description: z.string(),
    codeUrl,
    related,
    draft: z.boolean().default(false),
  }),
});

export const collections = { series, writing, speak, projects, research };
