# Tasks

The live org-level task list. Cross-repo and long-horizon only — see [`README.md`](README.md)
for what belongs here versus in a repo's roadmap or issues.

## Active

- [ ] **[web] Redo the SNH website** - clear "what this is" at the top, rewrite copy, reorganize (`public/socialnetwork-health.html`). Inactive discussion list already dropped (2026-07-25, `4d55fce`). NOTE: homepage deep-links files in `research/` — the plan/research restructure below changes paths, so update links + redeploy together
- [ ] **[web] Redo the DWebCamp talk as a video** - first delivery surfaced the gaps; video comes out better (deck: `presentations/dwebcamp-berlin-2026/`)
- [ ] **[org] Restructure the plan + research/ layout** - move `research/plan.md` → repo root; merge the two egocentric measurement docs; new `positioning/` folder (move `social_cohesion.md` there); recast plan steps as processes-with-milestones; full punch list in `plans/2026-07-24-cowork-session-notes.md` (Claude Code job)
- [ ] **[org] Write the positioning / vision doc** - so collaborators orient to Rich's focus; supportive of other directions, clear about his own
- [ ] **[org] Formally archive prt — harvest first** - pre-meeting-review idea → prm; import-pipeline sophistication → prm; scan 19 issues for PNT bits; add "prm is the successor" to README; then archive on GitHub (list in session notes)
- [ ] **[community] Write the collaborator ask** - not funding: OSS orgs doing the same research + community members for weekly test-and-build sessions
- [ ] **[community] Pick a lower-friction discussion venue** - Signal group is the leading candidate (open source, API — signal-cli bots could capture meeting minutes to feed weekly planning); Bluesky / Matrix as alternatives
- [ ] **[community] Ship SNH newsletter #1** - weekly cadence target thereafter
- [ ] **[community] Weekly YouTube check-in** - recurring; sync with the video editor on updates
- [ ] **[infra] Create the private brainstorms repo** - uncurated/sensitive brainstorms + gitignored-sync stuff only; starter bundle ready. Name TBD ("snh-brainstorms" is the placeholder); expect several categories of dev-group-private material, not just brainstorms
- [ ] **[infra] Move the toolkit MediaWiki to DigitalOcean** - `socialnetwork_toolkit` + `snhtoolkitmw` reactivation (dormant since 2024)
- [ ] **[infra] Make MediaWiki Claude-editable and administrable** - agent-run wiki ops; big speedup for toolkit content (follows the move)
- [ ] **[designs] Dogfood PRM; get it to "usable"** - a few features away; make it the daily contact manager, use it for project outreach
- [ ] **[designs] Fellows calendaring — design the events registry** - EHF board request (2026-07-22); privacy-preserving global event calendar in fellows_local_db; centralized-first-decentralize-later OK; brief in session notes; design starts ~2026-08-01 (post-vacation)
- [ ] **[designs] Scope Vault** - simplest reference design: OpenClaw-assisted SaaS export backup + the "Exit/Interop Manual" wiki; includes exploring how to SECURE OpenClaw/AI-OS-automation behavior
- [ ] **[research] Recast M1/M2/M3 as processes with milestones** - they're ongoing processes that hit milestones, not one-shot deliverables; define the milestone tests + process cadences (M1: fellows in real use + PRM usable + Vault started; M2: needs ≥1 community on step-1 tools)

## Waiting On

- [ ] **PRM v0.2 merge → PNT graduation wave** - in final testing since 2026-06-27; unblocks the data-floor trio + EX-H7 fail-closed + AI-write tiers upstream (PNT roadmap Tier 1)

## Someday

- [ ] **[community] Weekly-prep automation** - Cowork scheduled task: prep newsletter, YouTube check-in, outreach + a low-stress agenda for the weekly meeting (initially Rich + 1–2 helpers); feed it Signal meeting minutes via signal-cli bots. Set up once the meeting/venue exists
- [ ] **[community] EHF yearly fellows newsletter** - opt-in; gauge interest by contacting all fellows; run it if enough opt in
- [ ] **[designs] Improve SNHDB** - multi-perspective research summaries (snhdb#3), corpus repair plan, toolkit-site AI search
- [ ] **[toolkit] PNT Tier 2 surfaces** - `/pna-evaluate` audit UX (PNT#55), plain-language validator (PNT#62), papers → publication, ref-drift lint
- [ ] **[org] Ideas repo: public or private?** - then create it
- [ ] **[infra] Secret hygiene on the wiki repos → make them public**

## Done

- [x] ~~Decide where org planning lives~~ (2026-07-24 — public, in the hub repo; brainstorms stay private)
- [x] ~~Full org review: repos, roadmaps, issues + reMarkable dump synthesis~~ (2026-07-24, Cowork)
- [x] ~~Deliver the DWeb Camp Berlin 2026 talk~~ (2026-07 — deck + PDF in `presentations/dwebcamp-berlin-2026/`)
- [x] ~~**[infra]** Add planning files to the hub repo (public)~~ (2026-08-03 — `plans/` + `plans/TASKS.md`, this bundle)
