import pathlib

import pytest


@pytest.fixture(scope="session")
def assets_path():
    return pathlib.Path("tests") / "assets"
