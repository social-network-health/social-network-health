"""Shared helpers for the org tooling.

One source of truth per fact applies to the tooling too: three scripts need the list of
repos that carry the shared block, so the parser lives here rather than in each of them.

Stdlib only.
"""

import re
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
SRC = HUB.parent
CANONICAL = HUB / "docs" / "shared" / "org-conventions.md"

# Markers are anchored to the start of a line on purpose. The canonical doc explains the
# marker syntax in prose, so an unanchored pattern can match the explanation instead of
# the real block.
BLOCK_RE = re.compile(
    r"^<!-- BEGIN SHARED: org-conventions.*?^<!-- END SHARED: org-conventions[^>]*-->",
    re.S | re.M,
)

TABLE_ANCHOR = "source of truth for which repos"


def extract_block(text):
    """The shared block, or None. Matches only real line-start markers."""
    m = BLOCK_RE.search(text or "")
    return m.group(0) if m else None


def repos_from_canonical(text=None):
    """Repo names from the table in the canonical doc — the single source of truth.

    Parsed from the markdown table so that adding or removing a repo is a one-line edit
    to a document a human actually reads, rather than a list buried in a script.
    """
    text = text if text is not None else CANONICAL.read_text()
    anchor = re.search(TABLE_ANCHOR, text)
    if not anchor:
        sys.exit(f"error: {CANONICAL.name} has no repo table "
                 f"(looked for the sentence containing {TABLE_ANCHOR!r})")

    repos, started = [], False
    for line in text[anchor.end():].splitlines():
        s = line.strip()
        if not s:
            if started:
                break          # blank line ends the table
            continue
        if s.startswith("|"):
            started = True
            repos.extend(re.findall(r"`([^`]+)`", s))
        elif started:
            break              # prose after the table
    if not repos:
        sys.exit(f"error: found the repo table in {CANONICAL.name} but parsed no repo names")
    return repos


def repo_root(repo):
    return HUB if repo == HUB.name else SRC / repo
