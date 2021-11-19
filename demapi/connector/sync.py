from __future__ import annotations

import abc
import contextlib
import dataclasses
import typing

import requests

from demapi.connector.file import File

BaseSyncConnectorType = typing.TypeVar("BaseSyncConnectorType")


class BaseSyncConnector(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def new(
        cls: typing.Type[BaseSyncConnectorType],
    ) -> typing.ContextManager[BaseSyncConnectorType]:
        pass  # pragma: no cover

    @abc.abstractmethod
    def post(self, url: str, data: dict, file: File) -> bytes:
        pass  # pragma: no cover

    @abc.abstractmethod
    def get(self, url: str) -> bytes:
        pass  # pragma: no cover


@dataclasses.dataclass
class RequestsConnector(BaseSyncConnector):
    session: requests.Session

    @classmethod
    @contextlib.contextmanager
    def new(cls) -> RequestsConnector:
        session = requests.Session()
        self = cls(session=session)
        with session:
            yield self

    def post(self, url: str, data: dict, file: File) -> bytes:
        file_obj = {file.multipart_name: (file.name, file.content)}
        return self.session.post(
            url,
            data=data,
            files=file_obj,
        ).content

    def get(self, url: str) -> bytes:
        return self.session.get(url).content
