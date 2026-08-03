# Cowork session notes — 2026-07-24

*Org review + planning-system bootstrap. Decisions and punch lists from Rich's read-through
of the repos, the reMarkable dump (`2026-07-21-remarkable-snh-dump.md`), and plan.md.
Actionable items were pulled into `/TASKS.md`; the detail lives here.*

## Decisions

- **Org planning is public and lives in this repo**: `/TASKS.md` at the root + `plans/`.
- **Private org repo ("brainstorms")** exists only for uncurated/sensitive brainstorms and
  formerly-gitignored files that need to sync between machines. Brainstorms move public
  only after review; none are checked in publicly until reviewed.
- **Personal life planning** (finances, health, home, family) → a separate private repo
  under `richbodo`, not in the org.
- **prt will be formally archived** after a harvest pass (list below).
- **M1/M2/M3 = plan.md Steps 1–3**, and they are **ongoing processes that hit milestones**,
  not one-shot deliverables. The plan needs to say so, per step: the process, its cadence,
  and the milestone tests.

## Plan + research/ restructure (Claude Code punch list, hub repo)

1. **Move `research/plan.md` → `/plan.md`** (repo root). It's the project's `.plan`;
   nobody puts one in an obscure subfolder.
2. **Reconcile the two egocentric-measurement docs** —
   `research/measurement/community-network-health-explainer.md` (the architecture-pattern
   take) and `research/measurement/egocentric_to_community_network_health_research_note.md`
   (the research note). They cover much of the same ground. Differentiate them first, then
   merge into one doc plus, if needed, a small note holding the non-overlapping remainder.
3. **Create a `positioning/` folder.** Move `research/measurement/social_cohesion.md`
   there — it's historical positioning, not measurement research.
4. **Recast the plan's steps as processes with milestones.** Step 2 in particular doesn't
   describe its implementation; fix while recasting. Current honest status for the recast:
   - **M1 (Step 1)** — close. fellows_local_db is a real reference design with real users
     (keep shipping features so it stays used); PRM is a few features from "usable";
     Vault should start as a third Step-1 use case. Note: Step 1 is never "done" — a safe
     place for relationship data must track a changing environment.
   - **M2 (Step 2)** — implementable solo anytime, but only becomes meaningful with a
     community using Step-1 tools; the fellows and PRM communities are both candidates.
   - **M3 (Step 3)** — propose to a research team once M1+M2 are demonstrably underway.
5. **Website link hygiene:** the homepage deep-links `research/` files by GitHub URL —
   moving plan.md / measurement docs breaks them. Update
   `public/socialnetwork-health.html` and redeploy (`just deploy`) in the same change.

## Positioning (new workstream)

Beyond the folder: write the actual positioning/vision doc. As collaborators arrive, Rich
wants the project's focus legible — supportive of adjacent directions people bring, clear
about what he himself is working on.

## prt harvest list (before archiving)

- **Pre-meeting review** idea → PRM: before a meeting/event, review the contacts who'll be
  there — names, faces, what you know (e.g. a family event with relatives you barely
  know). Future angle: same surface through smart glasses, live.
- **Import pipeline:** prt's import approach was more sophisticated than PRM's current
  one — review and port what's better.
- **Scan prt's 19 open issues + roadmap** for PNT-relevant material (the CRT concepts
  already live on in the hub repo's protocols research).
- **Add a "PRM is the natural successor" note** to prt's README, then archive the repo
  on GitHub.

## Fellows calendaring brief (EHF events registry)

- **Context:** the Edmund Hillary Fellowship board, while winding down the legal entity,
  asked Rich (2026-07-22) for (1) an events registry going forward and (2) see the
  yearly-newsletter item below. There was never a good registry — just Google Calendar.
  ~50 fellows use fellows_local_db; a ~200-fellow WhatsApp group covers less than half of
  ~500 fellows; realistic expectation is many will keep posting events to WhatsApp anyway.
- **Shape:** a calendaring feature of fellows_local_db displaying a global event calendar.
- **Constraints/desires:** privacy-preserving; as decentralized as possible (Rich wants to
  explore "encrypted spaces"-style approaches); acceptable to **start centralized and
  decentralize later**. Open problems: how clients find a server via some persistent proxy
  URL (mechanism unknown — candidate new tech); server currently stores data unencrypted —
  explore encrypted-pull instead (e.g. key delivered by email or in an HTTPS URL, data
  encrypted at rest).
- **Status:** not yet in design. Rich is on vacation until ~2026-08-01; design thinking
  starts then, work lands in the fellows_local_db repo. First project of its kind for the
  org — genuinely new territory.

## EHF yearly newsletter

Opt-in yearly newsletter to all fellows ("fun if people contributed"). Gauge interest by
contacting everyone; run it if enough opt in.

## Vault + OpenClaw

Vault = the simplest reference design: back up your SaaS systems from their exports, with
an **OpenClaw** (agent framework) plugin assisting the exports, plus the **Exit/Interop
Manual** wiki (how to export/back up each SaaS, how to replace functionality or not, how
to interoperate). The research edge: **AI OS automation for fast SaaS export, and how to
secure OpenClaw's behavior** — a new and largely unexplored area.

## Weekly-prep automation (Cowork, later)

A weekly scheduled Cowork task that preps: SNH newsletter draft, YouTube check-in notes,
outreach follow-ups, and a low-stress agenda for the weekly meeting (initially Rich plus
one or two occasional helpers). If the discussion venue becomes a Signal group, signal-cli
bots could capture meeting minutes and feed the next week's prep. Set up once the meeting
and venue exist.
