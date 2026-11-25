/** URL-safe form of a tag, e.g. "Data Engineering" -> "data-engineering". */
export function tagSlug(tag: string): string {
  return tag
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/** Value for an item's `data-tags` attribute, read by the TagFilter script. */
export function tagData(tags: string[]): string {
  return tags.map(tagSlug).join(' ');
}

/** Distinct tags across entries, most used first, then alphabetically. */
export function collectTags(entries: { data: { tags: string[] } }[]) {
  const counts = new Map<string, { label: string; count: number }>();
  for (const entry of entries) {
    for (const tag of entry.data.tags) {
      const slug = tagSlug(tag);
      const current = counts.get(slug);
      if (current) current.count += 1;
      else counts.set(slug, { label: tag, count: 1 });
    }
  }
  return [...counts.entries()]
    .map(([slug, { label, count }]) => ({ slug, label, count }))
    .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label));
}
