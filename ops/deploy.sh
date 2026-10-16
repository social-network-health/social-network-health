#!/usr/bin/env bash
# Deploy the socialnetwork.health static site to the droplet.
#
# The site is exactly three files from public/:
#   socialnetwork-health.html                  -> index.html (served at /)
#   privacy.html                               -> privacy.html (served at /privacy)
#   78e65dce-3229-46b0-be38-02da250aaddc.svg   -> favicon/logo (referenced at web root)
#
# The site root and operator ownership are provisioned by ops/ansible (caddy
# role), so this rsyncs in as the operator with no sudo. Mirrors the pattern in
# ../globaldonut/deploy.sh.
#
# Usage:
#   SNH_HOST=rsb@<droplet-or-reserved-ip> ./ops/deploy.sh
# or edit the default below once the droplet exists.
set -euo pipefail

HOST="${SNH_HOST:-rsb@170.64.248.173}"
PORT="${SNH_PORT:-22}"
DEST="${SNH_DEST:-/var/www/socialnetwork.health/}"

if [[ "$HOST" == *REPLACE_WITH_* ]]; then
  echo "Set SNH_HOST=rsb@<droplet-ip> (or edit ops/deploy.sh). Aborting." >&2
  exit 1
fi

cd "$(dirname "$0")/.."   # repo root

# Stage the files under their served names, then rsync --delete so the site
# root contains exactly these files.
stage="$(mktemp -d)"
trap 'rm -rf "$stage"' EXIT
cp public/socialnetwork-health.html "$stage/index.html"
cp public/privacy.html "$stage/"
cp public/78e65dce-3229-46b0-be38-02da250aaddc.svg "$stage/"

# Force sane perms on the staged tree so rsync -a propagates them to the site
# root. mktemp dirs are 0700; without this the caddy user (which serves the
# files) couldn't read or traverse the site root. (Avoids rsync --chmod, which
# the older macOS rsync rejects.)
chmod 755 "$stage"
chmod 644 "$stage"/*

rsync -avz --delete -e "ssh -p ${PORT}" "$stage/" "${HOST}:${DEST}"

echo "Deployed to ${HOST}:${DEST}"
