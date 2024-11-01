from src.exceptions.exceptions import ModelInvalid
from src.prototypes.inter_service_json_csv import InterServiceJsonCsv
from src.use_cases.use_case_json_to_csv import UseCaseJsonToCsv


class ServiceJsonCSV(InterServiceJsonCsv):
    def __init__(self) -> None:
        self.use_case = UseCaseJsonToCsv()

    async def json_to_csv_swap(self, data: list[dict[str, any]]) -> str:
        first_keys = data[0].keys()

        other_keys = (i.keys() for i in data)

        invalid_keys = tuple(True for keys in other_keys if keys != first_keys)

        if len(invalid_keys) > 0:
            raise ModelInvalid(
                message="all dictionaries must have the same keys"
            )

        return await self.use_case.execute(data)
