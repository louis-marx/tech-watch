"""Types shared by the bricks of the engine."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Article:
    """An article published by a source."""

    source: str
    title: str
    link: str
