import pytest

from src.masks import get_mask_card_number, get_mask_account


# Тестирование функции get_mask_card_number в модуле masks.py

def test_get_mask_card_number_1(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number # "7000 79** **** 6361"

@pytest.mark.parametrize("card_number, mask_card_number", [(123, "Введено не 16 цифр" ), (12345678912345678, "Введено не 16 цифр"), (-123456, "Введено число < 0")])
def test_get_mask_card_number_2(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


# Тестирование функции test_get_mask_account в модуле masks.py

@pytest.mark.parametrize("account_number, masked", [(123456789, "** 6789" ), (12345, "Введено меньше 6 цифр"), (-123456, "Введено число < 0")])
def test_get_mask_account(account_number, masked):
    assert get_mask_account(account_number) == masked
