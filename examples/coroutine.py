import asyncio
import base64
import pathlib

import demapi


async def main():
    base_path = pathlib.Path("tests") / "assets"
    conf = demapi.Configure(
        base_photo=base_path / "example.png",
        title="test",
        # explanation="test",
    )
    image = await conf.coroutine_download()
    image.save(base_path / "example.jpg")
    with open(base_path / "example.base64", "wb") as file:
        file.write(base64.b64encode(image.content))


if __name__ == "__main__":
    asyncio.run(main())
