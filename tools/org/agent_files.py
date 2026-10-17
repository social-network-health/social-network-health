#!/usr/bin/env python3
"""Check the agent files every block-carrying repo keeps, on disk and on origin/main.

Since block v8, AGENTS.md is every repo's instructions file and every agent we use reads it.
Around it, each repo in the canonical doc's table keeps:

  AGENTS.md                      under 24,000 bytes (Antigravity CLI truncates past that)
  CLAUDE.md                      first line `@AGENTS.md`, and never a second copy of the block
  .agents/skills/prime/SKILL.md  a prime skill
  .agents/skills/<name>/SKILL.md spec frontmatter: `name` matching the folder, a `description`,
                                 and no tool-specific keys
  .claude/skills/<name>          a symlink to ../../.agents/skills/<name> for every repo skill,
                                 and nothing else — no Claude-only skills
  .claude/commands/prime.md      gone: it would shadow the prime skill in Claude Code

  ./tools/org/agent_files.py               # check disk and origin/main
  ./tools/org/agent_files.py --disk-only   # skip the network
  ./tools/org/agent_files.py --no-fetch    # use local origin/main refs as they are

The block's text is sync_conventions.py's job; this checks the files around it. Like that
script, it checks main because main is what shipped, and disk because that's where you work.

Stdlib only.
"""

import argparse
import os
import posixpath
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (CLAUDE_STUB, INSTRUCTIONS, extract_block,   # noqa: E402
                     repo_root, repos_from_canonical)

MAX_BYTES = 24_000
# The open Agent Skills spec's frontmatter keys. Anything else is tool-specific, and claude.ai
# rejects skills that carry extras.
SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
SKILLS = ".agents/skills"
CLAUDE_SKILLS = ".claude/skills"


def git(root: Path, *args):
    try:
        r = subprocess.run(["git", "-C", str(root), *args],
                           capture_output=True, text=True, timeout=90)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


class Disk:
    """The working tree."""

    def __init__(self, root: Path):
        self.root = root

    def read(self, rel):
        p = self.root / rel
        return p.read_text() if p.is_file() else None

    def listdir(self, rel):
        p = self.root / rel
        return sorted(os.listdir(p)) if p.is_dir() else []

    def link(self, rel):
        """The symlink's target, or None if rel isn't a symlink."""
        p = self.root / rel
        return os.readlink(p) if p.is_symlink() else None


class Main:
    """origin/main, read through git without checking anything out."""

    def __init__(self, root: Path):
        self.root = root

    def _entry(self, rel):
        out = git(self.root, "ls-tree", "origin/main", "--", rel)
        return out.split(None, 3) if out else None   # mode, type, sha, path

    def read(self, rel):
        return git(self.root, "show", f"origin/main:{rel}")

    def listdir(self, rel):
        out = git(self.root, "ls-tree", "--name-only", "origin/main", "--", rel.rstrip("/") + "/")
        return sorted(Path(line).name for line in (out or "").splitlines())

    def link(self, rel):
        e = self._entry(rel)
        return self.read(rel) if e and e[0] == "120000" else None


def frontmatter(text):
    if not text or not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    keys = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if m:
            keys[m.group(1)] = m.group(2).strip().strip("'\"")
    return keys


def skill_text(view, name):
    """A skill's SKILL.md, following the skill folder if it is itself a symlink."""
    rel = f"{SKILLS}/{name}"
    target = view.link(rel)
    if target is not None:
        rel = posixpath.normpath(posixpath.join(SKILLS, target))
    return view.read(f"{rel}/SKILL.md")


def check(view) -> list[str]:
    problems = []

    agents = view.read(INSTRUCTIONS)
    if agents is None:
        problems.append(f"no {INSTRUCTIONS}")
    else:
        size = len(agents.encode())
        if size >= MAX_BYTES:
            problems.append(f"{INSTRUCTIONS} is {size:,} bytes — keep it under {MAX_BYTES:,}")
        if extract_block(agents) is None:
            problems.append(f"{INSTRUCTIONS} has no shared block")

    claude = view.read("CLAUDE.md")
    if claude is None:
        problems.append(f"no CLAUDE.md — it should be one line, {CLAUDE_STUB}")
    else:
        first = next((line.strip() for line in claude.splitlines() if line.strip()), "")
        if first != CLAUDE_STUB:
            problems.append(f"CLAUDE.md doesn't start with {CLAUDE_STUB}")
        if extract_block(claude) is not None:
            problems.append(f"CLAUDE.md has a copy of the shared block — it belongs in {INSTRUCTIONS}")

    skills = view.listdir(SKILLS)
    if "prime" not in skills:
        problems.append(f"no prime skill ({SKILLS}/prime/SKILL.md)")
    for name in skills:
        fm = frontmatter(skill_text(view, name))
        if fm is None:
            problems.append(f"{SKILLS}/{name}: no SKILL.md with frontmatter")
            continue
        if fm.get("name") != name:
            problems.append(f"{SKILLS}/{name}: frontmatter name is {fm.get('name')!r}, not {name!r}")
        if not fm.get("description"):
            problems.append(f"{SKILLS}/{name}: no description")
        extra = sorted(set(fm) - SPEC_KEYS)
        if extra:
            problems.append(f"{SKILLS}/{name}: tool-specific frontmatter {', '.join(extra)}")
        want = f"../../{SKILLS}/{name}"
        got = view.link(f"{CLAUDE_SKILLS}/{name}")
        if got != want:
            problems.append(f"{CLAUDE_SKILLS}/{name} should be a symlink to {want}"
                            + (f" (points to {got})" if got else ""))

    for name in view.listdir(CLAUDE_SKILLS):
        if name not in skills:
            problems.append(f"{CLAUDE_SKILLS}/{name} is Claude-only — move it to {SKILLS}/{name} "
                            "and link it")

    if view.read(".claude/commands/prime.md") is not None:
        problems.append(".claude/commands/prime.md still exists — the prime skill replaces it")

    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--disk-only", action="store_true", help="skip origin/main (no network)")
    ap.add_argument("--no-fetch", action="store_true",
                    help="use the local origin/main ref without fetching first")
    args = ap.parse_args()

    print(f"agent files: {INSTRUCTIONS} + one-line CLAUDE.md + skills in {SKILLS}\n")
    print(f"  {'repo':<28} {'disk':<10} {'main':<10}")
    failed = {}
    for repo in repos_from_canonical():
        root = repo_root(repo)
        if not root.is_dir():
            print(f"  {repo:<28} {'—':<10} {'—':<10} NOT CHECKED OUT")
            failed[repo] = ["not checked out at ../" + repo]
            continue
        disk = check(Disk(root))
        if args.disk_only:
            main_problems, main_state = [], "not checked"
        else:
            if not args.no_fetch:
                git(root, "fetch", "--quiet", "origin", "main")
            main_problems = check(Main(root))
            main_state = "ok" if not main_problems else f"{len(main_problems)} issue(s)"
        disk_state = "ok" if not disk else f"{len(disk)} issue(s)"
        print(f"  {repo:<28} {disk_state:<10} {main_state:<10}")
        lines = [f"disk: {p}" for p in disk] + [f"main: {p}" for p in main_problems]
        if lines:
            failed[repo] = lines

    print()
    if not failed:
        scope = "on disk" if args.disk_only else "on disk and on main"
        print(f"Every repo keeps its agent files right {scope}.")
        return 0
    for repo, lines in failed.items():
        print(f"{repo}:")
        for line in lines:
            print(f"    {line}")
    print()
    print("Layout and reasons: the canonical doc, hub docs/shared/org-conventions.md.")
    print("A failing check here is a real signal — investigate rather than route around it.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
