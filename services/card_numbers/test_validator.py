import pytest
from services.card_numbers.validator import CardNumberValidator
from services.card_numbers.generator import CardNumberGenerator


def test_validate_credit_card_number():
    valid_card_number = "4111111111111111"
    assert CardNumberValidator.validate(valid_card_number) is True
    invalid_card_number = "4111111111111112"
    assert CardNumberValidator.validate(invalid_card_number) is False
    card_number_generator = CardNumberGenerator()
    generated_card_number = card_number_generator.generate_credit_card_number("4")
    result = CardNumberValidator.validate(generated_card_number)
    assert result is True
