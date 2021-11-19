import base64
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

    sync_photo = config.download()
    async_photo = await config.coroutine_download()

    sync_photo_base = base64.b64encode(sync_photo.content)
    async_photo_base = base64.b64encode(async_photo.content)
    result_photo_base = (assets_path / "example.base64").open("rb").read()

    assert sync_photo_base == async_photo_base == result_photo_base
