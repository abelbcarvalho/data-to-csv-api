import pytest

from src.exceptions.exceptions import ModelInvalid
from tests.conftest import VarTestAttrs
from tests.mocks.json_csv import (
    json_success,
    csv_success,
    json_fail_one,
    json_fail_two,
)


@pytest.mark.asyncio
async def test_service_data_to_csv_success() -> None:
    response = await VarTestAttrs.service_json_csv.json_to_csv_swap(json_success)

    assert response == csv_success


@pytest.mark.asyncio
async def test_service_data_to_csv_fail_case_one() -> None:
    with pytest.raises(ModelInvalid) as exc_info:
        await VarTestAttrs.service_json_csv.json_to_csv_swap(json_fail_one)

    assert str(exc_info.value) == "all dictionaries must have the same keys"


@pytest.mark.asyncio
async def test_service_data_to_csv_fail_case_two() -> None:
    with pytest.raises(ModelInvalid) as exc_info:
        await VarTestAttrs.service_json_csv.json_to_csv_swap(json_fail_two)

    assert str(exc_info.value) == "all dictionaries must have the same keys"
