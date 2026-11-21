"""Check that the chain runs from end to end, without network."""

import pytest

from tech_watch import collect
from tech_watch.pipeline import run


def test_run_produces_an_episode(
    monkeypatch: pytest.MonkeyPatch, rss_feed: bytes
) -> None:
    monkeypatch.setattr(collect, "fetch", lambda _source: rss_feed)

    episode = run(["https://example.org/feed"])

    assert episode.startswith(
        "First article\nExample feed\nhttps://example.org/first\n\nSecond article\n"
    )
