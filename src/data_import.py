import csv
import logging
import os

import pandas as pd

from pathlib import Path
log_path = Path(__file__).parent.parent / "logs" / "data_import.log"

logger = logging.getLogger("data_import")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv_file(path_to_file: str) -> list:
    """
    Функция, которая принимает на вход путь до csv-файла и возвращает список словарей с данными о
    финансовых транзакциях. Если файл пустой, не csv-файл или не найден, функция возвращает пустой список.
    :param path_to_file: путь до csv-файла
    :return: список словарей
    """
    logger.info("Начала выполняться функция read_csv_file")
    list_of_transactions = []

    try:
        _, file_extension = os.path.splitext(path_to_file)  # Получаем расширение файла
        if file_extension == ".csv":  # Проверяем, является ли оно '.csv'

            with open(path_to_file, encoding="utf-8") as f:  # Открываем файл и читаем строки
                logger.info(f"Открываем файл {path_to_file} и читаем строки")

                first_char = f.read(1)
                if not first_char:
                    logger.info(f"Файл {path_to_file} пустой, возвращен пустой список.")
                    print(f"Файл {path_to_file} пустой, возвращен пустой список.")
                    return []

                f.seek(0)  # перемещаем указатель чтения/записи в начало файла

                # Читаем CSV-файл и создаем словари из строк файла
                dicts_of_transactions = csv.DictReader(f, delimiter=";")

                # Складываем словари в список
                for row in dicts_of_transactions:
                    list_of_transactions.append(row)
                # print(type(list_of_transactions))
                logger.info("Функция read_csv_file возвратила список словарей с данными о финансовых транзакциях.")
                return list_of_transactions

        else:
            logger.info(f"Файл {path_to_file} не .csv файл, возвращен пустой список.")
            print(f"Файл {path_to_file} не .csv файл, возвращен пустой список.")
            return []

    except FileNotFoundError as ex:
        logger.error(f"Файл {path_to_file} не найден. Произошла ошибка: {ex}")
        print(f"Файл {path_to_file} не найден, возвращен пустой список.")
        return []

    except Exception as ex:
        logger.error(f"Это общее исключение.{ex}")
        print(f"Это общее исключение.{ex}")

    return []


# print(read_csv_file(path_to_file="../data/transactions.csv"))
# print(read_csv_file(path_to_file="../data/empty.csv"))  # вызов функции для пустого файла
# print(read_csv_file(path_to_file="../data/operations.json")) # вызов функции с не csv файлом
# print(read_csv_file(path_to_file="transactions.csv"))  # вызов функции, если путь до файла указан не верно


def read_excel_file(path_to_file: str) -> list:
    """
    Функция, которая принимает на вход путь до Excel-файла и возвращает список словарей с данными о
    финансовых транзакциях. Если файл пустой, не Excel-файл или не найден, функция возвращает пустой список.
    :param path_to_file: строка - путь до Excel-файла
    :return: список словарей
    """
    logger.info("Начала выполняться функция read_excel_file")

    try:
        _, file_extension = os.path.splitext(path_to_file)  # Получаем расширение файла

        if file_extension == ".xlsx":  # Проверяем, является ли расширение - '.xlsx'
            logger.info(f"Загружаются данные из Excel-файла {path_to_file} в объект DataFrame")
            df_transactions = pd.read_excel(path_to_file)  # читаем Excel-файл и создаем DataFrame

            if df_transactions.empty:
                logger.info(f"Файл {path_to_file} пустой, возвращен пустой список.")
                print(f"Файл {path_to_file} пустой, возвращен пустой список.")
                return []
            else:
                # Трансформируем DataFrame в список словарей с ключами, соответствующими названиям столбцов
                list_of_transactions = df_transactions.to_dict(orient="records")
                logger.info("Функция read_excel_file возвратила список словарей с данными о финансовых транзакциях.")
                return list_of_transactions

        else:
            logger.info(f"Файл {path_to_file} не Excel файл, возвращен пустой список.")
            print(f"Файл {path_to_file} не .xlsx файл, возвращен пустой список.")
            return []

    except FileNotFoundError as ex:
        logger.error(f"Файл {path_to_file} не найден. Произошла ошибка: {ex}")
        print(f"Файл {path_to_file} не найден, возвращен пустой список")
        return []

    except Exception as ex:
        logger.error(f"Это общее исключение.{ex}")
        print(f"Это общее исключение.{ex}")

    return []


# print(read_excel_file(path_to_file="../data/transactions_excel.xlsx"))
# print(read_excel_file(path_to_file="../data/empty.xlsx"))  # вызов функции для пустого файла
# print(read_excel_file(path_to_file="../data/operations.json")) # вызов функции с не Excel файлом
# print(read_excel_file(path_to_file="transactions_excel.xlsx"))  # вызов функции, если путь до файла указан не верно
