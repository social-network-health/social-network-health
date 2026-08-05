# Memoriams — What Open-Source Communities' Memorials Teach About Prevention

**Status:** v1.1 (2026-08-05), anonymized public summary. The named case records
behind this document are kept in the org's private repository — see "Publication
posture" below. How this document's norms bind every other document in the org is
set out in [`docs/publication-standards/identifiable-people.md`](../../docs/publication-standards/identifiable-people.md).

*If you or someone you know is struggling: in the US, call or text **988**
(Suicide & Crisis Lifeline); elsewhere, https://findahelpline.com.*

---

## What this is

We have studied memoriams to open-source software community members who have lost
their lives to suicide. As part of our postvention practice — and although we are not
publishing any information about these individuals — we have recorded here what those
memoriams said about the causes of their untimely passing, and we will use that data to
consider future methods of prevention. This document also retains, in full, the
postvention practice norms and their defining resources, and explains our method.

## Method

- **Sourcing:** public record only — official statements, project memorial pages,
  family public statements, and reliable news coverage. Rumor and leaked private
  material were excluded by rule.
- **Verification:** a deep-research pass with adversarial verification (three
  independent verifiers per claim, checking quotes against fetched primary sources;
  run `wf_7ca9a59e-94b`, 2026-07-08), plus a targeted single-verifier follow-up pass
  for two cases. Every statement in this summary traces to a verified record.
- **Classification:** two tiers, following postvention guidance (norm 6 below) — a
  death is treated as *confirmed* only on an official ruling or a family's public
  statement in reliable sources; deaths that were publicly mourned without a publicly
  established cause are recorded as *cause not public* and never asserted otherwise.
- **Safe messaging:** the norms below are applied throughout — "died by suicide,"
  never method, no glamorizing, restraint in detail, crisis resources present.
- **Privacy:** the named case records (six, spanning 2010–2021: four confirmed, two
  cause-not-public) are kept as private working data in the org's private
  repository, one file per person, each carrying its verification provenance.
- **Practice survey (added 2026-08-05):** the memorial-practice and postvention findings
  below rest on a *second, separate* study — a primary-source survey of roughly thirty
  projects, foundations, conferences, registries and platforms — plus a literature review
  run across five bibliographic indexes and the project's own paper corpus. Neither
  touched the case records. Both were conducted under
  [`docs/publication-standards/identifiable-people.md`](../../docs/publication-standards/identifiable-people.md):
  aggregate and de-identified throughout, no individual named, no cause attributed to any
  person. Their full briefs are staged privately. Where the survey could not test something
  without case-linked data, it says so rather than inferring.

## What the memoriams said about causes (anonymized)

1. **External structural pressure, named publicly.** In one case the family's public
   statement directly connected the death to the pressure of a federal prosecution —
   and the community's memorial response organized around reforming those legal
   conditions. This is the clearest documented case of an OSS community publicly
   linking a member's death to an external structural cause and acting on it.
2. **Community conditions, named from inside.** One project leader's memoriam is a
   first-person analysis of open source itself as a contributing environment: chronic
   and acute stressors, isolation, community splits and forks, and the high prevalence
   of ADHD, autism, bipolar disorder, and depression among contributors. It accepts
   community responsibility ("our role in creating both the chronic stressors… as well
   as the acute stressors"), commits to valuing contributors over their code output,
   and commits to regular check-ins — the seed of this project's
   `../protocols/checkin_protocol.md`.
3. **Founder/startup pressure, debated in public.** Around one death, the press
   carried an unusually open dialogue about founder depression, stress, and startup
   pressure — while a co-founder publicly cautioned against oversimplified causal
   narratives, which is itself a postvention norm (norm 4) in action.
4. **Openly acknowledged struggle.** One memoriam context included a long, publicly
   acknowledged history of depression, spoken of plainly and without stigma by the
   person's family.
5. **Most often: silence on cause.** The dominant pattern is omission. The largest project
   memorial page we studied names many causes of death freely — illness, accident — while
   attributing none to suicide. Our verified case records establish that this is *omission
   rather than absence*. **The specific linkage supporting that is held in the private case
   records and deliberately not stated here**, because naming which entries it concerns
   would identify an individual by combination
   ([publication standards](../../docs/publication-standards/identifiable-people.md) §A3,
   disclosed per §A6). The conclusion is unaffected: project memorials alone cannot carry
   the public-health record; official rulings and family statements do.

**Prevention leads we take from this:** upstream network-health work (cohesion,
check-ins, belonging) targets exactly the conditions named in (2); structural-pressure
cases (1) argue that prevention includes defending members against external threats,
not only internal community health; and the silence on cause (5) means prevention research
cannot rely on community self-reporting to understand the scale of the problem. That last
lead turned out to have a second, independent half — official statistics cannot carry it
either — which is set out in [Why the scale of this is not measurable](#why-the-scale-of-this-is-not-measurable).

## What the memorial practices teach (de-identified patterns)

1. **Permanent by construction, not by choice.** Communities vary in how much of their
   internal life is written down, and how much of that is public — a spectrum running from
   organizations that record almost nothing outside private channels to ones whose
   deliberations, decisions and history are public artifacts by default. **Open-source
   projects sit at the far open end of that spectrum**, for a structural reason: they are
   distributed digital collaborations whose members manage their own resources and
   communications, so coordination has to happen in durable, publicly readable artifacts
   rather than in a room.

   Memorials inherit that substrate. They are project-history chapters, release
   dedications, roster entries, archived announcements — media that cannot expire:
   version-controlled history, packaged and mirrored documentation, immutable standards
   series, conference archives. As the limit case, one tribute is embedded in a public
   blockchain. Across the ~30 entities surveyed, **not one had a takedown, sunset,
   retention limit, or expiry provision of any kind.** For several, removal is not merely
   against policy but *mechanically impossible* — the artifact has already replicated to
   every mirror and every clone.

   This bears directly on norm 7, which recommends organization-run online memorial pages
   come down after 30–60 days. **That recommendation assumes an organization owns a page it
   can take down.** Here the memorial usually is not a page anyone owns. The guidance does
   not merely sit in tension with open-source practice — its precondition is absent.
   Archival records and active-grief memorial pages are different objects, and guidance
   written for the second does not reach the first.

   **A caution about the unit of analysis.** The above is a claim about the *group*, and the
   group sits at one end of a spectrum. **It cannot be ascribed to any individual project.**
   Communities within open source behave very differently: a few maintain rich recurring
   practice, most improvise, several have no memorial practice at all. What generalizes is
   the substrate — where a memorial is made, the medium tends to make it *individually
   authored* and *exceptionally persistent*. How much any particular community
   memorializes, and how deliberately, is not predicted by that.
2. **Postvention is absent from open-source governance.** Postvention is the organized
   response *after* a death — support for the bereaved, and prevention of further deaths
   among those exposed (the norms and their sources are set out below). It has essentially
   no presence in this population. A code search across public repositories found the term
   in clinical and statutory material and in **no** open-source governance,
   community-health, or maintainer document. The most widely adopted code of conduct in the
   field contains no mention of death or bereavement, and neither did the conference codes
   checked directly. The code-of-conduct genre is built around misconduct: someone does
   something wrong, and the document says what happens next. **Loss does not fit that
   shape**, so it falls outside the frame rather than being deliberately excluded.

   Where written procedure does exist — roughly 6 of 30, most of it authored within the
   last two years — it covers **offboarding rather than mourning**: credential disablement,
   roster hygiene, package succession, with the memorial left to whoever knew the person.
   The two most developed procedures were written by infrastructure maintainers as
   operational runbooks, not by governance bodies as policy. A recurring irony in those
   documents: several retirement paths require the departing person to send a signed
   message or file the request themselves. **The documented path cannot be walked in the
   one case where it matters most.**

   *Our interpretation, offered as such:* the absence and the permanence are plausibly the
   same fact. Nobody writes a takedown policy for an artifact that cannot be taken down,
   and nobody writes a grief procedure for a community with no body responsible for grief.
3. **Cause-of-death statement is ungoverned, not normed.** No policy at any surveyed
   project, foundation, conference or registry governs whether a memorial states a cause.
   The prevailing default is silence — name, role, dates, no cause — but it is not uniform:
   a few surfaces state causes for some entries and not others, with **adjacent entries in
   the same document differing**. Administrative forms are cause-free *structurally* rather
   than deliberately; an account-closure runbook has no field a cause could occupy.

   We previously called this an *omission norm*. That was the wrong word. A norm implies a
   rule someone adopted and others follow; **what exists is an absence of governance,
   producing an aggregate that resembles a norm from a distance.** The distinction is not
   academic — it determines what an intervention could target. There is no policy to appeal
   to here, and none to change.

   The narrower pattern in (5) above rests on our own case-linked records and stands as
   reported. **The practice survey could not test that half independently**, since doing so
   requires linking specific deaths to specific entries — out of scope under our
   publication standards.
4. **Memorial-by-continuing-the-work.** Annual memorial hackathons continuing the
   person's projects; memoriam posts that end in commitments to change community
   practice. The "focus on the lived life" principle, in OSS dialect. Rarer than expected:
   it concentrates in package-succession machinery and in named awards, funds or
   foundations, and most communities reuse existing machinery — orphan/adopt queues,
   maintainer reassignment — rather than building memorial-specific paths.
5. **Parity in practice.** The communities we studied memorialize deaths by suicide
   with the same forms they use for every other death — postvention guidance's parity
   principle (norm 5), arrived at independently.

## Why the scale of this is not measurable

Two separate blind spots make the size of this problem unknowable with current data. They
arise from unrelated causes and happen to cover the same population, so neither can be used
to check the other.

**The community record cannot carry it.** Practice (3) above establishes that cause-of-death
statement in open-source memorials is ungoverned and predominantly silent. A count assembled
from what communities publish about their own dead would therefore undercount by an unknown
factor — not because anyone conceals anything, but because nobody ever decided the record
should carry it.

**Official statistics cannot carry it either, and here the reason is structural.**
Occupational suicide surveillance works by taking deaths, assigning each one an occupation,
and dividing by an employed population. Every step of that pipeline excludes open-source
contribution by construction:

- The **denominator is paid employment.** Published rate tables are computed over employed
  populations, and the source analyses explicitly exclude unpaid workers.
- The **numerator assigns one occupation per death.** A death certificate records a single
  *usual occupation*, derived from paid work history.
- **Maintainership is never that occupation.** For most contributors, open-source work is
  unpaid and done alongside a paid job — so it appears in neither the numerator's occupation
  field nor the denominator's employment count.

The consequence is not that open-source contributors are recorded as low risk. It is that
**they are not recorded as open-source contributors at all.** A contributor employed as a
software engineer appears as a software engineer; one employed as a teacher appears as a
teacher; one not in paid work may not enter the rate calculation at all. **The population is
dissolved into other populations before the arithmetic begins.**

That also explains the shape of the literature. A review across five independent
bibliographic indexes, plus this project's own corpus, found **no peer-reviewed study**
linking any open-source-specific condition to suicide risk or ideation. The adjacent
literatures are real and growing — contributor burnout, harassment and disengagement on one
side; occupational suicide surveillance on the other — but **their measurement boundaries do
not meet.** The gap is not an oversight anyone can be faulted for. It is where two fields'
instruments stop.

### The base-rate trap

One number could easily be read as settling the question. Computing occupations sit **well
below** the working-population suicide rate — roughly half, among men, in the most recent US
national figures — and have stayed flat across a decade in which the overall working-age rate
rose substantially. • Sussell et al., *MMWR* 72(50):1346–1350 (2023),
https://doi.org/10.15585/mmwr.mm7250a2

That is real and should be stated plainly. It is also **uninformative about the population
this study concerns**, for the reason just given: those rates describe people whose *paid*
occupation is computing. They say nothing about unpaid contributors, and they cannot separate
a contributor from a non-contributor inside the same occupational code.

*Two cautions on the figures themselves.* An earlier report in this series was **retracted in
full** after occupation-miscoding errors changed its conclusions — a useful indication of how
much precision the underlying pipeline actually supports. • retraction notice, *MMWR*
67(25):729, https://doi.org/10.15585/mmwr.mm6725a7 — and any keyword search of these tables
for "computer" also surfaces a *hardware repair trade* with a markedly elevated rate, which is
not a software occupation and has repeatedly been misread as one.

We also do not know the overlap. **How many open-source contributors hold full-time computing
employment — and how many are students, between jobs, retired, or employed outside computing
— is not answerable from any public source.** A contributor base drawn mostly from well-paid
computing employment and one drawn mostly from the other groups would carry very different
baseline risks, and nothing available distinguishes them. Establishing that relationship is a
precondition for reading any occupational figure as evidence about this population; it is
recorded as an open question below.

### What would be worth measuring instead

The deeper problem is that occupational statistics answer a question adjacent to ours. They
describe a **labour category**. What matters for prevention is a **community** — the group a
person actually communicates with regularly, and which would notice if they went quiet.

These are not the same unit, and the difference is not merely definitional:

- A person's employer may have no overlap at all with the community where they are known, and
  where their absence would register.
- Community membership is where the mechanisms this research concerns — cohesion, belonging,
  check-ins, the noticing of silence — actually operate.
- **An intervention has to be delivered somewhere.** It is delivered into a group with
  communication channels, norms, and people willing to check on each other. It cannot be
  delivered into an occupational code.

This is why the program's measurement work targets **community-level network health rather
than workplace indicators**. Workplace metrics measure something real; they measure the wrong
unit for this purpose. A community metric can be computed for a group that actually
communicates, acted on by that group, and validated against outcomes that group can
influence. An occupational rate can do none of those three.

That is not a retreat from measurement. It is a claim about which denominator makes the
numerator mean anything.

## Postvention guidance: the norms and where they are defined

"Postvention" (term coined by Edwin Shneidman, 1972) is the organized response *after*
a suicide — support for the bereaved, and prevention of further deaths, since exposure
to a suicide raises risk in the exposed. The norms below are what the guidance actually
says, each with the document that defines it. All starred (•) sources were fetched and
quote-verified in the research pass behind this file; the WHO entry is the standard
international anchor, listed for completeness but not verified in that pass.

**Who writes the norms.** In the US: the American Foundation for Suicide Prevention
(AFSP) and the Suicide Prevention Resource Center (SPRC) publish the operative
postvention toolkits; reportingonsuicide.org is the media-guidelines consortium
(developed with CDC, NIMH, and journalism bodies, resting on 100+ contagion studies);
state health offices adapt these (e.g. New York State's Suicide Prevention Office).
Internationally: the International Association for Suicide Prevention (IASP, language
guidelines) and the WHO (media resource). A systematic comparison of 24 national
guideline sets (PubMed 30340101) shows field-wide convergence — these are consensus
norms, not one organization's opinion.

**The norms:**

1. **Safe language.** Say "died by suicide" / "took their life"; never "committed"
   (frames suicide as crime or moral failing), never "successful"/"failed attempt."
   Defined in: • AFSP, "How to Talk Safely About Suicide"
   (https://afsp.org/how-to-talk-safely-about-suicide/); • reportingonsuicide.org
   Recommendations; • IASP language guidelines (https://www.iasp.info/languageguidelines/);
   • NYS guide (below).
2. **Never describe method.** Mentioning method measurably increases contagion risk;
   focus on the lived life instead. Defined in: • AFSP ethical-reporting guidance
   (https://afsp.org/ethicalreporting/); • AFSP, *After a Suicide: A Postvention
   Toolkit for Workplaces* (2024).
3. **Restrained coverage.** Contagion risk scales with the *amount, duration,
   prominence, and content* of coverage — the reporting-effects literature treats the
   relationship as causal (review: PMC7967741; CDC 2024 MMWR cluster guidance).
   Defined in: • AFSP workplace toolkit; • reportingonsuicide.org
   (https://reportingonsuicide.org/recommendations/).
4. **No glamorizing, no sanctifying, no oversimplified causes.** Don't make the person
   a saint or celebrity; don't attribute the death to a single cause or overstate
   suicide's frequency. Defined in: • NYS Suicide Prevention Office, *A Guide for
   Communities, Organizations & Coalitions… Responding to a Death by Suicide* (Feb 2021)
   (https://www.preventsuicideny.org/wp-content/uploads/2021/05/Community-PV-Guide_Final.pdf);
   • reportingonsuicide.org.
5. **Parity principle.** Memorialize a death by suicide "the same general approach" as
   a death from cancer or an accident — neither erased nor set apart. Defined in:
   • AFSP workplace toolkit (Memorialization section, p. 10).
6. **Acknowledge once confirmed.** Publicly acknowledge a loss as suicide *if it has
   been confirmed*, balancing the family's right to privacy against treating suicide as
   a public-health issue. Defined in: • NYS guide, p. 4. (This is the rule behind our
   two-tier confirmed / cause-not-public classification.)
7. **Time-limit organization-run online memorials.** AFSP recommends org-established
   online memorial pages use safe messaging, include help resources, and come down
   after 30–60 days; peer-created tributes are to be *monitored*, not removed. Defined
   in: • AFSP workplace toolkit ("Online Memorial Pages and Social Media", p. 10; the
   same guidance appears in AFSP's schools and residency-program toolkits).
8. **Always include help-seeking resources.** Any communication about a suicide death
   should carry crisis resources (in the US, 988). Defined in: • AFSP;
   • reportingonsuicide.org.
- Not verified in our pass, listed as the standard international anchor: WHO,
  *Preventing Suicide: A Resource for Media Professionals* (latest ed. 2023).

## Publication posture

The guidance supports keeping a research record (norm 6's public-health framing; norm
5's argument against erasure) while constraining it (norms 2–4, 8). Because no
postvention literature we verified addresses *permanent research archives* specifically
(the 30–60-day guidance targets active-grief memorial pages), we resolved the tension
conservatively: **named case records stay private** (held in the org's private
repository, safe-messaging rules inside), and **this anonymized summary is the public
document** — methods, verified patterns, norms, and resources, with no information about
the individuals.

That resolution still stands. What has changed since is its **scope**: it originally bound
only these two layers, and a sibling document citing the same underlying material drifted
to the opposite posture as a result. The norms above now bind **every document in every
org repo** via [`docs/publication-standards/identifiable-people.md`](../../docs/publication-standards/identifiable-people.md),
which also adds the release gate, the quotation rule, and an honest register of what the
field has no answer for. Contributors editing any layer must follow it.

## Open questions

1. ~~Do other major communities (Linux kernel, Python, security/crypto, conferences'
   in-memoriam sessions) maintain formal memorial practices comparable to those
   studied?~~ **Answered 2026-08-05.** A primary-source survey of ~30 projects,
   foundations, conferences, registries and platforms found: permanence universal with
   zero exceptions; written procedure rare (~6 of 30), recent, and administrative;
   postvention categorically absent; cause-statement ungoverned. Recorded in practices
   (1)–(3) above. **A methodological warning worth carrying forward:** one community marks
   deceased contributors with a typographic convention carrying no legend anywhere on the
   page — nineteen years old, and invisible to any keyword search. Keyword methods cannot
   see structural or typographic conventions, and other projects may have similar ones.

   **Still open, and deliberately split off:** *are there further cases meeting the
   confirmation standard?* That is a different question with a different risk profile — it
   expands a sensitive case record rather than surveying public practice. Under
   [publication standards](../../docs/publication-standards/identifiable-people.md) Part B
   it needs a stated research purpose **before** collection, not after: what decision would
   more cases change? Note that our strongest current findings are practice-level, and more
   *practice* data strengthens them without more *case* data.
2. Is there postvention literature specifically addressing permanent archival/research
   records versus active-grief memorial pages?
3. ~~Beyond the one first-person community analysis we verified, is there peer-reviewed
   work linking OSS-specific conditions (maintainer burnout, harassment, legal
   pressure, isolation) to suicide risk?~~ **Answered 2026-08-05: no — zero studies.**
   Established across five independent bibliographic indexes and confirmed against this
   project's own corpus, where 49 open-source and developer full texts contained no
   peer-reviewed mention of suicide at all. The adjacent literatures exist on both sides
   and do not meet; see [Why the scale of this is not
   measurable](#why-the-scale-of-this-is-not-measurable) for why that gap is structural
   rather than an oversight. **The one first-person analysis remains the only bridge
   between the two literatures, and it is not peer-reviewed.**
4. **What is the relationship between open-source contribution and computing employment?**
   How many contributors hold full-time computing jobs; how many are students, between
   jobs, retired, or employed outside computing; and how far does that distribution differ
   between projects? No public source answers this. It is a precondition for reading any
   occupational statistic as evidence about this population, and it is the question that
   would most improve the argument in *Why the scale of this is not measurable*.
5. **Can the permanence finding be turned into guidance the postvention field lacks?**
   Published memorialization guidance assumes a page an organization can take down. This
   population has memorials that are irrevocable by construction, and no body responsible
   for grief. Nobody has written guidance for that case — the gap is field-wide, not ours
   — and we have now had to adopt a position on it in order to publish at all.
