from collections.abc import Callable

from dataclasses import dataclass


@dataclass
class Checkers:
    is_json_invalid: Callable = lambda e: not e
    is_list_dicts: Callable = lambda e: isinstance(e, list) and all(isinstance(i, dict) for i in e)
