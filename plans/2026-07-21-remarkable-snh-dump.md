# reMarkable dump — SNH project

*Written on the tablet ~2026-07-21 (a few days before transcription); transcribed into the
planning repo 2026-07-24 via Cowork. Throwaway by design — do not update; write a new dump.*

## The list

1. **Redo the SNH website.** Problems top-down: the discussion list is inactive and
   shouldn't be listed; a number of things need rewriting as copy; reorganize. It should be
   clear up front what the project is, right at the top.
   - Subtask: **redo the presentation.** First delivery at DWebCamp revealed what's
     missing. Redo as a video — they come out better.
2. **Search for collaborators.** People ask about funding — don't need it. Need
   collaborators: (a) open-source software orgs that want to do the same kind of research,
   (b) members of my own communities who'll meet once a week, test the software they want
   to use, and develop new features with me.
3. **Vision sidebar:** near-term goal is to hit M1 and M2, then propose M3 to a team that
   can help us conduct experiments within our own communities.
4. **Practical next steps:**
   - Improve the SNHDB (research-paper search + skills).
   - Move MediaWiki out of its current place to DigitalOcean (toolkit.socialnetwork.health).
   - Make MediaWiki Claude Code-editable and administrable — big speedup for that work.
   - Consider a Bluesky discussion group, or Signal, or a Matrix mirror — the email list is
     too high-friction for a lot of people.
5. **Use PRM.** Wrote it for someone else; want to use it myself and make it awesome —
   I kind of need it.
6. **Create the new private repo.** Things kept gitignored on individual machines
   (brainstorming sessions etc.) need a private repo — moving machine to machine loses
   access to gitignored files.
7. **Manage the YouTube video updates.** Someone else does them; check in weekly.
8. **Release a weekly newsletter.**
9. (1, 2, 7, 8 are the community-building things that really need attention now.)

## Reference designs

- **PRM:** make it my favorite contact manager; use it to contact people about this project.
- **fellows_local_db:** keep adding features that pass upstream conformance. New demand
  from that community for **calendaring** (asked just days ago — not yet planned).
- **Vault (new):** the simplest reference design. Backs up all your SaaS systems from
  exports; an agent plugin (OpenClaw?) helps with the exports; ships an **Exit/Interrupt
  (Exit/Interop) Manual** — a wiki: how to export and back up SaaS data, how to replace
  functionality (or not, if impossible), how to interoperate with various SaaS systems.

*Note: these are relatively new and may not appear in the hub repo's `research/plan.md`.*

## Pulled into TASKS.md (2026-07-24)

All nine items + the three reference-design notes were seeded into `TASKS.md` — items
1, 2, 4, 6, 7, 8 and the design notes as Active; 3 as the [research] M1/M2/M3 task;
SNHDB improvement to Someday alongside existing repo issues.
