# Publication standards

Standards for **what the organization publishes, and how** — across every surface we publish on.

These are org-wide. They bind every repo, not just this one. They are meant to be checked when
relevant and ignored the rest of the time, so each document is named for the situation that triggers
it rather than for the project that produced it.

## What we publish, and where

The org publishes on three surfaces with genuinely different audiences and production models. See
[`RELATED_REPOS.md`](../../RELATED_REPOS.md) for what each repo is; this table is about publishing,
not about code.

| Surface | What it is | Audience | Reversible? |
|---|---|---|---|
| **Original research** — the repos | Research documents, specs, threat models, protocol notes, the paper corpus. Mostly in this hub's [`research/`](../../research/), plus the PNA Spec and positioning work in `personal_network_toolkit`, and the corpus in `snhdb` | Researchers, practitioners, contributors, other agents | **Yes** — git-tracked text we can amend, generalise further, or withdraw |
| **The toolkit wiki** — [toolkit.socialnetwork.health](https://toolkit.socialnetwork.health) | Science education: best practices and research findings written for practitioners. The largest published body of SNH work | Practitioners and the general public | **Yes** — editable in place |
| **The video archive** — [YouTube](https://www.youtube.com/@SocialNetworkHealth) | Science education: recorded talks, check-ins, and training material for trainers and researchers | Practitioners, trainers, the general public | **No** — once published and mirrored, it cannot be retracted |

Two of the three are science education rather than primary research, and are written for a much
broader and less specialist audience. That changes the *register*, not the obligations: **the
standards here bind all three.** A claim about a real person is no less consequential in a video
than in a threat model — and reaches more people.

The reversibility column is not decoration. It is the axis the release gate in
[`identifiable-people.md`](identifiable-people.md) actually turns on, and it is why the video work
has always used a full signed-release-and-review process while a research document can sometimes
proceed while permission is still being sought. Same standard, different setting, for a stated
reason.

The website itself ([socialnetwork.health](https://socialnetwork.health)) and delivered
conference talks are publication surfaces too. Talks are **irreversible** once delivered — treat
them like video.

## What's here

| Document | Read it when |
|---|---|
| [`identifiable-people.md`](identifiable-people.md) | You are writing about a real, identifiable person — including someone identifiable indirectly, by a combination of details, or through a source you cite. Covers the release gate, generalisation, quotation and re-identification, citation transparency, and — for the sensitive-subject case that prompted it — cause discipline and safe messaging around suicide and bereavement. |

That is the only document so far, and its name is deliberate. It is not "memoriams standards": the
memoriams study is what forced us to write it, but almost all of it — the release gate, the
jigsaw-identification rules, the searchable-quote problem, disclosing what you withheld — applies to
any research about identifiable people. That includes personal-network and relationship data, which
is most of what this organization works on.

Its suicide-and-bereavement material (cause discipline in §A2, safe messaging in §A5) is a
topic-specific overlay sitting inside the general standard. If a second sensitive-subject overlay
ever needs writing, that is the natural seam to split on — general rules in one document, per-topic
overlays beside it. One topic does not justify the split yet.

## Related

- [`memoriams.md`](../../research/research_library/memoriams.md) — the postvention norms, with their
  defining sources, and the anonymised public summary those norms were first written for.
- The research briefs the standard was built from are staged in the org's private repository. They
  contain no case material; they are private because raw research output is not worth a reader's
  time until it has been reviewed.
