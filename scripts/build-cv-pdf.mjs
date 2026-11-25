// Builds public/<cvPdfFileName> from cv/cv.typ using the data in src/data/cv.ts.
// Usage: npm run cv:pdf [-- <output>]   (requires the `typst` CLI: https://typst.app)
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

import {
  cvHeader,
  cvSummary,
  experience,
  cvProjects,
  education,
  publications,
  teaching,
  skills,
  cvPdfFileName,
} from '../src/data/cv.ts';
import { socialLinks } from '../src/data/social.ts';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

// Links shown under the name in the PDF header.
const pdfLinkLabels = ['GitHub', 'LinkedIn', 'ORCID'];
const links = [
  { label: 'thegraph.es', href: 'https://thegraph.es' },
  ...socialLinks.filter((link) => pdfLinkLabels.includes(link.label)),
];

const data = {
  header: cvHeader,
  summary: cvSummary,
  links,
  experience,
  projects: cvProjects,
  education,
  publications,
  teaching,
  skills,
};

// Optional output path, e.g. `npm run cv:pdf -- /tmp/cv-{p}.png` to preview pages as images.
const output = path.resolve(process.argv[2] ?? path.join(root, 'public', cvPdfFileName));

// Pin the PDF's creation date to the last commit touching the CV sources, so regenerating
// an unchanged CV gives a byte-identical file (and no spurious diff before a deploy).
const sources = ['src/data/cv.ts', 'src/data/social.ts', 'cv/cv.typ', 'scripts/build-cv-pdf.mjs'];
let timestamp = [];
try {
  const ct = execFileSync('git', ['log', '-1', '--format=%ct', '--', ...sources], {
    cwd: root,
    encoding: 'utf8',
  }).trim();
  if (ct) timestamp = ['--creation-timestamp', ct];
} catch {
  // Not a git checkout: fall back to Typst's default (current time).
}

try {
  execFileSync(
    'typst',
    [
      'compile',
      '--root',
      root,
      // Only Typst's bundled fonts, so the PDF looks the same on any machine.
      '--ignore-system-fonts',
      ...timestamp,
      '--input',
      `data=${JSON.stringify(data)}`,
      path.join(root, 'cv', 'cv.typ'),
      output,
    ],
    { stdio: 'inherit' }
  );
} catch (error) {
  if (error.code === 'ENOENT') {
    console.error(
      'typst not found. Install it with `brew install typst` or `cargo install typst-cli`.'
    );
  }
  process.exit(1);
}

console.log(`Wrote ${path.relative(root, output)}`);
