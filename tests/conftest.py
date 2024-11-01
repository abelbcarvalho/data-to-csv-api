from dataclasses import dataclass

from src.core.data_to_csv import DataToCsv
from src.prototypes.inter_service_json_csv import InterServiceJsonCsv
from src.services.service_json_csv import ServiceJsonCSV


@dataclass
class VarTestAttrs:
    data_to_csv: DataToCsv = DataToCsv()
    service_json_csv: InterServiceJsonCsv = ServiceJsonCSV()
