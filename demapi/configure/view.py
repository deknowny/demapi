import dataclasses
import io
import pathlib
import typing

from demapi.configure.params import (
    Color,
    ImageFormat,
    JPEGType,
    PictureType,
    Size,
)
from demapi.configure.payload import RequestPayload
from demapi.connector.coroutine import AiohttpConnector, BaseAsyncConnector
from demapi.connector.file import File
from demapi.connector.sync import BaseSyncConnector, RequestsConnector
from demapi.loader import GeneratedImage, Loader

ImageType: "typing.TypeAlias" = typing.Union[
    str, bytes, pathlib.Path, io.BytesIO
]


@dataclasses.dataclass
class Configure:
    # Base demotivator settings
    base_photo: ImageType
    title: typing.Optional[str] = None
    explanation: typing.Optional[str] = None
    picture_type: PictureType = PictureType.DEMOTIVATOR

    # Text size
    header_size: Size = Size.AUTO
    explanation_size: Size = Size.AUTO

    # Text colors
    header_color: Color = Color.WHITE
    explanation_color: Color = Color.WHITE

    # Output File Settings
    copy_exif_and_metadata: bool = False
    image_format: ImageFormat = ImageFormat.JPEG
    jpeg_type: JPEGType = JPEGType.STANDARD
    jpeg_quality: int = 92  # [0; 1]

    # UploadingSettings
    loader: Loader = Loader()

    def download(
        self, connector: typing.Optional[BaseSyncConnector] = None
    ) -> GeneratedImage:
        payload = self._as_request_payload()
        if connector is None:
            with RequestsConnector.new() as session:
                return self.loader.download(payload, session)
        return self.loader.download(payload, connector)

    async def coroutine_download(
        self, connector: typing.Optional[BaseAsyncConnector] = None
    ) -> GeneratedImage:
        payload = self._as_request_payload()
        if connector is None:
            async with AiohttpConnector.new() as session:
                return await self.loader.coroutine_download(payload, session)
        return await self.loader.coroutine_download(payload, connector)

    def _as_request_payload(self) -> RequestPayload:
        image_bytes = self._resolve_image()
        file = File(content=image_bytes)
        data = {
            "efset1": self.picture_type.value,
            "efset2": self.title,
            "efset3": self.explanation,
            "efset4": self.header_size.value,
            "efset5": self.header_color.value,
            "efset6": self.explanation_size.value,
            "efset7": self.explanation_color.value,
            "jpegtype": self.jpeg_type.value,
            "jpegqual": self.jpeg_quality,
            "outformat": self.image_format.value,
            "jpegmeta": (not self.copy_exif_and_metadata) + 1,
        }
        return RequestPayload(data=data, file=file)

    def _resolve_image(self) -> bytes:
        if isinstance(self.base_photo, bytes):
            return self.base_photo
        elif isinstance(self.base_photo, (str, pathlib.Path)):
            with open(self.base_photo, "rb") as file:
                return file.read()
        elif isinstance(self.base_photo, io.BytesIO):
            return self.base_photo.getvalue()
        else:
            raise TypeError(
                "Can't recognize a `base_image` with type"
                f"`{type(self.base_photo)}`"
            )
