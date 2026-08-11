export interface ExperienceEntry {
  role: string;
  company: string;
  location: string;
  period: string;
  bullets: string[];
}

export interface CvProject {
  name: string;
  description: string;
  href?: string;
}

export interface EducationEntry {
  degree: string;
  institution: string;
  location?: string;
  period: string;
  details?: string;
}

export interface Publication {
  title: string;
  href: string;
  venue?: string;
  date?: string;
  authors?: string;
}

export interface TeachingEntry {
  role: string;
  institution: string;
  period: string;
  description?: string;
}

export interface SkillGroup {
  category: string;
  items: string[];
}

export const cvHeader = {
  name: 'Manuel Gijón',
  titles: 'Senior Software Engineer · Tech Lead',
  location: 'Barcelona, Spain · Remote',
  keywords: ['Rust', 'Python', 'Data Engineering', 'ML Systems', 'Mathematics']
};

export const cvSummary =
  'Software engineer with a background in mathematics and mathematical engineering, ' +
  'specializing in data-intensive software, ML infrastructure and high-performance ' +
  'systems. Experience across software engineering, ML engineering, research ' +
  'engineering and technical leadership. Interested in Rust, quantitative computing ' +
  'and performance-critical systems.';

// MOCK DATA — replace with real roles, dates, and achievement bullets.
export const experience: ExperienceEntry[] = [
  {
    role: 'Senior Software Engineer / Tech Lead',
    company: 'Northwind Analytics',
    location: 'Barcelona / Remote',
    period: '2025–Present',
    bullets: [
      'Lead a team of 5 engineers building the company’s real-time feature store, cutting p99 serving latency from 80ms to 12ms.',
      'Designed the migration path from a Python monolith to a Rust-based ingestion pipeline handling 200k events/sec.',
      'Own technical direction for the data platform: architecture reviews, on-call rotation, and hiring.',
      'Introduced a columnar storage layer on Apache Arrow/Parquet, reducing storage costs by 35%.'
    ]
  },
  {
    role: 'Machine Learning Engineer',
    company: 'Vantable AI',
    location: 'Barcelona',
    period: '2022–2025',
    bullets: [
      'Built and shipped the model-serving infrastructure powering the company’s recommendation engine.',
      'Reduced training pipeline runtime by 60% by rewriting hot paths from Python into Rust extensions.',
      'Set up CI/CD and reproducible ML pipelines (data versioning, model registry, canary deploys).',
      'Mentored two junior engineers through their first production ML launches.'
    ]
  },
  {
    role: 'Research Engineer',
    company: 'Institute for Applied Mathematics',
    location: 'Barcelona',
    period: '2020–2022',
    bullets: [
      'Developed numerical solvers for optimization problems in collaboration with the applied math research group.',
      'Published two peer-reviewed papers on numerical methods for large-scale optimization.',
      'Built internal tooling for reproducible experiments and benchmarking across research projects.'
    ]
  }
];

// MOCK DATA — replace with real projects.
export const cvProjects: CvProject[] = [
  {
    name: 'arrow-tsdb',
    description:
      'An experimental embedded time-series database in Rust, using memory-mapped segments and delta-of-delta compression.',
    href: 'https://github.com/MGijon/arrow-tsdb'
  },
  {
    name: 'featurepipe',
    description:
      'A lightweight Python/Rust hybrid library for defining and serving ML feature pipelines with strict schema validation.',
    href: 'https://github.com/MGijon/featurepipe'
  },
  {
    name: 'optim-notes',
    description:
      'A collection of annotated implementations of classical numerical optimization algorithms, used as teaching material.',
    href: 'https://github.com/MGijon/optim-notes'
  }
];

// MOCK DATA — replace with real degrees/institutions.
export const education: EducationEntry[] = [
  {
    degree: 'MSc in Mathematical Engineering',
    institution: 'Universitat Politècnica de Catalunya (UPC)',
    location: 'Barcelona, Spain',
    period: '2018–2020',
    details: 'Thesis on numerical methods for large-scale convex optimization.'
  },
  {
    degree: 'BSc in Mathematics',
    institution: 'Universidad de Sevilla',
    location: 'Seville, Spain',
    period: '2014–2018'
  }
];

// MOCK DATA — replace with real publications and links.
export const publications: Publication[] = [
  {
    title: 'Delta-Encoded Storage for High-Frequency Time-Series Workloads',
    href: '#',
    venue: 'Journal of Applied Data Systems',
    date: '2024',
    authors: 'M. Gijón, A. Torres'
  },
  {
    title: 'A Comparative Study of Numerical Solvers for Large-Scale Convex Optimization',
    href: '#',
    venue: 'International Conference on Numerical Methods',
    date: '2021',
    authors: 'M. Gijón, L. Fernández, R. Costa'
  }
];

// MOCK DATA — replace with real teaching experience.
export const teaching: TeachingEntry[] = [
  {
    role: 'Teaching Assistant, Numerical Optimization',
    institution: 'Universitat Politècnica de Catalunya (UPC)',
    period: '2019–2020',
    description: 'Led weekly lab sessions and graded coursework for a graduate-level optimization course.'
  },
  {
    role: 'Instructor, Introduction to Rust for Data Engineers',
    institution: 'Community workshop series',
    period: '2023–Present',
    description: 'Designed and taught a recurring hands-on workshop introducing Rust to Python data engineers.'
  }
];

export const skills: SkillGroup[] = [
  { category: 'Systems', items: ['Rust', 'Python'] },
  { category: 'Data', items: ['SQL', 'PostgreSQL', 'Parquet', 'Apache Arrow', 'ETL'] },
  { category: 'ML', items: ['Machine Learning', 'ML Infrastructure', 'Model Serving'] },
  { category: 'Infrastructure', items: ['Docker', 'Kubernetes', 'CI/CD', 'Linux'] },
  { category: 'Mathematics', items: ['Statistics', 'Probability', 'Numerical Methods', 'Optimization'] }
];
