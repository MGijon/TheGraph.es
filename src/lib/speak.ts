import { getCollection } from 'astro:content';

export const kindLabel: Record<string, string> = {
  talk: 'Talk',
  workshop: 'Workshop',
  panel: 'Panel',
  podcast: 'Podcast',
  interview: 'Interview',
  other: 'Session',
};

/**
 * Published speak entries split into upcoming (soonest first) and past (most recent first).
 * "Today" is the build date, so an event moves to past on the first deploy after it happens.
 */
export async function getSpeakEntries() {
  const entries = await getCollection('speak', ({ data }) => !data.draft);

  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const upcoming = entries
    .filter((e) => e.data.date >= today)
    .sort((a, b) => a.data.date.valueOf() - b.data.date.valueOf());
  const past = entries
    .filter((e) => e.data.date < today)
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  return { upcoming, past };
}
