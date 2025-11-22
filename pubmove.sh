#!/usr/bin/env bash

# pubmove.sh
# Moves a file from the mpr.drafts submodule to the base repository
# and cleanly removes it from the submodule

set -euo pipefail

# Configuration
SUBMODULE_PATH="content/mpr.drafts"
TARGET_PATH="content"
SUBMODULE_NAME="mpr.drafts"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Usage function
usage() {
    cat << EOF
Usage: $0 <filename>
       $0 undo <filename>

Commands:
  $0 <filename>       Move a file from the submodule to the base repository
  $0 undo <filename>  Undo a previous move operation (before pushing)

Arguments:
  filename    Name of the file to move/undo (relative to submodule root)

Examples:
  $0 my-post.md
  $0 undo my-post.md

Move operation:
  1. Copy the file from content/mpr.drafts/ to content/
  2. Remove the file from the submodule with a git commit
  3. Add the file to the base repository
  4. Update the submodule reference in the base repository

Undo operation:
  1. Unstage changes in the base repository
  2. Delete the copied file
  3. Reset the submodule to the previous commit
  4. Restore the file in the submodule
EOF
    exit 1
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
    local FILENAME="$1"
    local DEST_FILE="${TARGET_PATH}/${FILENAME}"

    verify_repo_root

    log_info "Starting undo process for: $FILENAME"

    # Step 1: Check if the file exists in base repository
    if [ ! -f "$DEST_FILE" ]; then
        log_warn "File not found in base repository: $DEST_FILE"
        log_warn "It may have already been removed or the move was never completed."
    fi

    # Step 2: Unstage changes in base repository
    log_info "Step 1: Unstaging changes in base repository"

    # Check if file is staged
    if git diff --cached --name-only | grep -q "^${DEST_FILE}$"; then
        git restore --staged "$DEST_FILE"
        log_info "Unstaged: $DEST_FILE"
    else
        log_warn "File was not staged: $DEST_FILE"
    fi

    # Check if submodule is staged
    if git diff --cached --name-only | grep -q "^${SUBMODULE_PATH}$"; then
        git restore --staged "$SUBMODULE_PATH"
        log_info "Unstaged: $SUBMODULE_PATH"
    else
        log_warn "Submodule was not staged"
    fi

    # Step 3: Delete the copied file
    if [ -f "$DEST_FILE" ]; then
        log_info "Step 2: Deleting copied file"
        rm "$DEST_FILE"
        log_info "Deleted: $DEST_FILE"
    fi

    # Step 4: Reset submodule to previous commit
    log_info "Step 3: Resetting submodule to previous commit"

    pushd "$SUBMODULE_PATH" > /dev/null

    # Get current and previous commit
    CURRENT_COMMIT=$(git rev-parse HEAD)
    PREVIOUS_COMMIT=$(git rev-parse HEAD~1)

    # Check if the last commit was a file removal
    LAST_COMMIT_MSG=$(git log -1 --pretty=%B)
    if [[ "$LAST_COMMIT_MSG" =~ "Remove ${FILENAME}" ]]; then
        log_info "Found removal commit: $LAST_COMMIT_MSG"
        git reset --hard HEAD~1
        NEW_COMMIT=$(git rev-parse HEAD)
        log_info "Submodule reset from $CURRENT_COMMIT to $NEW_COMMIT"

        # Verify file is back
        if [ -f "$FILENAME" ]; then
            log_info "File restored in submodule: $FILENAME"
        else
            log_error "File not found after reset. Manual intervention may be needed."
        fi
    else
        log_error "Last commit doesn't appear to be a file removal for $FILENAME"
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
    echo "  - File unstaged and deleted from base repository: $FILENAME"
    echo "  - Submodule reset to previous commit"
    echo "  - File restored in submodule: ${SUBMODULE_PATH}/${FILENAME}"
    echo ""
}

# Move function (original functionality)
move_file() {
    local FILENAME="$1"
    local SOURCE_FILE="${SUBMODULE_PATH}/${FILENAME}"
    local DEST_FILE="${TARGET_PATH}/${FILENAME}"

    verify_repo_root

    # Verify source file exists
    if [ ! -f "$SOURCE_FILE" ]; then
        log_error "Source file does not exist: $SOURCE_FILE"
        exit 1
    fi

    # Verify destination doesn't already exist
    if [ -f "$DEST_FILE" ]; then
        log_error "Destination file already exists: $DEST_FILE"
        log_warn "Remove or rename the existing file before running this script."
        exit 1
    fi

    # Verify submodule is initialized
    if [ ! -d "${SUBMODULE_PATH}/.git" ]; then
        log_error "Submodule not initialized. Run: git submodule update --init"
        exit 1
    fi

    log_info "Starting file move process for: $FILENAME"
    log_info "Source: $SOURCE_FILE"
    log_info "Destination: $DEST_FILE"

    # Step 1: Copy the file to the base repository
    log_info "Step 1: Copying file to base repository"
    cp "$SOURCE_FILE" "$DEST_FILE"

    if [ ! -f "$DEST_FILE" ]; then
        log_error "Failed to copy file"
        exit 1
    fi

    log_info "File copied successfully"

    # Step 2: Remove file from submodule and commit
    log_info "Step 2: Removing file from submodule"

    pushd "$SUBMODULE_PATH" > /dev/null

    # Check if there are any uncommitted changes in submodule
    if ! git diff-index --quiet HEAD --; then
        log_warn "Submodule has uncommitted changes. Stashing them."
        git stash push -m "Auto-stash before moving $FILENAME"
    fi

    # Remove the file
    git rm "$FILENAME"

    # Commit the removal
    COMMIT_MSG="Remove ${FILENAME} (moved to base repository)"
    git commit -m "$COMMIT_MSG"

    log_info "File removed from submodule and committed"

    # Get the new commit hash
    SUBMODULE_COMMIT=$(git rev-parse HEAD)
    log_info "Submodule now at commit: $SUBMODULE_COMMIT"

    popd > /dev/null

    # Step 3: Add file to base repository staging area
    log_info "Step 3: Adding file to base repository staging area"
    git add "$DEST_FILE"
    log_info "File added to staging area"

    # Step 4: Update submodule reference
    log_info "Step 4: Updating submodule reference"
    git add "$SUBMODULE_PATH"
    log_info "Submodule reference updated"

    # Step 5: Show status
    log_info "Step 5: Current git status"
    echo ""
    git status
    echo ""

    log_info "File move process completed successfully!"
    echo ""
    echo "Summary:"
    echo "  - File copied from submodule to base repository: $FILENAME"
    echo "  - File removed from submodule (committed)"
    echo "  - Submodule updated to commit: $SUBMODULE_COMMIT"
    echo ""
    echo "Next steps:"
    echo "  1. Review the changes with: git diff --cached"
    echo "  2. Commit the changes in the base repository with:"
    echo "     git commit -m 'Move ${FILENAME} from drafts submodule to main content'"
    echo "  3. Push the submodule changes:"
    echo "     cd ${SUBMODULE_PATH} && git push"
    echo "  4. Push the base repository changes:"
    echo "     git push"
    echo ""
    echo "To undo this operation (before pushing), run:"
    echo "  $0 undo $FILENAME"
    echo ""
}

# Main script logic - parse arguments
if [ $# -eq 0 ]; then
    echo -e "${RED}Error: Missing arguments${NC}"
    usage
fi

# Check for undo command
if [ "$1" = "undo" ]; then
    if [ $# -ne 2 ]; then
        echo -e "${RED}Error: undo command requires a filename${NC}"
        usage
    fi
    undo_move "$2"
else
    if [ $# -ne 1 ]; then
        echo -e "${RED}Error: Invalid arguments${NC}"
        usage
    fi
    move_file "$1"
fi
