# Org upkeep — what's guaranteed, and what's on you

Several repos, one or two developers, a lot of agents. This is the whole maintenance story.

**If you read one line:** run `just check-org`. It verifies what can be verified and prints
what it deliberately doesn't.

## The design: three kinds of rule, three kinds of guard

Every process convention in this org fails in one of three ways, and the failure mode — not
the importance of the rule — decides what guards it. Getting this wrong in either direction
is expensive: automating a habit produces brittle machinery that checks nothing, and trusting
memory for cross-repo state produces silent drift.

| | Failure mode | Guard | Examples |
|---|---|---|---|
| **A** | Invisible across repos. No single file or diff reveals it. | **A command.** Human attention doesn't scale across repos. | the shared block in every `AGENTS.md`; the agent files around it; org skills installed and unshadowed |
| **B** | Visible in one diff. A reviewer can see the omission. | **The PR.** | the prime skill not updated for a new load-bearing doc; users guide not updated for a UX change; a dated `plans/` file edited |
| **C** | No artifact at all. The rule shapes an action or it doesn't. | **`AGENTS.md`, and nothing else.** | `--body-file` over inline `--body`; triage reds before shipping; upstream `main` beats local plans; fail loudly |

**Do not build checks for C.** There is nothing to observe. A check that cannot fail is worse
than no check — it manufactures confidence.

## A — the commands

```bash
just check-org           # everything, plus what it doesn't cover
just check-conventions   # the shared block in each AGENTS.md: on disk AND on origin/main
just sync-conventions    # propagate the canonical block to working trees
just check-agent-files   # AGENTS.md size, the one-line CLAUDE.md, skills and their links
just check-skills        # org skills on this workstation, for every agent
just install-skills      # create/repair the symlinks — once per workstation
```

### Why the block check reads `main`, not just disk

They answer different questions, and only one of them is the truth:

- **disk** — "are my working copies consistent right now?" Useful before opening PRs.
- **main** — "is what actually *shipped* consistent?" This is the real state of the org.

Checking only disk is how propagated-but-never-merged work hides. Not hypothetical: the block
was synced locally and PRs were opened, but several merged *before* the follow-up commits
were pushed to their branches — and GitHub does not reopen a merged PR when new commits
arrive on it. Disk stayed green while `main` sat a version behind, invisibly, across most of the org.

The check reports both, and names the states:

| State | Meaning |
|---|---|
| `ok` | disk and main both match canonical |
| `stale` | **warning, exit 0** — main is current; the working tree sits on a branch cut before the block landed. Switch/rebase when you next work there |
| `UNSHIPPED` | correct on disk, not on main — PR open, or **stranded behind an already-merged PR** |
| `BEHIND` | this repo hasn't taken the current version — run `sync-conventions` |
| `EDITED` | the copy was edited in place, which is never correct — including a disk copy claiming the current version with different text while main is green |
| `MISSING` | no block in that `AGENTS.md`, and main doesn't have the current one either |

`main` is the truth; disk is the workstation. Only states where what *shipped* is wrong
(or where disk claims something false) fail the check.

`check-agent-files` reads disk and `main` the same way, for the files around the block: every
repo's `AGENTS.md` under 24,000 bytes, a one-line `CLAUDE.md` (`@AGENTS.md`), a prime skill,
spec-only skill frontmatter, and a `.claude/skills` link for every skill in `.agents/skills`.
The layout and its reasons are at the top of the canonical doc.

`check-skills` is **workstation-scoped** — skills install into each agent's user folder
(`~/.claude/skills`, `~/.agents/skills`, and Antigravity's when it's installed), so there is no
`main` to compare against. Green means *your* machine is set up; it says nothing about a
teammate's.

### Changing a convention

1. Edit **`docs/shared/org-conventions.md`** only. Never a repo's copy.
2. Bump the version in *both* markers (`v4` → `v5`).
3. `just sync-conventions` — rewrites every working tree.
4. Commit and open **one PR per repo**. They're separate repos; there's no way around it.
5. **After merging, run `just check-conventions` again.** `--write` only touches disk, and
   disk being right is not the same as it having shipped.

Anything repo-specific — ports, `just` recipes, worktree scripts, language conventions —
stays outside the markers in that repo's own sections. `sync-conventions` never touches it.

**Adding or removing a repo from the org:** edit the table in
[`docs/shared/org-conventions.md`](shared/org-conventions.md). All three scripts parse that
one table, so it's the only place to change. A repo being archived leaves the table rather than
take new versions, so its frozen copy never fails the check. (`bootstrap` prefers `gh repo list`, which is
self-updating, and falls back to the table.)

**About the hashes** in `check-conventions` output: they're a sha256 of the block *text*,
first 12 characters — not git commits. Identical text produces an identical hash, so **every
repo showing the same value is the success condition**, not a coincidence. A differing hash
means differing bytes.

## B — what the PR is the gate for

No command catches these, because each is visible in the diff of the change that breaks it:

- **The prime skill updated when a load-bearing document or module lands.** Prime is bespoke per
  repo, so no checksum applies — but a prime that misses the file where the invariants live
  sends every future session searching for it.
- **The users guide updated when user-visible behavior changes.** Each app repo already
  states this; accepting the PR accepts the doc change with it.
- **Dated files under `plans/` left alone.** They're append-only thinking artifacts; a diff to
  an old one is the violation, and it's visible.

## C — what lives only in AGENTS.md

The cross-repo working rules in the shared block. They're there because a committed file is
the only channel that reaches every worktree and every concurrent agent — agent memory is
keyed to the working directory, so a worktree at a different path starts empty.

## Shared skills: symlink, never copy

Agents have user-level and repo-level skills. There is **no org level**, so an org skill is
built from one of those:

| Mechanism | Drifts? | Use for |
|---|---|---|
| **Symlink** from each agent's user folder (`~/.agents/skills/<name>`, `~/.claude/skills/<name>`, …) → the owning repo | never — it *is* upstream | **the default** |
| **Vendored copy** in a repo's `.agents/skills/` | silently, and fast | only with a pinned commit and a re-sync plan |

A repo's *own* skills — its prime, say — are different: they live in that repo's
`.agents/skills/` and nowhere else, with a `.claude/skills` link for Claude Code.

Learned the expensive way: `fellows_local_db` vendored the PNA Toolkit skill with a provenance
note honestly predicting drift. It drifted — ten commits behind, a rename behind, and a whole
flow behind — so a session there offered two skills with near-identical trigger text, one
stale, and nothing said which to prefer.

The registry and the rename aliases are at the top of
[`tools/org/org_skills.py`](../tools/org/org_skills.py), with the folders each agent reads
(`TARGETS`). Add a row when the org publishes a skill, or renames one. **Agents discover skills
at session start — restart them after installing.**

## Onboarding a workstation — and staying current

One command does both. Clone this repo first, then:

```bash
just bootstrap      # clone what's missing, refresh what isn't, install the skills
just check-org      # verify
```

`bootstrap` is **safe to run any time** — it's the new-machine setup *and* the routine
"bring everything up to date" command. It gets the repo list from `gh repo list`, so a repo
added to the org shows up without anyone editing a list. Without `gh` it falls back to the
list in `docs/shared/org-conventions.md` and says so.

### The safety contract

`bootstrap` will **never** `checkout`, `reset`, `stash`, `merge`, or force anything, and it
never touches a dirty working tree beyond fetching refs. Concretely:

| Your repo | What happens |
|---|---|
| missing | cloned to `../<name>` |
| clean, on `main` | fast-forwarded |
| clean, on a feature branch | `main` ref fast-forwarded; **you stay on your branch** |
| dirty | refs fetched, working tree untouched, reported as `DIRTY` |
| private, no access | reported as `CLONE FAILED`; everything else still proceeds |

The worst case is that `main` moves forward while you sit on a feature branch — which is what
you wanted anyway. `just bootstrap-dry` shows what it would do without doing it.

Restart your agents afterwards: skills are discovered at session start.

## The agents on a workstation

Every repo's `AGENTS.md` and prime skill work in all four of these (verified 2026-10-17), and
`just install-skills` links the org skills for each. Re-run it after installing a new agent.

| Agent | Install, then sign in | Notes |
|---|---|---|
| Claude Code | — | Reads `AGENTS.md` through the one-line `CLAUDE.md`. `/prime` |
| Codex | `brew install --cask codex` (or `npm install -g @openai/codex`); `codex login` with a ChatGPT account | `$prime`. Headless: `codex exec -s read-only '$prime'` |
| Antigravity CLI (`agy`) | Google's installer puts it in `~/.local/bin`; sign in with a Google account | `/prime`. Headless (`agy -p`) can't run shell commands until they're allowed in its `settings.json` (`permissions.allow`, e.g. `command(git status -sb)`) |
| OpenCode on Ollama | `brew install opencode`; Ollama 0.15 or later, and a local model | Agents need a 64k context; Ollama gives 32k on a 32 GB Mac and less on smaller ones. Make a 64k alias — a Modelfile with `FROM <model>` and `PARAMETER num_ctx 65536`, then `ollama create <alias> -f Modelfile` — and add an `ollama` provider for it to `~/.config/opencode/opencode.json` (base URL `http://localhost:11434/v1`). Small models (4B) follow the files but get details wrong; prefer 20–30B if memory allows |

## When a check fails

**Investigate it.** These checks exist because the drift they catch is otherwise invisible, so
a failure is information you cannot get another way. If one becomes noisy, brittle, or starts
failing for a reason you don't understand, that's a bug in the check worth fixing — not a
reason to stop running it or to work around it.

## When to automate further

Not yet. For one or two developers with rare convention changes, these commands are enough.
The problem was never that changes were hard to make; it was that drift was invisible.

If it starts to hurt, in order: `check-org` in CI (awkward — it needs sibling checkouts), a
pre-push hook in the hub, then a bot that opens the per-repo PRs. Each adds maintenance and
failure modes of its own.

One note from experience: when you find you've broken a rule you had already written down, the
fix is usually a check, not more words in the rule. Adding emphasis to a sentence nobody
re-read at the critical moment changes nothing. That is how the `main` comparison came to
exist.
