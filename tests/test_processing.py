import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date

# Тестирование функции filter_by_state

# С применением фикстур


def test_filter_by_state(list_of_dictionaries: list, new_list_of_dictionaries: list) -> None:
    assert filter_by_state(list_of_dictionaries) == new_list_of_dictionaries


def test_filter_by_state_state(list_of_dictionaries: list, new_list_of_dictionaries_state: list) -> None:
    assert filter_by_state(list_of_dictionaries, state="CANCELED") == new_list_of_dictionaries_state


def test_filter_by_state_no_state(list_of_dictionaries: list) -> None:
    assert filter_by_state(list_of_dictionaries, state="CANCEL") == []


def test_filter_by_state_no_state_(list_of_dictionaries: list) -> None:
    assert filter_by_state(list_of_dictionaries, state="") == []


# С применением параметризации

list_of_dictionaries_param = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


@pytest.mark.parametrize(
    "list_, state_param, new_list",
    [
        (list_of_dictionaries_param, "CANCEL", []),
        (list_of_dictionaries_param, "", []),
        (
            list_of_dictionaries_param,
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            list_of_dictionaries_param,
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state_no_state_1(list_: list, state_param: str, new_list: list) -> None:
    assert filter_by_state(list_, state=state_param) == new_list


# Тестирование функции sort_by_date

# С применением фикстур


# Значении параметра ascending по умолчанию (True)
def test_sort_by_date_t(list_of_dictionaries: list, new_list_of_dictionaries_date: list) -> None:
    assert sort_by_date(list_of_dictionaries) == new_list_of_dictionaries_date


# Значении параметра ascending = False
def test_sort_by_date_f(list_of_dictionaries: list, new_list_of_dictionaries_date_false: list) -> None:
    assert sort_by_date(list_of_dictionaries, False) == new_list_of_dictionaries_date_false


# С за двоением даты при значении параметра ascending по умолчанию (True)
def test_sort_by_same_date_t(list_of_dictionaries_same_date: list, new_list_of_dictionaries_same_date_t: list) -> None:
    assert sort_by_date(list_of_dictionaries_same_date) == new_list_of_dictionaries_same_date_t


# С за двоением даты при значении параметра ascending по умолчанию (True)
def test_sort_by_same_date_f(list_of_dictionaries_same_date: list, new_list_of_dictionaries_same_date_f: list) -> None:
    assert sort_by_date(list_of_dictionaries_same_date, False) == new_list_of_dictionaries_same_date_f


def test_sort_by_data_empty() -> None:
    assert sort_by_date([]) == []


# Тестирование функции process_bank_search

# С применением параметризации

list_dict_description = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "description": "Перевод организации"},
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "description": "Перевод с карты на карту",
    },
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "description": "Открытие вклада"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441", "description": ""},
]


new_list_dict_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "description": "Перевод организации"}
]
new_list_dict_2 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "description": "Перевод с карты на карту",
    }
]
new_list_dict_3 = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "description": "Открытие вклада"}
]


@pytest.mark.parametrize(
    "list_dist, search, new_list_dict",
    [
        (list_dict_description, "организации", new_list_dict_1),
        (list_dict_description, "карты", new_list_dict_2),
        (list_dict_description, "открытие", new_list_dict_3),
    ],
)
def test_process_bank_search(list_dist: list[dict], search: str, new_list_dict: list[dict]) -> None:
    assert process_bank_search(list_dist, search) == new_list_dict


categories_list_ = [
    "Перевод со счета на счет",
    "Открытие вклада",
    "Перевод организации",
    "Перевод с карты на карту",
    "Перевод с карты на счет",
]
new_dict_ = {"Открытие вклада": 1, "Перевод организации": 1, "Перевод с карты на карту": 1}


@pytest.mark.parametrize(
    "list_dist, categories_list, new_dict", [(list_dict_description, categories_list_, new_dict_)]
)
def test_process_bank_operations(list_dist: list[dict], categories_list: list, new_dict: dict) -> None:
    assert process_bank_operations(list_dist, categories_list) == new_dict
