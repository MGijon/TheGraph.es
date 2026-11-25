---
name: deploy
description: Release thegraph.es to production. Regenerates the CV PDF (public/Manuel-Gijon-Agudo-CV.pdf) from src/data/cv.ts, commits it if it changed, checks formatting and the build, then creates and pushes the vX.Y.Z tag that triggers the GitHub Actions deploy. Use when the user asks to deploy, release, ship to production, or cut/push a version tag.
argument-hint: '[vX.Y.Z]'
disable-model-invocation: true
---

# Deploy thegraph.es

Deploys are tag-triggered: pushing a tag matching `v*.*.*` runs `.github/workflows/deploy.yml`,
which builds the site and uploads `dist/` to the server. This skill makes sure the CV PDF is fresh
before that tag goes out. The README's "Deploying" section is the source of truth for the process.

The version to release is: `$ARGUMENTS` (may be empty).

## 1. Preconditions — stop and report if any fail

Run from the repository root.

- `git fetch origin --tags`
- Current branch is `master` (`git branch --show-current`). If not, stop: the change must be merged
  to `master` first (README step 1). Do not merge or switch branches on the user's behalf.
- Working tree is clean (`git status --porcelain` is empty).
- Local `master` matches `origin/master` (`git rev-parse master` == `git rev-parse origin/master`).
  If behind, `git pull --ff-only`; if diverged, stop and ask.
- `typst` is installed (`typst --version`). If not, stop and tell the user to install it
  (`brew install typst` or `cargo install typst-cli`).

## 2. Pick the version

- Latest tag: `git tag --list 'v*.*.*' --sort=-v:refname | head -1`.
- If `$ARGUMENTS` is a version, use it (add a leading `v` if missing). It must match `vX.Y.Z`, must
  not already exist (`git rev-parse -q --verify "refs/tags/<version>"` fails), and must be greater
  than the latest tag.
- If no version was given, ask the user with the AskUserQuestion tool, offering the next patch,
  minor and major versions after the latest tag (patch first, marked recommended).

## 3. Regenerate the CV PDF

- `npm run cv:pdf`
- The PDF is `public/<cvPdfFileName>` (`cvPdfFileName` in `src/data/cv.ts`; currently
  `Manuel-Gijon-Agudo-CV.pdf`). If `git status --porcelain public/` shows it changed, commit only
  that file: `git add public/<file> && git commit -m "chore(cv): regenerate CV PDF for <version>"`
  (append the commit attribution lines from the session's instructions, if any).
- If nothing changed, say so and continue. The PDF's creation date is pinned to the last commit that
  touched the CV sources, so an unchanged CV regenerates byte-identically.

## 4. Verify

- `npm run format:check` — if it fails, stop and report the files (`npx prettier --list-different .`).
  Do not reformat and push without asking.
- `npm run build` — if it fails, stop and report the error.

## 5. Confirm, then push

Pushing is outward-facing and the tag deploys to production, so confirm first. Show the user:

- the version, and the commit it will point at (`git log -1 --oneline`)
- whether a CV PDF commit was created
- the commits since the previous tag (`git log --oneline <latest-tag>..HEAD`)

Ask for an explicit go-ahead. Only after a yes:

```sh
git push origin master            # only if step 3 created a commit
git tag -a <version> -m "<version>"
git push origin <version>
```

## 6. Report

- The tag that was pushed and the commit it points at.
- Where to watch the deploy: the "Deploy to production" workflow under the repo's Actions tab
  (`https://github.com/MGijon/TheGraph.es/actions`).
- If the user wants to roll back, point them to the README's "Rolling back" section; do not
  delete or move tags yourself.
