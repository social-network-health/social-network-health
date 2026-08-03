# plans/

Dated, throwaway-by-design planning dumps for the Social Network Health org — reMarkable
transcriptions, session notes, brainstorm outputs curated for the public record.

## What belongs here (and what doesn't)

This is **cross-repo, org-level, long-horizon** planning: the big-picture direction of the
whole GitHub organization, revisited periodically rather than tracked continuously. It is
deliberately *not* a substitute for the two things that already work:

| Layer | Lives in | Horizon |
|---|---|---|
| "What should the org be doing?" | **here** — `plans/` + `plans/TASKS.md` | months; revisited occasionally |
| "Where is this repo headed?" | that repo's own `ROADMAP.md` / planning docs | weeks–months |
| "What's the next unit of work?" | that repo's **GitHub issues** | days |

Some overlap between the layers is fine and expected. What does *not* belong here is
issue-grade detail — which PR to open, which issue to take first. If a note is only
actionable inside one repo, it belongs in that repo.

These are text files in a repo rather than a GitHub Project board on purpose: the board UX
doesn't fit how this planning actually gets done, and plain markdown is legible to both a
human skimming it once a month and an LLM agent reading it at the start of a session.

**A plan is a thinking artifact, not a live status page.** Reality will overtake these
files, and that's fine — nobody should be keeping them current. `TASKS.md` is the one
exception; see below.

## Conventions

- One file per dump: `YYYY-MM-DD-<topic>.md`. **Append-only** — never update an old plan;
  write a new one. Old plans are reflection material, not living documents.
- The workflow: plan anywhere → dump here → pull the one or two genuinely interesting
  tasks into `TASKS.md` (or a repo issue) → leave the rest alone.
- `plans/TASKS.md` is the live org-level task list — the one file here that *is* kept
  current. Sections: Active / Waiting On / Someday / Done. Task format:
  `- [ ] **[area] Title** - context, links`. Areas:
  `[web] [community] [infra] [designs] [toolkit] [research] [org]`.
- Per-repo work lives in that repo's issues and plans — tasks here link to them
  (`PNT#55`, `prm#66`, `fellows#296`). This list holds only cross-repo, org-level state.
- Uncurated or sensitive brainstorms do **not** go here — they live in the private
  brainstorms repo until reviewed.
