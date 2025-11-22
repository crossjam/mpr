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
