---
title: "op and direnv"
date: 2025-11-15
author: "C. Ross Jam"
status: published
---

1password has a great [command line interface (CLI) framework][1]. As
my secrets manager of choice, I like to keep api keys in 1password.

Meanwhile, I also use [direnv][2] to automagically establish
environment variables in project directories. AI toolkits typically
pick up their api keys via environment variables. OPENAI\_API\_KEY is
the canonical example. direnv picks up the variables to setup via a
.envrc file.

Being super lazy, I’d rather not cut and paste from 1password to
append the right information to .envrc. I thought of writing a script
from scratch, but then started poking around on the web. Found this
[interesting comment][3] on GitHub in a repository about connecting
direnv and 1password:

> I just found out that you can just do this in .envrc, so I'm
> actually not sure what's the main benefit of the plugin if that
> already works. Maybe I'm missing a use case though. 

```bash
export MY_SECRET=${MY_SECRET_2:-$(op item get 'db/some-database' --fields password --format json | jq -r .value)}
```

I asked Claude to turn that one-liner into a script and wound up with
this:

```bash
#!/bin/bash

# Usage: ./set-env.sh ENV_VAR_NAME OP_ITEM_SPEC [FIELD]

ENV_VAR="$1"
OP_ITEM="$2"
FIELD="${3:-token}"

if [ -z "$ENV_VAR" ] || [ -z "$OP_ITEM" ]; then
    echo "Usage: $0 ENV_VAR_NAME OP_ITEM_SPEC [FIELD]"
    exit 1
fi

EXPORT_LINE="export ${ENV_VAR}=\${${ENV_VAR}:-\$(op item get '${OP_ITEM}' --fields ${FIELD} --format json | jq -r .value)}"

# Check if the variable already exists and update/insert
if grep -q "^export ${ENV_VAR}=" .envrc; then
    # Update existing line
    sed -i.bak "/^export ${ENV_VAR}=/c\\
${EXPORT_LINE}" .envrc
    echo "Updated ${ENV_VAR} in .envrc"
else
    # Append new line
    echo "${EXPORT_LINE}" >> .envrc
    echo "Added ${ENV_VAR} to .envrc"
fi
```

Next up, hand this off to Claude Code Web to turn it into a Python
CLI tool. I’d like to have more introspection and interactive
selection of keys.

Generating a Bash script, test driving, then handing off to Claude
Code for conversion to Python seems to be a development process that
works for me.

[1]: https://developer.1password.com/docs/cli/
[2]: https://direnv.net
[3]: https://github.com/tmatilai/direnv-1password/pull/9#issuecomment-3384819136
