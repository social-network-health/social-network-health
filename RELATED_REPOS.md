# Related repositories & resources

This repo (`social-network-health`) is the organizing hub for the Social Network Health (SNH)
research program. The software, specs, and workshop materials live in sibling repositories,
all under the **[social-network-health](https://github.com/social-network-health) GitHub
organization**.

## The sibling-checkout convention

**Check out all project repos at the same filesystem hierarchy level** — side by side in one
parent directory of your choice. From any repo's root, every related repo is then at `../<name>`,
so cross-repo work resolves paths **relative to the repo root** (`../prm`,
`../personal_network_toolkit`, …), never as absolute paths — the parent directory differs per
host. Not every directory at that level need be related to SNH; the tables below list the repos
that are.

## Core software (active)

| Repo | Local path | Remote | Role |
|---|---|---|---|
| personal_network_toolkit | `../personal_network_toolkit` | github.com/social-network-health/personal_network_toolkit | The PNA Toolkit — spec, contracts, skill, MCP servers, and lints for building/validating **Personal Network Applications**. The central toolkit; the PNA Spec and positioning paper live in its `spec/` and `docs/`. |
| prm | `../prm` | github.com/social-network-health/prm | Personal Relationship Manager — local web app, PNA reference design (attested at Toolkit v0.2). |
| fellows_local_db | `../fellows_local_db` | github.com/social-network-health/fellows_local_db | EHF Fellows Local Directory — local-first SQLite + PWA directory app; the toolkit's first reference design; hosts three v1 MCP servers. |
| prt | `../prt` | github.com/social-network-health/prt | Personal Relationship Toolkit — Python TUI relationship manager; earlier generation, basis for prm (listed as archived on the website). |

## Talks & workshop material

All current talk material lives **in this repo** under `presentations/` (one folder per talk:
delivered PDF at top level, Slidev source in `deck/`). The PNT workshop deck — the starting
point for the DWeb Camp Berlin 2026 deck — was briefly imported here (July 2026) and then
removed once that talk shipped; it remains in the standalone repo and in this repo's git
history under `presentations/pnt-workshop/`:

| Repo | Local path | Remote | Role |
|---|---|---|---|
| pnt-workshop | *(not checked out locally — clone to `../pnt-workshop` if needed)* | github.com/richbodo/pnt-workshop (candidate for archiving) | Slidev slide deck + talk notes for Personal Network Toolkit workshops. Superseded by the DWeb Camp Berlin 2026 deck. |

## Research infrastructure (active)

| Repo | Local path | Remote | Role |
|---|---|---|---|
| snhdb | `../snhdb` | github.com/social-network-health/snhdb | Public research-paper library: PDFs, markdown conversions, YAML metadata cards, and `card-schema.yaml` (the pilot refinement of the card format drafted in `research/research_library/planning/knowledge-base-plan.md`). Ships a user-wide Claude Code skill (`/snhdb <question>` — install per its README) for cited corpus search from any session. Will sync with the Google Drive research corpus and power the AI search engine planned for toolkit.socialnetwork.health. New 2026-07. |

## Websites & educational materials

| Repo | Local path | Remote | Role |
|---|---|---|---|
| social-network-health | (this repo) | github.com/social-network-health/social-network-health | The main website, https://socialnetwork.health (`public/`, deployed via `ops/`), plus the research documents and presentations behind it. |
| snhtoolkitmw | `../snhtoolkitmw` | github.com/social-network-health/snhtoolkitmw | MediaWiki extension bundle/config for the SNH toolkit wiki (https://toolkit.socialnetwork.health). Dormant since 2024; reactivating July 2026. |
| socialnetwork_toolkit | `../socialnetwork_toolkit` | github.com/social-network-health/socialnetwork_toolkit | MediaWiki install/config + content for the toolkit wiki. **Its README warns secrets are checked in — treat as sensitive, never mirror publicly.** Dormant since 2024; reactivating July 2026. |

## Localhost port registry

Each app repo pins a fixed local port and documents its own serialization rules. This table
exists so a **new** repo doesn't claim one that's already taken — check here before picking.

| Port | Claimed by | What runs on it |
|---|---|---|
| 8765 | `fellows_local_db` | the app server (fixed by convention — do not change) |
| 8770 | `prm` | the workspace server (`just serve`) |
| 8791 | `personal_network_toolkit` | Visual Validator test server (`just test-viewer`, opt-in) |
| 8009 | `personal_network_toolkit` | report viewer (`just view-reports`, opt-in) |

Within a repo, worktrees isolate the filesystem but **not** these ports — server-based runs
must be serialized across worktrees. See that repo's `CLAUDE.md` for its specifics.

## Non-repo resources

- **Toolkit wiki (live):** https://toolkit.socialnetwork.health — MediaWiki of best practices and research findings; the primary body of published SNH work.
- **Paper corpus (Google Drive, public):** https://drive.google.com/drive/u/0/folders/1CQIZnHCojqnvGuiOmn9UR7Jbf9nGlICD — full papers & metadata behind `research/threat_modelling/references/references.md`.
- **SNH GPT — Researcher (retired):** custom GPT grounded in the corpus (kept linked from the homepage's Research library card until fully removed).
- **Search with Claude Desktop (instructions):** https://docs.google.com/document/d/1QlV5VQE1dEqhYEget6jJUSHRhCDfgrynyYdgXm6BoWU — the most-used how-to for querying the library with AI tools.
- **Video archive:** https://www.youtube.com/@SocialNetworkHealth
- **Live site:** https://socialnetwork.health — served from this repo's `public/`, deployed via `ops/`.
