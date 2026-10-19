#!/usr/bin/env python3
"""Validate the authoritative org task IDs without fetching any other repository."""
from pathlib import Path
import re
import sys


def main():
    path=Path(__file__).resolve().parents[2]/'plans/ORG-TASKS.md'
    text=path.read_text();errors=[];seen=set();section=None
    allowed={'Active','Waiting On','Waiting','Blocked','Planned','Deferred','Needs review','Done','Cancelled','Watching'}
    if '<!-- org-task-register: 1 -->' not in text:errors.append('missing register version marker')
    for number,line in enumerate(text.splitlines(),1):
        if line.startswith('## '):section=line[3:].strip()
        match=re.match(r'^- \[([ xX])\] ',line)
        if not match:continue
        ids=re.findall(r'<!-- task: (SNH-ORG-\d{4,}) -->',line)
        if len(ids)!=1:errors.append(f'line {number}: exactly one task ID is required')
        elif ids[0] in seen:errors.append(f'line {number}: duplicate ID {ids[0]}')
        else:seen.add(ids[0])
        if section not in allowed or section=='Watching':errors.append(f'line {number}: unknown task section {section}')
        if (match[1].lower()=='x')!=(section in {'Done','Cancelled'}):errors.append(f'line {number}: checkbox conflicts with section')
    if errors:
        print('\n'.join(errors));return 1
    print(f'Validated {len(seen)} stable org task IDs and checkbox states. Source assertions are not independently verified.')
    return 0


if __name__=='__main__':sys.exit(main())
