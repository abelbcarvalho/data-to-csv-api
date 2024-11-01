from src.core.data_to_csv import DataToCsv


class UseCaseJsonToCsv:
    def __init__(self) -> None:
        self.json_to_csv = DataToCsv()

    async def execute(self, data: list[dict[str, any]]) -> str:
        return await self.json_to_csv.json_to_csv(data)
