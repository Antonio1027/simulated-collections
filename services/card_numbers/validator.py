class CardNumberValidator:
    @staticmethod
    def validate(card_number: str) -> bool:
        if not card_number.isdigit() or len(card_number) != 16:
            return False
        digits = [int(d) for d in card_number]
        total = 0
        reverse_digits = digits[::-1]
        for i, d in enumerate(reverse_digits):
            if i % 2 == 1:
                d = d * 2
                if d > 9:
                    d -= 9
            total += d
        return total % 10 == 0
