class Utils:
    
    @staticmethod
    def reversed(number: int) -> int:
        try:
            return int(str(number)[::-1])
        except ValueError:
            return "Invalid input, please provide a valid integer"

    @staticmethod
    def formatter(number) -> tuple:
        if not isinstance(number, int):
            return "Invalid input, please provide a valid integer"

        try:
            binary_format = bin(number)[2:]
            octal_format = oct(number)[2:]
            return binary_format, octal_format
        except ValueError:
            return "Invalid input, please provide a valid integer"
