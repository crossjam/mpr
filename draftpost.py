#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "rich>=13.0.0",
#     "pypandoc>=1.13",
#     "python-slugify>=8.0.0",
# ]
# ///
"""
draftpost.py - Create a new blog post draft with YAML metadata header.

This script creates a new post in the mpr.drafts submodule with proper YAML
metadata formatting. It provides interactive prompts for post metadata and
can optionally grab content from the clipboard on macOS.
"""

import argparse
import os
import sys
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from slugify import slugify

console = Console()

# Default Lorem Ipsum content for new posts
LOREM_IPSUM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


def get_clipboard_content() -> Optional[tuple[str, str]]:
    """
    Attempt to get clipboard content on macOS using pbpaste.
    
    Returns:
        Optional tuple of (content, format) where format is 'txt', 'rtf', or None
    """
    if sys.platform != "darwin":
        return None
        
    try:
        # First try to get RTF format
        result = subprocess.run(
            ["pbpaste", "-Prefer", "rtf"],
            capture_output=True,
            text=False,
            timeout=5
        )
        
        if result.returncode == 0 and result.stdout:
            # Check if it's actually RTF by looking for RTF header
            if result.stdout.startswith(b'{\\rtf'):
                return (result.stdout.decode('utf-8', errors='ignore'), 'rtf')
        
        # Fall back to plain text
        result = subprocess.run(
            ["pbpaste"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0 and result.stdout.strip():
            return (result.stdout, 'txt')
            
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception) as e:
        console.print(f"[yellow]Could not access clipboard: {e}[/yellow]")
    
    return None


def convert_rtf_to_markdown(rtf_content: str) -> str:
    """
    Convert RTF content to Markdown using pandoc.
    
    Args:
        rtf_content: RTF formatted string
        
    Returns:
        Markdown formatted string
    """
    try:
        import pypandoc
        
        # Write RTF to a temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.rtf', delete=False) as f:
            f.write(rtf_content)
            rtf_file = f.name
        
        try:
            # Convert RTF to Markdown
            markdown = pypandoc.convert_file(rtf_file, 'markdown', format='rtf')
            return markdown
        finally:
            # Clean up temp file
            os.unlink(rtf_file)
            
    except ImportError:
        console.print("[yellow]pypandoc not available, returning RTF as-is[/yellow]")
        return rtf_content
    except Exception as e:
        console.print(f"[yellow]Could not convert RTF: {e}[/yellow]")
        return rtf_content


def get_post_content(use_clipboard: bool = True, file_path: Optional[str] = None) -> str:
    """
    Get post content from file, clipboard, or use Lorem Ipsum placeholder.
    
    Args:
        use_clipboard: Whether to attempt clipboard access
        file_path: Path to file to read content from (or '-' for stdin)
        
    Returns:
        Post content as a string (from file, clipboard, or Lorem Ipsum fallback)
    """
    content = ""
    
    # First priority: read from file if specified
    if file_path:
        try:
            if file_path == '-':
                # Read from stdin
                console.print("[cyan]Reading content from standard input...[/cyan]")
                content = sys.stdin.buffer.read().decode('utf-8', errors='replace')
                console.print("[green]✓[/green] Content read from stdin")
            else:
                # Read from file
                file_path_obj = Path(file_path)
                if not file_path_obj.exists():
                    console.print(f"[red]Error: File not found: {file_path}[/red]")
                    sys.exit(1)
                content = file_path_obj.read_text(encoding='utf-8', errors='replace')
                console.print(f"[green]✓[/green] Content read from file: {file_path}")
        except Exception as e:
            console.print(f"[red]Error reading file: {e}[/red]")
            sys.exit(1)
    
    # Second priority: try clipboard if enabled
    elif use_clipboard and sys.platform == "darwin":
        clipboard_data = get_clipboard_content()
        
        if clipboard_data:
            clipboard_content, clipboard_format = clipboard_data
            
            if clipboard_format == 'rtf':
                console.print("[cyan]RTF content detected in clipboard, converting to Markdown...[/cyan]")
                content = convert_rtf_to_markdown(clipboard_content)
                console.print("[green]✓[/green] RTF converted to Markdown")
            else:
                content = clipboard_content
                console.print("[green]✓[/green] Plain text content grabbed from clipboard")
    
    # Third priority: use Lorem Ipsum fallback
    if not content:
        console.print("[yellow]No content source available, using Lorem Ipsum placeholder.[/yellow]")
        content = LOREM_IPSUM
    
    return content.strip()


def get_output_directory(cli_dir: Optional[str] = None) -> Path:
    """
    Determine the output directory from CLI arg, environment variable, or default.
    
    Priority:
    1. Command-line argument (--output-dir)
    2. Environment variable (DRAFTPOST_OUTPUT_DIR)
    3. Default: content/mpr.drafts/posts
    
    Args:
        cli_dir: Directory specified via command-line argument
        
    Returns:
        Path object for the output directory
    """
    if cli_dir:
        return Path(cli_dir)
    
    env_dir = os.environ.get('DRAFTPOST_OUTPUT_DIR')
    if env_dir:
        return Path(env_dir)
    
    # Default location
    repo_root = Path(__file__).parent
    return repo_root / "content" / "mpr.drafts" / "posts"


def create_post(
    title: str,
    author: str,
    category: str,
    content: str,
    slug: Optional[str] = None,
    status: str = "draft",
    output_dir: Optional[Path] = None
) -> Path:
    """
    Create a new post file with YAML metadata header.
    
    Args:
        title: Post title
        author: Post author
        category: Post category
        content: Post content (markdown)
        slug: URL slug (auto-generated from title if not provided)
        status: Post status (default: "draft")
        output_dir: Directory to save the post (required)
        
    Returns:
        Path to the created post file
    """
    # Generate slug from title if not provided
    if not slug:
        slug = slugify(title)
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create filename from slug
    filename = f"{slug}.md"
    filepath = output_dir / filename
    
    # Check if file already exists
    if filepath.exists():
        overwrite = Confirm.ask(f"[yellow]File {filename} already exists. Overwrite?[/yellow]")
        if not overwrite:
            console.print("[red]Aborted.[/red]")
            sys.exit(1)
    
    # Get current date in the format used by existing posts
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Build the post content with YAML metadata header
    post_content = f"""Title: {title}
Date: {date_str}
Author: {author}
Category: {category}
Slug: {slug}
Status: {status}

{content}
"""
    
    # Write to file
    filepath.write_text(post_content)
    
    return filepath


def print_help():
    """Print help information and exit."""
    help_text = """
[bold cyan]draftpost.py - Create a new blog post draft[/bold cyan]

[bold]Usage:[/bold]
  ./draftpost.py [options]
  ./draftpost.py --help
  ./draftpost.py --file <filename>
  ./draftpost.py --output-dir <directory>
  cat content.txt | ./draftpost.py --file -

[bold]Description:[/bold]
  Creates a new blog post draft in the mpr.drafts submodule with proper YAML
  metadata headers. The script provides interactive prompts for post metadata
  and can obtain content from multiple sources.

[bold]Options:[/bold]
  -h, --help            Show this help message and exit
  -f, --file FILE       Read post content from FILE (use '-' for stdin)
                        If not specified, tries clipboard on macOS, then
                        falls back to Lorem Ipsum placeholder
  -o, --output-dir DIR  Output directory for the post
                        Default: content/mpr.drafts/posts or $DRAFTPOST_OUTPUT_DIR

[bold]Environment Variables:[/bold]
  DRAFTPOST_OUTPUT_DIR  Set default output directory for posts
                        Overridden by --output-dir option

[bold]Output Directory Priority:[/bold]
  1. Command-line argument (--output-dir)
  2. Environment variable ($DRAFTPOST_OUTPUT_DIR)
  3. Default: content/mpr.drafts/posts

[bold]Content Sources (in priority order):[/bold]
  1. File specified with --file option (or stdin with --file -)
  2. Clipboard content on macOS (via pbpaste)
     - Supports plain text and RTF formats
     - RTF is automatically converted to Markdown
  3. Lorem Ipsum placeholder text

[bold]Examples:[/bold]
  # Interactive mode with clipboard
  ./draftpost.py

  # Read content from a file
  ./draftpost.py --file my-post-content.md

  # Read content from stdin
  cat my-content.txt | ./draftpost.py --file -
  echo "Post content" | ./draftpost.py --file -

  # Specify custom output directory
  ./draftpost.py --output-dir /path/to/drafts

  # Use environment variable for output directory
  export DRAFTPOST_OUTPUT_DIR=/path/to/drafts
  ./draftpost.py

[bold]Output:[/bold]
  Posts are created in: content/mpr.drafts/posts/
  Format: YAML metadata header + Markdown content

[bold]Next Steps:[/bold]
  After creating a draft, use ./pubmove.sh to publish it:
  ./pubmove.sh <slug>.md
"""
    console.print(help_text)
    sys.exit(0)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Create a new blog post draft with YAML metadata header',
        add_help=False  # We'll handle --help ourselves for rich formatting
    )
    parser.add_argument(
        '-h', '--help',
        action='store_true',
        help='Show help message and exit'
    )
    parser.add_argument(
        '-f', '--file',
        type=str,
        metavar='FILE',
        help='Read post content from FILE (use "-" for stdin)'
    )
    parser.add_argument(
        '-o', '--output-dir',
        type=str,
        metavar='DIR',
        help='Output directory for the post (default: content/mpr.drafts/posts or $DRAFTPOST_OUTPUT_DIR)'
    )
    
    args = parser.parse_args()
    
    # Handle help flag
    if args.help:
        print_help()
    
    return args


def main():
    """Main entry point for the draftpost script."""
    # Parse command line arguments
    args = parse_args()
    
    console.print(Panel.fit(
        "[bold cyan]Draft Post Creator[/bold cyan]\n"
        "Create a new blog post in the mpr.drafts submodule",
        border_style="cyan"
    ))
    
    # Check if we can use clipboard on macOS
    can_use_clipboard = sys.platform == "darwin"
    
    # Prompt for metadata
    console.print("\n[bold]Post Metadata[/bold]")
    
    title = Prompt.ask("[cyan]Title[/cyan]")
    author = Prompt.ask("[cyan]Author[/cyan]", default="crossjam")
    
    # Optional: custom slug
    default_slug = slugify(title)
    use_custom_slug = Confirm.ask(
        f"[cyan]Use custom slug?[/cyan] (default: [dim]{default_slug}[/dim])",
        default=False
    )
    
    slug = None
    if use_custom_slug:
        slug = Prompt.ask("[cyan]Custom slug[/cyan]", default=default_slug)
    
    # Get content
    console.print("\n[bold]Post Content[/bold]")
    
    # If --file is specified, use that; otherwise ask about clipboard
    use_clipboard = False
    if args.file:
        # Content will be read from file
        pass
    elif can_use_clipboard:
        use_clipboard = Confirm.ask(
            "[cyan]Try to grab content from clipboard?[/cyan]",
            default=True
        )
    
    content = get_post_content(use_clipboard, args.file)
    
    # Determine output directory
    output_dir = get_output_directory(args.output_dir)
    
    # Show preview
    console.print("\n[bold]Preview[/bold]")
    console.print(Panel(
        f"[bold]Title:[/bold] {title}\n"
        f"[bold]Author:[/bold] {author}\n"
        f"[bold]Slug:[/bold] {slug or default_slug}\n"
        f"[bold]Output:[/bold] {output_dir}\n"
        f"[bold]Content:[/bold] {content[:100]}{'...' if len(content) > 100 else ''}",
        border_style="cyan"
    ))
    
    # Confirm creation
    if not Confirm.ask("\n[cyan]Create this post?[/cyan]", default=True):
        console.print("[red]Aborted.[/red]")
        sys.exit(1)
    
    # Create the post
    try:
        filepath = create_post(
            title=title,
            author=author,
            category="Uncategorized",
            content=content,
            slug=slug,
            status="draft",
            output_dir=output_dir
        )
        
        console.print(f"\n[bold green]✓[/bold green] Post created successfully!")
        console.print(f"[cyan]Location:[/cyan] {filepath}")
        console.print(f"\n[dim]Next steps:[/dim]")
        console.print(f"  1. Review and edit: [cyan]{filepath}[/cyan]")
        console.print(f"  2. When ready to publish, use: [cyan]./pubmove.sh {filepath.name}[/cyan]")
        
    except Exception as e:
        console.print(f"[bold red]Error creating post:[/bold red] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
