// CV template. Content comes from src/data/cv.ts (the same data as the /cv page),
// passed in as JSON by scripts/build-cv-pdf.mjs. Regenerate with: npm run cv:pdf

#let cv = json(bytes(sys.inputs.at("data", default: "{}")))

#let accent = rgb("#1f4e79")
#let muted = rgb("#555555")
#let faint = rgb("#777777")

#set document(title: cv.header.name + " — CV", author: cv.header.name)
#set page(paper: "a4", margin: (x: 1.8cm, y: 1.6cm))
#set text(font: "Libertinus Serif", size: 10pt, lang: "en")
#set par(justify: false, leading: 0.5em, spacing: 0.4em)
#show link: set text(fill: accent)

// ---- building blocks ----------------------------------------------------

// Sticky, so a heading never ends up alone at the bottom of a page.
#let section(title) = block(above: 1.6em, below: 0.2em, sticky: true, stack(
  spacing: 0.35em,
  text(size: 11pt, weight: "bold", fill: accent, upper(title)),
  line(length: 100%, stroke: 0.5pt + accent.lighten(40%)),
))

#let entry-head(title, period) = grid(
  columns: (1fr, auto),
  column-gutter: 1em,
  text(weight: "bold", title), text(fill: muted, period),
)

#let subtitle(..parts) = text(fill: muted, parts.pos().filter(p => p != none and p != "").join(" · "))

#let stack-line(items) = if items != none and items.len() > 0 {
  v(0.15em)
  text(size: 8.5pt, fill: faint, items.join(" · "))
}

#let bullets(items) = if items != none and items.len() > 0 {
  list(indent: 0.4em, body-indent: 0.5em, spacing: 0.35em, ..items)
}

// ---- header -------------------------------------------------------------

#align(center)[
  #text(size: 20pt, weight: "bold", cv.header.name) \
  #v(0.1em)
  #text(size: 11pt, cv.header.titles) \
  #text(fill: muted, cv.header.location) \
  #v(0.3em)
  #text(size: 9pt, cv.links.map(l => link(l.href, l.label)).join(h(0.5em) + "·" + h(0.5em)))
]

#v(0.8em)
#cv.summary

// ---- sections -----------------------------------------------------------

#section("Experience")
#for job in cv.experience {
  block(breakable: false, above: 1.1em)[
    #entry-head(job.role, job.period)
    #subtitle(job.company, job.at("location", default: none))
    #bullets(job.bullets)
    #stack-line(job.at("stack", default: none))
  ]
}

#if cv.projects.len() > 0 {
  section("Projects")
  for project in cv.projects {
    block(breakable: false, above: 1.1em)[
      #text(weight: "bold", project.name)
      #let links = (
        ("Source", project.at("href", default: none)),
        ("Docs", project.at("docsHref", default: none)),
      ).filter(l => l.at(1) != none)
      #if links.len() > 0 [
        #h(0.4em) #text(size: 9pt, links.map(l => link(l.at(1), l.at(0))).join(" · "))
      ]
      \ #project.description
    ]
  }
}

#section("Education")
#for entry in cv.education {
  block(breakable: false, above: 1.1em)[
    #entry-head(entry.degree, entry.period)
    #subtitle(entry.institution, entry.at("location", default: none))
    #if entry.at("details", default: none) != none [ \ #entry.details ]
  ]
}

#if cv.publications.len() > 0 {
  section("Publications")
  for pub in cv.publications {
    block(breakable: false, above: 1.1em)[
      #link(pub.href, text(weight: "bold", fill: black, pub.title)) \
      #subtitle(
        pub.at("venue", default: none),
        pub.at("date", default: none),
        pub.at("authors", default: none),
      )
    ]
  }
}

#if cv.teaching.len() > 0 {
  section("Teaching")
  for entry in cv.teaching {
    let description = entry.at("description", default: none)
    block(breakable: false, above: 1.1em)[
      #entry-head(entry.role, entry.period)
      #subtitle(entry.institution, entry.at("location", default: none))
      #if type(description) == array { bullets(description) } else if description != none [ \ #description ]
      #stack-line(entry.at("stack", default: none))
    ]
  }
}

#section("Skills")
#block(breakable: false, above: 0.8em, grid(
  columns: (auto, 1fr),
  column-gutter: 1.2em,
  row-gutter: 0.55em,
  ..cv.skills.map(g => (text(weight: "bold", g.category), g.items.join(" · "))).flatten(),
))
