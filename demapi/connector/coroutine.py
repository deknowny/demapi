from __future__ import annotations

import abc
import contextlib
import dataclasses
import ssl
import typing

import aiohttp
import certifi

from demapi.connector.file import File

ssl_context = ssl.create_default_context(cafile=certifi.where())
BaseAsyncConnectorType = typing.TypeVar("BaseAsyncConnectorType")


class BaseAsyncConnector(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def new(
        cls: typing.Type[BaseAsyncConnectorType],
    ) -> typing.ContextManager[BaseAsyncConnectorType]:
        pass  # pragma: no cover

    @abc.abstractmethod
    async def post(self, url: str, data: dict, file: File) -> bytes:
        pass  # pragma: no cover

    @abc.abstractmethod
    async def get(self, url: str) -> bytes:
        pass  # pragma: no cover


@dataclasses.dataclass
class AiohttpConnector(BaseAsyncConnector):
    session: aiohttp.ClientSession

    @classmethod
    @contextlib.asynccontextmanager
    async def new(cls) -> AiohttpConnector:
        session = aiohttp.ClientSession(
            skip_auto_headers={"User-Agent"},
        )
        self = cls(session=session)
        async with session:
            yield self

    async def post(self, url: str, data: dict, file: File) -> bytes:
        form_data = aiohttp.FormData()
        form_data.add_field(
            name=file.multipart_name,
            value=file.content,
            content_type="multipart/form-data",
        )
        for key, value in data.items():
            form_data.add_field(name=key, value=str(value))
        async with self.session.post(
            url, data=form_data, ssl=ssl_context
        ) as response:
            return await response.read()

    async def get(self, url: str) -> bytes:
        async with self.session.get(url, ssl=ssl_context) as response:
            return await response.read()
