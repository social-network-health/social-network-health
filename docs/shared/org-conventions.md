# Shared org conventions — canonical copy

**This file is the source of truth for the shared block.** Every repo in the
`social-network-health` org carries an identical copy of it, pasted into its `CLAUDE.md`.

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
own `CLAUDE.md` sections, outside the markers, where the tooling never touches it.

*This table is the tooling's source of truth for which repos carry the block — add or remove
a repo here when the org gains or loses one.*

| Repo carrying the block |
|---|
| `social-network-health` |
| `personal_network_toolkit` |
| `prm` |
| `fellows_local_db` |
| `snhdb` |
| `prt` |
| `snhtoolkitmw` |
| `socialnetwork_toolkit` |

---

<!-- BEGIN SHARED: org-conventions v6 -->
<!-- Canonical copy: social-network-health/docs/shared/org-conventions.md
     Do not edit this block in place. Edit the canonical copy and propagate. -->

> **⚙ Shared, generated section — don't edit it here.** Everything from this line down to
> *"Changing this block"* is identical in every repo in the org. Change it in the canonical
> copy (hub `docs/shared/org-conventions.md`) and run `just sync-conventions`; an edit made
> in place will be reported as `EDITED` and then overwritten. Repo-specific guidance belongs
> in this file's *other* sections, which the tooling never touches.

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
It lives in `CLAUDE.md` rather than agent memory because **memory is keyed to the working
directory** — a worktree at a different path starts with a fresh memory dir. A committed file
is the only channel that reaches every worktree and every concurrent agent.

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
- **Add a load-bearing document or module → update `.claude/commands/prime.md` in the same
  PR.** Priming is how every agent gets its systems-level picture of a repo, and a prime that
  misses the file where the invariants live sends every future session searching for it. This
  is the same rule as "a user-visible change updates the users guide in the same PR", applied
  to the agent's entry point. Prime is bespoke per repo, so no checksum catches this one —
  the PR is the only gate.
- **Prime is expensive; not priming is more expensive.** `CLAUDE.md` loads every session, so
  it holds what is always true and stays short. Prime is opt-in and costs tokens, so it holds
  the *reading list* — which files give systems-level understanding, and which to skim rather
  than read. Keep prime curated: name the seams, never glob a directory.

## Changing this block

This block is generated. To change it: edit the canonical copy, bump the version in both
markers, run `just sync-conventions` from the hub repo, then open one PR per repo.
`just check-conventions` verifies every copy matches; `just check-org` runs every org check.
Full procedure: hub `docs/org-upkeep.md`.

<!-- END SHARED: org-conventions v6 -->
