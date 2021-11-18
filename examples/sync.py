import pathlib

import demapi


base_path = pathlib.Path("assets")
conf = demapi.Configure(
    base_photo=base_path / "example_source.png",
    title="Yo",
    explanation="demotivator!!!!"
)
image = conf.download()
image.save(base_path / "example.png")
