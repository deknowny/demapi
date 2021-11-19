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
