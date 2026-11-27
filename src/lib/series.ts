import { getCollection } from 'astro:content';

/** Published posts in a series, ordered by `seriesOrder`, then by date. */
export async function getSeriesPosts(seriesId: string) {
  const posts = await getCollection(
    'writing',
    ({ data }) => !data.draft && data.series?.id === seriesId
  );
  return posts.sort(
    (a, b) =>
      (a.data.seriesOrder ?? Infinity) - (b.data.seriesOrder ?? Infinity) ||
      a.data.date.valueOf() - b.data.date.valueOf()
  );
}
