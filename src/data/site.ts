// Single source for who the site is about. Used in page text, metadata, the CV, and the
// schema.org structured data (JSON-LD) that helps search engines link the site to its author.

export const author = {
  name: 'Manuel Gijón Agudo',
  jobTitle: 'Senior Software Engineer',
  location: 'Barcelona, Spain',
};

export const site = {
  name: 'thegraph.es',
  url: 'https://thegraph.es',
  description: `${author.name}'s notes on data engineering, distributed systems, and research.`,
};

/** schema.org @id of the author, for other structured data (articles, events) to reference. */
export const personId = `${site.url}/#person`;
