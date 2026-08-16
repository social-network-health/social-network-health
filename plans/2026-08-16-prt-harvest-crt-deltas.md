# prt harvest: completion record + CRT-concept deltas

*2026-08-16. The prt harvest pass (ORG-TASKS "Formally archive prt — harvest first") ran
across all three passes: the open issues, the code, and ROADMAP.md. This note records
where everything landed and the one research delta the CRT diff produced.*

## Where the harvest landed

Sixteen issues filed on prm (prm#100–#115), covering: directory export + rendering
(prm#100, with the export-dir-as-contract architecture), the names-and-faces quiz
(prm#101, new — never documented in prt), the AI-guided-discovery epic (prm#102),
LLM tool-surface principles with the prt#43→#145 lesson and a 2024–26 evidence review
(prm#103), an LLM eval harness (prm#104), ranked-candidate proposals (prm#105), typed
contact-to-contact relationships — greenfield in prm (prm#106), relationship analytics
(prm#107), relationship UX + ego node as ideas (prm#108–#109), the interactions/recency
M2 schema hook (prm#110), import enhancements (prm#111), an at-rest-encryption decision
note (prm#112), backup save-slots UX (prm#113), search improvements (prm#114), and an
INV-14 "usable with no LLM" principle (prm#115).

Toolkit-bound: a design note on scanner path-set coverage drift (separate PNT PR).
prt's README already carries the successor note; GitHub archival is the remaining step.

## CRT-concept deltas against the protocols research

The prt archive's CRT vision (prt CLAUDE.md vision section) was diffed against
`research/protocols/notification-protocol.md` (v0.2) and
`research/measurement/egocentric_to_community_network_health_research_note.md`.
Result: almost fully superseded — with one genuine research delta.

**Covered (no action):** the progressive-disclosure "help" workflow (S0–S4 staged
disclosure, per-audience reveal policy) and community-health alerting — the latter
deliberately re-shaped by the check-in protocol as elapsed-time signals to chosen
checkers; prt's "alert on likely-unhealthy member" would be a regression against the
no-inference invariant, not a contribution.

**Delta — ZK proofs of connectedness as a user-facing artifact.** prt imagined:
accept a user's message logs locally, export a portable, verifiable proof of
connectedness. The measurement note's proof compiler (§5) covers proving *aggregate
statements* to an enclave, but two pieces are unspecified anywhere: (a) a user-held
portable connectedness credential, and (b) the mutual-edge matching problem (two PRMs
claiming the same tie — PSI-shaped, already flagged as unsolved in the note). Any
development must stay inside the stated posture: statistics only, never message
bodies. Parked here as a research prompt, not a proposal.

**Non-delta worth recording:** the notification protocol's open problem #3 (the
comms-channel/scheduling handoff at S3) is the one piece of prt's "agree on a
communications channel" idea that remains unsolved — but prt had no mechanism either.
The harvest confirms the gap is real and contributes nothing toward closing it.
