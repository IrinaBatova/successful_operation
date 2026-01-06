from typing import Iterator, Any
from pathlib import Path
from src import data_import, utils


def filter_by_currency(list_transactions: list, currency: str) -> Iterator:
    """
    Функция возвращает итератор, который поочередно выдает транзакции с заданным типом валюты (например, USD).
    - param list_transactions: принимает список словарей, представляющих транзакции;
    - param currency: принимает тип валюты в виде строки;
    - yield: возвращает итератор, который поочередно выдает транзакции и в них валюта операции соответствует заданной.
    """

    for transaction in (t for t in list_transactions if find_value(t, currency) == currency):
        yield transaction


def find_value(dictionary: dict, target_value: Any ) -> Any:
    """
    Функция возвращает, заданное значение, если оно есть в заданном словаре
    :param dictionary: принимает словарь (может быть с вложенными словарями)
    :param target_value: принимает значение, которое нужно найти в заданном словаре
    :return: возвращает заданное значение, если оно есть в словаре, если нет возвращает None
    """

    for key, value in dictionary.items():
        if isinstance(value, dict):  # Если значение — это словарь, вызываем функцию рекурсивно
            result = find_value(value, target_value)
            if result:
                return result
        elif value == target_value:
            return value
    return None


def transaction_descriptions(list_transactions: list) -> Iterator:
    """
    Функция возвращает описание каждой операции по очереди.
    - param list_transactions: принимает список словарей, представляющих транзакции;;
    - yield: возвращает итератор, который возвращает описание каждой операции по очереди.
    """

    for transaction in list_transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator:
    """
    Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999:
    - param start: принимает целое число, являющееся началом диапазона;
    - param stop: принимает целое число, являющееся концом диапазона;
    - yield: возвращает строку, номер банковской карты в формате XXXX XXXX XXXX XXXX.
    """

    for num in range(start, stop + 1):
        num_str = f"{num:016d}"
        formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted_number

if __name__ == "__main__":

    # Создаём путь к директории "data", находящейся в той же директории, что и текущий модуль
    file_path = str(Path(__file__).parent.parent / "data")  # метод .parent возвращает родительскую директорию текущего файла
    print(file_path)

    # # Загружаем json файл
    # list_transactions = utils.read_json_file(path_to_file=f"{file_path}/operations.json")
    # print(list_transactions)

    # Загружаем csv файл
    # list_transactions = data_import.read_csv_file(path_to_file=f"{file_path}/transactions.csv")

    # # Загружаем xlsx файл
    list_transactions = data_import.read_excel_file(path_to_file=f"{file_path}/transactions_excel.xlsx")

    # Вызов функции filter_by_currency
    usd_transactions = filter_by_currency(list_transactions, "RUB")
    try:
        for _ in range(25):
            print(next(usd_transactions))
    except StopIteration:
        print("Достигнут конец итератора")