import pytest

from src.widget import get_date, mask_account_card

# Тестирование функции mask_account_card в модуле widget.py


# С применением фикстур
def test_mask_account_card_1(card_type_number: str, mask_card_type_number: str) -> None:
    assert mask_account_card(card_type_number) == mask_card_type_number  # Visa Platinum 7000 79** **** 6361


def test_mask_account_card_3(account_number: str, mask_account_number: str) -> None:
    assert mask_account_card(account_number) == mask_account_number  # "Счет ** 9876"


# С применением параметризации
@pytest.mark.parametrize(
    "card_type_number, mask_card_type_number",
    [
        ("Visa Platinum 123", "Visa Platinum Введено не 16 цифр"),
        ("Visa Platinum 12345678912345678", "Visa Platinum Введено не 16 цифр"),
        ("Visa Classic 7000792289606361", "Visa Classic 7000 79** **** 6361"),
        ("МИР 1597531234567891", "МИР 1597 53** **** 7891"),
        ("Счет123456789654321", "Счет** 4321"),
        ("Счет 12345", "Счет Введено меньше 6 цифр"),
        ("", "Вы ничего не ввели"),
    ],
)
def test_mask_account_card_2(card_type_number: str, mask_card_type_number: str) -> None:
    assert mask_account_card(card_type_number) == mask_card_type_number


# Тестирование функции get_date в модуле widget.py


# С применением фикстур
def test_get_date_1(data: str, formatted_date: str) -> None:
    assert get_date(data) == formatted_date


# С применением параметризации
@pytest.mark.parametrize(
    "data, formatted_date", [("", "Вы ничего не ввели"), ("0000-00-00T02:26:18.671407", "00.00.0000")]
)
def test_get_date_2(data: str, formatted_date: str) -> None:
    assert get_date(data) == formatted_date
