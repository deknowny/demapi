import pathlib

import pytest

import demapi


@pytest.mark.asyncio
async def test_simple(assets_path):
    result_path = assets_path / "example.png"
    config = demapi.Configure(
        base_photo=result_path,
        title="test",
        explanation="test",
    )
    assert (
        config.download().content
        == (await config.coroutine_download()).content
    )
