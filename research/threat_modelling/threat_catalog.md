# Threat Catalog — Social Network Health Interventions for Remote-Worker Communities

**Status:** v2.0 (2026-06-10) — reorganized by generality; cites `references.md` by `[n]`.

**Living document.** This catalog is evolutionary: the analysis behind it is re-run
periodically or as needed, and the catalog is revised with what each pass finds. (The
`[n]` numbering in `references.md` stays append-only across revisions — see that file.)

**Provenance.** v1 distilled from the `snh-harm-research` multi-agent study (12 research seams
→ 92 raw → 38 consolidated → adversarially verified → synthesized; 52 agents, ~1.5M tokens). v1.1
added a completeness pass (17 new threats, K1–K6 citations lifted out of "pending," quarantine
Q-a/b/c resolved, 34 success-model leads). **This reorg = v2.0:** the v1 main catalog and the v1.1
"Completeness Addendum" are merged into ONE catalog, reordered by a three-tier *generality*
structure, with every inline citation converted to a numbered `[n]` reference into
`references.md`. Full verbose synthesis with all citation corrections:
`brainstorms/20260609-snh-threat-catalog.md` (gitignored). Grill log:
`brainstorms/20260609-102346-snh-session.md`. References: `references/references.md` (this repo;
originally drafted in the `host-happily-hub` repo and moved here).

---

## Purpose & how this fits

This is the **"where the mines are"** document. Before designing *any* social-network-health
(SNH) intervention for remote workers — and long before building the experimental
notification/response protocol — we need a documented, citable understanding of the credible
ways such interventions harm people.

It is the **first of two paired research datasets**:

1. **Threat model (this document)** — credible failure modes of SNH interventions for remote
   workers.
2. **Success model (forthcoming)** — design features and practices empirically linked to
   *better* outcomes in the remote-worker context (the "what works" counterpart; the content
   that will seed the toolkit's remote-teams Practice section). Appendix A captures the leads.

Together these become a reusable evidence base we draw on repeatedly. They feed, in dependency
order: **safety guardrails + design methodology** ("where we land" — nothing past it, including
experiments, is legitimate until it exists) → **the community guide** (a partly-assisted
meta-process for a community to build, *by and with itself*, a communications system that
improves its social network health, with stepwise safe experiment/evaluate/pivot) → **(long
term) the protocol experiment** (a privacy-preserving notification/response protocol + community
metrics — known to face hard challenges; deferred).

**The tier structure (new in v2.0).** v1 grouped threats by *mechanism* (A–K). v2.0 keeps that
mechanism grouping as a *secondary* sort and adds a primary sort by **generality** — how broadly
the threat applies:

- **Tier 1 — Fundamental:** risk factors & failure modes for the social-network health of *any*
  community, remote or not.
- **Tier 2 — Heightened for remote workers:** **2a** general remote-work amplifiers; **2b** the
  distributed / open-source-community sub-context.
- **Tier 3 — Channel / software-specific:** harms tied to a particular medium, feed, metric
  technology, data path, or AI mediation.

A universal risk-factor *core* is stated once in Tier 1 (e.g., **RF1 — social isolation & weak
belonging**), with its remote-amplified version cross-linked from Tier 2 (e.g., **K1**). Some
threats span tiers; where so, the entry carries an explicit cross-link line (**Universal core:**
…, **Amplifies →** …, or **Acute at … scale → cf. Tier …**).

**Scale & evidence stance.** We do **not** optimize for any scale. Remote-teams research spans
every size, so we follow the *strongest available evidence* for each threat (and, later, each
success case) wherever it sits — n=1 or n=1,000,000 — and report each study's **own scale and
context** in its evidence line, so the reader knows exactly what was shown and where. The `scale`
tag is only a light "where this is most acute" applicability aid; it is **never** a filter on
which evidence counts. (Detailed mitigations lean toward small home-cooked communities, N≈10–50,
because that is the immediate build context — but the catalog is meant to serve mid-size orgs,
platform-scale networks, and academic ideation equally.)

**Design stance.** Most harm here is *iatrogenic by design*, not the work of a bad actor. The
fight is for harm avoidance, maximal use of current evidence, and a well-informed design process.
Leaders are part of a system, not the sole point of failure.

---

## How to use this catalog

Each threat has a **stable ID** (e.g., `B1`) so the success model, guardrails doc, and future
research can reference it permanently — IDs are unchanged from v1/v1.1; only their *location* in
the document has moved. The "Mitigation seed" line is the bridge to the success model; the
"Consider further" line is an open question for the ongoing grill.

**Severity** (harm to a preventive remote-worker SNH intervention): `high` = serious individual
harm or silent corruption of the whole intervention · `medium` = meaningful but recoverable ·
`low` = friction/quality risk.
**Confidence** = verifier confidence in the evidence as characterized: `high` / `med`; `exp` =
expert-asserted, citation now supplied for most by the completeness pass.
**Scale** = a light applicability aid — where the threat is *most acute* (`team` N≈10–50 ·
`org` 100s–1000s · `platform` very large). It is **not** a filter on which evidence counts: we
follow the strongest evidence at *any* scale and report each study's own N/scale/context in its
evidence line.
**Layers** it threatens: **APP** (personal network app) · **PROTO** (notification/response
protocol) · **METRICS** (community health metrics) · **FACIL** (facilitation process) ·
**LEAD** (leadership/governance).

**Tiers** (the primary sort, new in v2.0):
- **Tier 1 — Fundamental** — applies to any community's social-network health.
- **Tier 2a — Remote-general** — heightened by remote work as such.
- **Tier 2b — Distributed / OSS sub-context** — specific to distributed / open-source communities.
- **Tier 3 — Channel / software-specific** — tied to a medium, feed, metric tech, data path, or AI.

**Citations** are `[n]` into `references.md` (numbered in order of first appearance in the v1.1
source; append-only and stable). Each kept its scale/context parenthetical so it can later become
a **deep link** on the toolkit MediaWiki (Anton Krom's PDF highlight extension opens the source,
finds the passage by text string, and highlights it). An inline citation with no match in
references.md is left as text with a trailing `[ref?]`.

---

## Tiered Register

### Tier 1 — Fundamental (any community's social-network health)

| ID | Threat | Sev | Conf | Scale | Refs | Cross-links |
|----|--------|-----|------|-------|------|-------------|
| **Fundamental risk factors** |
| RF1 | Social isolation & weak belonging (universal risk factor) | high | high | all | [128][133][134][226] | amplified by → K1 (2a) |
| **Iatrogenic design** |
| A1 | Single-session emotional-processing backfire (debriefing harm) | high | high | team·org | [1][2][3][4] | |
| A2 | Universal prevention worsening a vulnerable subgroup | high | high | org·platform·team | [5][6][7][8][157][158][159] | cf. A5 (2a) |
| A3 | Scared-Straight / fear-arousal deterrence backfire | med | high | all | [9][10][11] | |
| **Labeling / medical model** |
| B1 | Labeling / at-risk identification (master threat) | high | high | all·acute team | [15][16][17][18][19] | |
| B2 | False-positive "at-risk" designation harms non-converters | high | med | team·org | [20][21][22][157][160] | |
| B3 | Responder/facilitator bias from diagnostic frame | med | high | all | [23][24] | |
| B4 | Self-stigma / prevalence inflation from medicalized framing | med | med | all | [25][26][157][161] | |
| **Contagion** |
| C1 | Peer contagion / deviancy training in aggregated support | high | high | team·org | [27][16][28][29] | |
| C2 | Suicide/crisis contagion via distress visibility (Werther) | high | high | all·acute platform+team | [30][31][32][33][34] | |
| **Metrics** |
| D2 | Goodhart/Campbell collapse + impression mgmt + selection | high | high | all·acute org | [44][45][46][163][132] | |
| D5 | Homophily–contagion confound misleads facilitators | med | high | all | [51][52] | |
| **Consent / governance** |
| F1 | Coerced/bundled consent at the moment of distress | high | high | all | [63][64][65] | cf. Q-a, Q-b (3) |
| F2 | Coercive financial incentives → compelled disclosure | high | high | org | [66][67] | |
| F3 | Non-consensual crisis escalation → harmful welfare/police checks | high | high | all·acute team | [68][69][70][64] | |
| **Help-seeking & stepped-care** |
| G1 | Chilling effect on help-seeking (stigma + reactance + coercion) | high | med | all | [71][72][73][164][138][165] | |
| G2 | Gatekeeper training: confidence without behavior change; repels high-risk | high | med | all | [74][75][76] | |
| G3 | Stepped-care evaporation: preventive layer fails to step up | high | med | all | [77][166] | |
| G4 | False reassurance: quick response masks unmet clinical need | med | med | all | [78][79] | |
| **Community / leadership** |
| I1 | Peer enforcement of harmful norms + polarization + call-out dynamics | high | med | all·acute team | [88][89][90][133][121] | |
| I2 | Leadership inaction / inadequate response to a first-time signal | high | med | all·acute team | [91][92][171][104] | |
| **Transfer / fidelity** |
| J1 | Voltage drop, model drift, surface-only cultural adaptation | high | med | org·platform·(team transfer) | [93][94][95][96][172][173][5] | |
| J2 | Successor-facilitator competency decay + satisfaction-masks-harm | high | med | all | [97][98][99][105] | |

*Other universal risk factors are already represented as Tier-1 mechanism entries: stigma /
labeling = the B-cluster; help-seeking barriers = G1. RF1 is the **only** new lifted entry.*

### Tier 2a — Remote-general (heightened by remote work)

| ID | Threat | Sev | Conf | Scale | Refs | Cross-links |
|----|--------|-----|------|-------|------|-------------|
| K1 | Remote isolation makes weak belonging the daily default | high | high | all | [129][132][130][131][136][100][225][226][227][228] | Amplifies → RF1 (T1) |
| K2 | Timezone dispersion, interruption, sleep/circadian disruption | high | high | all | [139][140][141][142][143][144][145][146][147][148] | |
| K3 | Tech displacement / underemployment / job insecurity → depression | high | high | all | [149][150][151][152][153][154][155][138][120] | |
| K3a | Anticipatory AI-threat distress (harms employed workers) | med | med | all | [152][150][180][154] | sub-entry of K3 |
| K3b | Reputation-premium collapse for high-skill freelancers | high | med | all | [181][182][153] | sub-entry of K3 |
| K3c | GenAI productivity-expectations ratchet | high | med | all | [183][184] | sub-entry of K3 |
| K4 | Declining in-person contact (post-COVID inflection) | med | high | all | [129][132][133] | |
| K5 | "Degraded mode": loss of embodied/experiential co-present learning | high | med | all | [156][217][218][219][220] | |
| K6 | Hard-to-corral / unreachable-in-bulk → selection bias & coverage gaps | high | med | all | [175][221][222][223][224] | |
| K7 | Professional/career isolation (distinct from social loneliness) | med | high | all | [145][225][228] | |
| K8 | Reciprocal distress↔isolation feedback loop | high | high | all | [174][225] | |
| K9 | Silent dropout / invisible attrition as a distress signal | high | med | all | [176][177][171] | |
| K10 | Telepressure / always-on → rumination, sleep loss, burnout | high | high | all | [142][139] | upstream of K2 |
| K11 | Inverted-U work-mode dose curve (fully-remote deficit vs hybrid) | high | med | all | [178][132][140][227][229] | |
| K12 | Long-term full-remote suppresses the need to belong | high | med | all | [179][165][227] | |
| H2 | Remote-network atrophy: weak-tie loss, video fatigue, onboarding failure | high | high | all (remote) | [84][85][86][87][167][168][169][170] | |
| D1 | Employer-adjacency: surveillance perception + disclosure retaliation | high | med | all | [12][42][43][162] | |
| A5 | Subgroup-masking — harm + averaged eval both hide the at-risk stratum | high\* | med | org·platform·team | [101][102][103] | cf. A2 (T1) |

\*A5 severity may be overstated (single cross-sectional study) — see Appendix B.

### Tier 2b — Distributed / OSS-community sub-context

| ID | Threat | Sev | Conf | Scale | Refs | Cross-links |
|----|--------|-----|------|-------|------|-------------|
| D6 | Invisible facilitation / emotional-labor blind spot | med | high | all | [104][105][106] | |
| D7 | Public-performance-audit impostor (AI-amplified) | med | med | all | [107][108][109][110] | |
| I3 | Entitled-user demand escalation → suppresses disclosure + trust vacuum | high | high | all | [119][120][121][122][123] | |
| I4 | Consensus-governance overload → facilitator burnout | med | med | all | [124] | |
| J3 | Single-maintainer "lottery factor" (knowledge concentration) | med | high | all | [125][126][127][123] | |
| H4 | Capable-contributor blind spot (risk indicators anti-predictive) | high | med | all | [116][117][118] | |

### Tier 3 — Channel / software-specific

| ID | Threat | Sev | Conf | Scale | Refs | Cross-links |
|----|--------|-----|------|-------|------|-------------|
| **Text-channel** |
| A4 | Symptom-surveillance anxiety amplification ("worry engines") | med | med | all | [12][13][14] | |
| H1 | Text-only misattribution, dehumanization, toxic disinhibition | high | high | all | [80][81][82][83][116] | |
| H3 | AI-mediated interaction displaces human bonds | med | med | all | [113][114][115] | |
| C3 | Co-rumination, emotional contagion & cyberostracism in text | high | high | team·org | [35][36][37][38][108] | Universal core: contagion (cf. C1/C2, T1) |
| **Broadcast / feed** |
| C4 | Digital bystander effect: broadcast → diffusion → no response | high | med | org·platform | [39][40][41] | Universal core: contagion (cf. C1/C2, T1) |
| D3 | Engagement-ranked / silent curation amplification of distress | high | high | platform·(any feed) | [47][48] | |
| **Metrics / privacy-software** |
| D4 | Emotion-AI / biometric metrics mislabel healthy workers | med | med | all | [49][50] | |
| E2 | ZKP proves correct computation, NOT non-identifying output | high | high | all | [58][59] | |
| Q-c | Small-N re-identification from "aggregate" metrics (gates metrics) | high | high | acute team·org | [186][185][194][193][187] | cf. E1–E3 |
| **Help-seeking software** |
| G5 | Platform-distrust silencing (techno-insecurity mutes signals) | high | high | all | [111][112] | cf. G1 (T1), H1 |
| **Data-leakage** |
| E1 | Cumulative-release attacks (reconstruction / membership / composition) | high | high | acute team·org | [53][54][55][56][57] | |
| E3 | Behavioral-trace re-identification of pseudonymous signals | high | high | acute team | [60][61][62] | Acute at small-N remote scale → cf. Tier 2 |
| Q-a | Third-party SDK / tracking-pixel leakage + data-broker sale | high | high | all | [63][188][189][190] | cf. F1 |
| Q-b | Commercial pivot of help-seeking data | high | high | all | [63][191][192][64] | cf. F1 |
| **AI-mediated** *(see also H3, D4 above, and K3a–c in Tier 2a)* |

---

## Detailed catalog

> Each entry: **Mechanism** (causal chain) · **Evidence** (with `[n]` citations) · **Bites**
> (layers) · **Scale** (how it changes with community size) · **Mitigation seed** (→ success
> model) · **Consider further** (open grill question). Some entries also carry **Distinct from**,
> a **⚠ caveat**, and a **Correction applied** note (from the v1.1 reference audit), plus a tier
> cross-link line where the threat spans tiers.


# TIER 1 — Fundamental

> Risk factors and failure modes for the social-network health of **any** community, remote or
> not. Universal risk-factor *cores* live here once; remote-amplified versions are cross-linked
> from Tier 2.

## Fundamental risk factors

**RF1 — Social isolation & weak belonging (universal risk factor)** · `high` · conf high · all
- **Mechanism:** Social isolation / weak belonging / low social support erode wellbeing and
  help-seeking in **any** community. This is the universal substrate that an SNH intervention is
  ultimately trying to strengthen, and the upstream condition that raises baseline vulnerability
  to nearly every other threat in this catalog. (Remote work makes this the daily default — see
  **K1 (Tier 2a)**, the remote amplification of this same core.)
- **Evidence:** isolation OR 1.29, loneliness OR 1.26, living alone OR 1.32 — Holt-Lunstad, Smith,
  Baker, Harris & Stephenson 2015 **[128]** (70 prospective studies, combined N in the hundreds of
  thousands; effects stronger for working-age samples, mean age <65). Mortality of disconnection ≈
  smoking up to 15 cigarettes/day; time with friends fell ~70% 2003→2020 (150→40 min/day, ATUS);
  49% in 2021 had ≤3 close friends vs 27% in 1990 — US Surgeon General Advisory, Murthy 2023
  **[133]**. Thwarted belongingness (interpersonal theory of suicide) — Van Orden et al. 2010
  **[134]**. Social connection established as a critical factor for mental and physical health —
  Holt-Lunstad 2024 **[226]** (top-tier current review, *World Psychiatry*).
- **Bites:** the whole substrate; raises baseline vulnerability to the B-cluster, C-cluster, G1, H2.
- **Note:** the *problem the intervention targets*, not itself a failure mode; the universal core
  of K1. Other universal risk factors are already represented as Tier-1 mechanism entries
  (stigma/labeling = B-cluster; help-seeking barriers = G1).
- **Consider further (success model):** what reliably builds belonging in any community — and
  which builders survive the remote degraded mode (cf. K5)?

## A. Iatrogenic design — the intervention itself causes harm

**A1 — Single-session emotional-processing backfire** · `high` · conf high · team·org
- **Mechanism:** A mandatory structured session forcing articulation of distress right after an
  event interferes with natural habituation and appears to re-consolidate the trauma memory
  before the nervous system stabilizes → elevated PTSD.
- **Evidence:** single-session debriefing "equivalent to, or worse than" no intervention — Rose,
  Bisson, Churchill & Wessely 2002 **[1]** (15 RCTs). OR 2.51 (95% CI 1.24–5.09) at 1yr — Bisson
  et al. 1997 **[2]**. 3yr adverse outcomes — Mayou, Ehlers & Hobbs 2000 **[3]**. Review of harmful
  treatments — Lilienfeld 2007 **[4]**.
- **Bites:** PROTO, FACIL.
- **Scale:** Universal to any facilitated response; the harm is per-person, not size-dependent.
- **Mitigation seed:** No mandatory single-session emotional processing; responses are low-demand
  check-ins; watchful waiting + peer support; structured trauma work referred to professionals
  only after time elapses.
- **Consider further:** What is the minimum, *non-iatrogenic* shape of a "response"? Where is the
  line between a supportive check-in and a harmful debrief?

**A2 — Universal prevention worsening a vulnerable subgroup** · `high` · conf high · org·platform·team
- **Mechanism:** Content pushed to everyone raises symptom salience without coping scaffolding,
  primes misattribution (nocebo), becomes ruminative for some → a minority deteriorates while the
  mean improves.
- **Evidence:** no overall benefit, at-risk students worse at post & 1yr — MYRIAD RCT, Kuyken et
  al. 2022 **[5]** (n≈8,376, 84 schools). 12.42% reliable worsening (depression), 11.78% (anxiety)
  — Venturo-Conerly et al. 2023 **[6]**. School mental-health intervention harms — Guzman Holst et
  al. 2025 **[7]**. 43 harmful outcomes/17 RCTs — Werch & Owen 2002 **[8]**. 1/8 WISE Teens
  participants showed clinical depression post-program vs 1/13 in regular classes — Johnstone et al.
  WISE Teens RCT **[158]** (n=1,071 Australian teens, school RCT 2017–18), via McFillin 2023
  **[157]**. Location a significant predictor → universal approaches miss subgroups — Jibunoh et al.
  2024 **[159]** (n=5,000).
- **Bites:** APP, METRICS, FACIL.
- **Scale:** Worse the more *uniform* the rollout — acute at org/platform "push to everyone," but
  present at team scale too.
- **Mitigation seed:** Coping resources at every touchpoint; no standalone awareness content;
  pilot with **subgroup-worsening** monitoring (not just averages); opt-out / reduced-intensity track.
- **Consider further:** Can an *ecologically self-built* program even do subgroup analysis at N≈30,
  or is the safeguard only available at larger N?
- **Cross-link:** the *evaluation-blindness* angle on the same at-risk stratum is **A5 (Tier 2a)**.

**A3 — Scared-Straight / fear-arousal deterrence backfire** · `med` · conf high · all
- **Mechanism:** Vivid worst-case framing as a deterrent triggers reactance, social learning, and
  identity rebound → increases the warned-against behavior.
- **Evidence:** OR 1.68 (1.20–2.36) for reoffending vs nothing — Petrosino et al. 2022 **[9]** (9
  RCTs, N=946). "Ineffective" — NIJ CrimeSolutions **[10]**. Fear-appeal literature — Witte & Allen
  2000 **[11]**.
- **Bites:** FACIL, METRICS (communication copy).
- **Scale:** Universal; matters wherever messaging is authored.
- **Mitigation seed:** "Papageno orientation" — model coping success, not crisis. Ban urgency/alarm
  framing ("your community health is declining — act now"). Stories show recovery and effective help.
- **Consider further:** What is the catalog of *safe* framings? (Seeds a success-model entry.)

## B. Labeling / medical-model trap

**B1 — Labeling / at-risk identification (THE MASTER THREAT)** · `high` · conf high · all (acute team)
- **Mechanism:** Selection into an "at-risk/treatment" population → self-perception of needing
  treatment → anticipated devaluation → withdrawal/secrecy/lowered hope → network contraction →
  worse outcomes. A transient stressor crystallizes into a stable "career" as the group's troubled
  person; the label becomes a master status. **Identification itself is the harm** — no adversary
  needed, and it operates even via well-meaning facilitators or self-application.
- **Evidence:** modified labeling — withdrawal, secrecy, network shrinkage — Link et al. 1989 **[15]**.
  42% treatment vs 32% control undesirable outcomes (30yr) — McCord 1978 **[16]**. ~39%/49% mediated
  via reduced social support — Glass et al. 2014 **[17]**. Spoiled identity / courtesy stigma (taint
  extends to responders) — Goffman 1963 **[18]**. Earnings impact — Link 1987 **[19]**.
- **Bites:** APP, PROTO, METRICS, FACIL.
- **Scale:** Universal, but **acute at team scale** — at N≈10–50 any "at-risk" signal is de facto
  individual identification.
- **Mitigation seed:** Never expose individual signal frequency/history to anyone, incl.
  facilitators; ephemeral/unlinkable signals; asset-based non-deficit framing; treat *post-signal
  withdrawal by a previously-visible member* as a **sentinel event** (confidential follow-up), not
  positive variance.
- **Consider further:** This is the crux of the deferred protocol question — can a protocol *connect*
  someone without *identifying* them? (Parked: user has "a lot to say" here.)

**B2 — False-positive "at-risk" designation harms non-converters** · `high` · conf med · team·org
- **Mechanism:** Any "at-risk" flag mislabels a large fraction who'd never have had the problem; the
  label itself triggers anticipatory stigma, altered colleague behavior, self-stigma, secrecy. In a
  10–50-person group, probabilistic flagging *is* individual identification.
- **Evidence:** ~65% of clinical-high-risk cases never convert yet experience labeling shame/anxiety
  — Yang, Link et al. 2015 **[20]**. Nocebo RCT — awareness exposure increased false self-diagnosis —
  Sandra et al. 2025 **[21]** (n=215). Prevalence-inflation / awareness commentary — Foulkes &
  Stringaris 2023 **[22]**. TeenScreen admits ~84% chance of wrongly identifying teens as at-risk of
  suicide — Shaffer/Columbia TeenScreen **[160]**, via McFillin 2023 **[157]**.
- **Bites:** METRICS, APP.
- **Scale:** Acute at team scale (small N → flag = identification); present at org.
- **Mitigation seed:** No individual-level risk scoring/flagging; metrics community-level only; any
  metric-triggered outreach delivered **universally** to remove its marking value.
- **Consider further:** Is there any acceptable false-positive rate, or is individual flagging simply
  off the table?

**B3 — Responder/facilitator bias from diagnostic frame** · `med` · conf high · all
- **Mechanism:** A diagnostic/at-risk frame makes responders reinterpret ordinary behavior
  symptomatically and deliver lower-quality/patronizing/avoidant support — even when trained and
  well-intentioned. Managers with signal history apply biased performance assessments.
- **Evidence:** identical video rated worse with a diagnostic label than a behavioral description —
  Lam, Salkovskis & Hogg 2016 **[23]**. (Rosenhan 1973 **[24]** as illustrative background given
  later methodological criticism.)
- **Bites:** PROTO, FACIL, LEAD.
- **Mitigation seed:** Responders get a *connection* request without diagnostic framing; train on
  label bias; informationally isolate facilitators from individual signal histories.
- **Consider further:** How do you brief a responder enough to help, without handing them a frame
  that biases them?

**B4 — Self-stigma / prevalence inflation from medicalized framing** · `med` · conf med · all
- **Mechanism:** Accepting a MH label → internalizing stereotypes → lowered self-efficacy →
  avoidant coping → worsening. Macro: awareness leads some to re-categorize normal distress
  (loneliness, timezone fatigue) as disorder, adopt the script, and produce genuine new pathology.
- **Evidence:** self-stigma model (developed for already-diagnosed) — Corrigan & Watson 2002 **[25]**.
  Prevalence-inflation hypothesis (explicitly a "call to test") — Foulkes & Andrews 2023/2024 **[26]**.
  Medicalization → medication-seeking — McFillin 2023 **[157]**; reductionist events-based ACEs
  approach risks pathologizing — McDonald **[161]**. *(Severity downgraded high→med: plausible,
  partial clinical support, undemonstrated in remote-work contexts.)*
- **Bites:** FACIL, METRICS.
- **Mitigation seed:** Strengths-based, non-diagnostic language ("I could use connection," not "I'm
  struggling with my mental health"); problem-normalization ("common for distributed teams"); track
  positive indicators (connection, engagement) not deficit counts.
- **Consider further:** Untested at our scale/context — candidate for the first pilot's measurement.

## C. Contagion

**C1 — Peer contagion / deviancy training in aggregated support** · `high` · conf high · team·org
- **Mechanism:** Aggregating people with shared vulnerabilities lets peers reinforce the targeted
  states; distress/rule-breaking talk met with attention/empathy/laughter escalates. Worst with a
  predominantly high-risk group, unstructured time, thin facilitation.
- **Evidence:** deviancy training — Dishion, McCord & Poulin 1999 **[27]**. 42%/32% — McCord 1978
  **[16]**. Iatrogenic peer effects — Cho, Hallfors & Sanchez 2005 **[28]** (n=1,218). Homogeneous
  high-risk d=0.55 vs mixed/individual d=0.70 — Ang & Hughes meta-analysis **[29]**.
- **Bites:** PROTO, FACIL.
- **Scale:** Group-composition dependent (team/org); the *protocol* design controls exposure.
- **Mitigation seed:** Don't structure groups around distress-sharing; heterogeneous composition
  (mix struggling + thriving); trained facilitation; anti-rumination norms; route peer responses to
  **individual private channels first**, not broadcast; auto-rebalance if responder-pool distress
  concentrates.
- **Consider further:** In a 30-person community, is heterogeneous composition even achievable, or
  does small N force high-risk concentration?

**C2 — Suicide/crisis contagion via distress visibility (Werther)** · `high` · conf high · all (acute platform+team)
- **Mechanism:** Surfacing distress/crisis detail lets vulnerable members identify with and model
  the state via imitation, norm-shift ("crisis is the normal response"), and identification
  (amplified for a known peer). The protocol surfaces distress to peers — contagion's exact pathway.
- **Evidence:** 1,841 excess US suicides (+9.85%) after Robin Williams; suffocation +32.3% — Fink et
  al. 2018 **[30]**. 13 Reasons Why; causal attribution *disputed* — Bridge et al. 2019 **[31]**,
  disputed by Romer 2020 **[32]**. 25-study review — Calvo-Sánchez et al. 2024 **[33]**. WHO/AFSP
  safe-messaging; Papageno effect — **[34]**.
- **Bites:** PROTO, METRICS, FACIL.
- **Scale:** Platform (broadcast reach) **and** team (identified peers raise identification).
- **Mitigation seed:** Distress routes to **designated responders only — never a community feed**;
  severity tiers with **no free-text crisis narrative** to the group; validator strips
  method/location specifics + attaches resources; metrics never show raw distress counts; warm-handoff
  acute risk to crisis resources, not peers; Papageno design (every distress narrative carries a
  coping arc).
- **Consider further:** What's the visibility threshold at which peer-identified distress flips from
  supportive to contagious at N≈30? (Research gap.)

## D. Surveillance / metrics harm

**D2 — Goodhart/Campbell collapse + impression-management + selection bias** · `high` · conf high · all (acute org)
- **Mechanism:** (1) Once aggregate scores become targets, people perform the metric (respond to
  boost rates, avoid honest distress signals) → dashboard green while help-seeking collapses; (2) fear
  of consequences inflates positive surveys (a floor, not a reading); (3) volunteers are already
  healthier → overstated benefit; the most isolated are invisible. **Leaders declare success and
  defund at the point of failure.**
- **Evidence:** Campbell's law — Campbell 1979 **[44]**. Impression management 28–35% of variance
  even with anonymity — Keiser & Payne 2019 **[45]**. Workplace-wellness RCT null; 2020 *JAMA Int
  Med* confirms — Jones, Molitor & Reif 2019 **[46]**. CISD/D.A.R.E. sustained for decades on
  satisfaction (see J2). HR wellbeing practices conflict/contradict — Loon, Otaye-Ebede & Stewart
  2019 **[163]** (integrative review, 30+ studies). Engagement-without-thriving warns against
  engagement-as-wellbeing-proxy — Gallup 2025 **[132]**.
- **Bites:** METRICS, FACIL (evaluation).
- **Scale:** Universal; acute wherever metrics become KPIs (org).
- **Mitigation seed:** **Never make aggregate metrics a success criterion** tied to continuation or
  leadership evaluation — strictly diagnostic + lagging; track the *full* community incl. non-
  participants + exits; independent qualitative triangulation; pre-committed stopping rule; **treat a
  suspiciously positive trend as a gaming signal, not a win.**
- **Consider further:** If metrics can never be a success target, what *is* the legitimate success
  signal for the guide? (Bridges to the success model + the metrics-feasibility question.)

**D5 — Homophily–contagion confound misleads facilitators** · `med` · conf high · all
- **Mechanism:** Observational network metrics can't distinguish contagion (A caused B) from homophily
  (A,B distressed for the same environmental reason). A "wellbeing diffusion index" can be an artifact;
  facilitators then apply social interventions while the real stressor (overwork, isolation) goes
  untouched.
- **Evidence:** homophily–contagion confounding — Shalizi & Thomas 2011 **[51]**. "Contagion" of acne
  (62%) and headaches (47%) via the same methods — Cohen-Cole & Fletcher 2008 **[52]**.
- **Bites:** METRICS, FACIL.
- **Mitigation seed:** Any graph-based "spread" metric needs an explicit confound-control plan +
  statistician sign-off; give facilitators a checklist of shared-environment explanations to rule out.
- **Consider further:** Does the guide simply prohibit network "spread" metrics for lay facilitators?

## F. Consent / governance

**F1 — Coerced/bundled consent at the moment of distress** · `high` · conf high · all
- **Mechanism:** Broad data-sharing consent presented in ToS at acute distress, or as a precondition
  of help, when capacity is impaired and refusal is unrealistic; data later used for ads/AI-training/sale.
- **Evidence:** required MH intake then shared answers with ad platforms despite confidentiality
  promises — FTC v. BetterHelp (Mar 2023, $7.8M) **[63]**. "A ToS is not consent" — Crisis Text Line /
  Loris.ai, danah boyd Jan 2022 **[64]**. MH-app policy readability — Brookings 2023 **[65]**.
- **Bites:** APP, PROTO, FACIL.
- **Mitigation seed:** **Separate consent from help-seeking** — governance disclosures accepted during
  a calm onboarding, never at distress; ~6th-grade reading level; granular consent; withdrawable
  without losing access; review with a community advocate before launch.
- **Consider further:** Onboarding-time consent vs B1 (you can't fully understand consent before
  you've used the system) — how to keep consent live and re-affirmed?
- **Cross-link:** the data-leakage consequences are detailed at **Q-a / Q-b (Tier 3)**.

**F2 — Coercive financial incentives → compelled disclosure** · `high` · conf high · org
- **Mechanism:** Penalties for non-participation make refusal economically irrational, converting a
  "voluntary" program into a de facto mandatory medical exam + data-sharing requirement.
- **Evidence:** $25/wk opt-out fee + biometric screening — AARP Foundation v. Yale (2022, $1.29M
  settlement) **[66]**. Vacated 30%-surcharge rules as involuntary — AARP v. EEOC (D.D.C. 2017) **[67]**.
- **Bites:** PROTO, FACIL.
- **Scale:** Employer-program (org) specific.
- **Mitigation seed:** Structurally independent of any employer incentive/penalty/participation
  tracking; binding rule that utilization/signals never inform employment decisions.
- **Consider further:** Mostly out-of-scope for your volunteer communities — keep as a large-scale
  warning.

**F3 — Non-consensual crisis escalation → harmful welfare/police checks** · `high` · conf high · all (acute team)
- **Mechanism:** Automated crisis detection (keyword/sentiment/NLP) flags high-severity and escalates
  to emergency services/security/HR without consent; responders arrive in a way that outs MH status,
  creates a legal record/debt, or — with police — physical danger. Others learn and stop using it.
- **Evidence:** essay on crisis escalation — Calou & Zeavin 2022 **[68]**. Forced psychiatric
  hospitalization ~30× baseline suicide rate at 5–10yr — 2017 *JAMA Psychiatry* meta **[69]** (100
  studies). "Consent-Forward Paradigm" — Pendse et al. 2024 **[70]**. Crisis Text Line ~28
  non-consensual rescues/day — danah boyd **[64]**.
- **Bites:** PROTO.
- **Scale:** Universal; **acute for remote workers** — the employer/system knows the home address, so
  an automated wellness check *is* a disclosure of MH status.
- **Mitigation seed:** **Prohibit automated escalation to third parties by default**; any escalation
  beyond peers needs explicit, revocable, **advance** consent + a clear "do not escalate" option;
  surface crisis resources as **information, not triggered actions**; discuss scenarios before go-live.
- **Consider further:** This is the sharpest "well-intentioned automation kills trust" case — should the
  guide ban automated escalation entirely?

## G. Help-seeking suppression & stepped-care failure

**G1 — Chilling effect on help-seeking (stigma + reactance + coercion)** · `high` · conf med · all
- **Mechanism:** A formal help-signal channel can *suppress* help-seeking among those who most need
  it (label avoidance, self-stigma); coercive/collective participation makes the not-ready conceal
  → false negatives. Remote workers lack ambient informal help-seeking, so a stigmatized formal channel
  blocks all routes.
- **Evidence:** stigma and help-seeking — Corrigan, Druss & Perlick 2014 **[71]**. 144 studies; stigma
  4th-highest barrier; d≈−0.27 — Clement et al. 2015 **[72]**. No consistent benefit of compulsory
  community treatment — Kisely, Campbell & Preston 2011 **[73]**. "Avoiding the disclosure of mental
  health problems was a default position of workers" — Fukita, Kawasaki & Yorozuya 2025 **[164]** (10
  RCTs). Freelancer status correlated with MH-disorder history — Almeida et al. 2023 **[138]**.
  Professional isolation → social withdrawal, reluctance to seek support — Figueiredo et al. 2025
  **[165]**.
- **Bites:** entire intervention.
- **Mitigation seed:** Frame **entirely outside clinical language** — universal peer connection
  (everyone sends *and* responds), not a help-system for the distressed; explicitly voluntary,
  individually anonymous, never tied to performance or visible to management; leadership models
  help-seeking without enforcing it.
- **Consider further:** "Everyone sends and responds" is the leading candidate resolution to B1/C4 —
  does it dissolve the chilling effect, or just hide need?

**G2 — Gatekeeper training: confidence without behavior change; repels high-risk** · `high` · conf med · all
- **Mechanism:** (1) Gatekeeper programs raise knowledge/confidence but show no reliable improvement in
  observable helping behavior — a false "it's working" signal; (2) training the people *around*
  high-risk individuals can turn them into perceived *reporting nodes* rather than safe confidants.
- **Evidence:** MHFA: 6/9 high-quality studies no behavior change — Forthal et al. 2022 **[74]**. No
  significant skill improvement — 2025 gatekeeper RCT meta **[75]**. Wyman et al. 2010 **[76]** — *the
  17.8/37.8% figure is a baseline difference, not a training-caused decline* (also: gatekeeper training
  for adult staff found minimal change in adult–student communication about suicide; 18 high schools,
  453 peer leaders). (Part 2 plausible but not demonstrated as training-caused.)
- **Bites:** PROTO, FACIL.
- **Mitigation seed:** Don't treat training completion/confidence as readiness — require **observed
  role-play** before certifying responders + periodic behavioral follow-up; separate "trained" from
  "able"; keep responders free of evaluative/managerial authority.
- **Consider further:** Feeds the responder-readiness gate — what's the minimum *demonstrated*
  competency bar?

**G3 — Stepped-care evaporation: preventive layer fails to step up** · `high` · conf med · all
- **Mechanism:** The prevention→crisis continuum only works if people can escalate when they deteriorate;
  in practice step-up fails (clinical judgment over instruments, no formal agreements to the next level,
  patients lose contact with referrals). Someone stays trapped in the preventive layer as they worsen.
- **Evidence:** stepped-care step-up failure — Hermens et al. 2014 **[77]** (telehealth engagement
  ~56.6% initial; corrected figures). "Strategies limited to already identified high-risk individuals
  will not capture most youth who will die by suicide" — Wyman 2014 **[166]** (citing Luoma et al.).
- **Bites:** PROTO, FACIL.
- **Mitigation seed:** **Pre-connect explicit step-up pathways** (EAP, crisis line, clinician) before
  deployment, verified across time zones; severity/frequency threshold surfaces a **direct clinical
  resource**; **never let the preventive layer be the only layer.**
- **Consider further:** Directly operationalizes your "preventive AND emergency, not emergency-only"
  point — what's the minimum viable step-up for a small volunteer community without a budget?

**G4 — False reassurance: quick response masks unmet clinical need** · `med` · conf med · all
- **Mechanism:** A peer/automated response felt as "heard and helped" reduces urgency about
  professional care without any severity screen; the person disengages from professional pathways;
  conditions worsen; dashboards show high engagement mistaken for good outcomes.
- **Evidence:** only 32%/171 MH-app trials reported adverse events; deterioration 6.7% *but not
  different from controls* — Linardon et al. 2024 **[78]**. Commentary (false-reassurance) — Babu &
  Joseph 2025 **[79]**. (Direct causal evidence sparse.)
- **Bites:** PROTO, FACIL.
- **Mitigation seed:** Distinguish **"acknowledged" from "adequately supported"**; 24–48h follow-up;
  train peers *not* to position as clinical substitutes; make referral a standard output; track
  follow-through-to-referral, not just response rate.
- **Consider further:** How does a peer system know when *not* to reassure?

## I. Community / leadership

**I1 — Peer enforcement of harmful norms + polarization + call-out dynamics** · `high` · conf med · all (acute team)
- **Mechanism:** An ecologically-built program can encode and amplify existing maladaptive norms: (1)
  destructive conformity (stoicism/overwork → peer-shunning of help-signalers); (2) group polarization
  (homogeneous online deliberation → more extreme shame toward disclosure); (3) call-out dynamics (a
  named responder who "fails" becomes a target → "safety through silence").
- **Evidence:** peer punishment drove participation in *destructive* behavior — Abbink et al. 2017
  **[88]**. Group polarization, worse online/homogeneous — Sunstein 2002 **[89]**. Call-out chilling
  (~62% self-censor) — Aguiar 2025 **[90]**. "Among highly cohesive groups, there are also strong
  pressures to conform to the group norms" — Murthy 2023 Advisory Ch.3 **[133]**. User entitlement,
  low-quality contributions — Sapegin 2023/2024 **[121]**.
- **Bites:** FACIL, LEAD, PROTO.
- **Scale:** Universal; acute in tight (team) communities.
- **Mitigation seed:** **Norm-mapping phase** to surface maladaptive norms *before* protocol design;
  facilitators empowered to **challenge a destructive consensus**, not just mirror it; add a
  **help-seeking-suppression metric** (low signal in high-stress env = RED); structured dissent
  mechanisms; privacy-preserve responders (no public logging/grading); no naming-and-shaming.
- **Consider further:** "By and with the community" can *encode* the very norms that harm — how much
  authority does the facilitator/guide get to override community consensus?

**I2 — Leadership inaction / inadequate response to a first-time signal** · `high` · conf med · all (acute team)
- **Mechanism:** A leader receives a distress signal and fails to act (lack of training, boundary
  uncertainty, liability fear, avoidance). No response to a clear crisis, or a delayed/shaming response,
  confirms to the member *and the watching community* that signaling is unsafe — especially damaging on
  a first-time signal. Because reporting is low, leaders mistake silence for health.
- **Evidence:** harm underestimated due to low reporting — Grotto-de-Souza et al. 2023 **[91]**.
  Telework loneliness AOR 2.49 — Miyake et al. 2022 **[92]** (n=13,468). "Change at the center of FLOSS
  projects is uncommon… the founders' word still carries inordinate weight" — Crowston & Howison 2006
  **[171]**. BDFL veto bottleneck — Geiger et al. 2021 **[104]**.
- **Bites:** LEAD, PROTO.
- **Mitigation seed:** Escalation chain with **response-time SLAs** + auto-escalation fallback if no human
  ack; **leadership training a deployment prerequisite, not optional**; a **leader-readiness gate** (skills
  *and* institutional authority to respond); measure leadership response rate as a primary process metric.
- **Consider further:** You named leadership ignorance the greatest threat — but reframed leaders as part
  of a system. Does the gate test the *leader*, the *system*, or both?

## J. Transfer / fidelity — the "build-it-yourself ecological guide" failure cluster

**J1 — Voltage drop, model drift, surface-only cultural adaptation** · `high` · conf med · org·platform·(team transfer)
- **Mechanism:** A meta-process rebuilt by each community is exactly the transfer condition where EBPs
  decay: voltage drop (expert pilot → ordinary practitioners), model drift (each layer reinterprets
  components until only the name remains, while leadership believes it runs the validated model), and
  surface-only adaptation (language changes but not the deep-structure assumptions the program depends on).
- **Evidence:** median 52.6% voltage drop — McKay et al. 2023 **[93]** (DOI 10.1371/journal.pone.0268164).
  Scaling / voltage drop — Al-Ubaydli, List & Suskind 2019 **[94]** (NBER WP 25848); also List 2022 **[172]**.
  Model drift — Markström 2014 **[95]**. Transferability of health-promotion interventions — Schloemer &
  Schröder-Bäck 2018 **[96]**. MYRIAD (83% form-fidelity, null-to-harmful) — Kuyken et al. 2022 **[5]**.
  "Sources of Strength delivered with low implementation fidelity may have limited or even adverse impact"
  — Wyman, Cero, Brown et al. 2023 **[173]** (78 high schools, 39,960 students, 3 pooled RCTs).
- **Bites:** FACIL, LEAD.
- **Scale:** Acute at scale-up (org/platform), but any community-to-community transfer applies.
- **Mitigation seed:** Publish a **core-components inventory** (non-negotiable "active ingredients" vs
  adaptable periphery) communities map against at intake + 6-month review; **minimum-dose spec** + 30/90-day
  fidelity self-assessment ("voltage monitor"); **deep-structure diagnostic gate** before adoption
  (help-seeking norms, psychological safety, power, disclosure attitudes — block until prerequisites built);
  a **"model steward"** role (separate from the community) to flag drift.
- **Consider further:** This is *the* risk for a self-propagating guide — how do you keep "active
  ingredients" intact while honoring genuine ecological adaptation?

**J2 — Successor-facilitator competency decay + satisfaction-masks-harm** · `high` · conf med · all
- **Mechanism:** (1) Generational decay — each cohort of facilitators is trained more briefly; successors
  master surface mechanics but not judgment calls (when to escalate, unsafe disclosures, harmful dynamics)
  — invisible in async remote settings until a crisis; (2) measurement substitution — participants report
  satisfaction even when the process is null/harmful, so facilitators expand a harmful program (worsened by
  the community having *designed* it).
- **Evidence:** lay health workers want more supervision — Shahmalak et al. 2019 **[97]**. CISD
  satisfaction = gratitude, not symptom reduction — Kagee 2002 **[98]**. D.A.R.E. satisfaction with
  null/negative effects — West & O'Neal 2004 **[99]**. Intel 2023 survey: maintainer burnout 45% **and**
  documentation/onboarding 41% as paired top concerns → burnout degrades documentation → impairs successor
  onboarding — Intel 2023 Open Source Community Survey **[105]** (n=666; folds in the former J4 angle).
- **Bites:** FACIL, PROTO, METRICS.
- **Mitigation seed:** **Minimum competency standard** (not curriculum completion) with **observed
  role-play at each training generation**; supervision chain back to clinical/facilitation expertise;
  **cap train-the-trainer chains** (≤2 hops without re-certification); objective leading indicators
  *alongside* satisfaction; pre-committed stopping trigger; **independent outcome monitor** outside the
  facilitation team.
- **Consider further:** A "partly-assisted" guide could make AI the consistency-keeper across generations —
  is that a safe use of AI, or does it reintroduce voltage drop of a different kind?

---

# TIER 2a — Remote-general (heightened by remote work)

> Threats whose severity is *amplified by remote work as such*. **K is the terrain** — the
> baseline stressors and constraints that (i) define what the intervention must address (→ success
> model), (ii) make the population more vulnerable, *amplifying* the Tier-1 harms, and (iii) limit
> which interventions are even possible remotely. K-cluster source: domain expert (Rich),
> 2026-06-09; citations supplied by the v1.1 completeness pass. The number of these risk factors is
> *increasing*.

## K. Remote-worker baseline risk environment & operating constraints

**K1 — Remote isolation makes weak belonging the daily default (remote amplification of RF1)** · `high` · conf high · all
- **Mechanism:** Remote work makes isolation the daily default and weakens belonging to the remote
  community; ambient/informal contact is scarce. This *lowers the protective factors the
  intervention depends on* and raises baseline vulnerability. (This is the **remote amplification**
  of the universal risk factor RF1, not a separate phenomenon — the all-humans evidence lives in
  RF1; only the remote-specific evidence is kept here.)
- **Evidence:** remote work explains ~1/3 of the post-pandemic rise in distress; effect ~10× for
  those living alone — Emanuel, Harrington & Pallais 2026 **[129]** (N=588,322 employed US adults;
  five nationally representative surveys 2011–2024). Fully remote most engaged (31%) yet only 36%
  thriving vs 42% hybrid — Gallup 2025 **[132]**. Remote >3 days/week increases loneliness — He, Wei,
  Goodman, Pagan, Cuevas & Bather 2026 **[130]** (N=87,317, weighted ~33M employed US adults, 2024
  Household Pulse). Remote-work frequency moderately associated with loneliness, AOR 1.60 (95% CI
  1.04–2.46) — Miyake et al. 2021 **[131]** (n=4,052 Japanese desk workers, Dec 2020). *Current
  reviews:* integrated review of work and loneliness — McCarthy, Erdoğan, Bauer & Kudret 2025
  **[225]** (*Journal of Management*); social connection a critical health factor — Holt-Lunstad 2024
  **[226]** (*World Psychiatry*); sense of belonging in hybrid work settings — Urrila et al. 2025
  **[227]** (*J. Vocational Behavior*); teleworking effects on mental health — Figueiredo et al. 2024
  **[228]** (*IJERPH* systematic review). *Supporting
  (carried from v1's K1):* remote-work social isolation / wellbeing — Toscano & Zappalà 2020 **[136]**;
  remote-work survey context — Buffer *State of Remote Work* **[100]**.
- **Bites:** the whole substrate; amplifies B-cluster, C3/C4, G1, H2.
- **Note:** the *problem the intervention targets*, not a failure mode.
- **Amplifies → RF1 (Tier 1).** The universal mortality/belonging evidence (Holt-Lunstad 2015;
  Surgeon General 2023; Van Orden 2010) is stated once at RF1.
- **Consider further (success model):** what reliably builds belonging remotely?

**K2 — Timezone dispersion, interruption, sleep/circadian disruption → health** · `high` · conf high · all
- **Mechanism:** Cross-timezone work + frequent interruption → fragmented schedules, sleep
  disturbance, circadian misalignment → physical & mental-health decline; also makes synchronous
  connection (and synchronous interventions) hard to schedule.
- **Evidence:** WFH alone OR 1.71, work-during-nonwork-time OR 3.04, combined OR 3.93 (men 5.08) for
  sleep disturbance — combined-effect sleep study 2023 **[139]** (n=27,473; Sixth Korean Working
  Condition Survey 2020). Remote/hybrid more often associated with sleep/circadian disorders; severe
  disorders from irregular cadence — Polish National Health Programme 2021–2025 **[140]** (N>1,000).
  U-shaped, worst at <20% remote — Otsuka et al. 2026 **[141]** (n=824 Japanese workers, FY2021–FY2023,
  longitudinal). Telepressure → burnout β=0.19, mediated by work-related rumination — Qin, Yu, Cai,
  Jiang & Chung 2025 **[142]** (n=323). Social jetlag → depression, high social jetlag ≥2h OR 1.44 —
  Gao et al. 2025 **[143]** (n=148,410). Technostress→burnout→mood — Consiglio et al. 2023 **[144]**
  (n=225; e-work self-efficacy buffer). 24×7 availability technostress; professional isolation
  moderates wellbeing–performance — Jaiswal & Prabhakaran 2024 **[145]** (n=218 Indian IT). Hybrid
  technostress→detachment — Emerald Internet Research 2026 **[146]** (n=405). Sitting +31 min/day, ≥8h
  sitting OR 2.10 — sedentary-behavior meta-analysis **[147]** (n=282,264). Burnout–circadian review
  — **[148]**.
- **Bites:** operating constraint on any synchronous intervention (H2); amplifies vulnerability.
- **Consider further:** async-first design; respect-the-clock norms.

**K3 — Technological displacement / underemployment / job insecurity → depression** · `high` · conf high · all *(current, worsening)*
- **Mechanism:** AI/automation is displacing remote knowledge workers (acutely software developers;
  gig/freelance work such as Fiverr that supported livelihoods, e.g. in India) →
  unemployment/underemployment/insecurity → elevated depression. A *rising* macro stressor; the
  population is increasingly precarious.
- **Evidence:** 22–25yo developer employment −16% since late 2022 while experienced workers stable —
  Brynjolfsson, Chandar & Chen 2025 **[149]** (ADP payroll, 25M+ US workers). Automatable job → +4
  percentage-point probability of mental disorders — Blasco, Rochut & Rouland 2025 **[150]**
  (nationally representative French PSM). Layoff distress — Sharma et al. 2025 **[151]** (n=24 IT
  professionals + 20 Delphi experts, India, 2024). AI awareness → emotional exhaustion β=0.648; job
  insecurity carries 34.4% — Zheng & Zhang 2025 **[152]** (n=303). Firms substituted ~$1 reduced
  freelance spend for $0.03 AI — Kharazian 2026 **[153]** (thousands of firms, Q4 2021–Q3 2025). 54%
  say job insecurity significantly affects stress — APA 2025 Work in America **[154]** (n=2,017).
  Labor-market/MH — Posel et al. NIDS-CRAM **[155]**. Freelancer status correlated with MH-disorder
  history p=0.03; organizational employment inverse p=0.02 — Almeida et al. 2023 **[138]** (n=500, 35
  countries). Tidelift: 60% quit-or-considering — Speed/The Register 2025 **[120]**.
- **Bites:** raises baseline depression (amplifies every help-seeking, contagion, and labeling
  threat); a **confound for metrics** (D2/D5 — distress driven by the external labor market, not the
  community).
- **Consider further:** an intervention can't fix the labor market — what is the honest scope, and
  how do you avoid blaming the community for macro-driven distress?
- **Sub-entries below (K3a/K3b/K3c)** extend K3 without new IDs; K3 remains the single "external
  labor market drives distress" anchor.

**K3a — Anticipatory AI/automation-threat distress: fear of obsolescence harms even employed, non-displaced workers (incl. clinical construct AIRD)** · `medium` · conf med
- **Mechanism:** *Mere awareness* of AI in the workplace — without any actual job loss — predicts job
  insecurity, emotional exhaustion, anxiety, insomnia, identity loss, via AI-awareness →
  job-insecurity / work-family-interference → exhaustion. Clinicians propose a distinct syndrome
  ("AI Replacement Dysfunction") that impairs workers **before** displacement.
- **Evidence:** AI awareness → emotional exhaustion (β=0.648, p<0.001); job insecurity carried 34.4%
  of the effect, work-family interference 24.2%, serial path 16.8% — Zheng & Zhang 2025 **[152]**
  (n=303). Automatable-job workers had **+4 percentage-point** probability of severe mental disorder
  (corrected — see below), mediated by fear of job loss/skill obsolescence — Blasco, Rochut & Rouland
  2025 **[150]**. Clinical "AI Replacement Dysfunction" framework — McNamara & Thornton 2025 **[180]**.
  54% say job insecurity significantly affects stress — APA 2025 Work in America **[154]** (n=2,017).
- **Bites:** substrate, APP, PROTO.
- **Mitigation seed:** Track **subjective AI-threat perception** (not just actual job loss) as an
  early-warning signal; flag AIRD-type symptom clusters and high-automation-exposure occupations as
  priority subgroups; gatekeeper training should include AI job-loss as an explicit stressor category.
- **⚠ Corrections applied:** (1) Blasco effect is **+4 pp** (IZA DP15434), not +3. (2) The APA ~2×
  exhaustion/demotivation finding applies to firms hit by **government-policy changes broadly**
  (tariffs, federal cuts), **not AI-specific firms** — the APA report does not isolate AI-exposed
  firms; reframe as "~1.7–1.9× at policy-disrupted organizations, with AI obsolescence fears noted
  separately but without a dedicated effect size." Core phenomenon strongly supported across all four
  sources with corrections.

**K3b — Reputation-premium collapse for high-skill freelancers: expertise no longer buffers AI displacement (identity double-bind)** · `high` · conf med
- **Mechanism:** Generative AI compresses the historic reputational/earnings premium of top-tier
  freelancers (comparable output at negligible cost); the highest-skill, highest-reputation workers
  experience the steepest **relative** declines. This **inverts** the usual K3 framing — experienced
  experts who believed expertise was protective face an unexpected identity threat compounded by
  economic harm, a double-bind that "competence-as-protection" peer framing actively worsens.
- **Evidence:** ~2% decline in monthly contracts and ~5% earnings drop after GenAI releases; skilled
  freelancers now compete against algorithms — Hui, Reshef & Zhou 2024 **[181]** (Upwork, millions of
  contracts). Writing/editing/translation posts fell **20–50%** — Teutloff, Einsiedler, Kässi,
  Braesemann, Mishkin & del Rio-Chanona 2025 **[182]** (3M+ postings; top-earner harm labeled
  "suggestive"). Firms substituted ~$1 freelance spend for $0.03 AI; >50% of 2022 freelance buyers
  exited by Q3 2025 — Kharazian 2026 **[153]** (firm-level Q4 2021–Q3 2025).
- **Bites:** substrate, APP.
- **Mitigation seed:** Do **not** assume experienced/high-skill freelancers are psychologically
  resilient; peer support must acknowledge the reputational-premium collapse and identity threat;
  facilitators avoid framing competence as protection, and instead support AI-complementary reframing
  + income-volatility normalization.
- **⚠ Corrections applied:** (1) The "Winners and losers of generative AI" / *JEBO* paper authors are
  **Teutloff, Einsiedler, Kässi, Braesemann, Mishkin & del Rio-Chanona** **[182]** — distinguished
  from **Hui, Reshef & Zhou** (*Organization Science*) **[181]**, which is the Upwork contract study;
  the two are now cited to their correct sources. (2) Ramp/Kharazian published **Feb 2026** (not 2025);
  exit data runs to **Q3 2025** (not Q2). (3) The "top-earner harmed most" finding is real but
  **labeled "suggestive"** by the authors (secondary heterogeneity result) — do not present as
  definitive; the specific interaction coefficients (0.5%/1.7% per 1% prior earnings) are **unverified**
  paywalled regression estimates. (4) The "identity double-bind" is an editorial inference, not a
  direct claim of the papers.

**K3c — GenAI productivity-expectations ratchet: more output expected while hidden validation/debug burden rises → burnout for the still-employed** · `high` · conf med
- **Mechanism:** GenAI adoption inflates organizational throughput expectations while increasing
  **hidden** demands (validating, debugging, security-remediating AI output). Developers who can't
  sustain the accelerated pace face elevated burnout even as visible output grows — **employed but
  locked into an escalating output contract.** Demand amplification + invisible work under continued
  employment, plus a forecasting illusion (devs expect AI to save time but it costs time).
- **Evidence:** Job demands → burnout (β=0.398, p<0.001) — Feng, Afroz & Sarma 2025/2026 **[183]**
  (n=442 across 56 OSS communities + multinationals, PLS-SEM); qualitative: "I move fast with AI and
  move mountains of work, but I am losing my passion." RCT: experienced devs forecast AI would cut
  completion time 24% but it **increased** completion time **19%** — Becker et al. 2025 **[184]**
  (n=16 developers, 246 tasks; wide CIs).
- **Bites:** APP, PROTO, LEAD.
- **Mitigation seed:** Track invisible-work load (review burden, AI-output remediation hours)
  **separately** from commit velocity; facilitators name the expectations-ratchet in onboarding;
  help-seeking norms must affirm that "keeping up" is not a moral failure; protect autonomy over AI
  tool use and provide learning resources.
- **⚠ Corrections applied:** **The "~10 more PRs/year per core contributor" sub-claim appears in
  neither paper — flag/remove (unverified).** Note Becker n=16 with wide CIs in scale-context.
  "Non-renegotiable output contract" is an interpretive framing beyond what either paper directly
  demonstrates.

**K4 — Declining in-person contact (post-COVID inflection)** · `med` · conf high · all
- **Mechanism:** Since COVID, remote communities meet in person far less (travel cost/time); the
  periodic co-presence that built trust has thinned, and the trend is ongoing (observed in the
  decentralized-web-dev community).
- **Evidence:** time with friends fell ~70% 2003→2020 (150→40 min/day, ATUS); 49% in 2021 had ≤3
  close friends vs 27% in 1990 — Murthy 2023 Surgeon General Advisory **[133]**. 84% of remote workers
  spend entire workdays alone vs 23% onsite; 7% zero human contact — Emanuel et al. 2026 **[129]**.
  Gen Z nearly 2–3× more likely to report a lot of loneliness yesterday — Gallup 2025 **[132]**
  (n=19,043, May 2025). *Supporting:* Lyzwinski 2022/2024, *J Occ Health* 66:uiae005 (scoping review,
  62 studies) **[211]**; Wells et al. 2022 (systematic review, 34 studies) **[212]**.
- **Bites:** erodes the trust substrate the intervention assumes (H2; J1 deep-structure prerequisites).
- **Consider further:** should the guide recommend periodic co-presence as an active ingredient?

**K5 — "Degraded mode": loss of embodied / experiential co-present learning** · `high` · conf med · all
- **Mechanism:** Experiential learning involving the body and the physical presence of others is
  uniquely valuable for building community comfort and help-seeking. Remote operates in a *degraded
  mode* where some connection/help-seeking affordances simply aren't available — not a normal
  evolutionary state for humans.
- **Evidence:** "This mismatch can lead to frustration for both the developer struggling with
  unfamiliar code and the maintainer reviewing potentially flawed contributions" — Coates 2024 **[156]**
  (qualitative practitioner synthesis, citing Rob Mensching; thin single source). Grounded in the
  social-presence literature — Oh, Bailenson & Welch 2018 **[217]** (foundational review of
  social-presence theory) — and the embodiment / remote-collaboration literature: co-embodiment in
  remote interaction — Luria et al. 2019 **[218]**; the cost of losing embodied coordination —
  Sergeeva, Faraj & Huysman 2020 **[219]** (*Organization Science*); the multimodal cues remote
  collaboration strips out — Kim, Billinghurst & Kim 2020 **[220]**.
- **Bites:** caps the ceiling of any remote intervention; some school/military protective mechanisms
  may not transfer (J1 surface-vs-deep adaptation).
- **Mitigation seed (implied):** prioritize the protective factors with viable remote analogs; treat
  embodiment-dependent mechanisms as non-transferable until proven otherwise.
- **Now grounded** in the social-presence (Oh et al. 2018 **[217]**) and embodiment /
  remote-collaboration literature (**[218][219][220]**); a remote-worker-specific embodiment study is
  still desirable (see Appendix B).
- **Consider further (key success-model question):** which protective factors *require* embodiment,
  and which have viable remote analogs?

**K6 — Hard-to-corral / unreachable-in-bulk → selection bias & coverage gaps** · `high` · conf med · all
- **Mechanism:** Remote workers are notoriously hard to get onto one channel at one time; you reach —
  and gather SNH data from — only the reachable subset, so the least-reachable (often highest-need)
  are invisible. Interventions are simply harder to run remotely.
- **Evidence:** grounded in the hard-to-reach / non-response / respondent-driven-sampling methodology
  literature: systematic review of strategies for reaching socially disadvantaged groups — Bonevski et
  al. 2014 **[221]** (*BMC Med Res Methodol*, the strongest hard-to-reach methodology source); snowball
  adaptations for hard-to-reach subgroups — Sadler et al. 2010 **[222]**; respondent-driven sampling of
  hidden populations — Heckathorn 1997 **[223]** (foundational RDS method); recruitment interventions
  for vulnerable populations — UyBico, Pavel & Gross 2007 **[224]**. Closest adjacent: "burnout often
  goes unnoticed in the open-source community, as contributors silently drop out and disengage" —
  Raghunathan 2024 **[175]** (members become unreachable, biasing who stays visible; but this is the
  silent-attrition angle, K9, not recruitment-coverage). Also connects to D2 healthy-worker selection.
  **A remote-worker-specific coverage-bias study is still ideal** (see Appendix B).
- **Bites:** METRICS (selection bias), PROTO/FACIL (coverage), LEAD (mistaking the reachable sample's
  health for the community's).
- **Consider further:** channel-agnostic "meet them where they are" design (a stated PRM goal) and
  phone-tree fan-out (see design ideas in the session log) as partial coverage mitigations.

**K7 — Professional/career isolation as a distinct harm from social loneliness (lost mentoring, visibility, promotion penalty)** · `medium` · conf high · all *(was L1)*
- **Mechanism:** Remote workers lose informal mentoring, casual problem-solving, organizational
  visibility, and informal learning ("out of sight, out of mind"). This is empirically **distinct from
  social loneliness**: it produces missed-career-opportunity perceptions, reduced self-efficacy, a
  degraded wellbeing→performance link, and measurable career harm (e.g., promotion at ~half the rate
  despite higher productivity).
- **Evidence:** professional isolation moderated the wellbeing–performance relationship (3-way
  interaction p=0.010; performance lowest at high PI + low boundary control, 2.85 vs 4.05); 24×7
  availability technostress — Jaiswal & Prabhakaran 2024 **[145]** (n=218 Indian IT, 2022–23). Grounded
  theory: telecommuting reduces networking, informal learning, mentoring (stronger in public sector) —
  Cooper & Kurland 2002, *J. Organizational Behavior* 23:511–532, doi:10.1002/job.145 **[213]**. RCT:
  home workers 13% more productive but **promoted at half the rate** — Bloom, Liang, Roberts & Ying
  2015, *QJE* 130(1):165–218 **[214]**. Golden, Veiga & Dino 2008, *J. Applied Psychology*
  93(6):1412–1421 **[215]**. Integrated review of work and loneliness — McCarthy et al. 2025 **[225]**
  (*Journal of Management*); teleworking effects on mental health — Figueiredo et al. 2024 **[228]**
  (*IJERPH* systematic review).
- **Bites:** substrate, APP.
- **Mitigation seed:** Distinguish social- vs professional-isolation interventions; add lightweight
  visibility rituals (async show-and-tell, shared work logs, explicit mentoring pairings) that rebuild
  professional presence without surveillance; advocate promotion-criteria transparency to counter the
  remote advancement penalty.
- **Distinct from:** K1 (social belonging), K3 (job insecurity/displacement), H2 (weak-tie atrophy).
- **Note:** Jaiswal interaction stats (p=0.010; 2.85 vs 4.05) are paywalled — confirmed
  design/direction, treat exact values as unverified detail (not fabrication). Multi-decade,
  multi-method support.

**K8 — Reciprocal distress↔isolation feedback loop: distress independently increases perceived isolation; detection itself can feed the loop** · `high` · conf high · all *(was L2)*
- **Mechanism:** Isolation causes distress **and** distress independently increases perceived
  isolation — a bidirectional reinforcing loop. Critically, a wellness platform that **surfaces or
  amplifies distress signals** (e.g., highlighting who didn't engage) can worsen isolation perception;
  interventions targeting only one direction will fail.
- **Evidence:** 3-wave cross-lagged SEM: both isolation→distress and distress→isolation paths
  significant; "The findings highlight a reciprocal effect between psychological distress and
  isolation" — Van Zoonen & Sivunen 2022 **[174]** (n=1,164 Finnish workers; 3-wave longitudinal
  Mar–Sep 2020; 77.2% remote 5 days/week). Integrated review situating the distress↔isolation dynamics
  of work loneliness — McCarthy et al. 2025 **[225]** (*Journal of Management*).
- **Bites:** APP, PROTO, METRICS.
- **Mitigation seed:** **Do not surface distress signals or non-engagement** in ways that heighten
  perceived isolation; break the loop with low-stakes positive touchpoints that reduce distress first;
  monitor distress **and** isolation as co-evolving indicators with early triggers before the loop
  self-sustains.
- **Distinct from:** K1 (isolation as upstream cause) and C2/C3 (visibility→contagion) — here the
  mechanism is the **self-sustaining loop** and the risk that **detection feeds it**.
- **Correction applied:** The "reverse path (distress→isolation) is *often stronger*" / "meta-analytic
  hints" framing **could not be verified** — the confirmed finding is **symmetric reciprocity** (both
  directions significant), with no confirmed directional ranking. Drop the "stronger reverse path"
  claim; the loop + both-directions-matter + detection-can-feed-it core is fully supported.

**K9 — Silent dropout / invisible attrition as a distress signal in distributed communities** · `high` · conf med · all *(was L3)*
- **Mechanism:** In remote/OSS communities there is **no visible absence**: distressed members simply
  stop contributing/communicating without signaling distress. Unlike physical workplaces where absence
  triggers concern, digital absence is normalized and unnoticed until total attrition — producing
  survivorship/selection bias where only resilient members stay visible, masking population-level
  distress. The missing signal is the member's **own silence/exit**, the very thing a preventive
  system must detect.
- **Evidence:** preferred re-anchors (peer-reviewed, empirical): Raman et al. 2020, "Stress and Burnout
  in Open Source," **ICSE-NIER 2020** (CMU) **[176]**; Guizani et al. 2021, emoji/dropout study **[177]**.
  Onion-model health indicators: low active-user participation + leadership-succession failure;
  "change at the center of FLOSS projects is uncommon" — Crowston & Howison 2006 **[171]** (observational
  over the 100,000+ SourceForge population). (The original lead source, Raghunathan 2024 **[175]**, is a
  low-tier whitepaper — downgraded; see correction.)
- **Bites:** APP, METRICS, FACIL.
- **Mitigation seed:** Treat sudden activity/contact drop as a signal requiring **human follow-up (with
  consent)**; establish non-technical touchpoints decoupled from work output; design outreach for
  members who go silent; use onion-model contribution mapping + lottery-factor as leading indicators.
- **Distinct from:** K6 (hard-to-corral selection bias *at recruitment*) and C4 (broadcast→no response).
- **⚠ Correction applied:** Raghunathan **[175]** is a **self-described whitepaper in a low-tier
  open-access journal (CARI Journals) — downgrade evidential weight**; the verbatim quote could not be
  confirmed against full text (likely close paraphrase). **Re-anchor on** Raman et al. 2020 **[176]**
  (ICSE-NIER 2020, peer-reviewed, empirical) and Guizani et al. 2021 **[177]** (arXiv:2102.05737). The
  phenomenon itself is well-supported.

**K10 — Telepressure / always-on availability drives rumination, sleep loss, burnout (modifiable upstream of K2)** · `high` · conf high · all *(was, in part, the K2 deep-dive)*
- **Mechanism:** Telepressure (perceived expectation to respond quickly) extends cognitive engagement
  into non-work hours → work-related rumination that blocks detachment/recovery; combined with actual
  after-hours work it **nearly quadruples sleep-disturbance odds.** The operative mechanism is the
  **social-availability norm itself** — directly modifiable by community design.
- **Evidence:** Telepressure → burnout (β=0.19, p<0.001), mediated by work-related rumination, worse
  when organizational support low — Qin, Yu, Cai, Jiang & Chung 2025 **[142]** (n=323). WFH alone OR
  1.71 for sleep disturbance; work-during-nonwork-time OR 3.04; **combined OR 3.93 (men 5.08)** —
  combined-effect sleep study 2023 **[139]** (n=27,473). Blurred boundaries OR 2.67 and >45 hrs/week
  OR 2.11 as strongest independent predictors of emotional exhaustion (63.1% prevalence) — *J. Health &
  Rehabilitation Research* (2025), "Prevalence of Burnout and Emotional Exhaustion in Remote or Hybrid
  Workers" (n=247) **[216]**.
- **Bites:** K2, H1, APP.
- **Mitigation seed:** Build explicit off-hours messaging norms + socially-enforced quiet windows;
  default the platform to silencing notifications outside working windows; model facilitator
  disconnection; use right-to-disconnect-style **collective rituals**, not individual willpower.
- **Distinct from:** K2 (timezone/interruption→circadian) and H1 (CMC misattribution) — the lever is
  the **availability norm**.
- **Correction applied:** Journal name fix — PMC12383041 is **Behavioral Sciences (MDPI)** **[142]**,
  not Frontiers. All statistics verified exactly.

**K11 — Inverted-U / non-monotonic work-mode dose curve: fully-remote shows a persistent mental-health/thriving deficit vs hybrid (with a hybrid sleep counter-twist)** · `high` (scoped) · conf med · all *(was L9)*
- **Mechanism:** Work-mode outcomes are non-monotonic. **Fully-remote carries a persistent
  mental-health/thriving deficit vs hybrid** in both COVID-era and post-COVID data, implying a
  purely-remote community has a structural disadvantage that better belonging design *reduces but may
  not fully erase*. Counter-twist: hybrid's **irregular cadence** produces the worst circadian/sleep
  disruption (instability of both modes without the regularity of either).
- **Evidence:** both exclusive-remote and exclusive-in-person had higher odds of poorer self-rated
  mental health vs hybrid (aOR=2.79); fully-remote highest engagement, lowest thriving (36% vs 42%
  hybrid); COVID-era artifact caveat — Bodner, Ruhl, Barr, Shridhar, Skakoon-Sparling & Card 2022
  **[178]** (n=1,576 Canadian, Apr–Jun 2021). "On-site ties hybrid on thriving" — Gallup 2025 **[132]**.
  Hybrid "least beneficial" for sleep due to irregular cadence — Polish National Health Programme
  2021–2025 **[140]** (N>1,000). Sense of belonging in hybrid work settings — Urrila et al. 2025
  **[227]** (*J. Vocational Behavior*); the paradox of remote work, where employee wishes and wellbeing
  collide — Olafsen, Stenling, Tafvelin & Bentzen 2024 **[229]** (*Human Resource Development
  International*).
- **Bites:** substrate, LEAD, APP.
- **Mitigation seed:** Design at least some in-person/synchronous touchpoints into nominally-remote
  communities to capture the hybrid mood benefit; **anchor hybrid cadence to a predictable rhythm** to
  avoid the circadian penalty of irregular switching.
- **Distinct from:** K1/K4 (isolation, declining in-person contact) and K2 (circadian) — the variable
  is the **work-mode configuration** and its non-monotonic dose-response.
- **⚠ Correction applied (framing downgrade):** **The clean "both extremes worse" inverted-U is
  overstated.** Bodner **[178]** is a **COVID-era artifact** (skewed sample: 77.2% hybrid, only 6.6%
  in-person-only; cross-sectional; in-person disadvantage likely reflects COVID safety anxiety).
  **Gallup [132] does NOT show a clean inverted-U:** on thriving, on-site **ties** hybrid (both 42%)
  and on-site has **lower** stress than both hybrid and remote. Correct reading: *fully-remote is worse
  than hybrid AND on-site on thriving; hybrid and remote are similarly stressed; on-site is not clearly
  worse than hybrid post-COVID.* Cite Bodner as a pandemic-context finding, not a structural law. The
  Polish sleep finding **[140]** is accurately cited and adds genuine nuance. Re-scope severity to the
  **fully-remote deficit** specifically (well-supported), not the symmetric U.

**K12 — Long-term full-remote work suppresses the *need to belong* itself (engagement-resistance risk)** · `high` (re-scoped) · conf med · all *(was L11)*
- **Mechanism:** Prolonged remote work appears to reduce not just the *fulfillment* of the belonging
  need but **the need itself**, lowering motivation to seek social re-integration and producing a
  self-reinforcing withdrawal tendency. Members fully remote for an extended period may not engage
  with the very programs designed to help them — a **timing-critical** hazard.
- **Evidence:** three-wave longitudinal study (n=876): heavy remote work "not only reduced employees'
  sense of community but also their need to belong to one," described as **unexpected**; "Remote work
  is not just either a good or a bad thing. It can increase flexibility, but also weaken the sense of
  community" — Finnish Institute of Occupational Health (Kaltiainen & Suutala) 2024/2025 **[179]**
  (City of Kuopio + OP Financial Group; observational/longitudinal, not causal). Corroborating
  withdrawal arm: professional isolation → social withdrawal and reluctance to seek support —
  Figueiredo, Margaça & Sánchez-García 2025 **[165]** (bibliometric review of 65 articles, 40
  countries; underlying studies cross-sectional). Sense of belonging in hybrid work settings — Urrila
  et al. 2025 **[227]** (*J. Vocational Behavior*).
- **Bites:** APP, PROTO, FACIL.
- **Mitigation seed:** Initiate preventive SNH interventions **EARLY** (before prolonged isolation
  sets in); do not rely on opt-in community spaces or assume stable belonging motivation; onboard
  members into community structures at entry; use proactive, facilitated connection rather than passive
  availability.
- **Distinct from:** K1 (weak belonging) and H2 (network atrophy) — here the **motivational substrate
  for community-building decays**.
- **⚠ Correction applied (important — most contested claim downgraded):** **Removed "irreversibility,"
  "down-regulation," "withdrawal-spiral / motivational-substrate decay" language and the ">6–12 month"
  threshold** — the FIOH source **[179]** describes a **self-reinforcing tendency**, *not*
  irreversibility, and uses none of those terms; the threshold has **no empirical basis** in either
  source. This collides with foundational theory (Baumeister & Leary 1995), where deprivation
  **intensifies** the belonging need rather than suppressing it. **Re-labeled as "belonging-need
  suppression / engagement-resistance," not "irreversibility."** Mitigation (early proactive
  intervention) remains well-grounded after the downgrade.

**K13 — AI-mediated displacement (terrain twin of H3 / K3)** *(cross-reference, no new ID)* — the
*baseline-terrain* face of bot displacement (declining human contact as ambient condition) is covered
by **H3 (Tier 3, mechanism)** + **K4 (declining in-person contact)** + **K3 (labor-market macro
stressor)**. No separate K ID; cross-linked.

## H2 — Remote-network atrophy (CMC cluster, remote-amplified)

**H2 — Remote-network atrophy: weak-tie loss, video fatigue, onboarding failure** · `high` · conf high · all (remote)
- **Mechanism:** Remote-only work degrades the social substrate the intervention runs on: weak/bridging
  ties atrophy (siloed strong-tie clusters; signals may never reach the best responder); videoconference
  fatigue makes the "rich" channel least accessible to the exhausted (selection toward the well-rested);
  remote-onboarded members form almost no bridging ties → the highest-need are least reachable.
- **Evidence:** WFH −32% weak-tie time, −9% bridging ties, −41% bridging collaboration; firm-wide remote
  made groups less interconnected — Yang, Holtz, Jaffe, Suri, Sinha et al. 2022 **[84]** (n=61,182
  Microsoft, natural experiment). Zoom Exhaustion & Fatigue scale — Fauville et al. 2021 **[85]**
  (N=2,724). Nonverbal overload (Zoom fatigue) — Bailenson 2021 **[86]**. Remote-onboarded employees
  resign more within 3yr — Smite et al. 2025 **[87]**. Internet Paradox — Kraut et al. 1998 **[167]**.
  255 studies on remote collaboration — Morrison-Smith & Ruiz 2020 **[168]**. Group belongingness top
  protective factor against videoconference fatigue — Bennett et al. **[169]** (n=55/279 VCs). 74% rate
  remote onboarding a failure — Speakwise 2026 **[170]**.
- **Bites:** underlying community layer, FACIL, APP (onboarding).
- **Mitigation seed:** **Network-mapping gate before launch** (find siloed clusters/missing bridges);
  track weak-tie density + new-member centrality as leading indicators; route **cross-cluster pairings**;
  structured weak-tie onboarding for ~8 weeks; **audit aggregate video-load; default to audio for the
  richer-medium step.**
- **Consider further:** The intervention assumes a social substrate that remote work has already
  eroded — does the guide need a "build the substrate first" pre-phase?

## D1 — Employer-adjacency (surveillance/metrics cluster, remote-amplified)

**D1 — Employer-adjacency: surveillance perception + disclosure retaliation** · `high` · conf med · all
- **Mechanism:** When perceived as employer-adjacent (company benefit/device/shared infra), two harms
  compound: (1) anticipated surveillance → the highest-risk self-censor, skewing participation and
  corrupting metrics; (2) disclosure retaliation → a signal seen/inferred by anyone with employment
  authority enters supervisor discretion (scrutiny, exclusion, documented "gaps") — plausibly deniable.
- **Evidence:** monitored vs unmonitored worse on MH (32%/24%), work-harms-MH (45%/29%), exhaustion
  (39%/22%), intent-to-leave (42%/23%) — APA 2023 Work in America **[12]** (n=2,515). Of disclosers
  with negative experiences, 46.7% lost jobs — Dewa et al. 2021 **[42]**. EEOC v. Ranew's Management
  ($250K) **[43]**. "Supervisors in this study appeared to know a great deal about the personal lives
  of the teleworkers" — Collins, Hislop & Cartwright 2016 **[162]** (UK public-sector teleworking).
  *(Several secondary stats corrected/removed by verifier.)*
- **Bites:** all layers, acutely PROTO + governance.
- **Scale:** Any employer context, any size.
- **Mitigation seed:** Run on **technically + visibly separate** infrastructure from any monitoring;
  route only to peers with **no employment authority** over the sender; make employer/manager access
  to individual data **technically impossible** (not policy-only); publish an auditable data-flow
  diagram; run a trust/legibility audit with real members; ideally worker-governed/independent
  ownership.
- **Consider further:** Your communities are *not* employer-run — does that neutralize D1, or does
  "any infra someone controls" reintroduce it?

## A5 — Subgroup-masking (iatrogenic cluster, remote-amplified)

**A5 — Subgroup-masking: harm + averaged intervention BOTH hide the at-risk stratum (defeats null-result evaluation)** · `high` (see caveat) · conf med · org·platform·team
- **Mechanism:** Remote work does not uniformly reduce engagement/wellbeing — it *selectively* harms
  high/moderate-loneliness workers while leaving low-loneliness workers unaffected. A universal
  intervention evaluated on population averages can show a **null** result while masking severe harm to
  the loneliest subgroup. This is a different angle from A2: not "universal prevention worsens a
  subgroup," but that **the underlying harm *and* an averaged-out evaluation both hide the same
  stratum** — so a clean-looking null is not evidence of safety.
- **Evidence:** Moderated mediation: for high-loneliness workers, remote work significantly negatively
  predicted job engagement (b=−0.08, β=−0.23, p<.001); for low-loneliness workers, no effect (b=−0.001,
  p=.96); authors explicitly warn that interventions averaging across employees miss the most-harmed
  subgroup — Bareket-Bojmel, Chernyak-Hai & Margalit 2023 **[101]** (n=349 US/UK Prolific,
  cross-sectional, 2022). **Quote:** *"Remote work predicted decreased job engagement only for employees
  with high and moderate levels of loneliness. These results challenge the widespread assumption that
  remote work impairs employee engagement."*
- **Bites:** APP, PROTO, METRICS.
- **Mitigation seed:** Risk-stratify (screen for high-loneliness, solo-living, junior/freelance
  subgroups); track **individual-level outcomes**, never group averages alone, to catch non-responders
  and harmed subgroups early; route the lonely subgroup to more intensive contact (step-care logic).
- **Distinct from:** A2 (worsening) — here the hazard is *evaluation blindness*.
- **⚠ Verifier caveat:** Cross-sectional Prolific sample → cannot establish causation (loneliness may
  precede both remote-work preference and disengagement). A representative Norwegian longitudinal study
  (n=1,511) **[102]** found remote work *positively* associated with engagement overall, so the
  population-level harm claim is not settled, and **severity=high may be overstated** for a population
  where lonely workers are *targeted* rather than averaged. Single unreplicated moderated-mediation
  study. **Convergent (not replication) support:** Becker et al. 2022 **[103]** (loneliness as a key
  mediator of remote-work harm).
- **Cross-link:** the *worsening* angle on the same stratum is **A2 (Tier 1)**.

---

# TIER 2b — Distributed / OSS-community sub-context

> The open-source / distributed-maintainer literature is the closest available proxy for
> distributed-community dynamics, but it is **dev-specific** — a generalization caveat applies to
> every entry in this tier (D6, D7, H4, I3, I4, J3). These extend their Tier-1 mechanism clusters
> (D-, H-, I-, J-) into the distributed sub-context.

## D. Surveillance / metrics (OSS sub-context)

**D6 — Invisible facilitation / emotional-labor blind spot: care work is untracked → hidden facilitator burnout + biased health metrics** · `medium` · conf high · all *(was L6)*
- **Mechanism:** Maintainers/facilitators perform complex, invisible interpersonal and organizational
  work (conflict mediation, donation/labor management, onboarding diplomacy, code-of-conduct
  enforcement). Because workload metrics capture only technical/visible output, any community-health
  metric layer systematically **underestimates the load on the very people SNH depends on** — burning
  them out and biasing the metrics simultaneously.
- **Evidence:** F/OSS maintainers perform "complex and often-invisible interpersonal and organizational
  work" — Geiger, Howard & Irani 2021 **[104]** (qualitative interviews across many F/OSS projects,
  UCSD). Maintainer burnout the **top** challenge at **45%** — Intel 2023 Open Source Community Survey
  **[105]** (n=666 self-selected). **~50% of OSS activities are invisible** and half of that work is
  uncompensated — OpenSauced 2024 **[106]** (quantitative anchor, 142 respondents). **Quote (confirmed
  verbatim abstract language):** *"F/OSS maintainers also perform complex and often-invisible
  interpersonal and organizational work to keep their projects operating as active communities of users
  and contributors."*
- **Bites:** FACIL, METRICS, LEAD.
- **Mitigation seed:** Make invisible facilitation labor visible, rotate it, and recognize it in
  acknowledgment systems; community-health metrics must include facilitation/social labor alongside
  technical contribution; distribute care labor explicitly before the community grows.
- **Distinct from:** J2 (successor competency decay) and K3 (economic precarity) — here the harm is the
  **measurement invisibility of care labor itself**.
- **Correction applied:** The "more difficult and draining aspects" line is a paraphrase of paper body,
  not a verbatim abstract pull — the verbatim abstract sentence is used above instead. Intel 45% is "of
  survey respondents," not a population estimate. Stronger quantitative anchor: OpenSauced **[106]** (142
  respondents).

**D7 — Public-performance-audit impostor phenomenon: output visibility drives anxiety, self-silencing, productivity suppression (AI-amplified)** · `medium` · conf med · all *(was L13)*
- **Mechanism:** Public code review, open contribution histories (commit graphs/leaderboards), and
  constant output visibility create a persistent performance-audit environment. Members chronically
  compare worth against visible metrics → impostor phenomenon, anxiety, self-silencing that suppress
  help-seeking and perceived productivity, progressing to depression/burnout. Remote/async removes the
  normalizing peer feedback that would attenuate it; AI adds a second layer (feeling inadequate vs. AI
  output speed).
- **Evidence:** n=624 software engineers across 26 countries — **52.7%** experience frequent-to-intense
  impostor phenomenon (women 60.6%, men 48.8%); statistically significant negative effect on perceived
  productivity across **all** SPACE constructs; may progress to depression/burnout — Guenes, Tomaz,
  Kalinowski, Baldassarre & Storey 2023 **[107]**. First-person Babel-maintainer account on
  commit-as-worth — Zhu 2019 **[108]** (n=1). **Quote:** *"The presence of IP showed a statistically
  significant negative effect on the perceived productivity for all SPACE framework constructs."*
- **Bites:** APP, FACIL, METRICS.
- **Mitigation seed:** De-prioritize individual-output leaderboards in community metrics; normalize
  struggle and surface routine peer vulnerability; onboarding/facilitator training names impostor
  phenomenon and its AI-augmented form; validate non-code contributions.
- **Distinct from:** B4 (self-stigma from labeling) and K1 — here the driver is the **visibility/audit
  architecture** of public contribution; concrete design lever = de-emphasize output dashboards.
- **⚠ Correction applied:** **DROP the likely-fabricated "Devsu 2025: 40% AI-induced impostor"
  statistic — unverifiable.** For the AI-amplification layer use instead: Stack Overflow **2025
  Developer Survey** **[109]** (n=49,009) — 20% of developers report declining confidence in personal
  problem-solving from AI over-reliance — plus the SO blog (Jul 31 2025) **[110]** qualitative coverage.
  Backbone (Guenes 2023 **[107]**, Zhu 2019 **[108]**) is solid.

## H. Communication-medium / CMC (OSS sub-context)

**H4 — Capable-contributor blind spot: visible high competence/output masks rapid deterioration; risk indicators are anti-predictive** · `high` · conf med · all *(was L4)*
- **Mechanism:** High-achieving / neurodivergent contributors maintain visible productivity and apparent
  normalcy until a sudden discontinuity; members and gatekeepers calibrate risk on recent output and
  **systematically miss the deterioration underneath**. The "capable contributor" profile is
  *anti-predictive* of safety — defeating any output- or distress-cue-based detection.
- **Evidence:** a project lead's published reflective account following a contributor's death —
  jackpot51 2021 **[116]** (n=1 reflective account). The source attributes the death to suicide as the
  author's stated belief; no cause was publicly established, and this catalog does not assert one. Its
  detection-relevant observation is that the contributor's visible competence and sustained output left
  the community with nothing observable to act on. The source names the broader pattern
  *anti-selection* — the claim that capability is inversely related to safety rather than protective;
  that claim rests on this account alone and is marked low-confidence below. Independent peer-reviewed
  corroboration of the high-capability/elevated-risk inversion: autistic individuals with exceptional
  cognitive ability show *elevated* suicidal ideation — Cassidy et al. 2022/2023 **[117]**. Prevalence
  anchor: 51% diagnosed vs ~19% US adults — OSMI Mental Health in Tech Survey 2016 **[118]**
  (n≈1,400 self-selected).
- **Source handling:** the contributor's age, the project, and the account's death-descriptive passages
  are deliberately withheld under [`docs/publication-standards.md`](../../docs/publication-standards.md)
  (§A2–A4). The source's own wording is not reproduced: it frames suicide in terms of achievement and
  uses outbreak metaphor, both excluded by our safe-messaging norms (§A5). The reference is retained so
  the claim stays checkable (§A6).
- **Bites:** APP, FACIL, LEAD.
- **Mitigation seed:** Do **not** rely on visible distress cues or productivity drops as primary risk
  indicators; build check-in/belonging infrastructure for high-performers; gatekeeper/peer training must
  explicitly name the capable-contributor blind spot and the misleading nature of competence-as-safety.
- **Distinct from:** G2 (gatekeeper false confidence) and B3 (responder diagnostic bias) — here visible
  competence is itself an actively-misleading safety cue. (Definitional overlap with G2/B3 is
  acknowledged.)
- **⚠ Correction applied:** **DROP the unverifiable "Chan, Business Insider 2020" secondary cite.** Cite
  OSMI 2016 data directly **[118]** (osmihelp.org/research, n≈1,400, self-selected). "Anti-selection"
  rests on a single n=1 essay (compelling, not a validated predictive model); Cassidy **[117]** provides
  the peer-reviewed mechanism support.

## I. Community / leadership (OSS sub-context)

**I3 — Entitled-user demand escalation suppresses distress disclosure and opens a trust vacuum for bad actors** · `high` · conf high · all *(was L5)*
- **Mechanism:** In publicly visible communities, when a maintainer/facilitator signals distress or
  capacity limits, **entitled consumers respond with escalating demands rather than support**. This
  asymmetric pressure (few maintainers, many demanders) suppresses honest help-seeking (one cannot
  signal need without receiving *more* demands), accelerates crisis, drives chronic emotional-labor
  burnout, **and opens a trust vacuum a malicious actor can exploit.**
- **Evidence:** xz/liblzma: the sole maintainer disclosed "my ability to care has been fairly limited
  mostly due to longterm mental health issues," following a coordinated sock-puppet pressure campaign —
  and the **only** actor who responded with "help" was the attacker who later inserted the backdoor —
  xz/liblzma incident (Lasse Collin) **[123]** (n=1 case; critical Linux infra, millions of systems).
  "Consumers make demands (some polite, some not-so-polite) of one maintainer (rarely two) that does
  everything" — Mensching 2024 **[119]**. Tidelift: 60% quit-or-considering — Speed/The Register 2025
  **[120]**. Practitioner account; user entitlement, low-quality contributions — Sapegin 2023/2024
  **[121]**. Severe interpersonal challenges (stalking, doxxing, harassment) rose 2017→2024 and drive
  dropout — "Shifting Sands of Toxicity" 2025 **[122]** (n=5,495 (2017) vs n=8,452 (2024) GitHub
  surveys). **Quote:** *"I haven't lost interest but my ability to care has been fairly limited mostly
  due to longterm mental health issues but also due to some other things."* (Collin)
- **Bites:** APP, FACIL, LEAD.
- **Mitigation seed:** Train members to recognize distress-coded language in public channels and respond
  with **offers of help, not demands**; create a "signal amplification" norm prioritizing wellbeing
  disclosures over issue queues; give facilitators low-friction deflection tools + moderator authority
  over hostile interactions; surface asymmetric workload via visibility dashboards.
- **Distinct from:** I1 (peer enforcement of *in-group* norms) — here the harmful pressure comes from
  **external consumers/free-riders**, and the documented consequence includes a **security/safety
  exploit**, not just polarization.
- **Correction applied (minor dates only — no fabrication):** Collin's quote originates June 2022
  (xz-devel list); the 2024 date refers to the Mensching article citing it. Sapegin originally published
  Sep 2023 (edited Feb 2024). Mensching's own verbatim line ("Consumers make demands…") is distinct from
  the Collin quote.

**I4 — Consensus-governance overload: open all-decisions consensus amplifies conflict + political labor → facilitator burnout** · `medium` · conf med · all *(was L8)*
- **Mechanism:** Communities relying on consensus for *all* decisions generate disproportionate
  coordination burden; conflict-averse members' attempts to "be nice" create ambiguity and stalemate;
  the resulting frustration and political labor burn out leaders and drive exodus. The **structure of
  decision-making itself** is the harm vector — and it has a documented fix (modular governance).
- **Evidence:** Jupyter (1,500+ contributors, 100+ repos) could not sustain consensus governance;
  community-wide frustration contributed to leader burnout; restructuring to an Executive Committee +
  Working Groups reduced it — Salkever 2023 **[124]** (32 interviews with maintainers of top-200
  critical OSS projects). **Quote:** *"the ambiguity that exists and the difficulty of really balancing
  a consensus model with a lot of people who tend to be conflict diverse or just want to be nice all the
  time results in patterns that are likely to burn folks out."*
- **Bites:** APP, FACIL, LEAD.
- **Mitigation seed:** Allocate explicit decision rights and conflict-resolution pathways before growth;
  avoid pure consensus above ~15–20 active participants; adopt modular governance (steering council +
  working groups).
- **Distinct from:** I-series (norm enforcement / leadership inaction) and J-series (fidelity decay).
- **⚠ Correction applied:** **Re-attribute the quote to Brian Granger, NOT Myles Borins.** The Jupyter
  interviewee in the Salkever (2023) **[124]** report is **Brian Granger** (Jupyter co-creator), **not
  Myles Borins** (who has no documented Jupyter-governance connection). The Jupyter restructuring is
  independently confirmed (jupyter.org/governance). Cite as Salkever (2023) — Jupyter case, **Granger**.

## J. Transfer / fidelity (OSS sub-context)

**J3 — Single-maintainer "lottery factor": knowledge concentration makes one person's burnout a whole-community crisis** · `medium` · conf high · all *(was L7)*
- **Mechanism:** In small distributed communities one person holds disproportionate technical **and
  social** knowledge; their burnout/departure/crisis leaves no continuity, and the resulting collapse
  or trust vacuum is itself a community-health crisis for everyone remaining. A "trust paradox"
  compounds it: incumbents hesitate to delegate for fear of quality loss, perpetuating the single point
  of failure.
- **Evidence:** Lottery factor: "If 50% of the PR contributions come from two or fewer contributors,
  the lottery factor is high." **61% of unpaid maintainers work entirely alone** — Socket.dev 2025
  **[126]**; **>18M of ~28M npm package releases have a single maintainer (>64%)** — Socket.dev 2025
  **[126]**; node-pre-gyp departure left the ecosystem scrambling 2+ years; xz-utils and Kubernetes
  Ingress NGINX retirement (Nov 11 2025) as exemplars — OpenSauced 2024 **[125]**. Paid maintainers 55%
  more likely to implement critical security practices — Tidelift 2024 **[127]** (n=437). xz incident
  context — **[123]**. **Quote:** *"This current unsustainable model is a ticking time bomb. When key
  maintainers leave, projects can quickly become outdated, insecure, or completely non-functional."*
- **Bites:** APP, LEAD, FACIL.
- **Mitigation seed:** Track community-wide lottery/bus factor as a health metric; build succession
  protocols and graduated-trust delegation (review access before merge rights); distribute institutional
  knowledge via documentation **before** crisis.
- **Distinct from:** I2 (leadership inaction on a signal) and J2 (successor competency decay) — here the
  hazard is the **structural concentration** of knowledge/dependency and the **irreversibility of sudden
  loss**.
- **Correction applied:** npm stat understated — real figure is **>18M of ~28M single-maintainer
  releases (>64%)**, not 16M (i.e., worse). Ecosyste.ms 1.4M is slightly dated (~1.7M now). "Ticking
  time bomb" / "trust paradox" quotes are approximate paraphrases of the OpenSauced **[125]** article —
  treat as such.

---

# TIER 3 — Channel / software-specific

> Harms tied to a particular medium (text), broadcast/feed mechanics, a metric technology, a data
> path, or AI mediation. Secondary grouping: **text-channel → broadcast/feed → metrics &
> privacy-software → data-leakage → AI-mediated.** Spanning threats keep their full detail and add
> a one-line link to their Tier-1 universal core.

## Text-channel

**A4 — Symptom-surveillance anxiety amplification ("worry engines")** · `med` · conf med · all
- **Mechanism:** Repeated prompts to self-monitor train hypervigilance to normal fluctuation;
  streaks/badges/red-dots manufacture micro-crises; the most conscientious (often most at-risk)
  over-engage with their own distress data.
- **Evidence:** monitored vs unmonitored 56%/40% stress, 45%/29% negative MH impact — APA 2023
  Healthy Workplaces **[12]** (n=2,515). 11/14 studies negative; authors note the link is *inferred*
  — Astill Wright et al. 2025 **[13]**. Essay (self-monitoring/anxiety) — Klintman 2025 **[14]**.
  *(Verifier downgraded some causal framing; mechanism real.)*
- **Bites:** APP, METRICS.
- **Scale:** Universal (app/UX level).
- **Mitigation seed:** Minimum effective check-in cadence; never display personal negative-trend
  data saliently; prohibit streaks/urgency badges/red-dots/scored mood dashboards; batch
  notifications; clinician-reviewed copy; frictionless permanent opt-out.
- **Consider further:** Is *any* individual self-tracking safe, or should tracking be community-level
  only by default?

**H1 — Text-only misattribution, dehumanization, toxic disinhibition** · `high` · conf high · all
- **Mechanism:** Text strips cues that activate empathy and self-regulation: (1) senders overestimate
  how legibly tone transfers → real distress read as "fine," benign messages read as alarming; (2)
  voice humanizes, text conceals → a help signal may read as aggression/weakness; (3) lack of eye
  contact drives flaming → a single mocking reply poisons the well community-wide.
- **Evidence:** senders predicted ~78% tone-decode, actual ~56% (≈chance) — Kruger, Epley, Parker & Ng
  2005 **[80]**. Voice humanizes vs text — Schroeder, Kardas & Epley 2017 **[81]**. Eye-contact >
  anonymity for disinhibition — Lapidot-Lefler & Barak 2012 **[82]**. Online disinhibition — Suler 2004
  **[83]**. A project lead's reflective account observes that the community's last exchanges with a
  contributor who later died were purely technical, and raises that as a possible contributing factor —
  jackpot51 2021 **[116]** (n=1 reflective account; death-descriptive wording withheld per
  [`docs/publication-standards.md`](../../docs/publication-standards.md) §A4).
- **Bites:** PROTO, METRICS, FACIL.
- **Mitigation seed:** Specify **richer-channel response (voice/async voice notes)** as standard; text
  only for initial ack; treat text signals as **imprecise triggers for richer follow-up, not
  diagnostic data**; templates that name uncertainty ("I read this as X — is that right?");
  **discount text-derived sentiment in metrics.**
- **Consider further:** Your IT background covers comms *effectiveness* — this is the *psychological*
  layer; a big seam for the success model (channel-by-type effects).

**H3 — AI-mediated interaction displaces human-to-human bonds: bot-filed issues/PRs/reviews erode belonging and mutual trust** · `medium` · conf med · all *(was L12)*
- **Mechanism:** As GenAI bots increasingly file issues, submit PRs, and perform code review,
  transactional AI-mediated exchanges displace human-to-human interaction, reducing mentorship,
  informal learning, and interpersonal trust — the social capital that sustains participation. Members
  never receive genuine **human** acknowledgment of their contribution, diminishing belonging and
  relatedness. Structurally distinct from H1: the counterpart is **non-human**, so the relational return
  that text normally still provides is absent.
- **Evidence:** Peer-reviewed roadmap (now in ACM TOSEM): "loss of community interaction emerges when
  generic AI comments may make reviews transactional, reducing human engagement and community bonds";
  grounded in self-determination theory — Feng, Milewicz, Murphy-Hill, Menezes, Serebrenik, Steinmacher
  & Sarma 2024 **[113]** (conceptual/vision paper, multidisciplinary team + 2 external expert
  validators; no empirical effect sizes yet). **Quote:** *"loss of interpersonal connection and mutual
  trust may diminish contributors' sense of belonging and relatedness."* Adoption context — **84%**
  moderate-to-high GenAI adoption — Lawson et al. / Linux Foundation 2024 **[114]**. Emerging empirical
  watch-item — Vaccargiu et al. (BoatSE '26) **[115]**.
- **Bites:** APP, PROTO, FACIL.
- **Mitigation seed:** Track the ratio of human-to-human vs. bot-mediated interactions at key
  touchpoints (code review, issue triage); create explicitly **human-only** spaces (synchronous rituals,
  mentorship pairings) that AI tools are not invited into.
- **Distinct from:** H1 (human↔human text CMC).
- **⚠ Correction applied:** "**94% GenAI adoption**" → **84%**. The "94% of OSS orgs use GenAI" figure is
  **unverified** against the primary Linux Foundation 2024 report, which states **84% moderate-to-high
  GenAI adoption** (Lawson et al. 2024 **[114]**) — use 84%. Threat is prospective/theoretical (no
  measured belonging/trust degradation yet); industry pattern may be augmentation rather than pure
  displacement. Emerging empirical literature is forming (Vaccargiu et al. **[115]**).

**C3 — Co-rumination, emotional contagion & cyberostracism in text** · `high` · conf high · team·org
- **Universal core:** emotional/behavioral **contagion** in support settings — the same mechanism as
  the C1/C2 contagion cluster (Tier 1); here it is realized in **text-only CMC**, where silence reads
  as active rejection.
- **Mechanism:** Text support can (a) loop into co-rumination; (b) spread emotional contagion to
  responders/observers; (c) inflict **cyberostracism** when a signal gets *no* response — in text-only
  CMC, silence reads as active rejection. The harm is *inaction*, so moderation can't detect it; in a
  small community the same few people signal and respond, closing the loop.
- **Evidence:** online support-seeking +depression β=0.28, +anxiety β=0.23; in-person negative —
  Mackenzie et al. 2023 **[35]**. Emotional contagion 23.4%, social exclusion 25.4% of adverse events —
  Easton et al. 2017 **[36]**. Cyberostracism — Williams et al. 2000 **[37]** + Hartgerink et al. 2015
  Cyberball meta (d>1.4) **[38]**. Public-performance reactive/validation loop — "constantly reactive,
  feeling exposed and lacking control" — Zhu 2019 **[108]** (n=1 Babel maintainer).
- **Bites:** PROTO, METRICS.
- **Mitigation seed:** **Timed-acknowledgment gate** — every signal gets ≥1 ack within a window;
  absence-of-response surfaced to designated responders, never hidden. Structured responder scripts
  with coping/closure; bounded routing not broadcast; track responder burden; professional off-ramps.
- **Consider further:** The acknowledgment gate seems essential — but does an automated ack itself
  become hollow/harmful? What's the minimum *human* guarantee?

## Broadcast / feed

**C4 — Digital bystander effect: broadcast → diffusion → no response** · `high` · conf med · org·platform
- **Universal core:** diffusion-of-responsibility **contagion of inaction** — the bystander dynamic of
  the C1/C2 contagion cluster (Tier 1); here it is triggered specifically by **broadcasting** a
  help-signal to a visible group.
- **Mechanism:** Broadcasting a help-signal to a visible group diffuses responsibility; response rate
  falls; the signaler reads silence as rejection; stigma + severity-uncertainty add inhibition.
- **Evidence:** response dropped 78.3% (sole recipient) → 21.7% (14 recipients); prosocial priming
  eliminated it — Scaffidi Abbate et al. 2022 **[39]**. Diffusion of responsibility — Barron & Yechiam
  2002 **[40]**; classic studies — Latané & Darley 1968 **[41]**. *(Scenario low-stakes; MH-signal
  inhibition is inference.)*
- **Bites:** PROTO.
- **Scale:** Worse as recipient set grows (org/platform), but present whenever >1 recipient.
- **Mitigation seed:** Route to a **specific named responder** with explicit responsibility + SLA,
  escalate if unacknowledged; prosocial-priming language; **prohibit open-broadcast distress signals**.
- **Consider further:** Named-responder routing collides with B1's "never identify" — the core tension.

**D3 — Engagement-ranked / silent curation amplification of distress** · `high` · conf high · platform·(any feed)
- **Mechanism:** Any ranking/filtering of the signal feed alters the emotional climate; engagement
  ranking over-weights negative content → a doom-loop. *Any* silent curation that shifts emotional
  state without users' knowledge is manipulation.
- **Evidence:** 689,003 feeds manipulated without consent; PNAS Expression of Concern — Kramer, Guillory
  & Hancock 2014 **[47]**. 32% of teen girls said Instagram worsened body image — Haugen "Facebook
  Files" 2021 **[48]**.
- **Bites:** APP, PROTO, METRICS.
- **Scale:** Platform-defining, but applies to any algorithmic feed.
- **Mitigation seed:** **Chronological or severity-tiered routing, never engagement-ranked**; no
  reaction/upvote counts on help signals; disclose all curation logic in consent; **no emotional-
  state-affecting algorithm operates silently.**
- **Consider further:** Mostly a large-scale lesson — what's the minimal-curation default for a small
  community feed?

## Metrics & privacy-software

**D4 — Emotion-AI / biometric metrics mislabel healthy workers** · `med` · conf med · all
- **Mechanism:** "Objective" biometric stress signals carry systematic error that mislabels certain
  populations (post-COVID autonomic dysfunction, chronic conditions, non-Western baselines) →
  aggregate elevates → outreach targets the non-distressed, experienced as surveillance.
- **Evidence:** 5 commercial HRV platforms, no clinical definitions — McLachlan & Truong 2023 **[49]**.
  Emotion-AI in the workplace — Roemmich, Schaub & Andalibi 2023 **[50]**.
- **Bites:** METRICS.
- **Mitigation seed:** **Exclude biometric/AI-inferred emotional signals** from metrics absent
  population-specific peer-reviewed validation; if used, disclose error rates + get explicit consent;
  default to self-report with genuine anonymity.
- **Consider further:** Simplest stance: ban inferred-emotion metrics outright in the guide?

**E2 — ZKP proves correct computation, NOT non-identifying output** · `high` · conf high · all
- **Mechanism:** ZKPs prove a computation ran correctly on private inputs — but say **nothing** about
  whether the output is identifying. A ZKP over a differencing query proves the count is correct yet
  doesn't protect the person. DP and ZKPs are orthogonal; conflating them produces false confidence.
- **Evidence:** ZKP verifies the DP mechanism was applied; DP must still be designed in — Garrido,
  Babel & Sedlmeir 2022 **[58]**. Both layers must coexist — Biswas & Cormode 2022 **[59]**.
- **Bites:** METRICS (design).
- **Mitigation seed:** Separation of concerns — **ZKP = verifiability, DP = output privacy; require
  BOTH**; "ZKP is our privacy protection" = escalate to a cryptographer.
- **Consider further:** Directly corrects the project's stated ZKP plan — metrics need DP *and* ZKP,
  not ZKP alone.

**Q-c — Small-community re-identification from "aggregate" metrics (CONFIRMED — GATES THE METRICS LAYER)** · `high` · conf high · acute team·org
- **Mechanism:** Quasi-identifier combinations collapse k-anonymity in small populations: in a community
  of ~10–200, {role + timezone + tenure} routinely yields equivalence classes of k=1 — so **no
  per-subgroup metric breakdown is safe by default.**
- **Evidence:** 3 quasi-identifiers (5-digit ZIP, gender, DOB) uniquely identified **87%** of the US
  population; companion "Simple Demographics Often Identify People Uniquely" (CMU 2000) — Sweeney 2002
  **[186]**. k-anonymity alone insufficient even when formally satisfied — Machanavajjhala et al. 2007
  **[185]**. Applied corroboration: HR-analytics tools (Lattice, CultureMonkey, CheckMarket) enforce
  minimum-cell rules (typically n ≥ 5) because role/shift/tenure/location breakdowns re-identify — **[194]**;
  Statistical Disclosure Control literature (OpenSAFELY, UK Data Service SDC Handbook) sets thresholds of
  5–10 and flags secondary disclosure via differencing — **[193]**. Curse of dimensionality — each added
  quasi-identifier multiplies unique combinations — Aggarwal **[187]**.
- **Bites:** METRICS (gates the whole layer).
- **Scale:** **Acute at team scale** — small N is the worst case.
- **Governing rule for the metrics layer (now established):** In a small remote-worker community
  (≈10–200), the combination of **role + timezone + tenure** is a quasi-identifier set whose
  intersection routinely yields equivalence classes of **k=1**. **No per-subgroup metric breakdown is
  safe by default.** Per-subgroup reporting requires, at minimum, a hard **minimum-cell threshold (n ≥
  5, often higher at small N)**, suppression of complementary cells to block differencing, and
  consideration of differential privacy over a multi-year release budget (which, per Research Gap #3,
  may render useful longitudinal small-N metrics infeasible — a possibility the methodology must accept).
- **Distinct from / consistent with:** E1–E3 (the cumulative-release, ZKP-gap, and behavioral-trace
  re-identification entries) — Q-c is the *aggregate-metric* face of the same privacy failure.
- **Status:** formerly quarantined; re-run through adversarial verification and **CONFIRMED (high
  confidence)** by the v1.1 completeness pass.

## Help-seeking software

> *(Placement note: the prompt's tier lists did not assign **G5**, but the Preserve list — G1–G5 —
> requires it. Its causal lever is a property of the **tooling itself** (perceived
> insecurity/complexity/invasiveness), explicitly independent of social stigma, so it is placed here
> in Tier 3 as a channel/software-specific harm rather than with the universal help-seeking entries
> G1–G4 in Tier 1.)*

**G5 — Platform-distrust silencing: perceived techno-insecurity/complexity/invasion suppresses psychological safety → mutes the signals the platform seeks** · `high` · conf high · all *(was L10)*
- **Mechanism:** When members perceive technology as unreliable, insecure, complex, or
  boundary-invading, they conserve cognitive resources by **staying silent** rather than voicing
  concerns/suggestions — with reduced psychological safety as the mediator. For a small SNH community
  this is self-defeating: distress signals and early warnings are never surfaced because the platform
  meant to detect them is itself distrusted.
- **Evidence:** techno-insecurity (β=−0.32), techno-complexity (β=−0.23), techno-invasion (β=−0.27) all
  reduced psychological safety; techno-insecurity (β=−0.19) and techno-complexity (β=−0.16) directly
  reduced promotive voice — Frontiers in Psychology 2025 **[111]** (n=361 Hungarian remote/hybrid,
  Mar–Apr 2022). Technostress fosters social isolation by replacing deep interaction with superficial
  digital exchange — American Journal of Applied Scientific Research 2025 **[112]** (systematic review,
  10 studies, 2015–2025). **Quote:** *"Technostress arises from the perception that information
  technology is unreliable, insecure, and uncertain, ultimately decreasing employees' belief that it is
  safe to take risks."*
- **Bites:** G1, H1, PROTO.
- **Mitigation seed:** Make the SNH platform demonstrably low-insecurity, low-complexity, non-invasive
  (participatory design, transparent data practices, radically simple UX); audit every added
  feature/notification channel for techno-invasion. **A distrusted platform will silence the very
  signals it seeks to detect.**
- **Distinct from:** G1 (general help-seeking chilling) and H1 (CMC disinhibition) — the causal lever is
  the **perceived insecurity/complexity/invasiveness of the tooling itself**, independent of social
  stigma.
- **Note:** COVID-era Hungarian cross-sectional sample may overestimate magnitude for a voluntary
  purpose-built platform — weakens magnitude, not existence. Mechanism multiply replicated in the broader
  technostress literature. ("paradoxically" in the review gloss is the threat author's addition, not a
  direct quote.)

## Data-leakage

**E1 — Cumulative-release attacks (reconstruction / membership / composition)** · `high` · conf high · acute team·org
- **Mechanism:** A preventive SNH system is **longitudinal** — repeated aggregates about the *same
  small group* — the exact threat model that defeats naive per-release noise. Reconstruction
  (Dinur–Nissim), membership inference/differencing (with side knowledge), and composition (DP epsilon
  accumulates additively) all apply.
- **Evidence:** reconstruction attack foundation — Dinur & Nissim 2003 **[53]**. Reconstructed 97M
  Census records, re-identified 3.4M at 95% — Abowd et al. 2025 **[54]**. Membership from aggregate
  frequencies — Jacobs et al. 2009 **[55]**. Membership at 95% with 5 queries in a 65-person beacon (a
  30-person community is *more* vulnerable) — Von Thenen et al. 2019 **[56]**. Composition attacks —
  Ganta et al. 2008 **[57]**.
- **Bites:** METRICS (over time); also cumulative session notes/trend reports.
- **Scale:** **Acute at team scale** — small N is the worst case, not the safe case.
- **Mitigation seed:** Formal **differential privacy with a GLOBAL lifetime privacy budget**
  (sequential-composition / Rényi accounting), not per-release noise; release only DP-noised outputs;
  fixed pre-registered breakdowns (no differencing); retention limits; **"we add noise per release" =
  red flag.**
- **Consider further:** Bombshell — may make useful longitudinal metrics *infeasible* at N=10–50.
  (Becomes the metrics-feasibility question.)

**E3 — Behavioral-trace re-identification of pseudonymous signals** · `high` · conf high · acute team
- **Acute at small-N remote scale → cf. Tier 2.** Behavioral uniqueness is highest at small N, exactly
  the remote-team build context (Tier 2a) — the re-identification risk concentrates where the immediate
  intervention lives.
- **Mechanism:** Even with no identifiers, behavioral patterns (timestamps, response latency,
  frequency, device/network metadata) are unique enough to re-identify. A curious admin matches a
  pseudonymous trace to a known person ("Alice always logs on at 6am Pacific"). Distinctiveness is
  highest in small teams.
- **Evidence:** Netflix de-anonymization — Narayanan & Shmatikov 2008 **[60]**. 4 points uniquely
  identify 95% in mobility data — De Montjoye et al. 2013 **[61]**. AOL search-log re-ID (2006) **[62]**.
- **Bites:** APP, PROTO.
- **Scale:** Acute at team scale (behavioral uniqueness highest at small N).
- **Mitigation seed:** Strip/bucket timestamps before storage; don't log device IDs/IPs/latency with
  signals; k-anonymize log exports; **separate metrics-access (aggregates) from admin-access (raw
  logs)** with audit trails.
- **Consider further:** Even a benevolent builder *inside* the community is a re-identification vector —
  how does the architecture bind the builder's own hands?

**Q-a — Third-party SDK / tracking-pixel leakage + onward data-broker sale (CONFIRMED, high)** · `high` · conf high · all
- **Mechanism:** Embedded third-party SDKs / tracking pixels exfiltrate mood check-ins, stress
  self-assessments, and therapy-initiation signals to ad platforms and data brokers; the help-seeking
  traces are then sold or shared. Consistent with F1.
- **Evidence:** required MH intake then shared answers, emails, IPs with Facebook/Snapchat/Criteo/
  Pinterest; $7.8M settlement, refunds began May 2024 — FTC v. BetterHelp (2023, case 2023169) **[63]**.
  Google/Meta/TikTok pixels collected self-assessment data + PII for **3.1 million** users (Oct 2019–Jan
  2023) — Cerebral pixel breach 2023 **[188]**. 11 of 37 data brokers willing to sell people identified
  by mental-health diagnosis, prices as low as **$0.20/record** — Duke Sanford report (Feb 2023) **[189]**.
  Every one of 25 sampled Android MH apps embeds ≥1 undisclosed tracker SDK; 68% fail to disclose >half —
  UC Irvine/UCR study (May 2026) **[190]**.
- **Bites:** APP, PROTO, METRICS, governance.
- **Mitigation seed:** No third-party analytics/ad SDKs or tracking pixels anywhere near help-seeking
  data; audit every embedded dependency for undisclosed trackers; self-hosted/first-party telemetry only;
  contractual + technical bars on onward sale.
- **Consider further:** a remote worker's mood check-ins / stress self-assessments / therapy-initiation
  signals are exactly the help-seeking traces at risk.
- **Status:** formerly quarantined; **CONFIRMED (high confidence)** by the v1.1 completeness pass.
- **Cross-link:** the consent-at-distress origin is **F1 (Tier 1)**.

**Q-b — Commercial pivot of help-seeking data without meaningful consent (CONFIRMED, high)** · `high` · conf high · all
- **Mechanism:** Help-seeking data collected under one promise is repurposed — shared beyond stated
  purposes, or transferred via acquisition/insolvency to a new owner with different incentives and a new
  ToS. Original consent does not cover the changed ownership/use. Consistent with F1.
- **Evidence:** sharing beyond stated purposes; $7.8M — FTC v. BetterHelp (2023) **[63]**. Shared
  sensitive MH/prescription data with LinkedIn/Snapchat/TikTok; ~3.2M consumers; $7.1M — FTC v. Cerebral
  (2024) **[191]**. 23andMe 2025 bankruptcy → potential transfer of health/genetic data on **~15M
  people**; coalition of **27 states** sued to require re-consent — **[192]**. Crisis Text Line/Loris.ai
  pattern noted in the original quarantine — danah boyd **[64]**.
- **Bites:** APP, PROTO, METRICS, governance.
- **Mitigation seed:** Bind data use to purpose in enforceable terms; data-portability + deletion on
  exit; provisions that survive acquisition/insolvency (re-consent on ownership change); minimize what is
  collected so there is little to pivot.
- **Consider further:** the acquisition/pivot/new-ToS vector is empirically established, not theoretical.
- **Status:** formerly quarantined; **CONFIRMED (high confidence)** by the v1.1 completeness pass.
- **Cross-link:** the consent-at-distress origin is **F1 (Tier 1)**.

## AI-mediated

> The AI-mediation harms are distributed across the catalog rather than collected in one block: **H3**
> (AI displaces human bonds, above in this tier), **D4** (emotion-AI mislabels, above), and the
> labor-market AI stressors **K3a / K3b / K3c** (Tier 2a). This subsection is a pointer, not a separate
> set of entries.

---

# Appendix A — Success-model leads (for the next phase)

> Carried forward verbatim from the v1.1 Completeness Addendum §5. Tagged with the threat IDs each may
> mitigate. Captured for the forthcoming success model; not yet adversarially weighted against each
> other. Every **Mitigation seed** in the catalog above is also a hypothesis about what *works*; the
> success model will research the positive evidence and link each design feature back to the threat IDs
> it addresses, so the two datasets form a single queryable evidence base.

**Network / cohesion programs**
- **Wingman-Connect (US Air Force)** — universal cohesion training of *intact units* produces
  **differential benefit for the most vulnerable** (no at-risk targeting). Cluster RCT, n≈1,485, 2017–19;
  reduced ideation/depression/occupational impairment (~50% fewer corrective-training events). *Wyman et
  al., JAMA Network Open Oct 2020; Soc Sci Med 296:114737 (2022) [135].* → mitigates **A5, B1, K1, K8,
  G2/G3**.
- **Sources of Strength** — train network-selected **opinion leaders**, not "at-risk" individuals; peer
  leaders 4× more likely to refer suicidal friends; 0 suicides in intervention vs 4 in control across 3
  pooled RCTs (78 schools, 39,960 students) [173]. → mitigates **B1, B2, G2, A5, K1**.
- **Cobbler 2 Cobbler (Rapid City)** — year-round peer mentoring + scenario-based **role-limitation**
  training + structured freshman integration; zero teen suicides since Sep 2011 (vs 14 in prior 30
  months) [201]. → mitigates **G2, G4, K1, K9**.
- **Youth-adult network integration** — sharing a common trusted adult lowered attempt rates (n=10,291,
  38 schools) [198]. → mitigates **I2, K1, G3**.
- **Diverse social-network size** (range of distinct contacts) buffers stress/worry/fatigue (n=902
  representative Austrian) [199]. → mitigates **K1, H2, K8**.

**Remote-specific connection**
- **Co-worker (horizontal) peer support** the dominant buffer (AOR 4.06 > supervisor 2.49 >
  remote-frequency) (Miyake n=4,052) [131]. → mitigates **K1, K7, I3**.
- **Higher mediated-communication frequency** reduces isolation longitudinally — buffer, not substitute
  (Van Zoonen & Sivunen, n=1,164) [174]. → mitigates **K1, K8, H2**.
- **Hybrid / minimum in-person threshold** (42% vs 36% thriving) (Bodner [178]; Gallup [132]; Emanuel
  [129]). → mitigates **K11, K1, K4, H2**.
- **Buddy/peer-pairing at onboarding** seeds weak ties before withdrawal (retention ~+52%,
  time-to-productivity ~−60%) [200]. → mitigates **H2, K1, K7, K12**.
- **Coworking / virtual co-presence** generates weak ties structurally, no networking event needed
  [202]. → mitigates **H2, K1, K4**.
- **Group belongingness** = top protective factor against videoconference fatigue (n=55/279 VCs) [169].
  → mitigates **K1, K2, H2**.

**Circadian / boundary**
- **Schedule/location autonomy** buffers technostress→detachment→burnout (Emerald n=405 [146]; Jaiswal
  n=218 [145]). → mitigates **K2, K10, K7**.
- **Chronotype-aligned flexibility** dissolves the social-jetlag→depression cascade for evening types
  (Gorgoni n=875 [203]; Otsuka n=824 [141]). → mitigates **K2, K10**.
- **Right-to-disconnect / collective off-hours norms** — employee health *and* firm ROA/EBITDA (~+0.8%);
  collective enforcement > individual willpower (n=136,429 firm-obs, 28 OECD countries) [204]. →
  mitigates **K2, K10, A4**.
- **Light therapy + behavioral sleep intervention** normalizes circadian profile, reduces burnout (n=43
  night-shift nurses) [205]. → timezone-dispersed analog; mitigates **K2** without surveillance.
- **E-work self-efficacy training** buffers technostress→burnout→mood (Consiglio n=225) [144]. →
  mitigates **K2, G5, K10**.

**Organizational / governance**
- **Visible, responsive support (not passive availability)** moderates wellbeing/productivity declines
  (Ralph n=2,225/53 countries [206]; Bentley n=804 [207]; Mindshare: 2× "no burnout" at supportive firms
  [208]). → mitigates **I2, K1, G3, D6**.
- **Climate for learning + belonging + inclusiveness** reduce burnout via satisfaction, esp. for
  non-leaders (Trinkenreich n=3,281) [137]. → mitigates **K1, I1, B4, D6**.
- **Modular governance** (Executive Committee + Working Groups) cures consensus-overload burnout (Jupyter)
  [124]. → mitigates **I4, I2, J3**.
- **Active-user buffer layer** insulates core contributors from support load (Crowston & Howison) [171].
  → mitigates **I3, J3, D6**.
- **Human infrastructure for maintainers** (funded co-maintainership, knowledge distribution, CoC
  enforcement, episodic-contributor acceptance) (Linaker et al. ESEM 2024, n=10) [209]. → mitigates
  **J3, D6, I3, K3**.
- **Funded/paid maintainership** as a wellbeing (+security) lever — paid maintainers 55% more likely to
  implement critical security practices (Tidelift n=437) [127]. → mitigates **K3, J3, D6, I3**.

**Help-seeking / norms**
- **Navigator-assisted help-seeking** (human-guided) — the **only** durable behavioral uptake (OR
  1.84–1.90; 98.6% utilization at 12 mo); passive info failed; adult gatekeeper-only training did not
  work (Fukita systematic review, 10 RCTs) [164]. → mitigates **G1, G2, G3, G4**.
- **Personal 1:1 contributor outreach** converts anonymous users into members (Storybook: 200+
  meetings/yr, ~20% repeat) [196]. → mitigates **K1, K9, H3, B1**.
- **Structured peer-support workshops** naming chronic stressors ("personal ecology," GitHub n=40) [197].
  → mitigates **K1, D6, I3**.
- **Peer storytelling by credible peers** (OSMI) breaks stigma, triggers disclosure [118]. → mitigates
  **G1, B4, H4, K1**.
- **Public norm-change after a death** ("we will no longer value contributors by the code they crank
  out" — a project lead's published commitment) — durable artifact subordinating output to wellbeing
  [116]. → mitigates **D7, H4, D2, D6**.
- **Flexible/low-expectation contribution norms** (no weekend-work expectation) reduce burnout/silent
  dropout (Raghunathan [175]; GitHub). → mitigates **K9, K10, I3**.

**AI-era**
- **Hope-activation micro-interventions** for lonely remote workers (hope mediated remote→engagement for
  high-loneliness; loneliness interventions g=0.43) (Bareket-Bojmel n=349 [101]; Hickin meta-analysis
  [195]). → mitigates **A5, K1, K12**.
- **Job resources (AI-use autonomy + reskilling)** buffer GenAI burnout (β=−0.360) (Feng n=442) [183]. →
  mitigates **K3c, K3a, J3**.
- **CSR** buffers AI-adoption→insecurity→depression (3-wave, n=403/287 orgs) (Kim & Lee 2025) [210]. →
  mitigates **K3a, K3, B4**.
- **AI-complementary skill acquisition / reframing** reverses freelancer income decline (+~40%/hr)
  (Kharazian/Ramp) [153]. → mitigates **K3b, K3, K3c**.

---

# Appendix B — Research gaps & weak-flagged items

> Merges the v1 main-body **Research gaps** with the v1.1 Completeness Addendum **§6 (Remaining gaps)**.

## B.1 — Threats that are single-source or low-confidence (re-source before they drive design)

- **A5** — single unreplicated cross-sectional study (Bareket-Bojmel 2023 [101]); causation unestablished;
  one large longitudinal study (Norwegian, n=1,511 [102]) points the *other* way at the population level.
  **Severity=high may be overstated.** Needs a longitudinal/experimental test of subgroup masking under an
  *actively targeted* (not averaged) design.
- **H4 (capable-contributor blind spot)** — the "anti-selection" core rests on a **single n=1 reflective
  essay [116]**; only indirectly corroborated (Cassidy 2022/2023 high-IQ-autism [117]). Definitional
  overlap with G2/B3 unresolved. Needs a controlled study; treat as low-confidence.
- **K9 (silent attrition)** — strongest cited source (Raghunathan [175]) is a **low-tier whitepaper**;
  re-anchored on Raman et al. (ICSE-NIER 2020 [176]) + Guizani et al. (arXiv:2102.05737 [177]).
- **K12 (belonging-need suppression)** — **irreversibility downgraded/removed** (theoretically contested vs
  Baumeister & Leary); rests on one observational Finnish study (n=876 [179]). Needs longitudinal causal
  work on whether suppressed belonging motivation recovers, and on the engagement-resistance timing window.
- **H3 (AI-mediated displacement)** — entirely prospective; **no measured belonging/trust degradation
  yet**; "94%" adoption figure corrected to 84% [114]. Watch emerging empirical work (Vaccargiu et al.,
  BoatSE '26 [115]).
- **K3b/K3c** — top-earner finding is "suggestive" (authors' own label [182]); some cited regression
  coefficients/sub-claims unverifiable (paywalled) or **not found in source** (the "~10 PRs/year" claim —
  removed); Becker RCT n=16 with wide CIs [184].
- **K5 ("degraded mode")** — **still thin**: one practitioner source [156]. Target the experiential-learning
  / embodiment / co-presence literature for a primary citation.
- **D7 AI-amplification layer** — fabricated Devsu stat removed; the AI-amplified-impostor angle lacks a
  rigorous quantitative source (qualitative SO-blog coverage only [109][110]).
- **I4 quote attribution** — re-attributed to **Brian Granger** (not Myles Borins); re-verify against the
  Salkever (2023) full PDF [124].

## B.2 — Catalog-level open gaps (what to study next)

1. **Mechanism tests in non-clinical, remote-worker populations** are still mostly absent — most Tier-1/A–J
   citations are clinical/school/justice/general-CMC. Prevalence inflation (B4), async deviancy training
   (C1), and the gatekeeper "repelling" effect (G2.2) are explicitly *undemonstrated* in this context. The
   OSS literature is the closest proxy for distributed-community dynamics but is dev-specific
   (generalization caveat applies to D6/D7/H3/H4/I3/I4/J3/K9).
2. The **"repelling the highest-risk" mechanism (G2.2)** is theorized but unproven — needs a controlled
   study.
3. **Small-N DP utility/privacy tradeoff at N=10–50 over a multi-year budget** — defensive parameterization
   is unworked; now *more* pressing given Q-c confirmation; may show useful longitudinal per-subgroup
   metrics are infeasible at this N (a possibility the methodology must be prepared to accept). Highest-
   leverage open question for the metrics layer.
4. Whether **any** community health metric survives Goodhart + suppression + selection simultaneously in a
   small voluntary remote community (plausibly: qualitative + process measures must be primary).
5. **Re-verify the three quarantined privacy threats (Q-a/b/c) before designing metrics** — done in v1.1
   (all CONFIRMED, high); keep under review.
6. **Werther/contagion visibility threshold** for a tight identified community (C2) — when does
   peer-identified distress flip from supportive to contagious at small N?
7. **Facilitator-competency decay rate** for a self-propagating model (J1/J2) — how many train-the-trainer
   hops before judgment falls below a safety floor, and whether async remote delivery accelerates it.
8. **K6 (hard-to-corral/unreachable → selection bias) remains genuinely under-cited.** No dedicated source
   found in the completeness sweep. Recommend targeted sourcing in **survey non-response / hard-to-reach
   population methodology** (respondent-driven sampling; non-response bias in occupational-health surveys)
   to lift K6 out of "exp."

---

*End of Threat Catalog v2.0. Source: the v1.1 catalog (originally `host-happily-hub` repo; preserved
in this repo's git history as `drafts/threat_catalog.v1.1.bak.md`). References: `references/references.md`. This v2.0 reorganization
merges the v1 main catalog and the v1.1 Completeness Addendum into one tiered catalog; all ~50 detailed
entries (A1–A5, B1–B4, C1–C4, D1–D7, E1–E3, F1–F3, G1–G5, H1–H4, I1–I4, J1–J3, K1–K12, K3a–c, RF1,
Q-a/b/c) are preserved with content unchanged; only LOCATION, CITATIONS (now `[n]`), and the listed
CORRECTIONS were altered.*
