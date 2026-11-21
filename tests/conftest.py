"""Fixtures shared by the tests."""

import pytest


@pytest.fixture
def rss_feed() -> bytes:
    return b"""<?xml version="1.0"?>
<rss version="2.0">
  <channel>
    <title>Example feed</title>
    <link>https://example.org</link>
    <item>
      <title>First article</title>
      <link>https://example.org/first</link>
    </item>
    <item>
      <title>Second article</title>
      <link>https://example.org/second</link>
    </item>
  </channel>
</rss>"""
