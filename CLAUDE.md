# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The **organizing hub for the Social Network Health (SNH) research program**, plus the small static
website at https://socialnetwork.health. The actual software (PNA toolkit, PRM, etc.) lives in
sibling repositories — **read `RELATED_REPOS.md`** for the full map and the convention that all
related repos are checked out at `../<name>` relative to this repo root (same layout on every
workstation).

There is no web framework, no package manager, and **no test runner** here — don't claim tests
pass; there are none. (A TanStack/Bun app used to live here; it was removed in commit `749f3d9`.)

## Layout

```
public/                    the ENTIRE live site: one HTML file + one SVG logo
ops/                       Ansible + Caddy provisioning/deploy for the site (DigitalOcean droplet)
research/                  organized BY TOPIC:
  measurement/             community-network-health-explainer.md, egocentric→community note, social_cohesion.md
  threat_modelling/        threat_catalog.md + references/references.md (its bibliography)
  protocols/               notification-protocol.md (+ future metrics/statistics protocol notes)
  research_library/        research_summaries/ (per-paper subfolders: summary + code),
                           planning/knowledge-base-plan.md (read before corpus work),
                           paper-corpus/ (GITIGNORED generated artifacts: SQLite db + PDFs)
tools/paper-resolver/      resolve.py + SKILL.md + usage.md — DOI/title/topic → metadata + legal OA full text
presentations/             one folder per talk; the PDF at a talk's top level IS the presentation,
                           Slidev source + notes live in its deck/ subdir. Currently:
                           dwebcamp-berlin-2026/ (delivered 2026-07). Run a deck with
                           `just slides <folder>` (default: dwebcamp-berlin-2026/deck).
                           The old pnt-workshop deck lives in richbodo/pnt-workshop + git history.
plan.md                    the project's summary plan (M1/M2/M3 steps) — planning layer 1
plans/                     ORG-LEVEL planning: ORG-TASKS.md (the live cross-repo task list)
                           plus dated, append-only planning dumps (`YYYY-MM-DD-<topic>.md`).
                           Read plans/README.md before adding anything.
drafts/                    STUB ONLY — redirect README for old deep links; don't add content here
research/plan.md           STUB ONLY — plan.md moved to the repo root (Aug 2026)
RELATED_REPOS.md           single source of truth for sibling repos and external resources
```

## Planning has four layers — don't mix them

| # | Question | Lives in |
|---|---|---|
| 1 | "What is this project?" | `/plan.md` — the summary |
| 2 | "What should the org be doing?" | `plans/` + `plans/ORG-TASKS.md` |
| 3 | "Where is this repo headed?" | that repo's `docs/roadmap.md` |
| 4 | "What's in flight?" | that repo's GitHub issues + active branches |

**Layer 2 is org-only.** A task actionable inside one existing repo belongs in that repo's
roadmap or issues, never in `ORG-TASKS.md`. Org tasks may link down (`PNT#55`, `prm#66`,
`fellows#296`), but the repo stays the source of truth for its own status.

Never "update" a dated plan file — write a new one. `ORG-TASKS.md` is the sole exception:
it is kept current.

## The website

The live site is `public/socialnetwork-health.html` (self-contained HTML + inline CSS) plus the SVG
logo — served verbatim by Caddy on a droplet. To change the site, edit that file and run
`just deploy` (rsyncs the two files; needs the droplet SSH setup described in `ops/README.md`).
Admin/devops tasks run through the root `justfile` — `just` lists the recipes (deploy,
verify-live, provision, provision-caddy, ansible-deps). Provisioning is `ops/ansible/site.yml`;
the real `hosts.ini` is gitignored.

**Keep the homepage links in sync:** the HTML deep-links to files in `research/` by GitHub URL. If
research files move or are renamed, update the HTML and redeploy.

## research/ conventions

- `research/threat_modelling/references/references.md` numbering is **append-only** (`[n]` in
  order of first appearance, never renumbered) — documents cite `[n]` and must stay valid. Add
  new sources at the end with the next free number.
- `research/research_library/research_summaries/` holds per-paper "research primitive" summaries
  (one subfolder per paper: summary markdown + derived code).
- The threat catalog is v2.0; the old v1.1 exists only in git history (the `.bak` was deleted).

## Running the paper-resolver

See `tools/paper-resolver/usage.md` for validated invocations. The essentials:

- **Global flags (`--db`, `--download`, `--extract`, `--out`, `--json`) go BEFORE the subcommand**
  (`doi`/`batch`/`search`); subcommand args like `--limit` go after. Putting `--json` after the DOI errors.
- Always set `RESOLVER_EMAIL=richbodo@gmail.com` (required by Unpaywall; polite pool for OpenAlex).
- Needs network access (sandbox off for the call) and PyMuPDF for `--extract`.
- State lives in `research/research_library/paper-corpus/resolver.db` (gitignored, idempotent cache + corpus index).

## Cross-repo work

Sibling repos are at `../<name>` (see `RELATED_REPOS.md`). It's fine to read and operate on them
locally when a task calls for it. `../socialnetwork_toolkit` has secrets checked in — never copy
its contents anywhere public.

A `/prime` command (`.claude/commands/prime.md`) exists for deeper session orientation — it reads
the key research docs and confirms which sibling repos are present on the current host.
