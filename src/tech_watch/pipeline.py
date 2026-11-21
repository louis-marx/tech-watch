"""Chain the bricks: collect, choose, narrate."""

import argparse
from collections.abc import Sequence
from pathlib import Path

from tech_watch.choose import choose
from tech_watch.collect import collect
from tech_watch.narrate import narrate


def run(sources: Sequence[str], episode_file: Path) -> None:
    """Produce an episode from the sources."""
    articles = collect(sources)
    chosen = choose(articles)
    narrate(chosen, episode_file)


def main() -> None:
    """Write the audio episode made from the sources file."""
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument("sources_file", help="one feed address per line")
    parser.add_argument("episode_file", help="audio file to write, e.g. episode.m4a")
    arguments = parser.parse_args()
    sources = Path(arguments.sources_file).read_text(encoding="utf-8").split()
    run(sources, Path(arguments.episode_file))
