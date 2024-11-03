from fastapi import Request

from fastapi.responses import StreamingResponse

from abc import ABC, abstractmethod


class PrototypeControllerJsonCSV(ABC):
    @abstractmethod
    async def json_to_csv_swap(self, request: Request) -> StreamingResponse:
        pass
