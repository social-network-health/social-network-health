#!/usr/bin/env bash
# Configure Google sign-in for the team dashboard (dashboard.socialnetwork.health).
#
# Give it the OAuth client JSON you downloaded from Google Cloud Console (a "Web application"
# client whose redirect URI is https://dashboard.socialnetwork.health/oauth2/callback). It writes
# the client ID and secret, a fresh cookie secret, and any individually allowed Google accounts to
# the gitignored ops/ansible/secrets/dashboard-oauth.yml (mode 600). It never prints a secret.
# Then run `just provision-caddy`, and delete the downloaded JSON.
#
# Everything here is regenerable (new client secret in the console, new cookie secret by
# re-running), so it needs no backup.
#
# Usage: ./ops/dashboard-oauth.sh ~/Downloads/client_secret_XXXX.json
set -euo pipefail
cd "$(dirname "$0")/.."

json="${1:?usage: $0 path/to/client_secret.json}"
out=ops/ansible/secrets/dashboard-oauth.yml

echo "Anyone with a @socialnetwork.health Google account can sign in."
read -r -p "Other Google accounts to allow (comma-separated, or Enter for none): " extra

mkdir -p ops/ansible/secrets
umask 077
python3 - "$json" "$out" "$extra" <<'PY'
import json, secrets, base64, sys
src, out, extra = sys.argv[1], sys.argv[2], sys.argv[3]
web = json.load(open(src)).get("web")
if not web:
    sys.exit("That JSON has no 'web' section — create a *Web application* client, not Desktop.")
want = "https://dashboard.socialnetwork.health/oauth2/callback"
if want not in web.get("redirect_uris", []):
    sys.exit(f"The client's redirect URIs don't include {want} — add it in the console first.")
emails = [e.strip().lower() for e in extra.split(",") if e.strip()]
cookie = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode()
with open(out, "w") as f:
    f.write("# Written by ops/dashboard-oauth.sh. Gitignored. Google sign-in for the dashboard.\n")
    f.write(f"dashboard_oauth_client_id: {json.dumps(web['client_id'])}\n")
    f.write(f"dashboard_oauth_client_secret: {json.dumps(web['client_secret'])}\n")
    f.write(f"dashboard_oauth_cookie_secret: {json.dumps(cookie)}\n")
    f.write(f"dashboard_allowed_emails: {json.dumps(emails)}\n")
print(f"Wrote {out} (mode 600): client {web['client_id'][:12]}…, {len(emails)} extra account(s).")
PY
echo "Next: just provision-caddy   — then delete $json"
