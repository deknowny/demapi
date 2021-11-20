import pathlib

import pytest


@pytest.fixture(scope="session")
def assets_path():
    return pathlib.Path("tests") / "assets"


@pytest.fixture(scope="session")
def result_photo_base(assets_path):
    return (assets_path / "example.base64").open("rb").read()
