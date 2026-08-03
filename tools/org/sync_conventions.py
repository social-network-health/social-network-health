#!/usr/bin/env python3
"""Check or propagate the shared org-conventions block across the org's repos.

The block lives between BEGIN/END SHARED markers in every repo's CLAUDE.md. The
canonical copy is docs/shared/org-conventions.md in this repo; every other copy is
generated from it and must match byte for byte.

  ./tools/org/sync_conventions.py            # check (default) — exit 1 on drift
  ./tools/org/sync_conventions.py --write    # propagate the canonical block

Sibling repos are resolved at ../<name>, per the org's checkout convention. The repo
list is read from the canonical doc itself, so there's no second list to maintain.

Stdlib only, matching the convention in the sibling repos.
"""

import argparse
import hashlib
import re
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
CANONICAL = HUB / "docs" / "shared" / "org-conventions.md"
BLOCK_RE = re.compile(
    r"<!-- BEGIN SHARED: org-conventions.*?<!-- END SHARED: org-conventions[^>]*-->",
    re.S,
)


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def extract(text: str):
    m = BLOCK_RE.search(text)
    return m.group(0) if m else None


def repos_from_canonical(text: str):
    """The canonical doc names the repos carrying the block; parse that line."""
    m = re.search(r"Repos carrying the block:(.+?)\n\n", text, re.S)
    if not m:
        sys.exit("error: canonical doc has no 'Repos carrying the block:' line")
    return re.findall(r"`([^`]+)`", m.group(1))


def claude_md(repo: str) -> Path:
    return (HUB if repo == HUB.name else HUB.parent / repo) / "CLAUDE.md"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true",
                    help="propagate the canonical block instead of only checking")
    args = ap.parse_args()

    if not CANONICAL.exists():
        sys.exit(f"error: canonical file missing: {CANONICAL}")
    canon_text = CANONICAL.read_text()
    block = extract(canon_text)
    if block is None:
        sys.exit(f"error: no SHARED markers in {CANONICAL}")
    want = digest(block)
    version = re.search(r"BEGIN SHARED: org-conventions (\S+)", block).group(1)

    print(f"canonical {version}  {want}  ({CANONICAL.relative_to(HUB)})\n")

    drift, missing, wrote = [], [], []
    for repo in repos_from_canonical(canon_text):
        path = claude_md(repo)
        if not path.exists():
            print(f"  {repo:<28} MISSING CLAUDE.md ({path})")
            missing.append(repo)
            continue
        text = path.read_text()
        have = extract(text)

        if have is None:
            if args.write:
                print(f"  {repo:<28} no block — append manually, position matters")
            else:
                print(f"  {repo:<28} NO BLOCK")
            missing.append(repo)
            continue

        if digest(have) == want:
            print(f"  {repo:<28} ok       {want}")
            continue

        if args.write:
            path.write_text(BLOCK_RE.sub(lambda _: block, text, count=1))
            print(f"  {repo:<28} UPDATED  {digest(have)} -> {want}")
            wrote.append(repo)
        else:
            print(f"  {repo:<28} DRIFTED  {digest(have)} != {want}")
            drift.append(repo)

    print()
    if args.write:
        print(f"{len(wrote)} updated, {len(missing)} need attention.")
        if wrote:
            print("Commit each repo separately — one PR per repo.")
        return 1 if missing else 0

    if drift or missing:
        print(f"{len(drift)} drifted, {len(missing)} missing.")
        print("Fix: edit docs/shared/org-conventions.md, then `just sync-conventions`.")
        print("Never edit a repo's copy in place — that is how the drift started.")
        return 1
    print("All copies match the canonical block.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
