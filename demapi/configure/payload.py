import dataclasses

from demapi.connector.file import File


@dataclasses.dataclass
class RequestPayload:
    data: dict
    file: File
