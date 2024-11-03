from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import StreamingResponse

from src.exceptions.exceptions import SuperException, RequestException
from src.prototypes.prototype_controller_json_csv import PrototypeControllerJsonCSV
from src.prototypes.prototype_service_json_csv import PrototypeServiceJsonCsv
from src.services.service_json_csv import ServiceJsonCSV
from src.utilities.checkers import Checkers


class ControllerJsonCSV(PrototypeControllerJsonCSV):
    body: any

    def __init__(self) -> None:
        self.service: PrototypeServiceJsonCsv = ServiceJsonCSV()

    async def json_to_csv_swap(self, request: Request) -> StreamingResponse:
        try:
            await self.__valid_body__(request)

            csv_file = await self.service.json_to_csv_swap(self.body)

            return StreamingResponse(csv_file, media_type="text/csv")
        except SuperException as se:
            raise HTTPException(
                status_code=se.code,
                detail=str(se)
            )
        finally:
            self.body = any("")

    async def __valid_body__(self, request: Request) -> None:
        if not Checkers.is_json_invalid(request.json()):
            raise RequestException("request json cannot be null or empty")

        self.body = await request.json()

        if not Checkers.is_list_dicts(self.body):
            raise RequestException("request json must be a list of dicts")
