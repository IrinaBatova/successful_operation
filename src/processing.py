import re
from collections import Counter
from pathlib import Path

from src import data_import, utils


def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> list:
    """
    Функция отбора словарей по значению ключа "state":
    - param list_of_dictionaries: принимает список словарей;
    - param state: не обязательный, принимает опционально значение для ключа state (по умолчанию 'EXECUTED');
    - return: возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
     выбранному значению.
    """

    new_list_of_dictionaries = []

    for element in list_of_dictionaries:
        if element.get("state") == state:
            new_list_of_dictionaries.append(element)

    if not new_list_of_dictionaries:  # Заданное state не найдено
        return []

    return new_list_of_dictionaries


def sort_by_date(list_of_dictionaries: list, ascending: bool = True) -> list:
    """
    Функция сортировки словарей по значению ключа "date":
    - param list_of_dictionaries: принимает список словарей;
    - param ascending: необязательный параметр, задающий порядок сортировки (по умолчанию — убывание);
    - return: возвращает новый список словарей, отсортированный по дате (date).
    """

    list_of_dictionaries.sort(key=lambda x: x.get("date", ""), reverse=ascending)

    return list_of_dictionaries


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция отбора словарей где в значении ключа "description" есть, заданная строка:
    - param data: принимает список словарей;
    - param search: принимает, заданную для поиска строку;
    - return: возвращает новый список словарей, содержащий только те словари, у которых ключ description содержит
     заданную для поиска строку.
    """

    new_list_of_dictionaries = []
    search = search.lower()

    for operation in data:
        if "description" in operation and re.search(search, str(operation["description"]).lower()):
            new_list_of_dictionaries.append(operation)
    return new_list_of_dictionaries


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция создает словарь, где ключи это названия категорий, а значения это количество операций в каждой категории:
    - param data: принимает список словарей;
    - param categories: принимает список категорий операций;
    - return: возвращает словарь, в котором ключи — названия категорий, значения — кол-во операций в каждой категории.
    """

    # Используем генератор списков: element из списка data при совпадении с 'description' добавляется
    # в список list_categories
    list_categories = [
        element
        for element in categories
        for operation in data
        if "description" in operation and element == operation["description"]
    ]

    # Преобразуем объект Counter в обычный словарь
    dict_categories = dict(Counter(list_categories))

    return dict_categories


if __name__ == "__main__":

    file_path = str(Path(__file__).parent.parent / "data" / "operations.json")
    list_dictionaries_json = utils.read_json_file(path_to_file=file_path)

    file_path = str(Path(__file__).parent.parent / "data" / "transactions.csv")
    list_dictionaries_csv = data_import.read_csv_file(path_to_file=file_path)

    file_path = str(Path(__file__).parent.parent / "data" / "transactions_excel.xlsx")
    list_dictionaries_xlsx = data_import.read_excel_file(path_to_file=file_path)

    # Вызов функции отбора словарей по значению ключа "state"
    print(filter_by_state(list_dictionaries_json))
    print(filter_by_state(list_dictionaries_json, state="CANCELED"))

    # Вызов функции сортировки словарей по значению ключа "date"
    print(sort_by_date(list_dictionaries_json))
    print(sort_by_date(list_dictionaries_json, ascending=False))

    # Вызов функции отбора словарей где в значении ключа "description" есть, заданная строка
    search_bar = "открытие"
    print(process_bank_search(list_dictionaries_json, search_bar))

    # Вызов функции возвращающей словарь, где ключи: названия категорий, значения: количество операций каждой категории
    categories_list = [
        "Перевод со счета на счет",
        "Открытие вклада",
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
    ]
    print(process_bank_operations(list_dictionaries_json, categories_list))
