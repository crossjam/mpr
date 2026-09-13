Title: Search MPR
Date: 2025-06-13
Author: C. Ross Jam
Slug: mpr_search
Status: published

<link href="/pagefind/pagefind-modular-ui.css" rel="stylesheet">
<script src="/pagefind/pagefind-modular-ui.js"></script>
<div id="search-input"></div>
<div id="search-results"></div>
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        const instance = new PagefindModularUI.Instance();
        instance.add(new PagefindModularUI.Input({
            containerElement: "#search-input"
        }));
        const results = document.querySelector("#search-results");
        let searchID = 0;
        let pagefind;

        const renderResult = (result) => {
            const item = document.createElement("article");
            const title = document.createElement("h2");
            const link = document.createElement("a");
            link.href = result.url;
            link.textContent = result.meta.title;
            title.append(link);
            item.append(title);

            if (result.meta.date) {
                const date = document.createElement("time");
                date.textContent = result.meta.date;
                item.append(date);
            }

            const subResults = (result.sub_results || [])
                .filter((subResult) => subResult.url !== result.url);
            if (!subResults.length && result.excerpt) {
                const excerpt = document.createElement("p");
                excerpt.innerHTML = result.excerpt;
                item.append(excerpt);
            }

            if (subResults.length) {
                const sections = document.createElement("ul");
                subResults.forEach((subResult) => {
                    const section = document.createElement("li");
                    const sectionLink = document.createElement("a");
                    sectionLink.href = subResult.url;
                    sectionLink.textContent = subResult.title;
                    section.append(sectionLink);
                    const sectionExcerpt = document.createElement("p");
                    sectionExcerpt.innerHTML = subResult.excerpt;
                    section.append(sectionExcerpt);
                    sections.append(section);
                });
                item.append(sections);
            }

            return item;
        };

        instance.on("search", async (term) => {
            const currentSearchID = ++searchID;
            results.replaceChildren();
            if (!term) {
                return;
            }

            pagefind ??= await import("/pagefind/pagefind.js");
            const search = await pagefind.search(term, {
                sort: { date: "desc" }
            });
            const resultData = await Promise.all(
                search.results.map((result) => result.data())
            );
            if (currentSearchID !== searchID) {
                return;
            }
            resultData.forEach((result) => results.append(renderResult(result)));
        });
    });
</script>
