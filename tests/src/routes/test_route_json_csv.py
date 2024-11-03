from json import dumps

import pytest
from httpx import AsyncClient, ASGITransport

from app import app
from tests.mocks.json_csv import (
    json_success,
    csv_success,
    json_fail_one,
)

base_url = "http://testing:4040/api/v1/json-csv/"


@pytest.mark.asyncio
async def test_route_json_csv_success() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=base_url) as client:
        response = await client.post(
            "/file",
            content=dumps(json_success)
        )

    assert response.status_code == 200
    assert response.content == bytes(csv_success, "utf-8")


@pytest.mark.asyncio
async def test_route_json_csv_failure_case_one() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=base_url) as client:
        response = await client.post(
            "/file",
            content=dumps([])
        )

    assert response.status_code == 400

    message = "request json cannot be null or empty"
    compare = response.json()["detail"]

    assert message == compare


@pytest.mark.asyncio
async def test_route_json_csv_failure_case_two() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=base_url) as client:
        response = await client.post(
            "/file",
            content=dumps([
                dict(name="umbrella"),
                77
            ])
        )

    assert response.status_code == 400

    compare = "request json must be a list of dicts"
    message = response.json()["detail"]

    assert message == compare


@pytest.mark.asyncio
async def test_route_json_csv_failure_case_three() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=base_url) as client:
        response = await client.post(
            "/file",
            content=dumps(json_fail_one)
        )

    assert response.status_code == 400

    compare = "all dictionaries must have the same keys"
    message = response.json()["detail"]

    assert message == compare
