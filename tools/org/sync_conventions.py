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

main is the truth; disk is the workstation. When origin/main already carries the
current block but the working tree doesn't — because it sits on a branch cut before
the block landed — nothing in the org is broken. That's reported as a `stale`
WARNING and does not fail the check. The one exception: a disk copy claiming the
CURRENT version with different text is an in-place edit, which is always an error.

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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (BLOCK_RE, CANONICAL, HUB,   # noqa: E402
                     extract_block, repo_root, repos_from_canonical)

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
    "stale": (
        "warning, not a failure — origin/main already has the current block; the\n"
        "      working tree is just on a branch cut before it landed. Nothing to fix\n"
        "      org-wide: `git switch main` (or rebase) when you next work there."
    ),
}


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


extract = extract_block


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


def block_version(block):
    m = re.search(r"BEGIN SHARED: org-conventions (\S+)", block or "")
    return m.group(1) if m else None


def classify(disk, mainb, canon, check_main):
    if disk == canon:
        if not check_main or mainb == canon:
            return "ok"
        return "unshipped"
    if check_main and mainb == canon:
        # What shipped is current; only this working tree is behind. An older
        # version (or no block) means a branch cut before the block landed —
        # stale, a warning. Same-version-different-text is an in-place edit.
        if disk is not None and block_version(disk) == block_version(canon):
            return "edited"
        return "stale"
    if disk is None:
        return "missing"
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
    print("(hashes are sha256 of the block text, first 12 chars — every repo showing the")
    print(" same hash is the goal, not a coincidence. They are not git commits.)")
    if check_main and not args.no_fetch:
        print("fetching origin/main refs…")
    print()
    print(f"  {'repo':<28} {'disk':<14} {'main':<14} state")

    problems, warnings, wrote = {}, {}, []
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
        if state == "stale":
            branch = (git(root, "branch", "--show-current") or "").strip() or "(detached)"
            print(f"  {repo:<28} {d:<14} {m:<14} stale (on {branch})")
            warnings.setdefault(state, []).append(f"{repo} [{branch}]")
        else:
            print(f"  {repo:<28} {d:<14} {m:<14} {'ok' if state == 'ok' else state.upper()}")
            if state != "ok":
                problems.setdefault(state, []).append(repo)

    print()
    if args.write:
        print(f"{len(wrote)} updated on disk. Commit each repo separately — one PR per repo.")
        print("Then re-run `just check-conventions`: --write only touches disk, and disk")
        print("being right is not the same as it having shipped.")
        return 1 if problems else 0

    for state, repos in warnings.items():
        print(f"{state}: {', '.join(repos)}")
        print(f"      {GUIDANCE[state]}")
        print()

    if not problems:
        scope = "on main" if check_main else "on disk (main NOT checked)"
        if warnings:
            print(f"Shipped state is green — every repo matches the canonical block {scope}.")
            print("Stale working trees above are warnings and do not fail the check.")
        else:
            scope = "on disk and on main" if check_main else scope
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
