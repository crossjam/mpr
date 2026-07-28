"""
Archive Data Generator Plugin
Computes archive data once during site generation instead of on every page render
"""
from pelican import signals


def compute_archives(generator):
    """
    Reindex Pelican's already-computed period_archives (year/month groupings)
    into structures the theme can use without any per-page-render work:
      - ARCHIVE_YEARS: dict keyed by int year -> {year, url, count, months}
        (O(1) lookup for a year page's month links)
      - ARCHIVE_YEARS_LIST: same values, sorted descending, for the flat
        archives.html year index
      - CURRENT_ARCHIVE_YEAR: the latest year that has >=1 article, used by
        the sidebar instead of the calendar year so it can never point at an
        empty year
    """
    year_entries = generator.period_archives.get('year', [])
    month_entries = generator.period_archives.get('month', [])

    months_by_year = {}
    for month in month_entries:
        year = month['period_num'][0]
        months_by_year.setdefault(year, []).append({
            'num': month['period_num'][1],
            'name': month['period'][1],
            'url': month['url'],
            'count': len(month['articles']),
        })

    archive_years = {}
    for year_entry in year_entries:
        year = year_entry['period_num'][0]
        months = sorted(
            months_by_year.get(year, []), key=lambda m: m['num'], reverse=True
        )
        archive_years[year] = {
            'year': year,
            'url': year_entry['url'],
            'count': len(year_entry['articles']),
            'months': months,
        }

    archive_years_list = sorted(
        archive_years.values(), key=lambda y: y['year'], reverse=True
    )

    generator.context['ARCHIVE_YEARS'] = archive_years
    generator.context['ARCHIVE_YEARS_LIST'] = archive_years_list
    generator.context['CURRENT_ARCHIVE_YEAR'] = (
        archive_years_list[0]['year'] if archive_years_list else None
    )


def register():
    """Register the plugin with Pelican"""
    signals.article_generator_finalized.connect(compute_archives)
