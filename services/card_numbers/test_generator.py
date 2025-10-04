from services.card_numbers.generator import CardNumberGenerator


def test_credit_card_number_generator():
    card_generator = CardNumberGenerator()
    card_number = card_generator.generate_credit_card_number("5")
    assert len(card_number) == 16
    assert card_number.isdigit()
    assert card_number.startswith(("4", "5", "6"))  # Visa, MasterCard, or Discover


def test_generate_credit_card_number():
    card_generator = CardNumberGenerator()
    card_number = card_generator.generate_credit_card_number("4")
    assert len(card_number) == 16
    assert card_number.isdigit()
    assert card_number[0] in ["4", "5", "6"]  # Check if it starts with a valid BIN
    check_digit = card_number[-1]
    partial_number = card_number[:-1]
    assert card_generator._calculate_luhn_check_digit(partial_number) == int(
        check_digit
    )
