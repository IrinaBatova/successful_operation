from typing import Iterator


def filter_by_currency(list_transactions: list, currency: str) -> Iterator:
    """
    Функция возвращает итератор, который поочередно выдает транзакции с заданным типом валюты (например, USD).
    - param list_transactions: принимает список словарей, представляющих транзакции;
    - param currency: принимает тип валюты в виде строки;
    - yield: возвращает итератор, который поочередно выдает транзакции и в них валюта операции соответствует заданной.
    """

    for transaction in (t for t in list_transactions if t["operationAmount"]["currency"]["name"] == currency):
        yield transaction


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
