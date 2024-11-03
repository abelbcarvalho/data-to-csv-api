import pytest

from src.exceptions.exceptions import RequestException
from src.utilities.checkers import Checkers


async def example_for_testing_checkers_cases(body: any) -> None:
    if Checkers.is_json_invalid(body):
        raise RequestException("request json cannot be null or empty")

    if not Checkers.is_list_dicts(body):
        raise RequestException("request json must be a list of dicts")


@pytest.mark.asyncio
async def test_example_for_testing_checkers_cases_success() -> None:
    assert not await example_for_testing_checkers_cases([
        dict(name="banana")
    ])


@pytest.mark.asyncio
async def test_example_for_testing_checkers_cases_failure_null_or_empty() -> None:
    with pytest.raises(RequestException) as exc:
        await example_for_testing_checkers_cases([])

    assert str(exc.value) == "request json cannot be null or empty"


@pytest.mark.asyncio
async def test_example_for_testing_checkers_cases_failure_list_of_dicts() -> None:
    with pytest.raises(RequestException) as exc:
        await example_for_testing_checkers_cases([
            77,
            dict(name="apple")
        ])

    assert str(exc.value) == "request json must be a list of dicts"
