"""Choose: keep what goes into the episode."""

from collections.abc import Sequence

from tech_watch.domain import Article


def choose(articles: Sequence[Article]) -> list[Article]:
    """Return the articles to tell."""
    # Shell: every article.
    return list(articles)
