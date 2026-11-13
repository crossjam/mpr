"""Wrapping a post's paragraphs to a fixed width with flowmark.

Only plain paragraphs are refilled, and only their line breaks move.
Every other block, from blockquotes and code to lists, tables, and HTML
such as the summary marker, is kept exactly as written: flowmark renders
those in CommonMark style, which Pelican's Python-Markdown does not
always read the same way (it needs four-space indents for nested lists,
for one).
"""

import re

from flowmark import fill_text

from . import metadata

WIDTH = 88

# A line that starts or belongs to some block other than a plain paragraph
BLOCK_LINE = re.compile(
    r"""^(?:
      \s                    # indented: code, or a list item's continuation
    | [>#|<:{]              # blockquote, heading, table, HTML, definition, attribute list
    | [*+-](?:\s|$)         # bullet
    | \d+[.)](?:\s|$)       # numbered item
    | \[[^\]]*\]:           # link reference or footnote definition
    | \*\[                  # abbreviation
    | [-=_*`~]{3,}          # rule, setext underline, or fence
    | [-=|:\s]+$            # table separator or setext underline
    )""",
    re.VERBOSE,
)

FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


def split_header(text: str) -> tuple[str, str]:
    """Split a post into its metadata header, kept verbatim, and its body."""
    lines = text.splitlines(keepends=True)
    _, end, is_yaml = metadata.header_bounds([line.rstrip("\n") for line in lines])
    # A YAML header runs through its closing fence
    cut = end + 1 if is_yaml else end
    return "".join(lines[:cut]), "".join(lines[cut:])


def blocks(body: str) -> list[tuple[list[str], bool]]:
    """
    Split a body into runs of lines, each flagged whether it is a fillable paragraph.

    Blank lines and fenced code come back as runs of their own, never fillable.
    """
    runs: list[tuple[list[str], bool]] = []
    current: list[str] = []
    fence = ""

    def flush() -> None:
        if current:
            runs.append((current.copy(), is_paragraph(current)))
            current.clear()

    for line in body.splitlines():
        if fence:
            runs.append(([line], False))
            if line.strip().startswith(fence) and not line.strip().strip(fence[0]):
                fence = ""
        elif m := FENCE.match(line):
            flush()
            fence = m.group(1)
            runs.append(([line], False))
        elif not line.strip():
            flush()
            runs.append(([line], False))
        else:
            current.append(line)
    flush()
    return runs


def is_paragraph(lines: list[str]) -> bool:
    # A line ending in two spaces is a hard break, which flowmark rewrites as a
    # backslash that Python-Markdown does not honor
    return not any(BLOCK_LINE.match(line) or line.endswith("  ") for line in lines)


def fill(lines: list[str]) -> list[str]:
    """Refill a paragraph, keeping it as written if the result would read as another block."""
    # fill_text only moves line breaks, keeping links, code spans, and tags whole; it
    # leaves Markdown as written where fill_markdown would re-render it (_a_ as *a*)
    filled = fill_text("\n".join(lines), width=WIDTH).splitlines()
    return filled if filled and is_paragraph(filled) else lines


def format_body(body: str) -> str:
    """Wrap a body's plain paragraphs to WIDTH, leaving every other block untouched."""
    out: list[str] = []
    for lines, fillable in blocks(body):
        out.extend(fill(lines) if fillable else lines)
    return "\n".join(out) + ("\n" if body.endswith("\n") else "")


def format_post(text: str) -> str:
    """Format a whole post, keeping its metadata header exactly as it is."""
    header, body = split_header(text)
    return header + format_body(body)
