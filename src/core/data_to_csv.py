import pandas as pd


class DataToCsv:
    async def json_to_csv(self, data: list[dict[str, any]]) -> any:
        data_frame = pd.DataFrame(data)

        csv = data_frame.to_csv(index=False)

        return csv.replace("\r\n", "\n")
