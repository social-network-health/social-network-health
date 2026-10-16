#!/usr/bin/env bash
# Set the team dashboard's shared password (dashboard.socialnetwork.health).
#
# Prompts twice with input hidden and stores only a bcrypt hash, in the gitignored
# ops/ansible/secrets/dashboard.yml. The password itself is never written anywhere: share it with
# the team through a channel you trust. Then run `just provision-caddy` to apply it.
#
# A bridge until the dashboard moves to Google sign-in. The password is regenerable, so it needs
# no backup: lose it and run this again.
#
# Usage: ./ops/dashboard-password.sh [user]     (default user: snh)
set -euo pipefail
cd "$(dirname "$0")/.."

user="${1:-snh}"
out=ops/ansible/secrets/dashboard.yml

command -v htpasswd >/dev/null || {
  echo "needs htpasswd (macOS has it; on Debian/Ubuntu: apt install apache2-utils)" >&2; exit 1; }

line="$(htpasswd -nB -C 12 "$user")"   # prompts twice; prints user:hash
hash="${line#*:}"
[[ "$hash" == \$2* ]] || { echo "htpasswd did not return a bcrypt hash; nothing written" >&2; exit 1; }

mkdir -p ops/ansible/secrets
umask 077
cat > "$out" <<YAML
# Written by ops/dashboard-password.sh. Gitignored. A bcrypt hash, not the password.
dashboard_auth_user: "$user"
dashboard_auth_hash: "$hash"
YAML
echo "Wrote $out (mode 600). Apply it with: just provision-caddy"
