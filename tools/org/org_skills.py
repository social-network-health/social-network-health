#!/usr/bin/env python3
"""Check or install the org's shared Claude Code skills.

Org skills are installed as SYMLINKS from ~/.claude/skills/<name> into the repo that
owns the skill. A symlink follows upstream automatically; a copy drifts silently and
already has (fellows_local_db vendored the PNA Toolkit skill and fell a rename and
several flows behind).

  ./tools/org/org_skills.py             # check (default) — exit 1 if anything is off
  ./tools/org/org_skills.py --install   # create or repair the symlinks

Also flags vendored copies inside repos that SHADOW an org skill, because two skills
with near-identical trigger text is worse than one — the model may pick the stale one.

SCOPE — this checks THIS WORKSTATION, not what shipped. Skills are installed per
machine (~/.claude/skills), so there is no origin/main equivalent to compare against;
green here means your machine is set up, not that a teammate's is. Each developer runs
`just install-skills` once. The vendored-copy scan reads working trees, so it can miss a
copy that exists on main but not locally.

Stdlib only.
"""

import argparse
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parents[2]
SRC = HUB.parent
USER_SKILLS = Path.home() / ".claude" / "skills"

# name -> path of the skill directory, relative to the sibling-checkout root.
# Add a row when the org publishes a new shared skill.
ORG_SKILLS = {
    "pna-toolkit": "personal_network_toolkit/pna-toolkit",
    "snhdb": "snhdb/skill/snhdb",
    "paper-resolver": "social-network-health/tools/paper-resolver",
}

# Former names, so a stale vendored copy is recognised as a duplicate rather than
# reported as an unrelated skill. Add a row whenever an org skill is renamed.
ALIASES = {
    "pna-build-eval-contrib": "pna-toolkit",   # renamed upstream in PNT a56c3b1
}


def check_one(name: str, rel: str, install: bool):
    src = SRC / rel
    dst = USER_SKILLS / name

    if not src.exists():
        return f"{name:<18} SOURCE MISSING   {src} (is the repo checked out?)", False

    if dst.is_symlink():
        target = dst.resolve()
        if target == src.resolve():
            return f"{name:<18} ok               -> {rel}", True
        if install:
            dst.unlink()
            dst.symlink_to(src)
            return f"{name:<18} REPOINTED        -> {rel}", True
        return f"{name:<18} WRONG TARGET     -> {target}", False

    if dst.exists():  # a real directory — a copy, not a link
        return f"{name:<18} IS A COPY        {dst} — replace with a symlink", False

    if install:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.symlink_to(src)
        return f"{name:<18} INSTALLED        -> {rel}", True
    return f"{name:<18} NOT INSTALLED    (skill unavailable in your sessions)", False


def org_repos():
    """Only scan repos in this org — read the list from the canonical conventions doc."""
    import re
    doc = (HUB / "docs" / "shared" / "org-conventions.md").read_text()
    m = re.search(r"Repos carrying the block:(.+?)\n\n", doc, re.S)
    return re.findall(r"`([^`]+)`", m.group(1)) if m else [HUB.name]


def find_shadows():
    """Repo-level skills that duplicate an org skill, or vendor a copy that will drift.

    A repo-level SYMLINK to the same source an org skill uses is fine — it can't drift.
    Only copies, and links pointing somewhere else, are problems.
    """
    out = []
    for repo in org_repos():
        skills_dir = SRC / repo / ".claude" / "skills"
        if not skills_dir.is_dir():
            continue
        for entry in sorted(skills_dir.iterdir()):
            if not (entry / "SKILL.md").is_file():
                continue
            declared = ""
            for line in (entry / "SKILL.md").read_text().splitlines()[:6]:
                if line.startswith("name:"):
                    declared = line.split(":", 1)[1].strip()
                    break
            owner = next((r for r in ORG_SKILLS if r in (entry.name, declared)), None)
            if owner is None:
                owner = ALIASES.get(entry.name) or ALIASES.get(declared)
            where = f"{repo}/.claude/skills/{entry.name}"

            if entry.is_symlink():
                # same source as the registry entry -> harmless, skip
                if owner and entry.resolve() == (SRC / ORG_SKILLS[owner]).resolve():
                    continue
                out.append(f"  {where} -> {entry.resolve()} (symlink outside the registry)")
            elif owner:
                renamed = "" if entry.name == owner else f" (renamed upstream to '{owner}')"
                out.append(f"  {where} COPY duplicates org skill '{owner}'{renamed} — delete it; "
                           f"the user-level symlink already covers this repo")
            else:
                out.append(f"  {where} COPY (declares '{declared}') — vendored, will drift")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--install", action="store_true",
                    help="create or repair the symlinks instead of only checking")
    args = ap.parse_args()

    print(f"user skills dir: {USER_SKILLS}\n")
    ok = True
    for name, rel in ORG_SKILLS.items():
        line, good = check_one(name, rel, args.install)
        print("  " + line)
        ok = ok and good

    shadows = find_shadows()
    if shadows:
        print("\nvendored / shadowing skills:")
        print("\n".join(shadows))
        print("\n  A vendored copy drifts silently. Prefer the user-level symlink and")
        print("  delete the copy, or re-sync it deliberately and record the pinned commit.")
        ok = False

    print()
    if not ok:
        print("Fix what's flagged, then re-run. `--install` handles the symlinks.")
        print("Note: Claude Code discovers skills at session start — restart after installing.")
        print("A failing check here is a real signal — investigate rather than route around it.")
        return 1
    print("All org skills are symlinked and unshadowed ON THIS WORKSTATION.")
    print("(Per-machine setup — this says nothing about anyone else's checkout.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
