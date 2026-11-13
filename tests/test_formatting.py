"""Wrapping post paragraphs while leaving every other block as written."""

from mpr.formatting import WIDTH, format_body, format_post

LONG = " ".join(["word"] * 40)


def test_wraps_paragraphs_to_the_width():
    out = format_body(LONG + "\n")
    assert len(out.splitlines()) > 1
    assert all(len(line) <= WIDTH for line in out.splitlines())
    assert out.split() == LONG.split()


def test_joins_short_lines_in_a_paragraph():
    assert format_body("one\ntwo\nthree\n") == "one two three\n"


def test_keeps_blockquotes_and_code_as_written():
    body = "\n".join(
        [
            "> " + LONG,
            "> short",
            "",
            "```python",
            "x = '" + LONG + "'",
            "",
            "```",
            "",
            "    indented " + LONG,
            "",
        ]
    )
    assert format_body(body) == body


def test_keeps_python_markdown_lists_and_tables():
    body = "\n".join(
        [
            "* item " + LONG,
            "    * nested with four spaces",
            "",
            "1. first",
            "",
            "| a | b |",
            "|---|---|",
            "",
            "[^1]: " + LONG,
            "",
        ]
    )
    assert format_body(body) == body


def test_keeps_the_summary_marker_and_html():
    body = f"{LONG}\n\n<!-- PELICAN_END_SUMMARY -->\n\nAfter.\n"
    out = format_body(body)
    assert "\n\n<!-- PELICAN_END_SUMMARY -->\n\nAfter.\n" in out


def test_keeps_hard_line_breaks():
    body = "line one  \nline two\n"
    assert format_body(body) == body


def test_keeps_yaml_front_matter_exactly():
    header = '---\ntitle: "A: Title"\ndate: 2026-11-12 20:02\nstatus: draft\n---\n'
    out = format_post(header + "\n" + LONG + "\n")
    assert out.startswith(header + "\n")


def test_keeps_pelican_metadata_exactly():
    header = "Title: Old\nStatus: draft\n"
    out = format_post(header + "\n" + LONG + "\n")
    assert out.startswith(header + "\n")
    assert len(out.splitlines()) > 4


def test_is_idempotent():
    once = format_post("---\ntitle: x\n---\n\n" + LONG + "\n\n> " + LONG + "\n")
    assert format_post(once) == once


def test_moves_only_line_breaks():
    body = "_The Book_ by [_An Author_](https://example.com/x) was __great__, `a b c`. " + LONG
    out = format_body(body + "\n")
    assert out.split() == body.split()
    assert "`a b c`" in out
