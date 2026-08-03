# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The **organizing hub for the Social Network Health (SNH) research program**, plus the small static
website at https://socialnetwork.health. The actual software (PNA toolkit, PRM, etc.) lives in
sibling repositories.

There is no web framework, no package manager, and **no test runner** here — don't claim tests
pass; there are none. (A TanStack/Bun app used to live here; it was removed in commit `749f3d9`.)

## Repos needing special care

Not a repo list — [`RELATED_REPOS.md`](RELATED_REPOS.md) owns that. These are the two
hazards worth knowing before you touch a sibling:

- **`../socialnetwork_toolkit`** — live credentials in git history on every branch. Never
  copy, quote, or summarize its contents anywhere, and never make it public.
- **`../prt`** — being archived, with a harvest pass still pending. Don't start new work there.

A ninth repo, `richbodo/pnt-workshop`, sits outside the org and is a candidate for archiving.

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
plan.md                    summary plan for the SOFTWARE program (M1/M2/M3) — planning layer 1
docs/roadmap.md            where THIS repo is headed — planning layer 3
plans/                     ORG-LEVEL planning: ORG-TASKS.md (the live cross-repo task list)
                           plus dated, append-only planning dumps (`YYYY-MM-DD-<topic>.md`).
                           Read plans/README.md before adding anything.
drafts/                    STUB ONLY — redirect README for old deep links; don't add content here
research/plan.md           STUB ONLY — plan.md moved to the repo root (Aug 2026)
RELATED_REPOS.md           single source of truth for sibling repos and external resources
```

<!-- BEGIN SHARED: org-conventions v1 -->
<!-- Canonical copy: social-network-health/docs/shared/org-conventions.md
     Do not edit this block in place. Edit the canonical copy and propagate. -->

## The organization

Eight repos under the **[social-network-health](https://github.com/social-network-health)**
GitHub org. A developer normally has them **all checked out side by side in one parent
directory**, so from any repo root every other repo is at `../<name>`. Write cross-repo paths
relative to the repo root, never absolute — the parent directory differs per host.

**[`RELATED_REPOS.md`](https://github.com/social-network-health/social-network-health/blob/main/RELATED_REPOS.md)**
in the hub repo is the single source of truth for what those repos are and what each is for.
Don't restate the list in a repo's own docs — a second copy is a second thing to forget.

## Planning has four layers

| # | Question | Lives in |
|---|---|---|
| 1 | "What is the software program?" | hub [`plan.md`](https://github.com/social-network-health/social-network-health/blob/main/plan.md) — the M1/M2/M3 summary |
| 2 | "What should the org be doing?" | hub [`plans/`](https://github.com/social-network-health/social-network-health/tree/main/plans) + `plans/ORG-TASKS.md` |
| 3 | "Where is this repo headed?" | **this repo's** `docs/roadmap.md` |
| 4 | "What's in flight?" | **this repo's** GitHub issues and active branches |

Record a thought at the layer matching its scope.

**Layer 2 is org-only.** Work actionable inside one existing repo belongs in that repo;
`ORG-TASKS.md` links down to it rather than restating its status. **Layer 1 is narrower than
the organization** — `plan.md` summarizes the software and research program, not community
building, the toolkit wiki, or educational materials.

Dated files under `plans/` are append-only thinking artifacts. Never update one; write a new
one. `ORG-TASKS.md` is the sole exception — it is kept current.

## Cross-repo working rules

Each of these was learned the hard way in one repo. They apply in all of them.

- **PR and issue bodies via `--body-file`, never an inline `--body`.** Backticks and `$(…)`
  get shell-interpreted and silently drop content — a commit hash has been lost this way.
- **After a PR merges, verify every intended commit actually landed.** A dropped commit is
  silent; recover it in a follow-up rather than assuming the merge was faithful.
- **Triage every test failure as pre-existing or newly-introduced before shipping.** Stash
  and re-run against the base to tell which. Never absorb a pre-existing red into unrelated
  work, and never claim green while a known red stands.
- **Upstream `main` beats local staging plans.** In a multi-agent setup another agent may
  have already filed, merged, or evolved a cross-repo contribution. Check the upstream repo's
  `main` before developing one further — local `plans/` lag.
- **Fail loudly.** Convert an absent guarantee into a red test or a lint failure, never a
  silent pass. Deferrals carry an honest status marker — a strict-xfail, an `Open`/`partial`
  attestation, a documented "⏳ next" — never a bare `TODO` claiming a property the code
  doesn't deliver.
- **One source of truth per fact.** Restating a fact in a second document creates a drift
  surface. Put it in the doc that owns the category and link from the others.
- **Orient without moving; branch only to work.** Reading and priming never need a branch
  change — in a multi-worktree setup `main` is often checked out elsewhere, so a checkout
  fails or strands uncommitted work. Run `git worktree list` before starting. Repo-specific
  worktree setup and port serialization live in that repo's own sections.

<!-- END SHARED: org-conventions v1 -->

This repo has its own layer-3 work (website, research docs, presentations) in
[`docs/roadmap.md`](docs/roadmap.md). It has historically used **no issue tracker** — website
work is a see-it-live loop and a day of copy editing is often several small PRs. That's
deliberate; durable work goes in the roadmap rather than into issues.

The canonical copy of the shared block above lives here, in
[`docs/shared/org-conventions.md`](docs/shared/org-conventions.md). Edit it there and
propagate — never edit a copy in place.

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

## Session orientation

A `/prime` command (`.claude/commands/prime.md`) exists for deeper session orientation — it reads
the key research docs and confirms which sibling repos are present on the current host.
