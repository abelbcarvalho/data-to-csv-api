from dataclasses import dataclass

from src.controllers.controller_json_csv import ControllerJsonCSV
from src.prototypes.prototype_controller_json_csv import PrototypeControllerJsonCSV


@dataclass
class Controllers:
    json_to_csv: PrototypeControllerJsonCSV = ControllerJsonCSV()
