from __future__ import annotations
from typing import Callable

class Calculator:

    ROUND_DIGITS: int = 5

    def __init__(self, result: float = 0) -> None:
        self.result = result

    def __add__(self, other: float) -> Calculator:
        return Calculator(self.result + other)

    def __mul__(self, other: float) -> Calculator:
        return Calculator(self.result * other)

    def __sub__(self, other: float) -> Calculator:
        return Calculator(self.result - other)

    def __truediv__(self, other: float) -> Calculator:
        return Calculator(self.result / other)

    @staticmethod
    def symbol_to_operator(
                symbol: str
            ) -> Callable[[Calculator, float], Calculator]:

        symbol_map: dict[str, Callable[[Calculator, float], Calculator]] = {
            "+": Calculator.__add__,
            "-": Calculator.__sub__,
            "*": Calculator.__mul__,
            "x": Calculator.__mul__,
            "/": Calculator.__truediv__
        }

        if symbol in symbol_map:
            return symbol_map[symbol]
        else:
            raise ValueError("The inputted symbol is invalid.")

    def __str__(self) -> str:
        return str(
            int(self.result) if self.result.is_integer()
            else self.result.__round__(Calculator.ROUND_DIGITS)
        )