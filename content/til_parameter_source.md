---
title: "TIL: Click Context Parameter Source"
date: 2025-11-22
author: "C. Ross Jam"
status: published
---

TIL that [click][1], my favorite CLI processing toolkit, has a
mechanism to determine how a CLI option was provided
[Context.get_parameter_source][2]

> Get the source of a parameter. This indicates the location from
> which the value of the parameter was obtained. 
>
> This can be useful for determining when a user specified a value on
> the command line that is the same as the default value. It will be
> DEFAULT only if the value was actually taken from the default. 

[_Via Stack Overflow_][3]

[1]: https://click.palletsprojects.com
[2]: https://click.palletsprojects.com/en/stable/api/#click.Context.get_parameter_source
[3]: https://stackoverflow.com/questions/75512527/python-click-determine-whether-argument-comes-from-default-or-from-user
