# Shared org conventions — canonical copy

**This file is the source of truth for the block below.** Every repo in the
`social-network-health` org carries an identical copy of everything between the `BEGIN
SHARED` and `END SHARED` markers, pasted into its `CLAUDE.md`.

**To change a convention:** edit it here, bump the version in both markers, then propagate
the block to every repo's `CLAUDE.md`. Never edit a repo's copy in place — that's how the
improvement-in-one-repo, regression-in-another pattern starts.

**What belongs in the block:** facts and rules that are true in *every* repo. Anything
repo-specific — ports, `just` recipes, worktree helper scripts, language conventions — stays
in that repo's own `CLAUDE.md` sections, outside the markers.

Repos carrying the block: `social-network-health`, `personal_network_toolkit`, `prm`,
`fellows_local_db`, `snhdb`, `prt`, `snhtoolkitmw`, `socialnetwork_toolkit`.

---

<!-- BEGIN SHARED: org-conventions v2 -->
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

The layout is a convention of the working environment; it could change, but it holds for now.
It lives in `CLAUDE.md` rather than agent memory because **memory is keyed to the working
directory** — a worktree at a different path starts with a fresh memory dir. A committed file
is the only channel that reaches every worktree and every concurrent agent.

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

<!-- END SHARED: org-conventions v2 -->
