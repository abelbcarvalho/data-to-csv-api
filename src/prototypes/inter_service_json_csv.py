from abc import ABC, abstractmethod


class InterServiceJsonCsv(ABC):
    @abstractmethod
    async def json_to_csv_swap(self, data: list[dict[str, any]]) -> str:
        pass
