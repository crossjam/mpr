#!/usr/bin/env bash
# Bash completion for pubmove.sh

_pubmove_completion() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # Configuration (should match pubmove.sh)
    # Safety check: ensure required environment variables are set
    if [ -z "${SUBMODULE_PATH}" ] || [ -z "${POSTS_SUBDIR}" ]; then
        # If environment variables are not set, only offer basic commands
        echo "Warning: SUBMODULE_PATH and/or POSTS_SUBDIR not set. Draft completion unavailable." >&2
        local commands="undo --help -h"
        if [ $COMP_CWORD -eq 1 ]; then
            COMPREPLY=( $(compgen -W "$commands" -- "$cur") )
        fi
        return 0
    fi

    local DRAFTS_PATH="${SUBMODULE_PATH}/${POSTS_SUBDIR}"

    # Get the script name (could be ./pubmove.sh or just pubmove.sh)
    local script="${COMP_WORDS[0]}"

    # If we're at the first argument position
    if [ $COMP_CWORD -eq 1 ]; then
        # Offer 'undo' and '--help' as options, plus all draft items
        local commands="undo --help -h"

        # Add draft items if the drafts directory exists
        if [ -d "$DRAFTS_PATH" ]; then
            local draft_items=$(cd "$DRAFTS_PATH" 2>/dev/null && ls -A1 2>/dev/null | grep -v '^\.\.\?$')
            opts="$commands $draft_items"
        else
            opts="$commands"
        fi

        COMPREPLY=( $(compgen -W "$opts" -- "$cur") )
        return 0
    fi

    # If we're at the second argument and previous was 'undo'
    if [ $COMP_CWORD -eq 2 ] && [ "$prev" = "undo" ]; then
        # Only complete with items that exist in the drafts directory
        if [ -d "$DRAFTS_PATH" ]; then
            local draft_items=$(cd "$DRAFTS_PATH" 2>/dev/null && ls -A1 2>/dev/null | grep -v '^\.\.\?$')
            COMPREPLY=( $(compgen -W "$draft_items" -- "$cur") )
        fi
        return 0
    fi

    return 0
}

# Register the completion function
complete -F _pubmove_completion pubmove.sh
complete -F _pubmove_completion ./pubmove.sh
