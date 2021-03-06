import pytest

import demapi


@pytest.mark.asyncio
async def test_another_photo_entity(assets_path):
    with pytest.raises(demapi.ImageNotFoundError):
        config = demapi.Configure(
            base_photo=b"",
            title="test",
            explanation="test",
        )

        sync_photo = config.download()

    with pytest.raises(demapi.InvalidPhotoTypeError):
        config = demapi.Configure(
            base_photo=123,
            title="test",
            explanation="test",
        )

        sync_photo = config.download()
