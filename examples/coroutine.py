import asyncio
import pathlib

import demapi


async def main():
    base_path = pathlib.Path("assets")
    conf = demapi.Configure(
        base_photo=base_path / "example_source.png",
        title="ДАВАЙ ДАВАЙ УРААА",
        explanation="Еще одна бесполезная либа для бесполезного языка",
    )
    image = await conf.coroutine_download()
    image.save(base_path / "example.png")


if __name__ == "__main__":
    asyncio.run(main())
