# Creating Draft Posts: draftpost.py Script

## Overview

The `draftpost.py` script automates the creation of new blog post drafts with proper YAML metadata headers. It provides an interactive interface for entering post metadata and content, with optional clipboard integration on macOS.

## Features

- **Interactive Prompts**: User-friendly interface using the `rich` library
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
- **File Safety**: Warns before overwriting existing files

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
- `-o, --output-dir DIR`: Set output directory for the post

**Environment Variables:**
- `DRAFTPOST_OUTPUT_DIR`: Set default output directory for posts (overridden by `--output-dir`)

### Output Directory Priority

The output directory is determined in the following priority order:

1. **Command-line argument** (`--output-dir`)
2. **Environment variable** (`DRAFTPOST_OUTPUT_DIR`)
3. **Default**: `content/mpr.drafts/posts`

### Basic Usage

```bash
# Interactive mode (with clipboard on macOS)
./draftpost.py

# Read content from a file
./draftpost.py --file my-content.md

# Read content from stdin
cat my-content.txt | ./draftpost.py --file -
echo "Post content" | ./draftpost.py --file -

# Specify custom output directory
./draftpost.py --output-dir /path/to/custom/drafts

# Use environment variable for output directory
export DRAFTPOST_OUTPUT_DIR=/path/to/custom/drafts
./draftpost.py

# Combine options
./draftpost.py --file my-content.md --output-dir /path/to/drafts

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

Posts are created with the following YAML metadata header:

```markdown
Title: Your Post Title
Date: 2025-11-26 15:30
Author: crossjam
Category: Uncategorized
Slug: your-post-title
Status: draft

Your post content goes here...
```

### Default Location

Posts are created in: `content/mpr.drafts/posts/`

This matches the default location used by the `pubmove.sh` script for publishing.

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
│ Create a new blog post in the mpr.drafts submodule │
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
│ Content: This is my amazing post content...      │
╰──────────────────────────────────────────────────╯

Create this post? [y/n] (y): y

✓ Post created successfully!
Location: content/mpr.drafts/posts/my-amazing-post.md

Next steps:
  1. Review and edit: content/mpr.drafts/posts/my-amazing-post.md
  2. When ready to publish, use: ./pubmove.sh my-amazing-post.md
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

### Publishing a Draft

After creating and reviewing your draft, use the `pubmove.sh` script to publish it:

```bash
./pubmove.sh my-amazing-post.md
```

This will move the post from the `mpr.drafts` submodule to the main content directory.

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

### Directory Structure

```
content/
  mpr.drafts/
    posts/
      your-draft-post.md    # Created by draftpost.py
      another-draft.md
```

## Configuration

The script uses the same configuration as `pubmove.sh`:

- **Submodule Path**: `content/mpr.drafts`
- **Posts Subdirectory**: `posts`
- **Default Status**: `draft`

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

### File Already Exists

If a file with the same slug already exists:
- The script will prompt to confirm overwrite
- Choose "no" to abort and use a different title/slug

## See Also

- `PUBMOVE.md` - Documentation for publishing drafts to main content
- `pubmove.sh` - Script for moving posts from drafts to published content
