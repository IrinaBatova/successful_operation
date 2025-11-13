import os
import json
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
        #if os.path.isfile(path_to_file): # определяем, указывает ли заданный путь на существующий
            # файл
        with open(path_to_file, encoding='utf-8') as f: # Открываем файл и читаем строки
            first_char = f.read(1)
            if not first_char:
                print("Файл пустой")
                return []
            f.seek(0)
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

print(read_json_file(path_to_file="../data/empty.json"))
print(read_json_file(path_to_file="../data/operations.json"))
print(read_json_file(path_to_file="operations.json"))
