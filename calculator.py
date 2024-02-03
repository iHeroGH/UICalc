class Calculator:

    ROUND_DIGITS = 5

    def __init__(self, max_length: int = -1) -> None:
        self.final_result: float = 0
        self.next_value: float | str = ""
        self.current_operation: str = ""
        self.max_length = max_length

    def append_digit(self, digit: str):
        if not digit.isdigit():
            raise ValueError("Trying to enter a letter as a number.")

        if not self.current_operation:
            self.final_result = 0

        if len(str(self.next_value)) <= self.max_length:
            self.next_value = str(self.next_value) + digit

    def append_decimal(self):
        if not self.next_value:
            self.next_value = "0."
        elif "." not in str(self.next_value):
            self.next_value = str(self.next_value) + "."

    def symbol_to_operation(self, symbol: str) -> None:

        symbol = symbol.lower().strip()

        match(symbol):
            case ".":
                self.append_decimal()
                return
            case "ac":
                self.final_result = 0
                self.next_value = ""
                self.current_operation = ""
                return
            case "+/-":
                if self.next_value:
                    self.next_value = float(self.next_value)
                    if self.next_value.is_integer():
                        self.next_value = int(self.next_value)
                    self.next_value *= -1
                else:
                    self.final_result *= -1
                return
            case "%":
                if self.next_value:
                    self.next_value = float(self.next_value) / 100
                else:
                    self.final_result /= 100
                return

        self.process_current_operation()

        if symbol != "=":
            self.current_operation = symbol

            if not self.final_result:
                if self.next_value:
                    self.final_result = float(self.next_value)
                    self.next_value = ""

    def process_current_operation(self) -> None:
        if not self.next_value or not self.current_operation:
            return

        self.next_value = float(self.next_value)

        match(self.current_operation):
            case "+":
                self.final_result += self.next_value
            case "-":
                self.final_result -= self.next_value
            case "*" | "x":
                self.final_result *= self.next_value
            case "/":
                self.final_result /= self.next_value

        self.next_value = ""
        self.current_operation = ""

    def __str__(self) -> str:
        if self.next_value:
            return str(
                int(self.next_value) if float(self.next_value).is_integer()
                else self.next_value
            )
        else:
            return str(
                int(self.final_result) if self.final_result.is_integer()
                else self.final_result.__round__(Calculator.ROUND_DIGITS)
            )

    def __repr__(self) -> str:
        return f"Calculator({self.final_result}, {self.next_value}, {self.current_operation})"