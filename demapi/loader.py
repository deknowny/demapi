import dataclasses
import os
import re
import typing

from demapi.configure.payload import RequestPayload
from demapi.connector.sync import BaseSyncConnector


@dataclasses.dataclass
class GeneratedImage:
    content: bytes
    url: str

    def save(self, fp) -> None:
        with open(fp, "wb") as file:
            file.write(self.content)


@dataclasses.dataclass
class Loader:
    response_type: typing.Type[GeneratedImage] = GeneratedImage
    base_uri: str = "https://www.imgonline.com.ua/"
    preview_page_url: str = "demotivational-poster-result.php"
    image_url_pattern: typing.Pattern = re.compile(
        rb"download\.php\?"
        b"file=result_img/"
        rb"imgonline-com-ua-Demotivator-\S+\.jpg"
    )

    def download(
        self, payload: RequestPayload, connector: BaseSyncConnector
    ) -> GeneratedImage:
        preview_page = connector.post(
            self.base_uri + self.preview_page_url,
            data=payload.data,
            file=payload.file,
        )
        image_url = self._fetch_image_url(preview_page)
        image_bytes = connector.get(image_url)
        return GeneratedImage(image_bytes, image_url)

    def _fetch_image_url(self, preview_page) -> str:
        match_obj = self.image_url_pattern.search(preview_page)
        if match_obj is None:
            raise ValueError("Something happened wrong. No image URI found")
        return self.base_uri + match_obj.group(0).decode("UTF-8")
