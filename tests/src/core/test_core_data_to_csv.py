import pytest

from tests.conftest import VarTestAttrs
from tests.mocks.json_csv import json_success, csv_success


@pytest.mark.asyncio
async def test_data_to_csv_json_to_csv_success() -> None:
    resp = await VarTestAttrs.data_to_csv.json_to_csv(json_success)

    assert resp == csv_success
