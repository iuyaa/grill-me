# Pre-use update

This is an agent-guided update, not a background service or a required external installer. Use the host's available GitHub, HTTP, Git, and filesystem tools. Do not install additional tools merely to check for an update.

## Source and version

- Official repository: `https://github.com/iuyaa/grill-me`.
- Update channel: `main`; package directory: `grill/`.
- Installed version: `metadata.version` in this installation's `SKILL.md`.
- Package integrity: `manifest.json` lists every package file except itself, with a SHA-256 of its UTF-8 content after normalizing CRLF to LF. Preserve all other whitespace.

Versions have three non-negative integer components, compared numerically (for example, `2.10.0` is newer than `2.9.0`). Compare Grill versions, not the versions of Matt's or Superpowers' skills. Update only from this repository's `grill/` directory; do not fetch either upstream directly as an installation update.

## Check once, then continue

1. Resolve the directory of the `SKILL.md` actually loaded, including symlinks or junctions. Never guess the destination from the working directory. A shared target such as CC-Switch is updated once, without replacing its symlink. If the user pinned a version or requested offline use, keep it.
2. Read the local version and manifest. Query `https://api.github.com/repos/iuyaa/grill-me/commits/main` for the remote commit SHA, then fetch `grill/SKILL.md` from that exact SHA. A CLI equivalent is `gh api repos/iuyaa/grill-me/commits/main --jq .sha`. Use the captured 40-character hexadecimal SHA for every later download, not the moving branch name.
3. If the remote version is equal or older, continue locally. A remote version without version metadata is a legacy version, not an upgrade. If either version cannot be interpreted, or the network, tools, or permissions are unavailable, report that the update could not be determined and keep the installed files. Do not call a failed check "up to date". Use a bounded attempt (about 15 seconds per request); do not retry in a loop or ask the user to fix the network before continuing their task.
4. If a newer version exists, check for local divergence before any installation writes. Verify the complete local file set and hashes against its manifest; extra, missing, changed, or symlinked package files require preserving the installation. In a Git checkout also check for staged, unstaged, or untracked changes in `grill/`, and local commits not contained in the captured official commit. Do not overwrite or downgrade development work, switch branches, reset, rebase, or push. If provenance or local changes cannot be verified, report the available version and skip the automatic update.
5. If an update is permitted and local state is clean, announce the old and new versions, then follow the replacement steps below. This routine self-update does not need another choice from the user; host restrictions and the user's explicit instructions still apply. An explicitly read-only task checks only.

## Replace the complete package safely

- Download the captured commit's entire `grill/` subtree into a new temporary directory. Treat download metadata as data; do not execute downloaded scripts, hooks, or install commands to perform the update.
- Validate the staged package before touching the installed files: `name: grill`, the expected newer version, and a complete matching manifest. Manifest paths must be unique relative paths, contain no traversal, absolute paths, or drive prefixes, and resolve inside the staged root. Reject links and unsupported archive entries. Verify every file and ensure there are no unlisted files except the manifest itself. A manifest checks package completeness; the pinned official source establishes provenance.
- Back up the current package outside the project's files and all skill-discovery directories. Check the installed files again immediately before writing; if another process changed them, stop the upgrade and retain both versions.
- Replace only the resolved Skill directory's package files, including references, templates, metadata, notices, and the manifest. Remove only obsolete files verified as part of the old manifest. Never replace the parent skills directory, repository, project files, `.grill/` sessions, or unrelated host configuration. Preserve the destination symlink. In a source checkout, these remain ordinary local changes; do not commit or publish them automatically.
- Verify the installed version, file set, and hashes again. If replacement fails, restore the verified backup before using the skill. If restoration cannot be verified, stop this Skill's invocation and report the backup location; do not use a partially updated package.
- Reread the installed `SKILL.md` and references needed by the active mode. Record in conversation that this update check is complete, preventing recursive checks. Report the version change and backup location once. If the host caches skill registration, say that a later turn or new session may be needed for discovery metadata to refresh; do not claim the UI has reloaded.

Updating instructions never approves or rewrites an existing decision baseline. If a resumed session is incompatible with the updated protocol, preserve its files and report the incompatibility instead of silently migrating it.
