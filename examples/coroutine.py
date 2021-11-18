import asyncio
import pathlib

import demapi


async def main():
    base_path = pathlib.Path("tests") / "assets"
    conf = demapi.Configure(
        base_photo=base_path / "example_source.png",
        title="test",
        explanation="test",
    )
    image = await conf.coroutine_download()
    image.save(base_path / "example.jpg")


if __name__ == "__main__":
    asyncio.run(main())
