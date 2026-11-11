"""Reading and rewriting post metadata headers.

Posts carry either YAML front matter between '---' fences, or Pelican's
Markdown metadata: a run of "Key: value" lines before the first blank line.
"""

import json
import re
from datetime import datetime

# A metadata line: "Key: value"
META_LINE = re.compile(r"^([A-Za-z][\w-]*):(.*)$")

DATE_FORMAT = "%Y-%m-%d %H:%M"


def header_bounds(lines: list[str]) -> tuple[int, int, bool]:
    """
    Locate the metadata header of a post.

    Returns (start, end, is_yaml): the header's lines are lines[start:end].
    """
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return 1, i, True
        raise ValueError("unterminated YAML front matter")

    end = 0
    while end < len(lines) and META_LINE.match(lines[end]):
        end += 1
    return 0, end, False


def get_field(text: str, key: str) -> str | None:
    """Return a header field's raw value, or None when it is absent."""
    lines = text.splitlines()
    start, end, _ = header_bounds(lines)
    for line in lines[start:end]:
        m = META_LINE.match(line)
        if m and m.group(1).lower() == key:
            return m.group(2).strip()
    return None


def set_field(text: str, key: str, value: str) -> str:
    """Set a header field, replacing it in place or appending it."""
    lines = text.splitlines()
    start, end, is_yaml = header_bounds(lines)

    for i in range(start, end):
        m = META_LINE.match(lines[i])
        if m and m.group(1).lower() == key:
            lines[i] = f"{m.group(1)}: {value}"
            break
    else:
        # Match the header's style: lowercase keys in YAML, Title case otherwise
        name = key if is_yaml else key.capitalize()
        lines.insert(end, f"{name}: {value}")

    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def title_of(text: str) -> str | None:
    """A post's title with any surrounding quotes removed."""
    title = get_field(text, "title")
    return title.strip("\"'") if title else None


def yaml_string(value: str) -> str:
    """Quote a YAML scalar; JSON strings are valid YAML double-quoted scalars."""
    return json.dumps(value, ensure_ascii=False)


def new_post(title: str, author: str, content: str, date: datetime) -> str:
    """The text of a new draft post with YAML front matter."""
    return f"""---
title: {yaml_string(title)}
date: {date.strftime(DATE_FORMAT)}
author: {yaml_string(author)}
status: draft
---

{content}
"""


def publish_text(text: str, redate: bool, now: datetime) -> str:
    """Mark a post published, dating it now if undated or if asked to."""
    text = set_field(text, "status", "published")
    if redate or get_field(text, "date") is None:
        text = set_field(text, "date", now.strftime(DATE_FORMAT))
    return text
