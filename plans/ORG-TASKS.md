# Org tasks

The live **org-level** task list — planning layer 2. Cross-repo work, and work that has no
repo yet. Anything actionable inside a single existing repo belongs in that repo's roadmap
or issues instead; see [`README.md`](README.md) for the four layers.

*Reconciled against every org repo 2026-08-03. Items that turned out to be repo-level were
filed down and now appear only under [Watching](#watching).*

## Active

### community

- [ ] **Write the collaborator ask** - not funding: OSS orgs doing the same research + community members for weekly test-and-build sessions
- [ ] **Pick a lower-friction discussion venue** - Signal group is the leading candidate (open source, API — signal-cli bots could capture meeting minutes to feed weekly planning); Bluesky / Matrix as alternatives
- [ ] **Ship SNH newsletter #1** - weekly cadence target thereafter
- [ ] **Weekly YouTube check-in** - recurring; sync with the video editor on updates

### org

- [ ] **Write the positioning / vision doc** - so collaborators orient to Rich's focus; supportive of other directions, clear about his own. Deliverable lands in the hub repo's new `positioning/` folder — see [`../docs/roadmap.md`](../docs/roadmap.md)
- [ ] **Formally archive prt — harvest first** - three harvest passes, not one: (1) **the open issues** — ~7 of 19 carry real concept material, strongest are prt#147 (CRT/PRT notification protocol, unbuilt and captured nowhere else), prt#145 (small models can't chain bespoke per-lookup tools — give them one general SQL tool), prt#69 (confirm a new relationship against a rendered diagram of it), prt#37 (the decision record for rejecting SQLCipher); (2) **the code** — import-pipeline sophistication is *not* in the backlog, every import issue is closed; it lives in `prt_src/google_takeout.py`, `prt_src/google_contacts.py`, `cli_modules/services/import_google.py` + the Google People schema docs; (3) **`ROADMAP.md`** — self-declared obsolete but its "FUN FACTORS" section is transcribed brainstorm material worth mining. Then add a "PRM is the natural successor" note to the README and archive on GitHub. Substantive work stopped 2026-01-12
- [ ] **Point the shared `CLAUDE.md` block at the publication standard (block v8)** - `docs/publication-standards.md` binds every repo, but nothing currently tells an agent working in prm or PNT that it exists. The shared block is the only channel that reaches every repo and every session, so it needs one line pointing at it — the same mechanism that carried the `snhb` rule in v7. Costs a full propagation round: edit the canonical copy, `just sync-conventions`, one PR per repo. Worth batching with the next block change rather than spending a round on one line
- [ ] **Repo-by-repo consistency review** - walk each live repo with Rich: are its roadmap and issues current and mutually consistent? Then prioritize across the org. Known drift going in: PNT's `docs/roadmap.md` snapshot is dated 2026-06-27 and misses the July waves; `fellows_local_db/ROADMAP.md` is 4 dead lines while real planning lives in its `plans/`; root-`ROADMAP.md`-vs-`docs/roadmap.md` is inconsistent across the org (both root ones are dead, both `docs/` ones are alive)

### infra

- [ ] **Rotate the wiki credentials** - `socialnetwork_toolkit` has plaintext live credentials in its README (database, wiki admin, cPanel, FTP, a named developer's account) plus the production IP and SSH usernames; more in `C2_S3_Config/` (restic password, S3/B2 keys) and both `LocalSettings.php` files (`$wgDBpassword`, `$wgSecretKey`, `$wgUpgradeKey`). All of it is in git history on every branch, so deleting files achieves nothing — this is rotation, not scrubbing. ~2 years exposed. Order: **rotate → verify services → retire the repo**. The repo stays private; "make it public" is off the table
- [ ] **Replace the credential-sharing channel with the MediaWiki developer** - the secrets were checked in precisely to share them with the developer who built the MediaWiki mods. Needs a real mechanism (shared secret store / age-encrypted file / password manager sharing) before or alongside rotation, or the same thing happens again
- [ ] **Rebuild the toolkit wiki on DigitalOcean** - `socialnetwork_toolkit` + `snhtoolkitmw` reactivation (dormant since 2024-08-06). Significant cost saving over the current host. Neither repo has ever contained provisioning automation — `.gitmodules.safe` (61 submodules: 55 extensions, 4 skins, vendor) plus a manual README procedure is the whole deploy story, and `C2_S3_Config/backup.sh` is the only script. This repo's own Ansible + Caddy setup in `ops/` is the obvious template. `snhtoolkitmw` is already the sanitized successor, so the payload/secrets split is done — retire `socialnetwork_toolkit` rather than refactor it
- [ ] **Make the wiki Claude-editable and administrable** - agent-run wiki ops; big speedup for toolkit content. Follows the move
- [ ] **Point remaining doc links at the org** - local git remotes were fixed 2026-08-03, but in-repo markdown across several repos still says `github.com/richbodo/...`. Redirects cover it; clean it up before collaborators arrive

### designs

- [ ] **Dogfood PRM; get it to "usable"** - make it the daily contact manager and use it for project outreach. The feature gap is filed as a PRM issue — see [Watching](#watching)
- [ ] **Scope Vault** - the simplest reference design, and the only Step-1 use case with no repo yet. SaaS export backup with an OpenClaw-assisted export plugin, plus the "Exit/Interop Manual" wiki (how to export and back up each SaaS, how to replace functionality or not, how to interoperate). Research edge: AI-OS automation for fast SaaS export, **and how to secure OpenClaw's behavior** — largely unexplored. Shares a feature set with PRM's contact-research work (dedupe, unify, enrich from public sources) — expect to develop them alongside each other

## Waiting On

*(nothing — the PRM v0.2 → PNT graduation wave cleared when PRM v0.2 shipped; it's now tracked in PNT)*

## Someday

- [ ] **[community] Weekly-prep automation** - Cowork scheduled task: prep newsletter, YouTube check-in, outreach + a low-stress agenda for the weekly meeting (initially Rich + 1–2 helpers); feed it Signal meeting minutes via signal-cli bots. Set up once the meeting/venue exists
- [ ] **[community] EHF yearly fellows newsletter** - opt-in; gauge interest by contacting all fellows; run it if enough opt in
- [ ] **[org] Ideas repo: public or private?** - then create it
- [ ] **[infra] Toolkit-site AI search** - `snhdb` powering search on toolkit.socialnetwork.health; depends on the wiki move

## Watching

*Repo-level work that the org cares about. The repo is the source of truth for status — these
are links, deliberately without status claims. Do not restate progress here.*

| What | Where |
|---|---|
| PNT graduation wave — the three PRM spec riders | PNT#64 |
| PNT graduation wave — data-floor trio + EX-H7 fail-closed | PNT#119 |
| PNT roadmap stale; three brainstorm links dead (second half blocked on the private repo) | PNT#120 |
| `/pna-evaluate` audit UX | PNT#55 |
| Plain-language validator for the Visual Validator | PNT#62 |
| Papers → publication; ref-drift lint | PNT `docs/roadmap.md` Tier 2 |
| PRM daily-driver gap — install/update by a **non-technical** user, + AI contact research | *(Rich is testing the existing installer first; issue to follow)* |
| Fellows calendaring / EHF events registry — may surface a `fellows_local_db` rewrite before the feature lands | fellows#302 |
| `fellows_local_db/plans/personal_network_plan.md` superseded by PRM | fellows#303 |
| snhdb multi-perspective research summaries | snhdb#3 |
| snhdb corpus-repair Phase 5 guardrails | snhdb#6 |
| Hub repo: website redo, research restructure, M1/M2/M3 recast, talk video | [`../docs/roadmap.md`](../docs/roadmap.md) |

## Done

- [x] ~~Decide where org planning lives~~ (2026-07-24 — public, in the hub repo; brainstorms stay private)
- [x] ~~Full org review: repos, roadmaps, issues + reMarkable dump synthesis~~ (2026-07-24, Cowork)
- [x] ~~Deliver the DWeb Camp Berlin 2026 talk~~ (2026-07 — deck + PDF in `presentations/dwebcamp-berlin-2026/`)
- [x] ~~**[infra]** Add planning files to the hub repo (public)~~ (2026-08-03 — `plans/` + `plans/ORG-TASKS.md`)
- [x] ~~**[org]** Establish the four planning layers~~ (2026-08-03 — `plan.md` to root, `docs/roadmap.md` for the hub, org tasks reconciled against every repo)
- [x] ~~**[org]** Move `research/plan.md` → repo root~~ (2026-08-03 — redirect stub left behind for the delivered deck's links)
- [x] ~~**[infra]** Point all local git remotes at the `social-network-health` org~~ (2026-08-03 — 5 repos were still on `richbodo/*`)
- [x] ~~**[infra]** Create the private repo~~ (2026-08-04 — `snh-private`, brainstorms organized by repo, memoriams case records, memory; PRM's public brainstorm moved in)
- [x] ~~**[infra]** Make the brainstorm skill org-wide and host-independent~~ (2026-08-04 — `snhb` in `snh-private/skills/`, symlinked by `just install-skills`; routes by repo, checkpoints, commits at session end, and searches every repo's brainstorms)
- [x] ~~**[org]** Rename `plan.md` → `software-plan.md`~~ (2026-08-04 — the name now says what it covers; the homepage never linked it, so no redeploy)
- [x] ~~**[infra]** Close the memoriams residual exposure — the stale refs GitHub was still serving~~ (2026-08-04 — the 2026-07-13 rewrite never reached the merged-PR refs, and the affected commits were confirmed still served that morning. Rather than wait on a Support ticket with no SLA, the hub repo was backed up heads-and-tags-only, deleted, and recreated under the same org and name. All affected commits now 404. Viable here because the repo had **no forks** — with a fork network, deletion promotes a fork and the objects survive. Preserved: all 37 branches, full commit history, the 40 inbound `blob/main` links, the live site, topics and settings. Lost: 55 merged-PR records, two throwaway PR comments, and both counters. The drafted Support request in `snh-private/memoriams_data/` is now moot.)
- [x] ~~**[org]** Write an org-wide publication standard for writing about identifiable people~~ (2026-08-05 — `docs/publication-standards.md` v1.0, binding every document in every repo. Part A presentation rules apply always; Part B is a release gate whose *blocking vs deferred* setting turns on **reversibility**, not on how long a source has been public. Built from a survey of the WHO/Samaritans/Mindframe/#chatsafe reporting corpus, the AoIR/BPS/NESH internet-ethics corpus, and the CARE/ICMJE/COPE case-report corpus; the four research briefs are staged privately. Part C records, deliberately, the places where no standard exists — quoting a memoriam is ungoverned field-wide, which is what our own 2026-07-08 open question 2 had already spotted. Applied in the same PR to the threat catalog, which had drifted to the opposite posture from `memoriams.md`.)
- [x] ~~**[infra]** Close the client side of the memoriams scrub~~ (2026-08-05 — this workstation's clone was verified and cleaned during the rebuild. The Mac laptop was the only other client, and Rich is the sole committer, so no third copy exists. Its pre-rewrite clone is now zipped into a labeled backup folder on that machine — **contained and known, not eliminated**: that archive holds the original content itself, so it is the one remaining copy and should be treated as the data. Server-side pointers to it are dead. Details in `snh-private/memoriams_data/`.)
- [x] ~~**[org]** Ship shared block v7 to every repo~~ (2026-08-05 — all seven propagation PRs merged: PNT#125, prm#99, fellows#309, prt#163, snhdb#11, snhtoolkitmw#6, socialnetwork_toolkit#23. `just check-org` green — all eight repos match the canonical block on disk and on `main`. prt#163 needed a rebase first: it carried a duplicate `v4 -> v6` commit that main had already merged as #162.)
