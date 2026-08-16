"""
Explicit Modified Date Plugin

With DEFAULT_DATE = "fs", Pelican's readers.path_metadata() backfills both
`date` and `modified` from the file's on-disk mtime whenever a post doesn't
set them explicitly. That makes `modified` indistinguishable from "no
Modified: field was set" -- any incidental edit to a file (formatting, a
move, a rebuild touching the file) changes its mtime regardless of whether
the post's content was actually revised after publishing.

This patches path_metadata() to drop the `modified` fallback, leaving the
`date` fallback untouched. `modified` is then only present when a post's
front matter explicitly includes a Modified:/modified: field.
"""
from pelican import readers as pelican_readers

_original_path_metadata = pelican_readers.path_metadata


def _path_metadata_no_modified_fallback(*args, **kwargs):
    metadata = _original_path_metadata(*args, **kwargs)
    metadata.pop("modified", None)
    return metadata


def register():
    pelican_readers.path_metadata = _path_metadata_no_modified_fallback
