"""Check that the chain runs from end to end, without network nor voice."""

from pathlib import Path

import pytest

from tech_watch import collect, narrate
from tech_watch.pipeline import run


def test_run_speaks_titles_and_sources(
    monkeypatch: pytest.MonkeyPatch, rss_feed: bytes
) -> None:
    monkeypatch.setattr(collect, "fetch", lambda _source: rss_feed)
    spoken: list[str] = []
    monkeypatch.setattr(narrate, "speak", lambda text, _file: spoken.append(text))

    run(["https://example.org/feed"], Path("episode.m4a"))

    assert spoken == ["First article. Example feed.\n\nSecond article. Example feed."]
