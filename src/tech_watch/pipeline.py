"""Chain the bricks: collect, choose, narrate."""

from collections.abc import Sequence

from tech_watch.choose import choose
from tech_watch.collect import collect
from tech_watch.narrate import narrate


def run(sources: Sequence[str]) -> str:
    """Produce an episode from the sources."""
    articles = collect(sources)
    chosen = choose(articles)
    return narrate(chosen)
