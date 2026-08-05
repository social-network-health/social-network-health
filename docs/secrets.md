# Secrets

How the org stores and delivers secrets to the sites it runs. This document owns the
convention; individual repos link here rather than restating it.

Written 2026-08-05, prompted by the toolkit wiki move. It generalises what
`fellows_local_db` already half-does and fixes the gap that makes its secrets need periodic
re-setting.

## The problem, stated honestly

The org runs a growing number of DigitalOcean droplets. Today, machine secrets are set as
environment variables on the server by a one-off script, and **the server is the only place
those values live**.

Concretely, in `fellows_local_db`: `scripts/configure_email_auth_env.sh` (via
`just prod-configure-env`) writes `/etc/fellows/fellows-pwa.env`. Ansible does **not** create
that file — it only corrects ownership and mode, and only `when: fellows_env_stat.stat.exists`.
There is also a `repair_email_auth_env.sh` for when the file goes malformed.

Nothing off-box is the source of truth, so rebuilding the droplet loses the values and no
recipe can restore them. That is a missing-source-of-truth problem, not a storage-technology
problem, and it is worth being clear about which one you are solving.

There is also history. `../socialnetwork_toolkit` has live credentials committed to its git
history because that was the only channel available for sharing them with a contractor. Any
convention here has to have an obvious right answer for *"how do I give a collaborator access"*,
or the same thing happens again.

## Classify before you store

Treating every secret the same is what makes this feel bigger than it is. The useful test is:

> **Can this be regenerated without losing anything?**

| | Test | Where it lives | Examples |
|---|---|---|---|
| **1. Regenerable** | Regenerate freely; nothing is lost | **Nowhere.** Generated on the box by the playbook, written straight into the file that consumes it, never printed | DB passwords, `$wgSecretKey`, `$wgUpgradeKey`, `FELLOWS_SESSION_SECRET`, `FELLOWS_ALLOWLIST_HMAC_KEY` |
| **2. Not regenerable** | Losing it loses something | **The store** (below) | Postmark server token, B2 key pair, restic repository password |
| **3. Human, interactive** | A person types it, usually with MFA | Personal password manager — unchanged, out of scope | DigitalOcean, Cloudflare, Linode, Google Workspace, GitHub |
| **4. Per-person delegated** | Each person mints their own | That person's own machine; **never centralised** | MediaWiki bot passwords |

Two of these classifications carry most of the value.

**Category 1 should not be managed at all.** A secret nobody ever needs to read cannot leak
through a human channel, cannot go stale in a password manager, and cannot be shared by
accident. Generate it on the box, guard the task so it does not churn on re-runs, `no_log: true`,
and never store it anywhere. Rotation is deletion plus a re-run.

**Category 4 is the structural fix for the sharing problem.** With per-person credentials there
is *nothing to share*, so the failure mode that produced committed credentials has no way to
recur.

Note where the restic repository password lands. It is locally *generated*, so it looks like
category 1 — but losing it makes every existing backup permanently unreadable. **The test is
consequence, not origin.** Getting this one wrong is expensive and silent.

Applying the test leaves very little to actually store: the toolkit wiki has **three** values
(Postmark token, B2 key pair, restic password) and `fellows_local_db` has **one**
(`FELLOWS_POSTMARK_TOKEN`) — its session and allowlist keys are category 1 and should never have
required management.

## The store: `age`-encrypted files in `snh-private`

Category-2 secrets live in an [`age`](https://github.com/FiloSottile/age)-encrypted vars file
per site, committed to the **private** `snh-private` repo, decrypted at play time by a `just`
recipe that pipes it into `ansible-playbook --extra-vars`. It is never written unencrypted to
disk on the workstation.

Your personal password manager then holds exactly **one** new item: the passphrase to your `age`
identity. That is a category-3 human secret — the kind already handled well.

### Why this and not the alternatives

**Not `ansible-vault` committed to the site repo.** Most of the org's repos are *public*. An
encrypted blob in a public repo is cryptographically defensible and is nonetheless exactly the
shape of the thing that caused the existing exposure. A single shared vault password is also
all-or-nothing: you cannot grant one secret without granting all of them.

**Not the password manager's CLI read directly by Ansible.** Cleaner in theory — one source of
truth, no second copy — but it welds provisioning to a specific vendor. The org is currently on
Dashlane and considering Bitwarden; `age` is format-neutral, so that decision stays reversible
and is not forced by an infrastructure choice.

**`age` gives a real collaborator path.** Granting access is *adding someone's public key and
re-encrypting*. No secret is ever transmitted. Revoking is re-encrypting without their key.
That is a direct answer to the question that produced the original incident.

`snh-private` is already the org's proven channel for private things that follow a developer
between machines.

**Cost, stated plainly:** one new tool, a single small binary. If per-value diffs ever matter,
`sops` is the upgrade path; whole-file encryption is fine at three values.

## Delivery: the playbook owns the file

Every droplet app gets:

- `/etc/<app>/<app>.env` — owner `root`, group the service user, mode `0640`, **created and
  owned by the playbook**
- a systemd drop-in pointing `EnvironmentFile=` at it

This is not a new pattern. It is the pattern `fellows_local_db` already uses at runtime,
finished so that the automation owns it. Once the playbook creates the file, *"reset the env
vars once in a while"* becomes *"re-run `just provision`"*.

Applications that read PHP config rather than the environment — MediaWiki, for instance — take
the same approach with their own config file: root-owned, group-readable by php-fpm, written by
the playbook, never in git.

## Verify it, or the rule is a wish

The org rule is that anything which must hold in more than one place ships with a command that
checks it. For secrets that command is **`just check-secrets`**, per repo.

It asserts that every required key is present and non-empty on the box, with the expected owner
and mode. It prints **names only, never values**.

Today a missing Postmark token is discovered when mail silently stops. This converts that into
a loud failure, which is the org's "fail loudly" rule applied to configuration.

## Adding a new site

1. List its secrets and classify each one with the regenerable test.
2. Category 1 → a playbook task that generates on the box, guarded against churn, `no_log: true`.
3. Category 2 → add to that site's `age` file in `snh-private`.
4. Category 3 → personal password manager, as before.
5. Category 4 → document how each person mints their own; do not centralise.
6. Add the site's required-key list to its `just check-secrets`.

## Known gap

`fellows_local_db` predates this convention and does not yet follow it: its env file is written
by a script rather than the playbook, and its category-1 secrets are still hand-managed. The
retrofit is tracked in [`../plans/ORG-TASKS.md`](../plans/ORG-TASKS.md).
