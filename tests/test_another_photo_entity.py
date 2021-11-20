import io

import pytest

import demapi


@pytest.mark.asyncio
async def test_another_photo_entity(assets_path):
    photo_path = assets_path / "example.png"
    sync_photo2 = photo_path.open("rb")
    sync_photo3 = photo_path.open("rb").read()
    sync_photo4 = str(photo_path)
    sync_photo5 = io.BytesIO(photo_path.open("rb").read())

    async_photo2 = photo_path.open("rb")
    async_photo3 = photo_path.open("rb").read()
    async_photo4 = str(photo_path)

    sync_config1 = demapi.Configure(base_photo=photo_path)
    sync_config2 = demapi.Configure(base_photo=sync_photo2)
    sync_config3 = demapi.Configure(base_photo=sync_photo3)
    sync_config4 = demapi.Configure(base_photo=sync_photo4)
    sync_config5 = demapi.Configure(base_photo=sync_photo5)

    async_config1 = demapi.Configure(base_photo=photo_path)
    async_config2 = demapi.Configure(base_photo=async_photo2)
    async_config3 = demapi.Configure(base_photo=async_photo3)
    async_config4 = demapi.Configure(base_photo=async_photo4)

    assert (
        sync_config1.download().as_base64()
        == sync_config2.download().as_base64()
        == sync_config3.download().as_base64()
        == sync_config4.download().as_base64()
        == sync_config5.download().as_base64()
    )
    assert (
        (await async_config1.coroutine_download()).as_base64()
        == (await async_config2.coroutine_download()).as_base64()
        == (await async_config3.coroutine_download()).as_base64()
        == (await async_config4.coroutine_download()).as_base64()
    )
