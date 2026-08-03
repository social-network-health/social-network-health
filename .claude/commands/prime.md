# Prime — social-network-health (the hub)
> Read-only orientation: understand the org and this repo, then summarize. Do NOT switch
> branches or pull while priming — just orient.

## Run
git ls-files
git status -sb          # branch + ahead/behind + dirty state
just                    # devops + org-upkeep recipes
ls ..                   # which sibling repos are actually present on this host

## Read — the planning stack, top down
plan.md                 # layer 1: the software program in summary (M1/M2/M3)
plans/ORG-TASKS.md      # layer 2: what the whole org should be doing now
docs/roadmap.md         # layer 3: what THIS repo is doing (website, research, presentations)
RELATED_REPOS.md        # the eight repos, what each is for, the localhost port registry

That stack is the point of this repo. `plan.md` is deliberately narrower than the
organization — it covers the software and research program, not community work, the wiki, or
educational materials. Those live at layer 2.

## Read — only if the task calls for it
research/research_library/planning/knowledge-base-plan.md   # before any corpus work
docs/org-upkeep.md                                          # before changing a shared convention
plans/*.md                                                  # dated, append-only; history, not status

Skim the **section headings only** of the long research documents unless the task needs
them: `research/threat_modelling/threat_catalog.md`, `research/measurement/*.md`,
`research/protocols/*.md`.

## Know before you change anything
- **The website is one file:** `public/socialnetwork-health.html` (self-contained HTML + inline
  CSS) plus one SVG. Edit it and `just deploy`. There is no framework, no package manager, and
  **no test runner** — never claim tests pass.
- **The homepage deep-links `research/` files by full GitHub URL.** Moving or renaming a
  research file breaks the live site silently. Update the HTML and redeploy in the same change.
- **`../socialnetwork_toolkit` has live credentials in its git history.** Never copy, quote, or
  summarize its contents anywhere. `../prt` is mid-archive — don't start work there.

## Before summarizing
Give one short paragraph: what this repo is, which sibling repos are present locally, which
planning layer the task belongs at, and anything in flight that touches it. Orientation, not
a report.

$ARGUMENTS
