"""Where a new post's body comes from: a file, stdin, or the macOS clipboard."""

import subprocess
import sys
from typing import TextIO

import click

LOREM_IPSUM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


def warn(message: str) -> None:
    click.secho(message, fg="yellow", err=True)


def read_clipboard() -> tuple[str, str] | None:
    """Return (content, format) from the macOS clipboard, format 'rtf' or 'txt'."""
    if sys.platform != "darwin":
        warn("Clipboard access needs macOS (pbpaste)")
        return None

    try:
        rtf = subprocess.run(
            ["pbpaste", "-Prefer", "rtf"], capture_output=True, check=False, timeout=5
        )
        if rtf.returncode == 0 and rtf.stdout.startswith(b"{\\rtf"):
            return rtf.stdout.decode("utf-8", errors="ignore"), "rtf"

        text = subprocess.run(["pbpaste"], capture_output=True, check=False, text=True, timeout=5)
        if text.returncode == 0 and text.stdout.strip():
            return text.stdout, "txt"
    except (OSError, subprocess.TimeoutExpired) as e:
        warn(f"Could not access clipboard: {e}")

    return None


def rtf_to_markdown(rtf: str) -> str:
    """Convert RTF to Markdown with pandoc, or return it unchanged if that fails."""
    try:
        import pypandoc

        return pypandoc.convert_text(rtf, "markdown", format="rtf")
    except (ImportError, OSError, RuntimeError) as e:
        warn(f"Could not convert RTF, keeping it as-is: {e}")
        return rtf


def blockquote(text: str) -> str:
    """Prefix each line with '> ' to make a Markdown blockquote."""
    return "\n".join(f"> {line}" if line else ">" for line in text.split("\n"))


def post_body(source: TextIO | None, clipboard: bool, quote: bool) -> str:
    """Read the body from source or the clipboard, falling back to Lorem Ipsum."""
    body = ""
    if source is not None:
        body = source.read()
    elif clipboard and (clip := read_clipboard()):
        body, fmt = clip
        if fmt == "rtf":
            body = rtf_to_markdown(body)

    if not body.strip():
        warn("No content given, using Lorem Ipsum placeholder")
        body = LOREM_IPSUM

    body = body.strip()
    return blockquote(body) if quote else body
