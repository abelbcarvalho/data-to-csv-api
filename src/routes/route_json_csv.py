from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from src.utilities.controllers import Controllers

route_json_csv = APIRouter(prefix="/api/v1/json-csv")


@route_json_csv.post("/file")
async def json_to_csv_file_swap(request: Request) -> StreamingResponse:
    return await Controllers.json_to_csv.json_to_csv_swap(request)
