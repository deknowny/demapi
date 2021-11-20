import aiohttp
import pytest
import requests

import demapi


def test_sync_connector(assets_path, result_photo_base):
    result_path = assets_path / "example.png"
    config = demapi.Configure(
        base_photo=result_path,
        title="test",
        explanation="test",
    )

    sync_photo = config.download(
        connector=demapi.RequestsConnector(session=requests.Session())
    )
    assert result_photo_base == sync_photo.as_base64()


@pytest.mark.asyncio
async def test_async_connector(assets_path, result_photo_base):
    result_path = assets_path / "example.png"
    config = demapi.Configure(
        base_photo=result_path,
        title="test",
        explanation="test",
    )
    async with aiohttp.ClientSession() as session:
        async_photo = await config.coroutine_download(
            connector=demapi.AiohttpConnector(session=session)
        )
        assert result_photo_base == async_photo.as_base64()
