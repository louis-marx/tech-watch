"""Narrate: produce the episode."""

from collections.abc import Sequence

from tech_watch.domain import Article


def narrate(articles: Sequence[Article]) -> str:
    """Return the text of the episode."""
    return "\n\n".join(
        f"{article.title}\n{article.source}\n{article.link}" for article in articles
    )
