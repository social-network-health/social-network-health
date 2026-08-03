# Org upkeep — keeping eight repos consistent

Developer documentation for the things that have to stay the same across every repo in the
organization: the shared `CLAUDE.md` block, and the shared Claude Code skills.

**Everything here is one `just` command.** Run `just check-org` if you don't know which you
need — it runs all of them.

## The rule

> **A sync rule without a mechanical check is a wish.**
>
> Every convention in this org that must hold in more than one repo ships with a command
> that verifies it, and the rule names that command. If you can't name the check, the
> convention will drift and nobody will notice.

This is the cross-repo sibling of the rule each app repo already has — *"any change a user
would notice MUST update the users-guide in the same PR."* That one works because a human
reviewing the PR sees the missing doc change: the check is social, and it's local to one
repo and one diff.

Cross-repo rules get no such help. Nobody eyeballs eight repos, and the failure is silent —
you fix something in one repo, forget the others, and find out weeks later when an agent
follows stale guidance. That's the pattern this document exists to stop.

So the checks below are deliberately cheap: no CI, no hooks, no pre-commit. Just commands
short enough to run casually.

## The shared CLAUDE.md block

Every repo's `CLAUDE.md` carries an identical block between
`<!-- BEGIN SHARED: org-conventions vN -->` and the matching `END` marker. It holds only what
is true in *every* repo — the org and sibling convention, the four planning layers, and the
cross-repo working rules.

The canonical copy is [`docs/shared/org-conventions.md`](shared/org-conventions.md) in this
repo. Every other copy is generated from it.

```bash
just check-conventions    # all eight identical to canonical?
just sync-conventions     # propagate canonical into every repo
```

### To change a convention

1. **Edit `docs/shared/org-conventions.md` only.** Never a repo's copy — editing in place is
   exactly how the improvement-in-one-repo, regression-in-another pattern starts.
2. Bump the version in *both* markers (`v2` → `v3`).
3. `just sync-conventions` — rewrites the block in all eight.
4. `just check-conventions` — confirm.
5. Commit and open **one PR per repo**. They're separate repos; there's no way around this.

### What does not go in the block

Anything repo-specific: ports, `just` recipes, worktree helper scripts, language conventions,
the local documentation map. Those live in that repo's own `CLAUDE.md` sections, outside the
markers, and `sync-conventions` never touches them.

## Shared skills

Claude Code has user-level and repo-level skills. It has **no org level**, so an org skill is
built out of one of those — and the choice matters:

| Mechanism | Drifts? | Use for |
|---|---|---|
| **Symlink** `~/.claude/skills/<name>` → the owning repo | never — it *is* upstream | **the default for every org skill** |
| **Vendored copy** in a repo's `.claude/skills/` | silently, and fast | only with a pinned commit and a deliberate re-sync plan |

We learned this the expensive way: `fellows_local_db` vendored the PNA Toolkit skill with an
honest provenance note predicting it would drift. It did — a rename and several flows behind
upstream, which meant a fellows session offered two skills with near-identical trigger text,
one of them stale. The model could pick either.

```bash
just install-skills    # create/repair the symlinks (once per workstation)
just check-skills      # symlinked, current, and unshadowed?
```

`check-skills` also flags vendored copies that duplicate an org skill, and recognizes former
names so a renamed copy is caught rather than reported as something unrelated.

The registry lives at the top of [`tools/org/org_skills.py`](../tools/org/org_skills.py) —
add a row when the org publishes a new shared skill, and a row to `ALIASES` when one is
renamed.

**Claude Code discovers skills at session start.** Restart after installing.

### Onboarding a workstation

```bash
git clone <the org repos>   # all at one filesystem level — see RELATED_REPOS.md
cd social-network-health
just install-skills
just check-org
```

## What is deliberately *not* shared

**`prime`.** Each repo's `.claude/commands/prime.md` is bespoke and should stay that way.
`CLAUDE.md` is loaded on every session unconditionally, so it holds what is always true and
must stay short. Priming is opt-in and costs tokens, so it holds the *reading list* — which
files to read to get oriented here, in what order, and which to only skim. Those lists differ
per repo because the repos differ.

Prime is expensive; not priming is more expensive.

## When to automate further

Not yet. For two developers with rare convention changes, these commands are enough — the
problem was never that changes were hard to make, it was that drift was invisible.

The natural next steps, in order, when they start to hurt:

1. `just check-org` in each repo's CI (needs sibling checkouts in CI, which is the awkward part)
2. A pre-push hook in the hub
3. A bot that opens the eight PRs for you

Each adds maintenance and failure modes of its own. Don't reach for them until the manual
loop is genuinely annoying.
