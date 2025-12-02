import os
import json
from src import external_api
from typing import Any, Callable, Optional


def read_json_file(path_to_file: str) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список.
    :param path_to_file: путь до JSON-файла
    :return: список
    """

    try:
        #if os.path.isfile(path_to_file): # определяем, существует ли файл
        with open(path_to_file, encoding='utf-8') as f: # Открываем файл и читаем строки
            first_char = f.read(1)
            if not first_char:
                print("Файл пустой")
                return []
            f.seek(0) # перемещаем указатель чтения/записи в начало файла
            list_of_transactions = json.load(f)
            if type(list_of_transactions) is list:
                return list_of_transactions
            else:
                return []

    except FileNotFoundError:
        print("Файл не найден")
        return []

    except json.JSONDecodeError as e:
        print("Ошибка декодирования JSON!")
        print(f"Сообщение об ошибке: {e.msg}")
        print(f"Строка: {e.lineno}, колонка: {e.colno}")

    except Exception as e:
        print(e)

# transactions_1 = read_json_file(path_to_file="../data/operations.json")
# print(type(transactions_1))
# transactions_2 = read_json_file(path_to_file="../data/empty.json") # пустой файл
# print(transactions_1)
# print("Ok")
# print(transactions_2)


def transaction_amount(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях
    :param transaction:
    :return:
    """

    try:
        if transaction['operationAmount']['currency']['code'] == "RUB":
            amount_rub = float((transaction.get('operationAmount')).get('amount')) # получаем сумму в рублях
            #print(f"{amount_rub} руб.")
        else:
            amount_no_rub = (transaction.get('operationAmount')).get('amount')  # получаем сумму не в рублях
            currency = ((transaction.get('operationAmount')).get('currency')).get('code')  # получаем тип валюты
            amount_rub = external_api.currency_conversion(amount_no_rub, currency) # вызываем функцию конвертации валюты
            #print(f"{amount_no_rub} {currency} конвертировано в: {amount_rub} руб.")
        return amount_rub

    except Exception as e:
        print(e)


# transactions_2 = [
#     {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {
#             "amount": "31957.58",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589"
#     },
#     {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {
#             "amount": "8221.37",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "MasterCard 7158300734726758",
#         "to": "Счет 35383033474447895560"
#     }
# ]
#
# for el in transactions_2:
#     p = transaction_amount(el)
#     # print(p)
#     # print(el)


# print(read_json_file(path_to_file="../data/empty.json")) # вызов функции для пустого файла
# print(read_json_file(path_to_file="../data/operations.json"))
# print(read_json_file(path_to_file="operations.json")) # вызов функции, когда путь до файла указан не верно
