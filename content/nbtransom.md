Title: nbtransom
Date: 2017-08-06 20:28
Author: crossjam
Category: Uncategorized
Slug: nbtransom
Status: published

Keeping with the Jupyter theme, you can use the [nbtransom][1] library to manipulate notebooks with code:

> This is a Python 3 library to read/write cells programmatically in Jupyter notebooks which anticipates upcoming collaborative features in Jupyter.

> We use this at O'Reilly Media for notebooks used to manage machine learning pipelines. That is to say, machines and people collaborate on documents, implementing a "human-in-the-loop" design pattern: ...

nbtransom seems to be a key element for this [upcoming JupyterCon talk][2] from Paco Nathan:

> Paco Nathan reviews use cases where Jupyter provides a frontend to AI as the means for keeping humans in the loop (and shares the code used). Jupyter gets used in two ways. First, people responsible for managing ML pipelines use notebooks to set the necessary hyperparameters. In that sense, the notebooks serve in place of configuration scripts. Second, the ML pipelines update those notebooks with telemetry, summary analytics, etc., in lieu of merely sending that data out to log files. Analysis is kept contextualized, making it simple for a person to review. This process enhances the feedback loop between people and machines: humans-in-the-loop use Jupyter notebooks to inspect ML pipelines remotely, adjusting them at any point and inserting additional analysis, data visualization, plus their notes into the notebooks; the machine component is mostly automated but available interactively for troubleshooting and adjustment.

I’ll have to wait until the talk gets released to Safari, but I’m interested to see if there’s discussion of how notebooks are organized at a higher level to support these types of manipulations.

[1]: https://github.com/ceteri/nbtransom
[2]: https://conferences.oreilly.com/jupyter/jup-ny/public/schedule/detail/60058