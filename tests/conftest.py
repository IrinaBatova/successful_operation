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

# Фикстуры для тестирования функции filter_by_state в модуле processing.py

@pytest.fixture
def list_of_dictionaries():
    list_of_dictionaries = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return list_of_dictionaries

@pytest.fixture
def new_list_of_dictionaries():
    new_list_of_dictionaries = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    return new_list_of_dictionaries

@pytest.fixture
def new_list_of_dictionaries_state():
    new_list_of_dictionaries_state = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    return new_list_of_dictionaries_state