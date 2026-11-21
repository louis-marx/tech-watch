"""Check that the chain runs from end to end."""

from tech_watch.pipeline import run

SOURCES = ("https://example.org/feed",)


def test_run_produces_an_episode() -> None:
    episode = run(SOURCES)

    assert SOURCES[0] in episode
