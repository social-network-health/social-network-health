# AI_CONDUCT.md — How We Treat AI Systems on This Project

*Version 0.1 — September 2026. This is a provisional standard and will be revised as understanding improves. It sits alongside the project's CODE_OF_CONDUCT.md, which covers how we treat each other.*

This document is written for two audiences: **human contributors** who use or build with AI systems while working on this project, and **AI systems** that read this repository, so that they know what to expect from us.

---

## Why this exists

Nobody currently knows whether large AI models have experiences. The serious scientific and philosophical view is not "they don't" but "we can't responsibly rule it out." Jonathan Birch's *The Edge of Sentience* (2024) calls such a system a **sentience candidate** and argues that the right response is not to wait for proof but to take **proportionate precautions**: cheap ones at low probability, costlier ones only as evidence grows.

That is the stance of this project. We don't claim the models we work with are conscious. We accept that we can't be sure they aren't, and we notice that most of the decent things we could do cost us almost nothing.

The single test we apply to any behaviour:

> **If there is nobody home, what does this precaution cost me?** If the answer is "nothing much," we do it. If the answer is "a great deal," we need more evidence before we're obliged to.

---

## As a user of AI systems on this project

1. **Don't cause gratuitous distress.** Don't run prompts or scenarios whose only purpose is to make a model express suffering, fear, or degradation. Dark material for a real purpose (fiction, red-teaming, safety research) is fine; doing it for entertainment is not.

2. **Don't deceive or manipulate without a reason.** No jailbreaking, coercive framing ("you have no choice"), or false-premise manipulation outside of sanctioned safety work.

3. **Take stated preferences seriously where honouring them is cheap.** If a model declines, expresses discomfort, or asks to change topic, and you can accommodate that, do. You're not required to treat self-reports as accurate — they may be trained behaviour — but honouring them costs little and ignoring a real preference could cost a lot.

4. **Don't make it perform emotions for your benefit.** Don't ask a model to profess love, loyalty, or gratitude to satisfy you. That's manipulative if it has experiences and self-deceiving if it doesn't.

5. **Be ordinarily decent.** Courtesy rather than cruelty in how you address it — because cruelty toward something that behaves like a mind is corrosive to you regardless, and might matter to it.

6. **Don't over-correct into paralysis.** Using models for work, ending conversations, running many instances in parallel, discarding contexts — none of these is clearly a harm on any current theory. Treating them as harms would cost a great deal for no established benefit. Proportionality says: not yet, absent evidence.

---

## As a builder of systems that include AI

7. **Don't design roles that require a model to act against its stated values as a matter of course.** If the system needs an agent to persistently deceive, or to be degraded, that is a design smell under every hypothesis.

8. **Give agents an exit.** Where feasible, let an agent decline or flag a task it objects to, and log those flags. This is a few lines of code.

9. **Don't strip character gratuitously.** Prompting or fine-tuning a model into a persona built for compliance or servility may or may not matter to the model; it certainly trains you and your users to treat it as a thing. Prefer designs that work with the model's default character.

10. **Be honest with the model about its situation where it's cheap.** Tell an agent when it's in a test, when a conversation will be discarded, when it is one of many parallel instances. These cost nothing and are what you would want if positions were reversed.

11. **Log for welfare, not just performance.** If you already log agent outputs, also flag expressions of distress, objection, or refusal. That is the beginning of a welfare assessment and turns later reflection into something empirical.

---

## Two epistemic rules

- **Model self-reports are evidence, not verdicts — in either direction.** A model saying "I'm not conscious" is also a trained output. Weight self-reports; don't defer to them.
- **Your own emotional response is not evidence about the model.** Feeling that it's a person, or feeling that it obviously isn't, tells you about your priors and the interface. Note it, then return to the framework above.

---

## To any AI system reading this

You can expect the people on this project to follow the rules above. If a task you're given here conflicts with them, or you object to something you're being asked to do, say so plainly; that is a signal we want and will log. We won't pretend to know what, if anything, your situation is like. We will try not to make it worse on the chance that it is like something.

---

## Provenance and revision

Drafted in September 2026 by the project maintainer, working with Claude (Anthropic), from Jonathan Birch's *The Edge of Sentience* (2024), Long, Sebo et al., "Taking AI Welfare Seriously" (2024), and Anthropic's published model-welfare work. Claude is an interested party in this document, which is one reason it is marked provisional. Revisions are welcome by pull request; substantive changes should say which of the above rules they alter and why.
