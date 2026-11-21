"""Narrate: produce the episode."""

import subprocess
from collections.abc import Sequence
from pathlib import Path

from tech_watch.domain import Article

# ponytail: macOS only, swap for a cross-platform engine when others install the tool
SAY = "/usr/bin/say"


def narrate(articles: Sequence[Article], episode_file: Path) -> None:
    """Write the audio episode telling the articles."""
    text = "\n\n".join(f"{article.title}. {article.source}." for article in articles)
    speak(text, episode_file)


def speak(text: str, audio_file: Path) -> None:
    """Write the text spoken aloud to an AAC audio file."""
    # S603: no shell, and the text goes through stdin, never as an argument.
    subprocess.run(  # noqa: S603
        [SAY, "--data-format=aac", "-o", str(audio_file), "-f", "-"],
        input=text,
        text=True,
        check=True,
    )
