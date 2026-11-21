"""Chain the bricks: collect, choose, narrate."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from tech_watch.choose import choose
from tech_watch.collect import collect
from tech_watch.narrate import narrate


def run(sources: Sequence[str]) -> str:
    """Produce an episode from the sources."""
    articles = collect(sources)
    chosen = choose(articles)
    return narrate(chosen)


def main() -> None:
    """Print the episode made from the sources file given on the command line."""
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument("sources_file", help="one feed address per line")
    sources_file = Path(parser.parse_args().sources_file)
    sys.stdout.write(run(sources_file.read_text(encoding="utf-8").split()) + "\n")
