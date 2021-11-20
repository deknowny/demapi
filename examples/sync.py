import base64
import pathlib

import demapi


def main():
    base_path = pathlib.Path("assets") / "py-logo"
    conf = demapi.Configure(
        base_photo=base_path / "py-logo.png",
        title="Python",
        explanation="Official Python Logo",
        title_color=demapi.Color.ORANGE,
        explanation_color=demapi.Color.RED
    )
    image = conf.download()
    image.save(base_path / "py-logo-custom-colors.jpg")


if __name__ == "__main__":
    main()
