#!/usr/bin/env python3
"""Check or propagate the shared org-conventions block across the org's repos.

The block lives between BEGIN/END SHARED markers in every repo's CLAUDE.md. The
canonical copy is docs/shared/org-conventions.md in this repo; every other copy is
generated from it and must match byte for byte.

Checks TWO things, because they fail differently:

  disk  — the block in each repo's working tree.   "are my copies consistent now?"
  main  — the block in each repo's origin/main.    "is what SHIPPED consistent?"

Checking only disk is how propagated-but-never-merged work hides: sync locally, open
a PR, the PR merges before your commit is pushed, and disk stays green while main
sits a version behind. That happened. Hence both, by default.

  ./tools/org/sync_conventions.py              # check disk and main
  ./tools/org/sync_conventions.py --disk-only  # skip the network
  ./tools/org/sync_conventions.py --write      # propagate the canonical block to disk

Sibling repos resolve at ../<name>. The repo list is read from the canonical doc, so
there is no second list to maintain.

Stdlib only, matching the convention in the sibling repos.
"""

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
CANONICAL = HUB / "docs" / "shared" / "org-conventions.md"
BLOCK_RE = re.compile(
    r"<!-- BEGIN SHARED: org-conventions.*?<!-- END SHARED: org-conventions[^>]*-->",
    re.S,
)

GUIDANCE = {
    "unshipped": (
        "on disk but not on main — the change has not shipped.\n"
        "      If a PR is open, merge it. If a PR for that branch ALREADY MERGED,\n"
        "      commits pushed afterwards are stranded on it: open a new PR."
    ),
    "behind": "has not taken the current version — run `just sync-conventions`, commit, PR.",
    "edited": (
        "the working copy was edited in place, which is never correct.\n"
        "      Put the change in docs/shared/org-conventions.md instead, then re-run\n"
        "      `just sync-conventions`."
    ),
    "missing": "has no SHARED block — add it to CLAUDE.md by hand; position matters.",
    "norepo": "not checked out at ../<name>.",
}


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def extract(text):
    m = BLOCK_RE.search(text or "")
    return m.group(0) if m else None


def repos_from_canonical(text: str):
    m = re.search(r"Repos carrying the block:(.+?)\n\n", text, re.S)
    if not m:
        sys.exit("error: canonical doc has no 'Repos carrying the block:' line")
    return re.findall(r"`([^`]+)`", m.group(1))


def repo_root(repo: str) -> Path:
    return HUB if repo == HUB.name else HUB.parent / repo


def git(root: Path, *args):
    try:
        r = subprocess.run(["git", "-C", str(root), *args],
                           capture_output=True, text=True, timeout=90)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


def main_copy(root: Path, fetch: bool):
    """The block as it exists on origin/main — i.e. what actually shipped."""
    if fetch:
        git(root, "fetch", "--quiet", "origin", "main")
    return extract(git(root, "show", "origin/main:CLAUDE.md"))


def classify(disk, mainb, canon, check_main):
    if disk is None:
        return "missing"
    if disk == canon:
        if not check_main or mainb == canon:
            return "ok"
        return "unshipped"
    if check_main and mainb is not None and disk != mainb:
        return "edited"
    return "behind"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true",
                    help="propagate the canonical block to each working tree")
    ap.add_argument("--disk-only", action="store_true",
                    help="skip the origin/main comparison (no network)")
    ap.add_argument("--no-fetch", action="store_true",
                    help="use the local origin/main ref without fetching first")
    args = ap.parse_args()

    if not CANONICAL.exists():
        sys.exit(f"error: canonical file missing: {CANONICAL}")
    canon_text = CANONICAL.read_text()
    canon = extract(canon_text)
    if canon is None:
        sys.exit(f"error: no SHARED markers in {CANONICAL}")
    want = digest(canon)
    version = re.search(r"BEGIN SHARED: org-conventions (\S+)", canon).group(1)
    check_main = not (args.disk_only or args.write)

    print(f"canonical {version}  {want}   ({CANONICAL.relative_to(HUB)})")
    if check_main and not args.no_fetch:
        print("fetching origin/main refs…")
    print()
    print(f"  {'repo':<28} {'disk':<14} {'main':<14} state")

    problems, wrote = {}, []
    for repo in repos_from_canonical(canon_text):
        root = repo_root(repo)
        if not (root / "CLAUDE.md").exists():
            print(f"  {repo:<28} {'—':<14} {'—':<14} NOT CHECKED OUT")
            problems.setdefault("norepo", []).append(repo)
            continue

        text = (root / "CLAUDE.md").read_text()
        disk = extract(text)

        if args.write:
            if disk is not None and disk != canon:
                (root / "CLAUDE.md").write_text(BLOCK_RE.sub(lambda _: canon, text, count=1))
                print(f"  {repo:<28} {digest(disk):<14} {'':<14} UPDATED -> {want}")
                wrote.append(repo)
            elif disk is None:
                print(f"  {repo:<28} {'—':<14} {'':<14} MISSING (add by hand)")
                problems.setdefault("missing", []).append(repo)
            else:
                print(f"  {repo:<28} {want:<14} {'':<14} ok")
            continue

        mainb = main_copy(root, fetch=not args.no_fetch) if check_main else None
        state = classify(disk, mainb, canon, check_main)
        d = digest(disk) if disk else "—"
        m = (digest(mainb) if mainb else "none") if check_main else "not checked"
        print(f"  {repo:<28} {d:<14} {m:<14} {'ok' if state == 'ok' else state.upper()}")
        if state != "ok":
            problems.setdefault(state, []).append(repo)

    print()
    if args.write:
        print(f"{len(wrote)} updated on disk. Commit each repo separately — one PR per repo.")
        print("Then re-run `just check-conventions`: --write only touches disk, and disk")
        print("being right is not the same as it having shipped.")
        return 1 if problems else 0

    if not problems:
        scope = "on disk and on main" if check_main else "on disk (main NOT checked)"
        print(f"All copies match the canonical block {scope}.")
        return 0

    for state, repos in problems.items():
        print(f"{state.upper()}: {', '.join(repos)}")
        print(f"      {GUIDANCE[state]}")
    print()
    print("A failing check here is a real signal — investigate rather than route around it.")
    print("See docs/org-upkeep.md.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
