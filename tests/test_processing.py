import pytest

from src.processing import filter_by_state, sort_by_date


# Тестирование функции filter_by_state в модуле processing.py

# С применением фикстур
def test_filter_by_state(list_of_dictionaries, new_list_of_dictionaries):
    assert filter_by_state(list_of_dictionaries) == new_list_of_dictionaries

def test_filter_by_state_state(list_of_dictionaries, new_list_of_dictionaries_state):
    assert filter_by_state(list_of_dictionaries, state="CANCELED") == new_list_of_dictionaries_state

def test_filter_by_state_no_state(list_of_dictionaries):
    assert filter_by_state(list_of_dictionaries, state="CANCEL") == []

def test_filter_by_state_no_state_(list_of_dictionaries):
    assert filter_by_state(list_of_dictionaries, state = "") == []

# С применением параметризации

list_of_dictionaries_param = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

@pytest.mark.parametrize("list_, state_param, new_list", [(list_of_dictionaries_param, "CANCEL", []),
                                                          (list_of_dictionaries_param, "", []),
                                                          (list_of_dictionaries_param, "CANCELED", [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                                                                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
                                                          (list_of_dictionaries_param, "EXECUTED", [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])])

def test_filter_by_state_no_state(list_, state_param, new_list):
    assert filter_by_state(list_, state = state_param) == new_list

# Тестирование функции sort_by_date в модуле processing.py

# С применением фикстур

def test_sort_by_date_t(list_of_dictionaries, new_list_of_dictionaries_date):# значении параметра ascending по умолчанию (True)
    assert sort_by_date(list_of_dictionaries) == new_list_of_dictionaries_date

def test_sort_by_date_f(list_of_dictionaries, new_list_of_dictionaries_date_false):# значении параметра ascending = False
    assert sort_by_date(list_of_dictionaries, False) == new_list_of_dictionaries_date_false

def test_sort_by_same_date_t(list_of_dictionaries_same_date, new_list_of_dictionaries_same_date_t):# с за двоением даты при значении параметра ascending по умолчанию (True)
    assert sort_by_date(list_of_dictionaries_same_date) == new_list_of_dictionaries_same_date_t

def test_sort_by_same_date_f(list_of_dictionaries_same_date, new_list_of_dictionaries_same_date_f):# с за двоением даты при значении параметра ascending по умолчанию (True)
    assert sort_by_date(list_of_dictionaries_same_date, False) == new_list_of_dictionaries_same_date_f

def test_sort_by_data_empty():
    assert sort_by_date([]) == []