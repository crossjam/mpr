from datetime import datetime

from mpr import metadata

NOW = datetime(2026, 11, 10, 9, 30)

YAML_POST = """---
title: "Hello"
status: draft
---

Body text: with a colon.
"""

PELICAN_POST = """Title: Hello
Status: draft

Body text: with a colon.
"""


def test_publish_yaml_adds_date_inside_front_matter():
    text = metadata.publish_text(YAML_POST, redate=False, now=NOW)
    assert (
        text
        == """---
title: "Hello"
status: published
date: 2026-11-10 09:30
---

Body text: with a colon.
"""
    )


def test_publish_pelican_header_leaves_body_alone():
    text = metadata.publish_text(PELICAN_POST, redate=False, now=NOW)
    assert text.splitlines()[:3] == ["Title: Hello", "Status: published", "Date: 2026-11-10 09:30"]
    assert text.endswith("\nBody text: with a colon.\n")


def test_publish_keeps_existing_date_unless_redated():
    dated = metadata.set_field(YAML_POST, "date", "2020-01-01 00:00")
    assert (
        metadata.get_field(metadata.publish_text(dated, False, NOW), "date") == "2020-01-01 00:00"
    )
    assert metadata.get_field(metadata.publish_text(dated, True, NOW), "date") == "2026-11-10 09:30"


def test_new_post_quotes_awkward_titles():
    text = metadata.new_post('Say "hi": a post', "C. Ross Jam", "Body", NOW)
    assert metadata.get_field(text, "title") == '"Say \\"hi\\": a post"'
    assert metadata.get_field(text, "status") == "draft"
