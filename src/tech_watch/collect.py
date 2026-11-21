"""Collect: fetch the articles of the sources."""

from collections.abc import Sequence

from tech_watch.domain import Article


def collect(sources: Sequence[str]) -> list[Article]:
    """Return the articles published by the sources."""
    # Shell: one placeholder article per source, no network yet.
    return [
        Article(
            identifier=source,
            source=source,
            title=f"Placeholder article from {source}",
            link=source,
            summary="",
        )
        for source in sources
    ]
