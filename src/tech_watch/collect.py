"""Collect: fetch the articles of the sources."""

from collections.abc import Sequence
from typing import cast
from urllib.request import Request, urlopen
from xml.etree import ElementTree

from tech_watch.domain import Article

USER_AGENT = "tech-watch"
FETCH_TIMEOUT_SECONDS = 30


def collect(sources: Sequence[str]) -> list[Article]:
    """Return the articles published by the sources."""
    return [article for source in sources for article in parse_feed(fetch(source))]


def fetch(source: str) -> bytes:
    """Return the content of the feed at the address of the source."""
    if not source.startswith(("http://", "https://")):
        message = f"not an HTTP address: {source}"
        raise ValueError(message)
    # S310: the scheme is checked above, so no file:// or custom scheme gets here.
    request = Request(source, headers={"User-Agent": USER_AGENT})  # noqa: S310
    with urlopen(request, timeout=FETCH_TIMEOUT_SECONDS) as response:  # noqa: S310
        # urlopen is typed as returning Any; an HTTP response reads as bytes.
        return cast("bytes", response.read())


def parse_feed(content: bytes) -> list[Article]:
    """Return the articles of an RSS 2.0 feed."""
    # S314: xml.etree does not resolve external entities, and expat blocks
    # entity expansion bombs since 2.4.1.
    root = ElementTree.fromstring(content)  # noqa: S314
    channel = root.find("channel")
    if root.tag != "rss" or channel is None:
        message = f"not an RSS 2.0 feed: root element is <{root.tag}>"
        raise ValueError(message)
    source = channel.findtext("title", default="")
    return [_article(item, source) for item in channel.iter("item")]


def _article(item: ElementTree.Element, source: str) -> Article:
    return Article(
        source=source,
        title=item.findtext("title", default=""),
        link=item.findtext("link", default=""),
    )
