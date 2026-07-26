POE=uv run poe

DEBUG ?= 0
RELATIVE ?= 0
PORT ?= 0
SERVER ?= 0.0.0.0
SSH_KEY ?=

# This Makefile is a thin compatibility wrapper. The real task
# definitions live under [tool.poe.tasks] in pyproject.toml -- run
# `uv run poe` (or just `poe`, if installed) to list them directly.

help:
	$(POE)

html:
	$(POE) html --DEBUG $(DEBUG) --RELATIVE $(RELATIVE)

clean:
	$(POE) clean

regenerate:
	$(POE) regenerate --DEBUG $(DEBUG) --RELATIVE $(RELATIVE)

serve:
	$(POE) serve --DEBUG $(DEBUG) --RELATIVE $(RELATIVE) --port $(PORT)

serve-global:
	$(POE) serve-global --DEBUG $(DEBUG) --RELATIVE $(RELATIVE) --port $(PORT) --server $(SERVER)

devserver:
	$(POE) devserver --DEBUG $(DEBUG) --RELATIVE $(RELATIVE) --port $(PORT)

devserver-global:
	$(POE) devserver-global --DEBUG $(DEBUG) --RELATIVE $(RELATIVE) --port $(PORT) --server $(SERVER)

publish:
	$(POE) publish --DEBUG $(DEBUG) --RELATIVE $(RELATIVE)

ssh_upload:
	$(POE) ssh_upload --DEBUG $(DEBUG) --RELATIVE $(RELATIVE)

rsync_upload:
	$(POE) rsync_upload --DEBUG $(DEBUG) --RELATIVE $(RELATIVE) --SSH_KEY "$(SSH_KEY)"

.PHONY: help html clean regenerate serve serve-global devserver devserver-global publish ssh_upload rsync_upload
