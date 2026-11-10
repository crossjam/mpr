#!/usr/bin/env bash

# install-draft-hooks.sh
# Adds draft-branch guards to this clone's git hooks:
#
#   pre-push     refuses to push draft/* branches anywhere except the
#                private drafts remote, since origin is public
#   post-commit  skips automatic review of commits on draft/* branches
#
# The guards are inserted as marked blocks right after the shebang, so
# hooks installed by other tools keep working. Re-running is safe, and
# draftpost.py runs this on every invocation in case another tool has
# rewritten a hook since.

set -euo pipefail

# Substring that identifies the private drafts repository's URL
DRAFTS_URL_PATTERN="crossjam/mpr.drafts"

MARK_BEGIN="# >>> mpr draft guard >>>"
MARK_END="# <<< mpr draft guard <<<"

HOOKS_DIR="$(git rev-parse --git-common-dir)/hooks"

pre_push_block() {
    cat << EOF
$MARK_BEGIN
# Refuse to send draft/* branches to any remote but the private drafts repo
case "\$2" in
    *$DRAFTS_URL_PATTERN*) ;;
    *)
        while read -r local_ref _ remote_ref _; do
            case "\$local_ref \$remote_ref" in
                refs/heads/draft/*|*" refs/heads/draft/"*)
                    echo "pre-push: refusing to push \$local_ref to \$1 (\$2)." >&2
                    echo "pre-push: draft branches belong on the drafts remote: git push drafts <branch>" >&2
                    exit 1
                    ;;
            esac
        done
        ;;
esac
$MARK_END
EOF
}

post_commit_block() {
    cat << EOF
$MARK_BEGIN
# Draft prose stays private: no automatic review on draft/* branches
case "\$(git symbolic-ref --short -q HEAD)" in
    draft/*) exit 0 ;;
esac
$MARK_END
EOF
}

# Insert or refresh the guard block in one hook file
install_block() {
    local hook="$1" block="$2"
    local path="$HOOKS_DIR/$hook"
    local stripped tmp
    stripped="$(mktemp)"
    tmp="$(mktemp)"

    if [ ! -f "$path" ]; then
        printf '#!/bin/sh\n' > "$path"
    fi

    # Drop any previous copy of the block, then re-add it after the shebang
    awk -v b="$MARK_BEGIN" -v e="$MARK_END" '
        $0 == b {skip=1; next}
        $0 == e {skip=0; next}
        !skip
    ' "$path" > "$stripped"

    if head -n 1 "$stripped" | grep -q '^#!'; then
        { head -n 1 "$stripped"; printf '%s\n' "$block"; tail -n +2 "$stripped"; } > "$tmp"
    else
        { printf '#!/bin/sh\n%s\n' "$block"; cat "$stripped"; } > "$tmp"
    fi
    rm -f "$stripped"

    if ! cmp -s "$tmp" "$path"; then
        cat "$tmp" > "$path"
        echo "Updated draft guard in $path"
    fi
    rm -f "$tmp"
    chmod +x "$path"
}

install_block pre-push "$(pre_push_block)"
install_block post-commit "$(post_commit_block)"
