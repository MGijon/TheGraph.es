export interface ExperienceEntry {
  role: string;
  company: string;
  location: string;
  period: string;
  bullets: string[];
  stack?: string[];
}

export interface CvProject {
  name: string;
  description: string;
  href?: string;
  docsHref?: string;
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
  cta?: string;
}

export interface TeachingEntry {
  role: string;
  institution: string;
  location?: string;
  period: string;
  description?: string | string[];
  stack?: string[];
}

export interface SkillGroup {
  category: string;
  items: string[];
}

export const cvHeader = {
  name: 'Manuel Gijón',
  titles: 'Senior Software Engineer · ML Systems · Rust · Data Engineering',
  location: 'Barcelona, Spain · Remote',
  keywords: ['Rust', 'Python', 'Data Engineering', 'ML Systems', 'Mathematics']
};

export const cvSummary =
  'Software engineer with a background in mathematics and mathematical engineering, ' +
  'specializing in data-intensive software, ML infrastructure and high-performance ' +
  'systems. Experience across software engineering, ML engineering, research ' +
  'engineering and technical leadership. Interested in Rust, quantitative computing ' +
  'and performance-critical systems.';

export const experience: ExperienceEntry[] = [
  {
    role: 'Technical Lead, Senior Software Engineer',
    company: 'Eunoia Digital',
    location: 'Barcelona',
    period: 'January 2025 – Present',
    bullets: [
'Led the design and implementation of a data warehouse from the ground up for a large-scale footwear company, establishing the data foundation for future machine learning systems.',
    'Designed the data platform and orchestration architecture, integrating Kestra for workflow orchestration and Metabase for analytics and operational visibility.',
    'Established production engineering practices including CI/CD, automated testing, and ~95% test coverage.',
    'Owned the system architecture and technical decisions across data ingestion, transformation, orchestration, deployment, and observability.'
  ],
    stack: [
    'Python',
    'Kestra',
    'PostgreSQL',
    'Metabase',
    'Docker',
    'Kubernetes (K8s, K3s)',
    'CI/CD',
    'Pytest',
    'Git',
    'TypeScript (Next.js, React)',
    ]
  },
  {
    role: 'Research Engineer',
    company: 'Barcelona Supercomputing Center',
    location: 'Barcelona',
    period: 'June 2024 - October 2024',
    bullets: [
    'Developed software and data pipelines for training and evaluating LLMs and multimodal LLMs.',
    'Designed and implemented ETL infrastructure for processing multimodal datasets.'
    ],
    stack: ['Python', 'Pytest', 'PyTorch', 'Singularity', 'Git', 'GitLab']
  },
  {
    role: 'Software Engineer',
    company: 'Mundimoto',
    location: 'Barcelona',
    period: 'May 2022 – June 2023',
    bullets: [
      "Automated the manual processes in the company's logistics operations, massively reducing the cost of producing each motorbike."
    ],
    stack: [
      'Python',
      'Django',
      'Pytest',
      'TypeScript (Next.js, React)',
      'AWS',
      'Docker',
      'Kubernetes',
      'MySQL',
      'Git',
      'GitHub',
      'Datadog',
      'Metabase',
      'PagerDuty',
      'Apache Airflow',
      'Apache Kafka',
      'TDD',
      'DDD',
      'SOLID principles',
      'Hexagonal architecture'
    ]
  },
  {
    role: 'Software Engineer',
    company: 'Bling',
    location: 'Barcelona',
    period: 'January 2022 – April 2022',
    bullets: [
      "Developed, maintained, and grew the company's payments platform.",
      'Helped scale the product to over 1 million active users and more than 1 million cash advances served.',
      'Led the migration of the entire infrastructure from Google Cloud to AWS.',
      'Coordinated effectively across teams — from product to QA — in a squad split across France and Spain.',
      "Stayed on through the company's wind-down, seeing the platform through to the end of operations."
    ],
    stack: ['Python (Django)', 'Docker', 'PostgreSQL', 'Celery', 'Redis', 'Git', 'Datadog', 'Google Cloud', 'AWS']
  },
  {
    role: 'Software Developer',
    company: 'SIRT',
    location: 'Barcelona',
    period: 'April 2021 – November 2021',
    bullets: ['Developed backend services and APIs for several projects, including the BNEW 2021 platform.'],
    stack: ['Python (Django)', 'Docker', 'PostgreSQL', 'Git']
  },
  {
    role: 'Machine Learning Engineer',
    company: 'I-MAS',
    location: 'Barcelona',
    period: 'October 2019 – July 2020',
    bullets: [
      'Built an internal R&D platform for data collection and maintenance.',
      'Implemented machine learning solutions for classification and regression.',
      'Handled DevOps for the platform.'
    ],
    stack: [
      'Python',
      'Django',
      'Bootstrap',
      'JavaScript',
      'Three.js',
      'Pandas',
      'NumPy',
      'scikit-learn',
      'Keras',
      'Docker',
      'Jenkins',
      'Git',
      'MySQL',
      'Scrum'
    ]
  },
  {
    role: 'Project Coordinator',
    company: 'CARNET (Cooperative Automotive Research Network)',
    location: 'Barcelona',
    period: 'May 2018 – November 2018',
    bullets: [
      "Maintained and updated the company's main WordPress website.",
      'Built new webpages for various events.',
      'Designed and distributed newsletters via MailChimp.',
      'Helped organize and run the Citython 2018 hackathon.'
    ],
    stack: ['HTML', 'CSS', 'JavaScript', 'WordPress', 'Git', 'Mailchimp']
  }
];

export const cvProjects: CvProject[] = [
  {
    name: 'TemporalSeries',
    description:
      'A Rust library for quantitative time-series analysis, with multiple concrete and generic series ' +
      'types over configurable storage backends, plus statistical methods for moving averages, volatility, ' +
      'autocorrelation, and stationarity/normality hypothesis testing.',
    href: 'https://github.com/MGijon/TemporalSeries',
    docsHref: 'https://docs.rs/temporalseries/latest/temporalseries/'
  }
];

export const education: EducationEntry[] = [
  {
    degree: 'Master’s Degree in Advanced Mathematics and Mathematical Engineering',
    institution: 'Universitat Politècnica de Catalunya',
    location: 'Barcelona, Spain',
    period: '2017–2019'
  },
  {
    degree: 'Bachelor’s Degree in Mathematics',
    institution: 'Universidad Autónoma de Madrid',
    location: 'Madrid, Spain',
    period: '2012–2017'
  }
];

export const publications: Publication[] = [
  {
    title: 'Analyzing Distances in Word Embeddings and Their Relation with Seme Analysis',
    href: 'https://upcommons.upc.edu/server/api/core/bitstreams/7d7a670f-e103-43f8-937d-7bcb205b05bc/content',
    venue:
      'Artificial Intelligence Research and Development: Proceedings of the 22nd International ' +
      'Conference of the Catalan Association for Artificial Intelligence, vol. 319, p. 407, IOS Press',
    date: '2019',
    authors: 'M. Gijón Agudo, A. Vilalta Arias, D. Garcia-Gasulla'
  },
  {
    title: 'An Analysis of Word Embedding Spaces and Regularities',
    cta: 'Read the full thesis',
    href: 'https://upcommons.upc.edu/server/api/core/bitstreams/a24cfc56-7cb6-4433-ab8d-5fb2b11b55a2/content',
    venue: "Master's thesis — Universitat Politècnica de Catalunya",
    date: '2019'
  },
  {
    title: 'Modelos matemáticos de la disonancia',
    cta: 'Read the full thesis',
    href: 'https://upcommons.upc.edu/server/api/core/bitstreams/eee72244-282c-49d2-b0f4-69abfbddcaf2/content',
    venue: "Bachelor's thesis — Universitat Politècnica de Catalunya",
    date: '2017'
  }
];

export const teaching: TeachingEntry[] = [
  {
    role: 'Associate Professor',
    institution: 'Universitat Politècnica de Catalunya',
    location: 'Barcelona',
    period: 'February 2023 – June 2025',
    description: [
       'Taught practical Data Mining laboratory sessions to undergraduate Computer Science students ' +
    'across five academic terms, covering data preprocessing, exploratory data analysis, statistical ' +
    'methods, machine learning algorithms, model evaluation, and practical implementation in Python.' ]
  }
];

export const skills: SkillGroup[] = [
  { category: 'Systems', items: ['Rust', 'Python'] },
  { category: 'Data', items: ['SQL', 'PostgreSQL', 'Parquet', 'Apache Arrow', 'ETL'] },
  { category: 'ML', items: ['Machine Learning', 'ML Infrastructure', 'Model Serving'] },
  { category: 'Infrastructure', items: ['Docker', 'Kubernetes', 'CI/CD', 'Linux'] },
  { category: 'Mathematics', items: ['Statistics', 'Probability', 'Numerical Methods', 'Optimization'] }
];
