from abc import ABC


class SuperException(ABC, Exception):
    code: int

    def __init__(self, message: str) -> None:
        super().__init__(message)


class ModelInvalid(SuperException):
    def __init__(self, message: str, code: int = 400) -> None:
        super().__init__(message)
        self.code = code
