import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const writing = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/writing' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    description: z.string(),
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
    repoUrl: z.string().url().optional(),
    liveUrl: z.string().url().optional(),
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
    tags: z.array(z.string()).default([]),
    description: z.string(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { writing, speak, projects, research };
