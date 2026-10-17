# Shared org conventions — canonical copy

**This file is the source of truth for the shared block.** Every repo in the table below
carries an identical copy of it in its `AGENTS.md`.

**Where does the block start?** At the horizontal rule below — **everything after that line
is the block.** It's delimited by `<!-- BEGIN SHARED … -->` / `<!-- END SHARED … -->`, but
those are *HTML comments*: they're what the tooling matches on, and they are **invisible in a
rendered Markdown view**. If you went looking for them and found nothing, that's why — view
the raw source to see them. The rule below is here so the boundary is visible either way.

**To change a convention:** edit it here, bump the version in both markers, then run
`just sync-conventions` to propagate. Never edit a repo's copy in place — that's how the
improvement-in-one-repo, regression-in-another pattern starts, and `just check-conventions`
reports it as `EDITED`.

**What belongs in the block:** facts and rules true in *every* repo. Anything repo-specific —
ports, `just` recipes, worktree helper scripts, language conventions — stays in that repo's
own `AGENTS.md` sections, outside the markers, where the tooling never touches it.

**The files every repo in the table keeps** (checked by `just check-agent-files`):

- `AGENTS.md` — the repo's instructions, with this block in it. Under 24,000 bytes, because
  Antigravity CLI truncates longer files and Codex caps them at 32 KiB.
- `CLAUDE.md` — one line, `@AGENTS.md`, plus only lines that make sense for Claude alone.
  Claude Code reads `AGENTS.md` by itself only when no `CLAUDE.md` exists; the import makes it
  read the same file everywhere, including the Agent SDK.
- `.agents/skills/<name>/SKILL.md` — the repo's skills, in the cross-tool layout that Codex,
  Antigravity, OpenCode and most other agents read. Every repo has a `prime` skill.
- `.claude/skills/<name>` — a symlink to `../../.agents/skills/<name>`, because Claude Code
  doesn't read `.agents/skills` yet. No Claude-only skills.

*This table is the tooling's source of truth for which repos carry the block — add or remove
a repo here when the org gains or loses one.*

| Repo carrying the block |
|---|
| `social-network-health` |
| `personal_network_toolkit` |
| `prm` |
| `fellows_local_db` |
| `snhdb` |
| `snhtoolkitmw` |
| `snh-aios` |

**Not in the table, on purpose:** `snh-private` is a private data store, not a code repo.
Repos being archived leave the table rather than take new versions: `prt` keeps the v7 block it
already has until it's archived.

---

<!-- BEGIN SHARED: org-conventions v8 -->
<!-- Canonical copy: social-network-health/docs/shared/org-conventions.md
     Do not edit this block in place. Edit the canonical copy and propagate. -->

> **⚙ Shared, generated section — don't edit it here.** Everything from this line down to
> *"Changing this block"* is identical in every repo that carries it (listed in the hub's
> `docs/shared/org-conventions.md`). Change it in the canonical copy and run
> `just sync-conventions`; an edit made in place will be reported as `EDITED` and then
> overwritten. Repo-specific guidance belongs in this file's *other* sections, which the
> tooling never touches.

## The project

**Social Network Health (SNH)** studies the health of the social networks people live in, and
how a community can keep them healthy. It works in two strands:

- **Field studies**, about one a year, each run with a collaborator in a different setting.
  Field Study 1 studied Networks of Support's training work in schools and the military; its
  key findings are on the toolkit wiki, https://toolkit.socialnetwork.health. Each later field
  study publishes its own.
- **Software**: Personal Network Applications (PNAs) — user-owned apps for relationship data,
  built as reference designs and specs, first for remote, digitally connected communities.
  Most of these repos are that work.

A **key finding** is one that all three of these attest: a **practitioner** says it is a key
finding; **participants** in an intervention experienced it and can describe it; a
**researcher** states it is a key finding in social network health. Missing any one, call it a
finding. A finding from one setting doesn't automatically apply in another.

Anything about a real person — in code, docs, issues, commit messages, or video text — follows
the hub's
[publication standard](https://github.com/social-network-health/social-network-health/blob/main/docs/publication-standards/identifiable-people.md).

Where to look: findings → the toolkit wiki; research evidence → `snhdb`, the research library;
videos → https://www.youtube.com/@SocialNetworkHealth; every repo → the hub's
`RELATED_REPOS.md`. **Team members:** give your agent the project brief too — `snh-brief.md`,
from the team dashboard (https://dashboard.socialnetwork.health, *For AIs*) or the private
`snh-aios` repo.

## The organization

The repos of the **[social-network-health](https://github.com/social-network-health)** GitHub
org. A developer normally has them **all checked out side by side in one parent directory**,
so from any repo root every other repo is at `../<name>`. Write cross-repo paths relative to
the repo root, never absolute — the parent directory differs per host.

The set changes as repos are added and archived, so no document states a count; ask the org
(`gh repo list social-network-health`) or read `RELATED_REPOS.md`.

**[`RELATED_REPOS.md`](https://github.com/social-network-health/social-network-health/blob/main/RELATED_REPOS.md)**
in the hub repo is the single source of truth for what those repos are and what each is for.
Don't restate the list in a repo's own docs — a second copy is a second thing to forget.

The layout is a convention of the working environment; it could change, but it holds for now.
It lives in `AGENTS.md` rather than agent memory because **memory is keyed to the working
directory** — a worktree at a different path starts with a fresh memory dir. A committed file
is the only channel that reaches every worktree and every concurrent agent.

## Agents, instructions, and skills

We work with several agents — Claude Code, OpenAI Codex, Gemini (Antigravity CLI), and local
models (OpenCode on Ollama) — so everything here is written for any of them:

- **`AGENTS.md` is the instructions file**, read natively by every agent above. `CLAUDE.md` is
  one line, `@AGENTS.md`, so Claude Code reads the same file. Nothing Claude-only goes in
  `AGENTS.md`.
- **Skills live in `.agents/skills/<name>/SKILL.md`**, with a `.claude/skills/<name>` link for
  Claude Code. Frontmatter is the open Agent Skills spec's: `name` and `description`, nothing
  tool-specific. The org's shared skills (such as `snhb` and `snhdb`) are installed for every
  agent by `just install-skills` in the hub.
- **Every repo has a `prime` skill**: its reading list for a new session (`/prime` in Claude
  Code, `$prime` in Codex).

## Planning has four layers

| # | Question | Lives in |
|---|---|---|
| 1 | "What is the software program?" | hub [`software-plan.md`](https://github.com/social-network-health/social-network-health/blob/main/software-plan.md) — the M1/M2/M3 summary |
| 2 | "What should the org be doing?" | hub [`plans/`](https://github.com/social-network-health/social-network-health/tree/main/plans) + `plans/ORG-TASKS.md` |
| 3 | "Where is this repo headed?" | **this repo's** `docs/roadmap.md` |
| 4 | "What's in flight?" | **this repo's** GitHub issues and active branches |

Record a thought at the layer matching its scope.

**Layer 2 is org-only.** Work actionable inside one existing repo belongs in that repo;
`ORG-TASKS.md` links down to it rather than restating its status. **Layer 1 is narrower than
the organization** — `software-plan.md` summarizes the software and research program, not community
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
- **A sync rule without a mechanical check is a wish.** Anything that must hold in more than
  one repo ships with a command that verifies it, and the rule names the command. Nobody
  eyeballs every repo by hand, so silent drift is the default outcome otherwise.
- **Add a load-bearing document or module → update the `prime` skill
  (`.agents/skills/prime/SKILL.md`) in the same PR.** Priming is how every agent gets its
  systems-level picture of a repo, and a prime that misses the file where the invariants live
  sends every future session searching for it. This is the same rule as "a user-visible change
  updates the users guide in the same PR", applied to the agent's entry point. Prime is bespoke
  per repo, so no checksum catches this one — the PR is the only gate.
- **Prime is expensive; not priming is more expensive.** `AGENTS.md` loads every session, so
  it holds what is always true and stays short. Prime is opt-in and costs tokens, so it holds
  the *reading list* — which files give systems-level understanding, and which to skim rather
  than read. Keep prime curated: name the seams, never glob a directory.
- **Brainstorms are private and live in `snh-private`, never in a public repo.** Use the
  **`snhb`** skill: it captures to `../snh-private/brainstorms/<this repo>/`, checkpoints
  after every answer, and commits at session end so the thinking follows you between
  machines. It also *searches* every repo's brainstorms — ask it what you previously decided
  about something rather than re-deriving it. They're private because unreviewed thinking
  wastes the reader's time, not because it's secret; when one is worth publishing, review it
  and put a **cleaned copy** in the public destination, leaving the original where it is.

## Changing this block

This block is generated. To change it: edit the canonical copy, bump the version in both
markers, run `just sync-conventions` from the hub repo, then open one PR per repo.
`just check-conventions` verifies every copy matches; `just check-org` runs every org check.
Full procedure: hub `docs/org-upkeep.md`.

<!-- END SHARED: org-conventions v8 -->
