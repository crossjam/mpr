#!/usr/bin/env bash

# pubmove.sh
# Moves a file from the mpr.drafts submodule to the base repository
# and cleanly removes it from the submodule

set -euo pipefail

# Configuration
SUBMODULE_PATH="content/mpr.drafts"
POSTS_SUBDIR="posts"  # Subdirectory within submodule containing posts
TARGET_PATH="content"
SUBMODULE_NAME="mpr.drafts"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Usage function
usage() {
    local exit_code=${1:-1}
    cat << EOF
Usage: $0 <path>
       $0 undo <path>
       $0 --help | -h

Commands:
  $0 <path>       Move a file or directory from the drafts submodule to the base repository
  $0 undo <path>  Undo a previous move operation (before pushing)
  $0 --help | -h  Display this help message

Arguments:
  path    Name of the file or directory to move/undo (from the posts directory)

Examples:
  $0 my-post.md
  $0 my-directory
  $0 undo my-post.md
  $0 undo my-directory

Move operation:
  1. Copy the file/directory from content/mpr.drafts/posts/ to content/
  2. Remove the file/directory from the submodule with a git commit
  3. Add the file/directory to the base repository
  4. Update the submodule reference in the base repository

Undo operation:
  1. Unstage changes in the base repository
  2. Delete the copied file/directory
  3. Reset the submodule to the previous commit
  4. Restore the file/directory in the submodule

Note: Files and directories are expected to be in the '${POSTS_SUBDIR}' subdirectory of the submodule.

Bash Completion:
  To enable tab completion for draft names, source the completion script:
    source pubmove-completion.bash

  Or add it to your shell profile (~/.bashrc or ~/.bash_profile):
    echo 'source /path/to/pubmove-completion.bash' >> ~/.bashrc

  Then you can use tab completion:
    $0 <TAB>              # Lists all available drafts and commands
    $0 my-<TAB>           # Completes draft names starting with 'my-'
    $0 undo <TAB>         # Lists all available drafts for undo
EOF
    exit "$exit_code"
}

# Logging functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verify we're in the repository root
verify_repo_root() {
    if [ ! -f ".gitmodules" ]; then
        log_error "Not in repository root. Please run from the root of the mpr repository."
        exit 1
    fi
}

# Undo function
undo_move() {
    local ITEM_NAME="$1"
    local DEST_ITEM="${TARGET_PATH}/${ITEM_NAME}"

    verify_repo_root

    log_info "Starting undo process for: $ITEM_NAME"

    # Step 1: Check if the item exists in base repository
    if [ ! -e "$DEST_ITEM" ]; then
        log_warn "Item not found in base repository: $DEST_ITEM"
        log_warn "It may have already been removed or the move was never completed."
    fi

    # Step 2: Unstage changes in base repository
    log_info "Step 1: Unstaging changes in base repository"

    # Check if item is staged (works for both files and directories)
    if git diff --cached --name-only | grep -q "^${DEST_ITEM}"; then
        git restore --staged "$DEST_ITEM"
        log_info "Unstaged: $DEST_ITEM"
    else
        log_warn "Item was not staged: $DEST_ITEM"
    fi

    # Check if submodule is staged
    if git diff --cached --name-only | grep -q "^${SUBMODULE_PATH}$"; then
        git restore --staged "$SUBMODULE_PATH"
        log_info "Unstaged: $SUBMODULE_PATH"
    else
        log_warn "Submodule was not staged"
    fi

    # Step 3: Delete the copied item
    if [ -e "$DEST_ITEM" ]; then
        log_info "Step 2: Deleting copied item"
        if [ -d "$DEST_ITEM" ]; then
            rm -rf "$DEST_ITEM"
            log_info "Deleted directory: $DEST_ITEM"
        else
            rm "$DEST_ITEM"
            log_info "Deleted file: $DEST_ITEM"
        fi
    fi

    # Step 4: Reset submodule to previous commit
    log_info "Step 3: Resetting submodule to previous commit"

    pushd "$SUBMODULE_PATH" > /dev/null

    # Get current and previous commit
    CURRENT_COMMIT=$(git rev-parse HEAD)
    PREVIOUS_COMMIT=$(git rev-parse HEAD~1)

    # Check if the last commit was an item removal
    LAST_COMMIT_MSG=$(git log -1 --pretty=%B)
    if [[ "$LAST_COMMIT_MSG" =~ "Remove ${POSTS_SUBDIR}/${ITEM_NAME}" ]]; then
        log_info "Found removal commit: $LAST_COMMIT_MSG"
        git reset --hard HEAD~1
        NEW_COMMIT=$(git rev-parse HEAD)
        log_info "Submodule reset from $CURRENT_COMMIT to $NEW_COMMIT"

        # Verify item is back
        if [ -e "${POSTS_SUBDIR}/${ITEM_NAME}" ]; then
            log_info "Item restored in submodule: ${POSTS_SUBDIR}/${ITEM_NAME}"
        else
            log_error "Item not found after reset. Manual intervention may be needed."
        fi
    else
        log_error "Last commit doesn't appear to be an item removal for ${POSTS_SUBDIR}/${ITEM_NAME}"
        log_error "Last commit message: $LAST_COMMIT_MSG"
        log_warn "Aborting undo to prevent data loss. Please manually verify."
        popd > /dev/null
        exit 1
    fi

    popd > /dev/null

    # Step 5: Show status
    log_info "Step 4: Current git status"
    echo ""
    git status
    echo ""

    log_info "Undo completed successfully!"
    echo ""
    echo "Summary:"
    echo "  - Item unstaged and deleted from base repository: $ITEM_NAME"
    echo "  - Submodule reset to previous commit"
    echo "  - Item restored in submodule: ${SUBMODULE_PATH}/${POSTS_SUBDIR}/${ITEM_NAME}"
    echo ""
}

# Move function (handles both files and directories)
move_item() {
    local ITEM_NAME="$1"
    local SOURCE_ITEM="${SUBMODULE_PATH}/${POSTS_SUBDIR}/${ITEM_NAME}"
    local DEST_ITEM="${TARGET_PATH}/${ITEM_NAME}"

    verify_repo_root

    # Verify source item exists
    if [ ! -e "$SOURCE_ITEM" ]; then
        log_error "Source item does not exist: $SOURCE_ITEM"
        log_error "Looking for items in: ${SUBMODULE_PATH}/${POSTS_SUBDIR}/"
        exit 1
    fi

    # Verify destination doesn't already exist
    if [ -e "$DEST_ITEM" ]; then
        log_error "Destination item already exists: $DEST_ITEM"
        log_warn "Remove or rename the existing item before running this script."
        exit 1
    fi

    # Verify submodule is initialized
    if [ ! -e "${SUBMODULE_PATH}/.git" ]; then
        log_error "Submodule not initialized. Run: git submodule update --init"
        exit 1
    fi

    # Determine if we're moving a file or directory
    local ITEM_TYPE="file"
    if [ -d "$SOURCE_ITEM" ]; then
        ITEM_TYPE="directory"
    fi

    log_info "Starting $ITEM_TYPE move process for: $ITEM_NAME"
    log_info "Source: $SOURCE_ITEM"
    log_info "Destination: $DEST_ITEM"

    # Step 1: Copy the item to the base repository
    log_info "Step 1: Copying $ITEM_TYPE to base repository"
    if [ "$ITEM_TYPE" = "directory" ]; then
        cp -r "$SOURCE_ITEM" "$DEST_ITEM"
    else
        cp "$SOURCE_ITEM" "$DEST_ITEM"
    fi

    if [ ! -e "$DEST_ITEM" ]; then
        log_error "Failed to copy $ITEM_TYPE"
        exit 1
    fi

    log_info "$(echo "$ITEM_TYPE" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}') copied successfully"

    # Step 2: Remove item from submodule and commit
    log_info "Step 2: Removing $ITEM_TYPE from submodule"

    pushd "$SUBMODULE_PATH" > /dev/null

    # Check if there are any uncommitted changes in submodule
    if ! git diff-index --quiet HEAD --; then
        log_warn "Submodule has uncommitted changes. Stashing them."
        git stash push -m "Auto-stash before moving $ITEM_NAME"
    fi

    # Remove the item (path relative to submodule root)
    if [ "$ITEM_TYPE" = "directory" ]; then
        git rm -r "${POSTS_SUBDIR}/${ITEM_NAME}"
    else
        git rm "${POSTS_SUBDIR}/${ITEM_NAME}"
    fi

    # Commit the removal
    COMMIT_MSG="Remove ${POSTS_SUBDIR}/${ITEM_NAME} (moved to base repository)"
    git commit -m "$COMMIT_MSG"

    log_info "$(echo "$ITEM_TYPE" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}') removed from submodule and committed"

    # Get the new commit hash
    SUBMODULE_COMMIT=$(git rev-parse HEAD)
    log_info "Submodule now at commit: $SUBMODULE_COMMIT"

    popd > /dev/null

    # Step 3: Add item to base repository staging area
    log_info "Step 3: Adding $ITEM_TYPE to base repository staging area"
    git add "$DEST_ITEM"
    log_info "$(echo "$ITEM_TYPE" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}') added to staging area"

    # Step 4: Update submodule reference
    log_info "Step 4: Updating submodule reference"
    git add "$SUBMODULE_PATH"
    log_info "Submodule reference updated"

    # Step 5: Show status
    log_info "Step 5: Current git status"
    echo ""
    git status
    echo ""

    log_info "$(echo "$ITEM_TYPE" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}') move process completed successfully!"
    echo ""
    echo "Summary:"
    echo "  - $(echo "$ITEM_TYPE" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}') copied from submodule to base repository: $ITEM_NAME"
    echo "  - $(echo "$ITEM_TYPE" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}') removed from submodule (committed)"
    echo "  - Submodule updated to commit: $SUBMODULE_COMMIT"
    echo ""
    echo "Next steps:"
    echo "  1. Review the changes with: git diff --cached"
    echo "  2. Commit the changes in the base repository with:"
    echo "     git commit -m 'Move ${ITEM_NAME} from drafts submodule to main content'"
    echo "  3. Push the submodule changes:"
    echo "     cd ${SUBMODULE_PATH} && git push"
    echo "  4. Push the base repository changes:"
    echo "     git push"
    echo ""
    echo "To undo this operation (before pushing), run:"
    echo "  $0 undo $ITEM_NAME"
    echo ""
}

# Main script logic - parse arguments
if [ $# -eq 0 ]; then
    echo -e "${RED}Error: Missing arguments${NC}"
    usage 1
fi

# Check for help flag
if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    usage 0
fi

# Check for undo command
if [ "$1" = "undo" ]; then
    if [ $# -ne 2 ]; then
        echo -e "${RED}Error: undo command requires a path${NC}"
        usage 1
    fi
    undo_move "$2"
else
    if [ $# -ne 1 ]; then
        echo -e "${RED}Error: Invalid arguments${NC}"
        usage 1
    fi
    move_item "$1"
fi
