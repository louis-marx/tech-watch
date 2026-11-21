"""Check that the package installs and imports."""

import tech_watch


def test_package_is_importable() -> None:
    assert tech_watch.__doc__ is not None
