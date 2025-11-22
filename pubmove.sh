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

Moves a file from the mpr.drafts submodule to the base repository.

Arguments:
  filename    Name of the file to move (relative to submodule root)

Example:
  $0 my-post.md

This script will:
  1. Copy the file from content/mpr.drafts/ to content/
  2. Remove the file from the submodule with a git commit
  3. Add the file to the base repository
  4. Update the submodule reference in the base repository
EOF
    exit 1
}

# Check if filename argument is provided
if [ $# -ne 1 ]; then
    echo -e "${RED}Error: Missing filename argument${NC}"
    usage
fi

FILENAME="$1"
SOURCE_FILE="${SUBMODULE_PATH}/${FILENAME}"
DEST_FILE="${TARGET_PATH}/${FILENAME}"

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
if [ ! -f ".gitmodules" ]; then
    log_error "Not in repository root. Please run from the root of the mpr repository."
    exit 1
fi

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
