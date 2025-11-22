# Publishing from Drafts: Script Approach

## Problem

Moving content from the `mpr.drafts` git submodule to the main repository requires coordinating changes across two separate git repositories while maintaining clean history in both.

## Solution Approach

The `pubmove.sh` script automates the multi-step workflow for publishing posts from the drafts submodule:

### 1. Validation Phase
- Verify execution from repository root
- Confirm source file exists in submodule's `posts/` directory
- Check destination doesn't already exist
- Ensure submodule is properly initialized

### 2. File Transfer
- Copy file from `content/mpr.drafts/posts/` to `content/`
- Preserve file contents exactly as-is

### 3. Submodule Cleanup
- Enter submodule context
- Stage file removal with `git rm`
- Commit the deletion to submodule history
- Capture new submodule commit hash

### 4. Base Repository Update
- Stage the new file in base repository
- Stage the updated submodule reference
- Present status for user review

### 5. User Guidance
- Display clear summary of changes
- Provide exact commands for final commit and push
- Separate submodule and base repository push instructions

## Design Principles

**Safety First**: Multiple validation checks prevent destructive operations. Uncommitted submodule changes are automatically stashed.

**Atomic Operations**: Each git operation is discrete and reversible. The script stops before final commits, letting users review changes.

**Clear Feedback**: Color-coded output distinguishes info, warnings, and errors. Summary shows exactly what happened and what's next.

**Single Responsibility**: Script handles the mechanical coordination. Users retain control over final commit messages and push timing.

## Configuration

The script can be configured for different submodule paths and subdirectories by editing the configuration variables at the top of `pubmove.sh`:

```bash
# Configuration
SUBMODULE_PATH="content/mpr.drafts"
POSTS_SUBDIR="posts"  # Subdirectory within submodule containing posts
TARGET_PATH="content"
SUBMODULE_NAME="mpr.drafts"
```

### Configuration Variables

| Variable | Description | Default Value | Example Alternative |
|----------|-------------|---------------|---------------------|
| `SUBMODULE_PATH` | Path to the submodule directory | `content/mpr.drafts` | `drafts` or `content/blog-drafts` |
| `POSTS_SUBDIR` | Subdirectory within the submodule containing files | `posts` | `articles` or `pages` |
| `TARGET_PATH` | Destination directory in base repository | `content` | `posts` or `src/content` |
| `SUBMODULE_NAME` | Name of the submodule (informational) | `mpr.drafts` | `blog.drafts` |

### Example: Using a Different Subdirectory

To move files from `pages/` instead of `posts/` within the submodule:

```bash
POSTS_SUBDIR="pages"
```

This would look for files at `content/mpr.drafts/pages/<filename>` instead of `content/mpr.drafts/posts/<filename>`.

### Example: Different Submodule Location

If your submodule is at `drafts/` in the repository root:

```bash
SUBMODULE_PATH="drafts"
SUBMODULE_NAME="drafts"
```

This would look for files at `drafts/posts/<filename>` and move them to `content/<filename>`.

## Usage

### Moving a File

```bash
./pubmove.sh <filename>
```

The script looks for files in the `posts/` subdirectory of the drafts submodule.

Example:
```bash
./pubmove.sh my-draft-post.md
```

This will move `content/mpr.drafts/posts/my-draft-post.md` to `content/my-draft-post.md`.

### Undoing a Move (Wrong Filename)

If you run the script with the wrong filename, use the built-in undo command:

```bash
./pubmove.sh undo <filename>
```

Example:
```bash
./pubmove.sh undo my-draft-post.md
```

The undo command automatically:
- Unstages changes in the base repository
- Deletes the copied file
- Resets the submodule to the previous commit
- Verifies the file is restored in the submodule

**Important**: Undo only works before pushing. Once pushed, you'll need to create new commits to reverse the changes.

The script handles the git coordination complexity while keeping the user in control of the publishing workflow.
