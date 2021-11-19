import base64
import pathlib

import demapi


def main():
    base_path = pathlib.Path("tests") / "assets"
    conf = demapi.Configure(
        base_photo=base_path / "example.png",
        title="ДАВАЙ ДАВАЙ УРААА",
        explanation="Еще одна бесполезная либа для бесполезного языка"
    )
    image = conf.download()
    with open(base_path / "example.base64", "wb") as file:
        file.write(base64.b64encode(image.content))


if __name__ == "__main__":
    main()
