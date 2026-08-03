# The Social Network Health Plan

**Status:** living document (2026-07-10). First presented at DWeb Camp Berlin 2026
(`presentations/dwebcamp-berlin-2026/`). This is the summary form; each step links to the
research and software that carries it.

---

Social network health research tells us how great outcomes for everyone in our communities
are correlated. Education, interaction, and skill building are infinitely more important
than "underlying tech" — the best of which is inbuilt in us. Remote, digitally connected
communities cannot escape some tech, though. So we have a plan.

## Step 1 — A safe place for human relationship data

Develop and validate safe tools that bring our contact and relationship data local —
allowing us to interact outside of SaaS with confidence, even with the most sensitive
information. Start with the simplest things that work: home-cooked meals.

**Carried by:** the [PNA Toolkit](https://github.com/social-network-health/personal_network_toolkit)
([spec](https://github.com/social-network-health/personal_network_toolkit/blob/main/spec/PNA_Spec.md),
contracts, conformance suite) and its reference designs — fellows_local_db (complete, in
use) and PRM (in progress). The [threat catalog](research/threat_modelling/threat_catalog.md) gates
everything: know where the mines are, and design around them.

## Step 2 — Egocentric analysis

Develop and validate safe tools that bring our communications data local — allowing us to
understand our egocentric networks more fully, and act on that information to improve
outcomes within them.

**Carried by:** the PNA data layer (Step 1's root) plus the measurement research in
[`measurement/`](research/measurement/) — the
[community network health explainer](research/measurement/community-network-health-explainer.md) and
the [egocentric→community research note](research/measurement/egocentric_to_community_network_health_research_note.md).

## Step 3 — Sociocentric analysis and interaction

Develop and validate safe protocols that may allow remote communities to practice what has
previously been the domain only of local communities enhanced by experienced practitioners
working with the latest research in social network health. This is where the advanced tech
comes in — and **research teams are included before interventions**. If viable, this could
launch initiatives far beyond the creation of home-cooked software meals.

Step 3 is defined by its gate, not its deliverable: threat model → development → testing →
researcher engagement, all prior to deployment. Nothing past guardrails is legitimate until
the guardrails exist.

**Carried by:** the protocol design notes in [`protocols/`](research/protocols/) —
[notification protocol](research/protocols/notification-protocol.md) (one-button help-seeking with
staged disclosure), [check-in protocol](research/protocols/checkin_protocol.md) (proactive peer
check-ins — the outbound complement), and the measurement protocol thesis
(community-level aggregate health metrics estimated from consented egocentric fragments;
see [`measurement/`](research/measurement/)).

## Supporting infrastructure

- [snhdb](https://github.com/social-network-health/snhdb) — the SNH research corpus:
  papers, metadata cards, and an AI search skill, all local.
- [Threat catalog](research/threat_modelling/threat_catalog.md) — the standing harm model, evidence-linked.
- The [organizing hub](https://github.com/social-network-health/social-network-health)
  (this repo) and the website, [socialnetwork.health](https://socialnetwork.health).
