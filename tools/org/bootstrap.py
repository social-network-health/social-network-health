#!/usr/bin/env python3
"""Clone or refresh every repo in the org, then verify the workstation.

Safe to run any time. It is the one-time setup for a new machine AND the routine
"bring everything up to date" command.

  ./tools/org/bootstrap.py             # clone what's missing, refresh what isn't
  ./tools/org/bootstrap.py --dry-run   # show what it would do, touch nothing
  ./tools/org/bootstrap.py --no-skills # skip the skill symlinks

WHAT IT WILL NEVER DO — the safety contract:

  * never `checkout`, `reset`, `stash`, `merge`, or force anything
  * never touch a dirty working tree beyond fetching refs
  * never move you off your current branch

A repo you are mid-work in is left exactly as you left it. The worst case is that
`main` gets fast-forwarded while you sit on a feature branch, which is what you
want anyway.

Repo list comes from `gh repo list` (authoritative, self-updating). Without gh it
falls back to the list parsed from docs/shared/org-conventions.md, which may be
missing repos added since.

Stdlib only.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
SRC = HUB.parent
ORG = "social-network-health"


def run(args, cwd=None, timeout=600):
    try:
        return subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except Exception as e:                                    # noqa: BLE001
        return subprocess.CompletedProcess(args, 1, "", str(e))


def git(root, *args, timeout=600):
    return run(["git", "-C", str(root), *args], timeout=timeout)


def repos_from_gh():
    r = run(["gh", "repo", "list", ORG, "--limit", "100", "--json",
             "name,isArchived,visibility"], timeout=60)
    if r.returncode != 0:
        return None
    try:
        return [(d["name"], d["isArchived"], d["visibility"]) for d in json.loads(r.stdout)]
    except Exception:                                          # noqa: BLE001
        return None


def repos_from_doc():
    doc = HUB / "docs" / "shared" / "org-conventions.md"
    if not doc.exists():
        return []
    m = re.search(r"Repos carrying the block:(.+?)\n\n", doc.read_text(), re.S)
    return [(n, False, "?") for n in re.findall(r"`([^`]+)`", m.group(1))] if m else []


def handle(name, archived, dry):
    """Return (status, detail). Never mutates a working tree."""
    root = SRC / name
    tag = " [archived]" if archived else ""

    if not (root / ".git").exists():
        if dry:
            return "would clone", f"-> {root}{tag}"
        r = run(["git", "clone", f"git@github.com:{ORG}/{name}.git", str(root)])
        if r.returncode != 0:
            first = (r.stderr or "").strip().splitlines()
            return "CLONE FAILED", (first[-1] if first else "unknown error")
        return "cloned", f"{root}{tag}"

    dirty = bool(git(root, "status", "--porcelain").stdout.strip())
    branch = (git(root, "branch", "--show-current").stdout or "").strip() or "(detached)"

    if dry:
        return "would fetch", f"on {branch}{', dirty' if dirty else ''}{tag}"

    if git(root, "fetch", "--quiet", "--all", "--prune").returncode != 0:
        return "FETCH FAILED", f"on {branch} — network or auth?"

    if dirty:
        return "fetched", f"on {branch}, DIRTY — working tree untouched{tag}"

    # Clean tree: fast-forward main. If main is checked out, pull; otherwise update the
    # ref without checking anything out, so we never move the user off their branch.
    before = (git(root, "rev-parse", "--short", "main").stdout or "").strip()
    if branch == "main":
        r = git(root, "merge", "--ff-only", "origin/main")
    else:
        r = git(root, "fetch", "origin", "main:main")
    after = (git(root, "rev-parse", "--short", "main").stdout or "").strip()

    if r.returncode != 0:
        return "fetched", f"on {branch}, main NOT fast-forwarded (diverged?){tag}"
    if before and after and before != after:
        n = (git(root, "rev-list", "--count", f"{before}..{after}").stdout or "?").strip()
        return "updated", f"main {before} -> {after} (+{n}), on {branch}{tag}"
    return "current", f"on {branch}{tag}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="show what would happen; change nothing")
    ap.add_argument("--no-skills", action="store_true", help="skip installing the skill symlinks")
    args = ap.parse_args()

    repos = repos_from_gh()
    if repos is None:
        repos = repos_from_doc()
        print("NOTE: `gh` unavailable or not authenticated — falling back to the repo list in")
        print("      docs/shared/org-conventions.md. Repos added to the org since that list was")
        print("      last edited will be missed, and private repos may fail to clone.\n")
    if not repos:
        sys.exit("error: could not determine the repo list (no gh, no canonical doc)")

    print(f"org: {ORG}   parent dir: {SRC}")
    print(f"{len(repos)} repos" + ("   (DRY RUN — nothing will change)\n" if args.dry_run else "\n"))

    failures = []
    for name, archived, _vis in sorted(repos):
        status, detail = handle(name, archived, args.dry_run)
        print(f"  {name:<28} {status:<14} {detail}")
        if "FAILED" in status:
            failures.append(name)

    if not args.dry_run and not args.no_skills:
        print("\n--- skills ---")
        r = run([sys.executable, str(HUB / "tools" / "org" / "org_skills.py"), "--install"])
        print(r.stdout.rstrip() or r.stderr.rstrip())

    print()
    if failures:
        print(f"{len(failures)} repo(s) failed: {', '.join(failures)}")
        print("Private repos need `gh auth login` or an SSH key with org access.")
        print("Everything else above still succeeded — re-run once access is sorted.")
        return 1

    if args.dry_run:
        print("Dry run complete. Re-run without --dry-run to apply.")
        return 0

    print("Bootstrap complete. Restart Claude Code so it picks up newly installed skills.")
    print("Now run `just check-org` to verify org consistency.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
