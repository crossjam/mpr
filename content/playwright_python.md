Title: Playwright, Python, Requests-HTML
Author: crossjam
Date: 2024-12-20
Status: published

I was trying to lift and shift a web scraping script from my laptop to
a Linux VM. The script uses the [Requests-HTML][2] and works fine
OMM. On the VM, not so much. I just couldn’t get the right Ubuntu
dependencies installed so a headless Chrome browser integrated
correctly.

Enter [Requests-HTML-Playwright][3] which uses [playwright-python][4]
to wrap the [playwright][1] library. Should do the trick right?
Wrong. The `HTMLSession` from the `requests_html_playwright ` module
always failed. 

**HOWEVER!**, playwright-python apparently installs the correct Ubuntu
packages to make Requests-HTML operate properly. Go figure.

Victory?

[1]: https://playwright.dev/python/
[2]: https://requests.readthedocs.io/projects/requests-html/en/latest/
[3]: https://pypi.org/project/requests-html-playwright/
[4]: https://github.com/microsoft/playwright-python
