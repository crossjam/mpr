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


def get_post_content(use_clipboard: bool = True) -> str:
    """
    Get post content from clipboard or user input.
    
    Args:
        use_clipboard: Whether to attempt clipboard access
        
    Returns:
        Post content as a string
    """
    content = ""
    
    if use_clipboard and sys.platform == "darwin":
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
    
    if not content:
        console.print("\n[cyan]Enter post content (press Ctrl+D or Ctrl+Z when done):[/cyan]")
        console.print("[dim]Tip: You can paste content here or type it directly.[/dim]\n")
        
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass
        
        content = "\n".join(lines)
    
    return content.strip()


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
        output_dir: Directory to save the post (default: content/mpr.drafts/posts)
        
    Returns:
        Path to the created post file
    """
    # Generate slug from title if not provided
    if not slug:
        slug = slugify(title)
    
    # Set default output directory
    if output_dir is None:
        repo_root = Path(__file__).parent
        output_dir = repo_root / "content" / "mpr.drafts" / "posts"
    
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


def main():
    """Main entry point for the draftpost script."""
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
    category = Prompt.ask("[cyan]Category[/cyan]", default="Uncategorized")
    
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
    
    use_clipboard = False
    if can_use_clipboard:
        use_clipboard = Confirm.ask(
            "[cyan]Try to grab content from clipboard?[/cyan]",
            default=True
        )
    
    content = get_post_content(use_clipboard)
    
    if not content:
        console.print("[red]No content provided. Aborted.[/red]")
        sys.exit(1)
    
    # Show preview
    console.print("\n[bold]Preview[/bold]")
    console.print(Panel(
        f"[bold]Title:[/bold] {title}\n"
        f"[bold]Author:[/bold] {author}\n"
        f"[bold]Category:[/bold] {category}\n"
        f"[bold]Slug:[/bold] {slug or default_slug}\n"
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
            category=category,
            content=content,
            slug=slug,
            status="draft"
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
