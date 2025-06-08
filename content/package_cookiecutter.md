Title: Python Package Cookiecutter
Date: 2025-06-04
Author: C. Ross Jam
Status: published

Link parkin’: [python-package-cookiecutter][1]

> There are many cookiecutter templates, but this one is mine and I'm
> sharing it with you. With it, you can quickly create a full-featured
> Python package designed to be managed with uv, a default typer
> command-line interface, optional settings using pydantic-settings
> and logging using my favorite logger, loguru. Best of all, testing,
> code quality checks, and publishing to PyPI are all baked in and
> ready to go. 

I’ve been locked on to Simon Willison’s [click-app][2] cookiecutter,
mainly due to inertia, but this new one hits all my recent developer
buttons: [`uv`][7], [`loguru`][6], and [`typer`][5]. Also, TIL: [Poe
the Poet][3] and [`pydantic-settings`][4]

[1]: https://github.com/JnyJny/python-package-cookiecutter
[2]: https://github.com/simonw/click-app
[3]: https://poethepoet.natn.io/
[4]: https://docs.pydantic.dev/latest/api/pydantic_settings/
[5]: https://typer.tiangolo.com/
[6]: https://loguru.readthedocs.io/en/stable/
[7]: https://docs.astral.sh/uv/
