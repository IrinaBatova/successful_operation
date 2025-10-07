import pytest


# Фикстуры для тестирования функции get_mask_card_number в модуле masks.py

@pytest.fixture
def card_number():
    return 7000792289606361

@pytest.fixture
def mask_card_number():
    return "7000 79** **** 6361"

# Фикстуры для тестирования функции mask_account_card в модуле widget.py

@pytest.fixture
def card_type_number():
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def mask_card_type_number():
    return "Visa Platinum 7000 79** **** 6361"

@pytest.fixture
def account_number():
    return  "Счет 1234560000009876"

@pytest.fixture
def mask_account_number():
    return  "Счет ** 9876"

# Фикстуры для тестирования функции get_date в модуле widget.py

@pytest.fixture
def data():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def formatted_date():
    return "11.03.2024"

