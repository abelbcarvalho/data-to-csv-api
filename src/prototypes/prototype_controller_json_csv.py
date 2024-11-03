from fastapi import Request

from fastapi.responses import FileResponse

from abc import ABC, abstractmethod


class PrototypeControllerJsonCSV(ABC):
    @abstractmethod
    async def json_to_csv_swap(self, request: Request, response: FileResponse) -> FileResponse:
        pass
