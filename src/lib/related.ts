import { getCollection } from 'astro:content';

const linkable = ['writing', 'research', 'speak', 'projects'] as const;
export type LinkableCollection = (typeof linkable)[number];

const sectionLabel: Record<LinkableCollection, string> = {
  writing: 'Writing',
  research: 'Research',
  speak: 'Speak',
  projects: 'Project',
};

const categoryLabel = {
  engineering: 'Engineering project',
  venture: 'Venture',
} as const;

export interface RelatedItem {
  key: string;
  href: string;
  title: string;
  meta: string;
  date?: Date;
}

/**
 * Everything linked to `<collection>/<id>`: the entries it lists in its own `related`
 * field (in that order), followed by the entries that list it (newest first).
 * Drafts are skipped. A link to an entry that doesn't exist fails the build.
 */
export async function getRelated(
  collection: LinkableCollection,
  id: string
): Promise<RelatedItem[]> {
  const self = `${collection}/${id}`;

  const all = new Map<string, RelatedItem & { draft: boolean; related: string[] }>();
  for (const name of linkable) {
    for (const entry of await getCollection(name)) {
      const data = entry.data;
      const key = `${name}/${entry.id}`;
      const isProject = name === 'projects' && 'category' in data;
      all.set(key, {
        key,
        href: `/${key}`,
        title: data.title,
        meta: isProject ? categoryLabel[data.category] : sectionLabel[name],
        date: isProject ? undefined : data.date,
        draft: data.draft,
        related: data.related,
      });
    }
  }

  const current = all.get(self);
  if (!current) return [];

  const outgoing = current.related.map((ref) => {
    const target = all.get(ref);
    if (!target) {
      throw new Error(`"${self}" lists related entry "${ref}", which does not exist.`);
    }
    return target;
  });

  const incoming = [...all.values()]
    .filter((entry) => entry.related.includes(self))
    .sort((a, b) => (b.date?.valueOf() ?? 0) - (a.date?.valueOf() ?? 0));

  const seen = new Set<string>([self]);
  const result: RelatedItem[] = [];
  for (const { draft, related: _related, ...item } of [...outgoing, ...incoming]) {
    if (draft || seen.has(item.key)) continue;
    seen.add(item.key);
    result.push(item);
  }
  return result;
}
