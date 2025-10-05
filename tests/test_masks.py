import pytest

from src.masks import get_mask_card_number

def test_get_mask_card_number_1(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number # "7000 79** **** 6361"

@pytest.mark.parametrize("card_number, mask_card_number", [(123, "Введено не 16 цифр" ), (12345678912345678, "Введено не 16 цифр"), (-123456, "Введено число < 0")])
def test_get_mask_card_number_2(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number
