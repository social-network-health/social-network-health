# plans/

Dated, throwaway-by-design planning dumps for the Social Network Health org — reMarkable
transcriptions, session notes, brainstorm outputs curated for the public record.

## The four planning layers

Planning for this organization is stacked. Each layer answers a different question over a
different horizon, and material should sit at the layer that matches its scope:

| # | Question | Lives in | Horizon |
|---|---|---|---|
| 1 | "What is the software program?" | [`/software-plan.md`](../software-plan.md) — repo root | years; the stable summary |
| 2 | "What should the whole org be doing?" | **here** — `plans/` + [`ORG-TASKS.md`](ORG-TASKS.md) | months; revisited occasionally |
| 3 | "Where is this one repo headed?" | that repo's `docs/roadmap.md` | weeks–months |
| 4 | "What's being worked on right now?" | that repo's **GitHub issues** and active branches | days |

Layer 1 is the summary a newcomer or collaborator should hit first — the M1/M2/M3 steps and
what carries each. Layer 2 is this directory: cross-repo work, and work that has no repo yet.

**Layer 2 is for org-level work only.** If a task is actionable inside a single existing
repo, it belongs in that repo's roadmap or issues — not here. `ORG-TASKS.md` may *link*
down to repo work, but the repo stays the source of truth for its own status. Two copies of
the same fact is how this rots.

What does *not* belong here: issue-grade detail — which PR to open, which issue to take
first.

These are text files in a repo rather than a GitHub Project board on purpose: the board UX
doesn't fit how this planning actually gets done, and plain markdown is legible to both a
human skimming it once a month and an LLM agent reading it at the start of a session.

**A plan is a thinking artifact, not a live status page.** Reality will overtake these
files, and that's fine — nobody should be keeping them current. `ORG-TASKS.md` is the one
exception; see below.

## Conventions

- One file per dump: `YYYY-MM-DD-<topic>.md`. **Append-only** — never update an old plan;
  write a new one. Old plans are reflection material, not living documents.
- The workflow: plan anywhere → dump here → pull the one or two genuinely interesting
  tasks into `ORG-TASKS.md` (or a repo issue) → leave the rest alone.
- `plans/ORG-TASKS.md` is the live org-level task list. Each task carries an immutable
  `<!-- task: SNH-ORG-0001 -->` marker. Preserve it when renaming, moving or completing a
  task; never reuse a removed ID. Allocate the next unused number and run `just check-tasks`.
  The `org-task-register: 1` marker opts the whole file into strict identity validation.
- Section meanings:
  - **Active:** accepted current work. An unchecked box does not prove execution has started.
  - **Waiting On:** accepted work waiting for an identified reply, event or dependency.
  - **Needs review:** untriaged possibilities. No commitment, priority or timing is inferred.
    This replaces the undefined Someday label without changing the underlying tasks.
  - **Watching:** references to work owned elsewhere. Follow the linked source for status;
    these are not extra org tasks and must not be counted as such.
  - **Done:** explicitly completed work, checked off and retained with the same ID.
  - **Cancelled** (when needed): explicitly declined or stopped work, retained with its ID.
  - **Deferred** (when needed): deliberately postponed work; record a reason and a review
    date or condition. It is not a bucket for untriaged ideas.
- `###` headings (community, org, infrastructure, designs) describe topics, not states.
  Stable IDs are independent of either section or topic. Missing owner/due dates remain
  unknown. Do not infer goal completion from the number of checked tasks.
- Per-repo work lives in that repo's issues and plans — tasks here link to them
  (`PNT#55`, `prm#66`, `fellows#296`). This list holds only cross-repo, org-level state.
- Uncurated or sensitive brainstorms do **not** go here — they live in the private
  brainstorms repo until reviewed.
