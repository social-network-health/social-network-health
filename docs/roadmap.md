# Hub repo roadmap

*Planning layer 3 — where **this repo** is headed over the next weeks to months.*

This repo is both the org's home and a working repo with its own surfaces: the website, the
research documents, and the presentations. Org-wide direction lives one layer up in
[`../plans/ORG-TASKS.md`](../plans/ORG-TASKS.md); the summary plan is [`../software-plan.md`](../software-plan.md).

## How work happens here

Historically this repo has used **no issue tracker** — 56 PRs and zero issues by the time the
2026-08-04 rebuild reset both counters to zero (see `plans/ORG-TASKS.md`). That wasn't an
oversight: the website work is a see-it-live loop, and a day of copy editing can be five or ten
small PRs because you have to watch it running to know what it needs. That pattern stays.

What changes is that the *durable* work — the things that survive a single editing session —
gets written down here instead of living in someone's head or drifting into the org task list.

## Now

### Redo the website

The biggest single item. `public/socialnetwork-health.html` needs:

- A clear "what this is" statement **at the top** — currently a visitor has to work it out.
- A copy rewrite throughout.
- Reorganization of the cards/sections.

Already done: the inactive discussion list was dropped and the footer simplified (2026-07-25,
`4d55fce`).

**Constraint:** the homepage deep-links files in `research/` by full GitHub URL. Any research
file that moves or gets renamed breaks the site silently. Update the HTML and `just deploy` in
the same change. (`software-plan.md` moved to the root in Aug 2026 and was renamed 2026-08-04 — the
homepage never linked it, so both were free.)

### Finish the research/ restructure

Two items remain from the 2026-07-24 punch list
([`../plans/2026-07-24-cowork-session-notes.md`](../plans/2026-07-24-cowork-session-notes.md)):

1. **Reconcile the two egocentric-measurement docs.**
   `research/measurement/community-network-health-explainer.md` (the architecture-pattern take)
   and `research/measurement/egocentric_to_community_network_health_research_note.md` (the
   research note) cover much of the same ground. Differentiate them first, *then* merge into
   one document plus — if needed — a small note holding the non-overlapping remainder.
2. **Create `positioning/`** and move `research/measurement/social_cohesion.md` into it. It's
   historical positioning, not measurement research.

Both change paths the homepage links to. See the constraint above.

### Recast the plan's steps as processes with milestones

`software-plan.md` presents Steps 1–3 as if they were deliverables. They're **ongoing processes that hit
milestones**. Each step needs its process, its cadence, and its milestone test stated. Honest
status for the recast:

- **M1 (Step 1)** — close. `fellows_local_db` is a real reference design with real users; PRM is
  a few features from usable; Vault should start as a third Step-1 use case. Step 1 is never
  "done" — a safe place for relationship data has to track a changing environment.
- **M2 (Step 2)** — implementable solo at any time, but only *meaningful* once a community is
  using Step-1 tools. The fellows and PRM communities are both candidates.
- **M3 (Step 3)** — propose to a research team once M1 and M2 are demonstrably underway.
  Defined by its gate, not its deliverable.

## Next

### The positioning / vision doc

Lands in the new `positioning/` folder. Purpose: let collaborators orient to what Rich himself
is working on — supportive of adjacent directions people bring, clear about his own focus.
Blocked on `positioning/` existing.

### Redo the DWeb Camp talk as a video

The Berlin delivery surfaced what the talk was missing, and video comes out better than a
repeat live delivery. Source deck: `presentations/dwebcamp-berlin-2026/deck/` (Slidev — run it
with `just slides`). The delivered PDF stays as the record of what was actually presented.

## Later

- **Link hygiene sweep.** *This repo is clean* — its only `github.com/richbodo/` links point at
  `pnt-workshop`, which really does sit outside the org. The sibling repos still carry stale
  org links; tracked in [`../plans/ORG-TASKS.md`](../plans/ORG-TASKS.md). (Local git remotes
  were fixed 2026-08-03.)
- **Research library surfacing.** How `snhdb` and the toolkit wiki's AI search show up on the
  site — depends on the wiki move, which is org-level.

## Not in this repo

Software (PNA Toolkit, PRM, fellows_local_db, snhdb) lives in sibling repos — see
[`../RELATED_REPOS.md`](../RELATED_REPOS.md). Cross-repo and no-repo-yet work is org-level and
belongs in [`../plans/ORG-TASKS.md`](../plans/ORG-TASKS.md).
