import base64
import os.path

import pytest

import demapi


@pytest.mark.asyncio
async def test_simple(assets_path, result_photo_base):
    res_path = assets_path / "test.jpg"
    try:
        result_path = assets_path / "example.png"
        config = demapi.Configure(
            base_photo=result_path,
            title="test",
            explanation="test",
        )

        sync_photo = config.download()
        sync_photo.save(res_path)
        assert res_path.exists()
    finally:
        if res_path.exists():
            res_path.unlink()  # missing_ok for ^3.8
