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
    curl -s https://socialnetwork.health/privacy | grep -o '<title>[^<]*</title>'

# full droplet bootstrap via Ansible (needs ops/ansible/inventory/hosts.ini — see ops/README.md)
provision:
    cd ops/ansible && ansible-playbook site.yml

# re-render the Caddy config only
provision-caddy:
    cd ops/ansible && ansible-playbook site.yml --tags caddy

# set up Google sign-in for the team dashboard from a downloaded OAuth client JSON; then provision-caddy
dashboard-oauth json:
    ./ops/dashboard-oauth.sh {{json}}

# set the team dashboard's shared password (stores only a hash, gitignored); then run provision-caddy
dashboard-password user="snh":
    ./ops/dashboard-password.sh {{user}}

# install or update the team dashboard's hourly rebuild from snh-aios main
provision-dashboard-sync:
    cd ops/ansible && ansible-playbook site.yml --tags dashboard_sync

# register the droplet's deploy key on snh-aios, read-only (once, after provision-dashboard-sync)
dashboard-sync-key:
    #!/usr/bin/env bash
    set -euo pipefail
    key="$(ssh "${SNH_HOST:-rsb@170.64.248.173}" cat .ssh/snh-aios-deploy.pub)"
    if gh repo deploy-key list --repo social-network-health/snh-aios --json key --jq '.[].key' \
        | grep -qF "$(cut -d' ' -f2 <<<"$key")"; then
      echo "Already registered."
    else
      tmp="$(mktemp)"; trap 'rm -f "$tmp"' EXIT
      echo "$key" > "$tmp"
      gh repo deploy-key add "$tmp" --repo social-network-health/snh-aios --title "droplet: hourly dashboard sync"
    fi

# when the dashboard last synced, when it next will, and the last run's output
dashboard-sync-status:
    ssh "${SNH_HOST:-rsb@170.64.248.173}" 'systemctl list-timers snh-dashboard-sync.timer --no-pager; journalctl -u snh-dashboard-sync -n 15 --no-pager -q'

# install or update listmonk (updates.socialnetwork.health) and its Caddy site (restarts Caddy: brief blip)
provision-updates:
    cd ops/ansible && ansible-playbook site.yml --tags listmonk,caddy

# listmonk's admin, through an SSH tunnel (it never faces the internet); Ctrl-C closes it
updates-admin:
    @echo "listmonk admin: http://localhost:9000/admin — Ctrl-C closes the tunnel"
    ssh -N -L 9000:127.0.0.1:9000 "${SNH_HOST:-rsb@170.64.248.173}"

# whether listmonk and its nightly backup are running, and listmonk's last log lines
updates-status:
    ssh "${SNH_ROOT:-root@170.64.248.173}" 'systemctl is-active listmonk; systemctl list-timers listmonk-backup.timer --no-pager; ls -lh /var/backups/listmonk | tail -3; journalctl -u listmonk -n 15 --no-pager -q'

# install the Ansible collections the playbook needs (one-time setup)
ansible-deps:
    cd ops/ansible && ansible-galaxy collection install -r collections/requirements.yml -p collections

# run a Slidev deck from presentations/ locally (opens localhost:3030)
slides deck="dwebcamp-berlin-2026/deck":
    cd presentations/{{deck}} && bun install && bun run dev

# --- org at a glance -----------------------------------------------------------

# the org task list (planning layer 2) — what the whole org should be doing
dashboard:
    @cat plans/ORG-TASKS.md

# every open PR across every repo in the org, grouped, with links
prs:
    @./tools/org/open_prs.py

# just the PR URLs, one per line — pipe somewhere, or `just prs-urls | xargs open`
prs-urls:
    @./tools/org/open_prs.py --urls

# --- org upkeep (see docs/org-upkeep.md) ---------------------------------------

# clone/refresh every org repo + install skills. New workstation, or any time you want everything current
bootstrap:
    @./tools/org/bootstrap.py

# show what bootstrap would do without changing anything
bootstrap-dry:
    @./tools/org/bootstrap.py --dry-run

# every org consistency check + what is NOT checked. Run this when you come back to the project
check-org:
    #!/usr/bin/env bash
    # Deliberately NOT `check-org: check-conventions check-skills` — just aborts on a failed
    # dependency, and the boundary note below matters most when something has failed.
    rc=0
    ./tools/org/sync_conventions.py || rc=1
    echo
    ./tools/org/agent_files.py --no-fetch || rc=1
    echo
    ./tools/org/org_skills.py || rc=1
    echo
    echo "--- what these checks do and don't cover ---------------------------------"
    echo "CHECKED   the shared block in each AGENTS.md, on disk AND on each repo's origin/main"
    echo "CHECKED   AGENTS.md size, the one-line CLAUDE.md, skills and their links (disk + main)"
    echo "CHECKED   org skills symlinked for every agent and unshadowed (this workstation only)"
    echo
    echo "NOT CHECKED - the PR is the gate:"
    echo "  * the prime skill updated when a load-bearing doc or module lands"
    echo "  * the users guide updated when user-visible behavior changes"
    echo "  * dated files under plans/ left alone (append-only)"
    echo
    echo "NOT CHECKABLE - habits; they live in AGENTS.md and nowhere else:"
    echo "  * --body-file over inline --body    * triage reds before shipping"
    echo "  * upstream main beats local plans   * fail loudly, honest deferrals"
    echo
    echo "A failing check above is a real signal - investigate it."
    echo "Full map: docs/org-upkeep.md"
    exit $rc

# is the shared block identical in every AGENTS.md — on disk AND on main? (--disk-only skips network)
check-conventions:
    @./tools/org/sync_conventions.py

# propagate the canonical shared block to every working tree (then commit + PR each)
sync-conventions:
    @./tools/org/sync_conventions.py --write

# does every repo keep its agent files right — AGENTS.md, the one-line CLAUDE.md, skill links?
check-agent-files:
    @./tools/org/agent_files.py

# are the org's shared skills symlinked, current, and unshadowed on THIS workstation?
check-skills:
    @./tools/org/org_skills.py

# create or repair the org skill symlinks for every agent (run once per workstation)
install-skills:
    @./tools/org/org_skills.py --install

# validate stable organization task IDs and state/checkbox consistency
check-tasks:
    python3 tools/org/check_task_ids.py
