import random
from services.card_numbers.validator import CardNumberValidator


class CardNumberGenerator:
    def __init__(self):
        self.bins = ["4", "5", "6"]  # BINs for Visa, MasterCard, Discover

    def generate_credit_card_number(self, bin: str = None) -> str:
        if bin not in self.bins:
            raise ValueError(f"Invalid BIN. Choose from {self.bins}")
        number = [bin] + [str(random.randint(0, 9)) for _ in range(14)]
        partial_number = "".join(number)
        check_digit = self._calculate_luhn_check_digit(partial_number)
        card_number = partial_number + str(check_digit)
        if not CardNumberValidator.validate(card_number):
            return self.generate_credit_card_number(bin)
        return card_number

    def _calculate_luhn_check_digit(self, number: str) -> int:
        digits = [int(d) for d in number]
        for i in range(len(digits) - 2, -1, -2):
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            digits[i] = doubled
        total = sum(digits)
        return (10 - (total % 10)) % 10
