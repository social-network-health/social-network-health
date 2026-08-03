# Social Network Health

This research project has the goal of improving social network health in digitally connected but remote communities.

It aggregates several efforts:
- Implementations of protocols to communicate needs and community health metrics
- Efforts to create software better suited to individual and community health
- Production of educational materials that support understanding of social network health interventions

This repo is the **organizing hub**: the https://socialnetwork.health website, research documents,
and pointers to the software efforts we are developing in other places.

## AI skills and tools across the organization's repos

Much of this program is designed to be *operated through AI agents*. Three Claude Code skills,
one per major piece of the program, are the entry points:

| Skill | Lives in | What it does |
|---|---|---|
| **pna-toolkit** | [personal_network_toolkit](https://github.com/social-network-health/personal_network_toolkit) (`pna-toolkit/SKILL.md`) | The PNA Toolkit skill, four flows: **build** a conformant Personal Network Application from the spec, **evaluate** an existing app for conformance ("is this app safe to install?"), **contribute** back to the toolkit, and **harden** the environment a PNA runs in. |
| **snhdb** | [snhdb](https://github.com/social-network-health/snhdb) (`skill/snhdb/SKILL.md`) | Cited search over the SNH research-paper corpus: ask what the literature says, or evidence-check a claim. Installable user-wide (`/snhdb <question>` from any session) — see its README. |
| **paper-resolver** | this repo (`tools/paper-resolver/SKILL.md`) | Resolve a DOI, title, or topic search to metadata plus **legal** open-access full text; grows the research corpus that snhdb serves. See `tools/paper-resolver/usage.md`. |

### CLI tools

The CLI tooling on offer lives in the
[personal_network_toolkit](https://github.com/social-network-health/personal_network_toolkit)
`tools/` directory (run via its `justfile`):

| Tool | What it does |
|---|---|
| `just validate <candidate>` | Runs the deterministic lint suite against a candidate PNA and folds the results into one typed `evaluate-report.json` — the deterministic spine that the skill's LLM review then enriches. |
| The lint suite | Individually runnable deterministic checks: egress (does anything send data off-device?), export-readable, loopback-surface, attestation-evidence, report-fixtures, and spec-ID integrity. CI-enforced on the toolkit itself. |
| Visual Validator (`tools/report-viewer/`) | A zero-dependency browser viewer for evaluate reports, with a developer view and a plain-language end-user view ("is this app safe?"). |
| `swh-save` / `rearchive` | Archive reference designs to Software Heritage so accepted designs survive upstream repo deletion. |

(The paper-resolver above is also a plain CLI — `tools/paper-resolver/resolve.py` in this repo.)

## Layout

- `research/measurement/` — measuring community network health from egocentric data: the
  egocentric→community research note, the explainer, the social-cohesion note
- `research/threat_modelling/` — the threat catalog and its bibliography (`references/`)
- `research/protocols/` — protocol design notes (the SNH notification protocol)
- `research/research_library/` — per-paper `research_summaries/` (where papers applicable to
  proposed protocols are summarized and tested), the knowledge-base plan (`planning/`), and
  the gitignored paper corpus
- `tools/paper-resolver/` — tool for resolving papers to metadata + legal open-access full text
- `presentations/` — talk preparation
- [`plan.md`](plan.md) — **the summary plan**: the M1/M2/M3 steps and what carries each. Start here.
- [`docs/roadmap.md`](docs/roadmap.md) — where this repo (website, research docs, presentations) is headed
- `plans/` — org-level, cross-repo planning: the live [`ORG-TASKS.md`](plans/ORG-TASKS.md) list plus
  dated planning dumps. Per-repo direction lives in each repo's own roadmap and issues — see
  [`plans/README.md`](plans/README.md) for how the four planning layers fit together.
- `public/` + `ops/` — the static website and its droplet deploy

## Related repositories

The software (PNA toolkit, PRM, reference designs) lives in sibling repos — see
[`RELATED_REPOS.md`](RELATED_REPOS.md) for the map. Convention: all related repos are checked out
side by side, one level up from this repo root.
