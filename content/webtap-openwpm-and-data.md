Title: WebTAP, OpenWPM, and Data
Date: 2017-06-15 21:55
Author: crossjam
Category: Uncategorized
Slug: webtap-openwpm-and-data
Status: published

[WebTAP][1] is a public interest and research project at Princeton University looking into how Web entities track users through a variety of techniques. Based upon rigorous research methods they provide the public at large with insights and policy recommendations regarding online privacy.

[OpenWPM][2] is the software framework that WebTAP uses to conduct a large scale census of websites:
> OpenWPM is a web privacy measurement framework which makes it easy to collect data for privacy studies on a scale of thousands to millions of site. OpenWPM is built on top of Firefox, with automation provided by Selenium. It includes several hooks for data collection, including a proxy, a Firefox extension, and access to Flash cookies. Check out the instrumentation section below for more details.

OpenWPM is the basis of an [extensive academic publication][3] *(which I need to read)*.

The cherry on top is collection documentation and archiving of their [Web census data][4]. According to [a recent blog post][5] on a new notebook wrapper around the Web Census data, they collect 500GB of data on a monthly basis. Juicy!

Great work by computer science and policy researchers on behalf of the greater good.

[1]: https://webtap.princeton.edu/
[2]: https://github.com/citp/OpenWPM/
[3]: http://randomwalker.info/publications/OpenWPM_1_million_site_tracking_measurement.pdf
[4]: https://webtransparency.cs.princeton.edu/webcensus/index.html#data
[5]: https://freedom-to-tinker.com/2017/06/09/web-census-notebook-a-new-tool-for-studying-web-privacy/