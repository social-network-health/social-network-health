# Presentations

All SNH talk material lives here — one folder per talk, with the delivered artifact (a PDF)
at the folder's top level and the deck source beneath it.

- [`dwebcamp-berlin-2026/`](dwebcamp-berlin-2026/) — DWeb Camp Berlin 2026, *"Rooting the
  Social Graph with Personal Network Applications"* (delivered July 2026). The PDF is the
  presentation; the [Slidev](https://sli.dev/) source, speaker notes, and prep live in
  [`dwebcamp-berlin-2026/deck/`](dwebcamp-berlin-2026/deck/).

Run a Slidev deck locally from the repo root with `just slides <folder>` (defaults to
`dwebcamp-berlin-2026/deck`) — it installs deps and opens the slideshow at localhost:3030.
To re-export a PDF after edits: `bunx slidev export` inside the deck folder
(`playwright-chromium` is a dev dependency).

Past material: the Personal Network Toolkit workshop deck (the starting point for the DWeb
Camp deck) lives in the archived [`richbodo/pnt-workshop`](https://github.com/richbodo/pnt-workshop)
repo (archived 2026-08-04), and in this repo's git history under `presentations/pnt-workshop/`.
