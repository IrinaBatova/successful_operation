import pytest

from src.widget import mask_account_card, get_date


# Тестирование функции mask_account_card в модуле widget.py

def test_mask_account_card_1(card_type_number, mask_card_type_number):
    assert mask_account_card(card_type_number) == mask_card_type_number # Visa Platinum 7000 79** **** 6361

def test_mask_account_card_3(account_number, mask_account_number):
    assert mask_account_card(account_number) == mask_account_number # "Счет ** 9876"

@pytest.mark.parametrize("card_type_number, mask_card_type_number", [("Visa Platinum 123", "Visa Platinum Введено не 16 цифр" ),
                                                                     ("Visa Platinum 12345678912345678", "Visa Platinum Введено не 16 цифр"),
                                                                     ("Visa Classic 7000792289606361", "Visa Classic 7000 79** **** 6361"),
                                                                     ("МИР 1597531234567891", "МИР 1597 53** **** 7891"),
                                                                     ("Счет 123456789654321", "Счет ** 4321"),
                                                                     ("Счет 12345", "Счет Введено меньше 6 цифр")])
def test_mask_account_card_2(card_type_number, mask_card_type_number):
    assert mask_account_card(card_type_number) == mask_card_type_number

