# Admin/devops recipes for socialnetwork.health. Run `just` to list them.
# Server layout, provisioning details, and SSH notes: ops/README.md

# list available recipes
default:
    @just --list

# rsync the two public/ files to the droplet (override host with SNH_HOST=rsb@<ip>)
deploy:
    ./ops/deploy.sh

# check the live site responds and serves the expected title
verify-live:
    curl -sI https://socialnetwork.health/ | head -n1
    curl -s https://socialnetwork.health/ | grep -o '<title>[^<]*</title>'

# full droplet bootstrap via Ansible (needs ops/ansible/inventory/hosts.ini — see ops/README.md)
provision:
    cd ops/ansible && ansible-playbook site.yml

# re-render the Caddy config only
provision-caddy:
    cd ops/ansible && ansible-playbook site.yml --tags caddy

# install the Ansible collections the playbook needs (one-time setup)
ansible-deps:
    cd ops/ansible && ansible-galaxy collection install -r collections/requirements.yml -p collections

# run a Slidev deck from presentations/ locally (opens localhost:3030)
slides deck="dwebcamp-berlin-2026/deck":
    cd presentations/{{deck}} && bun install && bun run dev

# --- org upkeep (see docs/org-upkeep.md) ---------------------------------------

# every org consistency check + what is NOT checked. Run this when you come back to the project
check-org:
    #!/usr/bin/env bash
    # Deliberately NOT `check-org: check-conventions check-skills` — just aborts on a failed
    # dependency, and the boundary note below matters most when something has failed.
    rc=0
    ./tools/org/sync_conventions.py || rc=1
    echo
    ./tools/org/org_skills.py || rc=1
    echo
    echo "--- what these checks do and don't cover ---------------------------------"
    echo "CHECKED   the shared CLAUDE.md block, on disk AND on each repo's origin/main"
    echo "CHECKED   org skills symlinked and unshadowed (this workstation only)"
    echo
    echo "NOT CHECKED - the PR is the gate:"
    echo "  * prime.md updated when a load-bearing doc or module lands"
    echo "  * the users guide updated when user-visible behavior changes"
    echo "  * dated files under plans/ left alone (append-only)"
    echo
    echo "NOT CHECKABLE - habits; they live in CLAUDE.md and nowhere else:"
    echo "  * --body-file over inline --body    * triage reds before shipping"
    echo "  * upstream main beats local plans   * fail loudly, honest deferrals"
    echo
    echo "A failing check above is a real signal - investigate it."
    echo "Full map: docs/org-upkeep.md"
    exit $rc

# is the shared CLAUDE.md block identical everywhere — on disk AND on main? (--disk-only skips network)
check-conventions:
    @./tools/org/sync_conventions.py

# propagate the canonical shared block to every working tree (then commit + PR each)
sync-conventions:
    @./tools/org/sync_conventions.py --write

# are the org's shared skills symlinked, current, and unshadowed on THIS workstation?
check-skills:
    @./tools/org/org_skills.py

# create or repair the ~/.claude/skills symlinks (run once per workstation)
install-skills:
    @./tools/org/org_skills.py --install
