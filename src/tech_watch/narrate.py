"""Narrate: produce the episode."""

from collections.abc import Sequence

from tech_watch.domain import Article


def narrate(articles: Sequence[Article]) -> str:
    """Return the text of the episode."""
    # Shell: titles only.
    return "\n".join(article.title for article in articles)
