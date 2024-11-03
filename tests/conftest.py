from dataclasses import dataclass

from src.core.data_to_csv import DataToCsv
from src.prototypes.prototype_service_json_csv import PrototypeServiceJsonCsv
from src.services.service_json_csv import ServiceJsonCSV


@dataclass
class VarTestAttrs:
    data_to_csv: DataToCsv = DataToCsv()
    service_json_csv: PrototypeServiceJsonCsv = ServiceJsonCSV()
