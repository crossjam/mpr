# Template Rendering Speedup Implementation Plan

## Problem Summary

With 1,874 articles, the `archives_sidebar.html` template processes all articles on every page render because it's included in `base.html:74`. This creates O(n) processing on every page, resulting in significant performance degradation.

## Implementation Plan

### Phase 1: Pre-compute Archives Data (Recommended - Highest Impact)

**Estimated Impact:** 95-99% reduction in sidebar processing time

#### Step 1.1: Create Python Plugin

Create `plugins/archive_data.py`:

```python
"""
Archive Data Generator Plugin
Computes archive data once during site generation instead of on every page render
"""
from collections import defaultdict
from pelican import signals


def compute_archives(generator):
    """
    Compute archives data from all articles and add to context

    This runs once during generation and makes ARCHIVES_DATA available
    to all templates, eliminating the need to recompute on every page.
    """
    archives = defaultdict(lambda: {'name': '', 'count': 0})

    for article in generator.articles:
        year_month = article.date.strftime('%Y/%m')
        month_name = article.date.strftime('%B %Y')
        archives[year_month]['name'] = month_name
        archives[year_month]['count'] += 1

    # Sort by year/month descending and convert to list of tuples
    generator.context['ARCHIVES_DATA'] = sorted(
        [(k, v) for k, v in archives.items()],
        reverse=True
    )


def register():
    """Register the plugin with Pelican"""
    signals.article_generator_finalized.connect(compute_archives)
```

#### Step 1.2: Update pelicanconf.py

Add the plugin to the PLUGINS list:

```python
# Before (line 8):
PLUGINS = ["summary", "pelican_json_feed", "yaml_metadata"]

# After:
PLUGINS = ["summary", "pelican_json_feed", "yaml_metadata", "archive_data"]
```

#### Step 1.3: Simplify archives_sidebar.html

Replace the entire template with:

```jinja2
{% if ARCHIVES_DATA %}
    <div id="user_meta">
        <h4>Archives</h4>
        <ul>
            {% for year_month, data in ARCHIVES_DATA %}
                <li>
                    <a href="{{ SITEURL }}/{{ year_month }}/">
                        {{ data['name'] }}
                        <span class="count">({{ data['count'] }})</span>
                    </a>
                </li>
            {% endfor %}
        </ul>
    </div>
{% endif %}
```

**Benefits:**
- Computation happens once during generation
- Processing done in Python (much faster than Jinja2)
- Simple template with just iteration (no grouping/counting logic)

---

### Phase 2: Add Jinja2 Caching (Alternative/Additional)

**Estimated Impact:** 90-95% reduction in sidebar processing time

If keeping the logic in templates or as an additional safety measure:

#### Step 2.1: Enable Jinja2 Cache Extension

Add to `pelicanconf.py`:

```python
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.do', 'jinja2.ext.loopcontrols', 'jinja2.ext.cache']
}
```

#### Step 2.2: Wrap Template with Cache

Modify `themes/crossjam-svbhack/templates/includes/archives_sidebar.html`:

```jinja2
{% if dates %}
    {% cache 3600, 'archives_sidebar' %}  {# Cache for 1 hour #}
    <div id="user_meta">
        <h4>Archives</h4>
        {% set dates_by_month = {} %}

        {# Group articles by year and month #}
        {% for article in dates %}
            {% set year_month = article.date.strftime('%Y/%m') %}
            {% set month_name = article.date.strftime('%B %Y') %}
            {% if year_month not in dates_by_month %}
                {% set _ = dates_by_month.update({year_month: {'name': month_name, 'count': 1}}) %}
            {% else %}
                {% set _ = dates_by_month.update({year_month: {'name': month_name, 'count': dates_by_month[year_month]['count'] + 1}}) %}
            {% endif %}
        {% endfor %}

        <ul>
            {% for year_month, data in dates_by_month|dictsort|reverse %}
                <li>
                    <a href="{{ SITEURL }}/{{ year_month }}/">
                        {{ data['name'] }}
                        <span class="count">({{ data['count'] }})</span>
                    </a>
                </li>
            {% endfor %}
        </ul>
    </div>
    {% endcache %}
{% endif %}
```

**Note:** Cache timeout (3600 seconds = 1 hour) can be adjusted based on how frequently content is published.

---

### Phase 3: Optimize Other Template Loops (Lower Priority)

The following loops in `base.html` are less critical but could be optimized if needed:

- Lines 57-58: `MENUITEMS` loop
- Lines 60-62: `pages` loop (if `DISPLAY_PAGES_ON_MENU`)
- Lines 63-65: `categories` loop (if `DISPLAY_CATEGORIES_ON_MENU`)
- Lines 66-68: `LINKS` loop
- Lines 69-71: `SOCIAL` loop

These are likely small datasets and don't require immediate attention unless profiling shows they're problematic.

---

## Testing Plan

### 1. Benchmark Before Changes

```bash
# Time a full site generation
time pelican content -s pelicanconf.py

# Or use Pelican's debug mode
pelican content -s pelicanconf.py --debug
```

### 2. Implement Phase 1 (Python Plugin)

Follow steps 1.1-1.3 above

### 3. Benchmark After Changes

```bash
time pelican content -s pelicanconf.py
```

Compare generation times.

### 4. Verify Output

- Check that archives sidebar appears correctly on multiple pages
- Verify article counts match expected values
- Test archive links navigate correctly

### 5. Test Edge Cases

- Empty blog (no articles)
- Single article
- Articles spanning multiple years
- Multiple articles in same month

---

## Recommended Approach

**Implement Phase 1 (Python Plugin)** as it provides:
- Best performance improvement
- Cleaner separation of concerns (computation in Python, presentation in templates)
- Easier to maintain and debug
- More efficient for 1,874 articles

Phase 2 can be added later if additional caching is desired, or used as a fallback if Phase 1 has issues.

---

## Rollback Plan

If issues arise:

```bash
# Revert to main branch
git checkout main

# Or remove the plugin from pelicanconf.py
# and restore original archives_sidebar.html
```

Keep original `archives_sidebar.html` in version control for easy restoration.

---

## Performance Expectations

Based on 1,874 articles:

| Approach | Processing per Page | Total Site Build Impact |
|----------|-------------------|------------------------|
| Current | ~1,874 iterations | High (repeated on every page) |
| Python Plugin | ~10 iterations | Very Low (computed once) |
| Jinja2 Cache | ~1,874 iterations (cached) | Medium (computed once, then cached) |

For a site with 100+ pages, Python plugin should show 10-50x speedup in overall generation time.
