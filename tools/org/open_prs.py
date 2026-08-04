#!/usr/bin/env python3
"""List every open PR across the whole organization, with links.

One `gh search prs --owner` call covers the org, so a repo added to it shows up here
without anyone editing a list.

  ./tools/org/open_prs.py            # grouped by repo, newest first within each
  ./tools/org/open_prs.py --urls     # just the URLs, one per line (pipe to a browser)

Stdlib only.
"""

import argparse
import json
import subprocess
import sys
from collections import defaultdict

ORG = "social-network-health"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--urls", action="store_true",
                    help="print only URLs, one per line")
    args = ap.parse_args()

    if subprocess.run(["gh", "auth", "status"], capture_output=True).returncode != 0:
        print("gh is not authenticated — run `gh auth login`", file=sys.stderr)
        return 1

    r = subprocess.run(
        ["gh", "search", "prs", "--owner", ORG, "--state", "open", "--limit", "100",
         "--json", "number,title,url,repository,isDraft,author,updatedAt"],
        capture_output=True, text=True, timeout=90)
    if r.returncode != 0:
        print((r.stderr or "gh search failed").strip(), file=sys.stderr)
        return 1

    prs = json.loads(r.stdout or "[]")
    if not prs:
        print(f"No open PRs across {ORG}.")
        return 0

    if args.urls:
        for p in sorted(prs, key=lambda p: (p["repository"]["name"], p["number"])):
            print(p["url"])
        return 0

    by_repo = defaultdict(list)
    for p in prs:
        by_repo[p["repository"]["name"]].append(p)

    drafts = 0
    print(f"{len(prs)} open PR(s) across {ORG}\n")
    for repo in sorted(by_repo):
        print(f"{repo}")
        for p in sorted(by_repo[repo], key=lambda p: p["number"]):
            mark = "[draft] " if p["isDraft"] else ""
            drafts += 1 if p["isDraft"] else 0
            who = (p.get("author") or {}).get("login", "")
            print(f"  #{p['number']:<5} {mark}{p['title']}")
            print(f"         {p['url']}" + (f"   ({who})" if who else ""))
        print()

    if drafts:
        print(f"({drafts} of them draft.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
