"""Check the reading of feeds, without network."""

import pytest

from tech_watch.collect import fetch, parse_feed
from tech_watch.domain import Article

ATOM_FEED = b'<feed xmlns="http://www.w3.org/2005/Atom"><title>Atom</title></feed>'


def test_parse_feed_returns_the_articles_of_an_rss_feed(rss_feed: bytes) -> None:
    first, second = parse_feed(rss_feed)

    assert first == Article(
        source="Example feed",
        title="First article",
        link="https://example.org/first",
        summary="First summary",
    )
    assert second.summary == ""


def test_parse_feed_rejects_a_feed_that_is_not_rss() -> None:
    with pytest.raises(ValueError, match=r"not an RSS 2\.0 feed"):
        parse_feed(ATOM_FEED)


def test_fetch_rejects_an_address_that_is_not_http() -> None:
    with pytest.raises(ValueError, match="not an HTTP address"):
        fetch("file:///etc/passwd")
