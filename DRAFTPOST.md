# Creating Draft Posts: draftpost.py Script

## Overview

The `draftpost.py` script starts a new blog post draft on its own branch. It creates `draft/<slug>` from `main`, writes `content/<slug>.md` with a YAML metadata header marked `status: draft`, commits it, and pushes the branch to the private `drafts` remote. It provides an interactive interface for entering post metadata and content, with optional clipboard integration on macOS.

Drafts never land on `main` until they are published with `publishpost.py`; see `PUBLISHPOST.md` for that step and for the one-time remote and hook setup.

## Features

- **Interactive Prompts**: User-friendly interface using the `rich` library
- **One Branch per Draft**: Each draft lives on `draft/<slug>`, pushed only to the private `drafts` remote
- **Command Line Options**: Support for `--help` and `--file` arguments
- **Multiple Content Sources**:
  - Read from file with `--file <filename>`
  - Read from standard input with `--file -`
  - Clipboard integration on macOS via `pbpaste`
  - Lorem Ipsum placeholder fallback
- **YAML Metadata Generation**: Automatically creates properly formatted metadata headers
- **Clipboard Support** (macOS only):
  - Detects and retrieves clipboard content via `pbpaste`
  - Supports plain text format
  - Automatically converts RTF to Markdown (requires pandoc)
- **Automatic Slug Generation**: Creates URL-friendly slugs from post titles
- **Default Values**: Sensible defaults for author and status fields
- **Safety Checks**: Refuses to run with uncommitted changes, when the branch already exists, or when the slug matches a published post

## Requirements

The script uses the uv script format with inline dependencies:

- Python >= 3.10
- `rich` >= 13.0.0 (for interactive prompts and formatting)
- `pypandoc` >= 1.13 (for RTF to Markdown conversion)
- `python-slugify` >= 8.0.0 (for URL slug generation)

**Optional**:
- `pandoc` system package (for RTF conversion on macOS)

## Usage

### Command Line Options

```bash
./draftpost.py [options]
```

**Options:**
- `-h, --help`: Show help message and exit
- `-f, --file FILE`: Read post content from FILE (use `-` for stdin)
- `-q, --quote`: Format content as a markdown blockquote
- `-e, --edit`: Open the post in `$EDITOR` before the first commit

### Basic Usage

```bash
# Interactive mode (with clipboard on macOS)
./draftpost.py

# Read content from a file
./draftpost.py --file my-content.md

# Read content from stdin
cat my-content.txt | ./draftpost.py --file -
echo "Post content" | ./draftpost.py --file -

# Create the post and edit it before the first commit
./draftpost.py --file my-content.md --edit

# Show help
./draftpost.py --help
```

The script will interactively prompt you for:

1. **Title**: The post title
2. **Author**: Post author (default: "crossjam")
3. **Custom Slug** (optional): Override the auto-generated slug

### Content Sources (Priority Order)

The script obtains post content from the following sources in priority order:

1. **File specified with `--file` option** (or stdin with `--file -`)
2. **Clipboard** (macOS only, via `pbpaste`)
   - Plain text format
   - RTF format (converted to Markdown)
3. **Lorem Ipsum placeholder** (fallback)

### Post Metadata Format

Posts are created with proper YAML frontmatter:

```markdown
---
title: "Your Post Title"
date: 2025-11-26 15:30
author: "crossjam"
status: draft
---

Your post content goes here...
```

### Where the Draft Goes

The script runs these steps after you confirm the preview:

1. Refreshes the draft-branch hook guards (`install-draft-hooks.sh`)
2. Creates and switches to `draft/<slug>`, starting from `main`
3. Writes `content/<slug>.md`
4. Opens it in your editor, if `--edit` was given
5. Commits it as `Start draft: <title>`
6. Pushes the branch with `git push -u drafts draft/<slug>`, so a plain `git push` on the branch goes to the drafts remote

If the push fails (offline, say), the commit stays local and the script prints the push command to run later.

### Clipboard Integration (macOS)

When running on macOS, the script can:

1. Detect clipboard content using `pbpaste`
2. Handle plain text format directly
3. Convert RTF format to Markdown (if pandoc is available)
4. Fall back to Lorem Ipsum placeholder if clipboard is empty

**Note**: PostScript (ps) format is ignored per the requirements.

### Example Session

#### Interactive Mode with Clipboard

```
╭────────────────────────────────────────────────────╮
│ Draft Post Creator                                 │
│ Start a new blog post on its own draft branch      │
╰────────────────────────────────────────────────────╯

Post Metadata
Title: My Amazing Post
Author (crossjam): C. Ross Jam
Use custom slug? (default: my-amazing-post) [y/n] (n): n

Post Content
Try to grab content from clipboard? [y/n] (y): y
✓ Plain text content grabbed from clipboard

Preview
╭──────────────────────────────────────────────────╮
│ Title: My Amazing Post                           │
│ Author: C. Ross Jam                              │
│ Slug: my-amazing-post                            │
│ Branch: draft/my-amazing-post (from main)        │
│ Content: This is my amazing post content...      │
╰──────────────────────────────────────────────────╯

Create this post? [y/n] (y): y

✓ Switched to new branch draft/my-amazing-post
✓ Post created successfully!
Location: content/my-amazing-post.md
✓ Pushed draft/my-amazing-post to drafts

Next steps:
  1. Edit content/my-amazing-post.md, commit, and git push (goes to drafts)
  2. When ready to publish, from main: ./publishpost.py my-amazing-post
```

#### Using --file Option

```bash
# Create a content file
cat > post-content.md << 'EOF'
This is my blog post content.

It has multiple paragraphs and **markdown formatting**.

## A Heading

- List item 1
- List item 2
EOF

# Create post from file
./draftpost.py --file post-content.md
```

#### Using stdin

```bash
# Pipe content directly
echo "Quick post content" | ./draftpost.py --file -

# Or from another command
curl https://example.com/content.txt | ./draftpost.py --file -
```

## Workflow Integration

### Creating a Draft Post

1. Run `./draftpost.py` (optionally with `--file <filename>`)
2. Enter post metadata when prompted
3. Content is obtained from:
   - File specified with `--file` option
   - Clipboard (macOS, if enabled)
   - Lorem Ipsum placeholder (fallback)
4. Review the preview
5. Confirm creation

### Working on a Draft

Edit, commit, and `git push` on the draft branch as usual. Run `uv run poe devserver` to preview; drafts render at `/drafts/<slug>.html` with a Draft badge, and do not appear on the front page.

A draft branch can also be checked out in its own worktree (for example with kwt), so several drafts can be open at once.

### Publishing a Draft

From `main`:

```bash
./publishpost.py my-amazing-post
```

See `PUBLISHPOST.md`.

## Technical Details

### Script Format

The script uses uv's inline script dependencies format (PEP 723):

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "rich>=13.0.0",
#     "pypandoc>=1.13",
#     "python-slugify>=8.0.0",
# ]
# ///
```

This allows the script to be self-contained with its dependencies automatically managed by uv.

### RTF Conversion

RTF conversion is handled by pypandoc, which requires the pandoc system package:

```bash
# On macOS
brew install pandoc

# On Ubuntu/Debian
apt-get install pandoc
```

If pandoc is not available, RTF content will be returned as-is without conversion.

## Configuration

Constants at the top of `draftpost.py`:

- **`BASE_BRANCH`**: branch drafts start from (`main`)
- **`DRAFTS_REMOTE`**: private remote draft branches are pushed to (`drafts`)

## Troubleshooting

### Clipboard Not Working

If clipboard access fails on macOS:
- Ensure `pbpaste` is available (standard on macOS)
- Check system permissions for clipboard access
- Lorem Ipsum placeholder will be used automatically

### RTF Conversion Failed

If RTF conversion fails:
- Install pandoc: `brew install pandoc` (macOS)
- The script will return RTF as-is if conversion is unavailable

### Branch or File Already Exists

If `draft/<slug>` already exists, or `content/<slug>.md` is already a published post on `main`, the script stops before changing anything. Choose a custom slug.

### Uncommitted Changes

The script switches branches, so it refuses to run with uncommitted changes to tracked files. Commit or stash them first.

## See Also

- `PUBLISHPOST.md` - Publishing a draft branch onto main, and one-time setup
- `publishpost.py` - Script for publishing a draft branch
