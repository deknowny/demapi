import pathlib

import demapi


base_path = pathlib.Path("assets")
conf = demapi.Configure(
    base_photo=base_path / "example_source.png",
    title="ДАВАЙ ДАВАЙ УРААА",
    explanation="Еще одна бесполезная либа для бесполезного языка"
)
image = conf.download()
image.save(base_path / "example.png")
