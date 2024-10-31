import pytest

from src.core.data_to_csv import DataToCsv
from tests.mocks.json_csv import json_success, csv_success


data_to_csv = DataToCsv()


@pytest.mark.asyncio
async def test_data_to_csv_json_to_csv_success() -> None:
    resp = await data_to_csv.json_to_csv(json_success)

    assert resp == csv_success
