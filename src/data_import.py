import os
import csv
import pandas as pd
import json
import logging


logger = logging.getLogger("data_import")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/data_import.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv_file(path_to_file: str) -> list:
    """
    Функция, которая принимает на вход путь до csv-файла и возвращает
    список словарей с данными о финансовых транзакциях. Если файл
    пустой, не csv-файл или не найден, функция возвращает пустой список.
    :param path_to_file: путь до csv-файла
    :return: список словарей
    """
    logger.info('Начала выполняться функция read_csv_file')
    list_of_transactions = []

    try:
        _, file_extension = os.path.splitext(path_to_file)  # Получаем расширение файла
        if file_extension == '.csv':  # Проверяем, является ли оно '.csv'

            with open(path_to_file, encoding="utf-8") as f:  # Открываем файл и читаем строки
                logger.info(f"Открываем файл {path_to_file} и читаем строки")

                first_char = f.read(1)
                if not first_char:
                    logger.info(f"Файл {path_to_file} пустой, возвращен пустой список.")
                    print("Файл пустой")
                    return []

                f.seek(0)  # перемещаем указатель чтения/записи в начало файла
                dicts_of_transactions = csv.DictReader(f, delimiter=';') # читаем CSV-файл и создаем словари из строк файла
                # print(type(dicts_of_transactions))

                # Складываем словари в список
                for row in dicts_of_transactions:
                    list_of_transactions.append(row)
                # print(type(list_of_transactions))
                return list_of_transactions

        else:
            logger.info(f"Файл {path_to_file} не CSV файл, функция read_csv_file возвратила пустой список.")
            print("Это не CSV файл")
            return []

    except FileNotFoundError as ex:
        logger.error(f"Файл {path_to_file} не найден. Произошла ошибка: {ex}")
        print(f"Файл {path_to_file} не найден")
        return []

    except Exception as ex:
        logger.error(f"Это общее исключение.{ex}")
        print(f"Это общее исключение.{ex}")

    # return []

print(read_csv_file(path_to_file="../data/transactions.csv"))
# print(read_csv_file(path_to_file="../data/empty.csv"))  # вызов функции для пустого файла
# print(read_csv_file(path_to_file="../data/operations.json")) # вызов функции с не csv файлом
# print(read_csv_file(path_to_file="transactions.csv"))  # вызов функции, если путь до файла указан не верно

def read_Excel_file(path_to_file: str) -> list:
    """
    Функция, которая принимает на вход путь до Excel-файла и возвращает
    список словарей с данными о финансовых транзакциях. Если файл
    пустой, не Excel-файл или не найден, функция возвращает пустой список.
    :param path_to_file: путь до Excel-файла
    :return: список словарей
    """
    logger.info('Начала выполняться функция read_Excel_file')
    list_of_transactions = []

    try:
        _, file_extension = os.path.splitext(path_to_file)  # Получаем расширение файла
        if file_extension == '.xlsx':  # Проверяем, является ли оно '.xlsx'

            with open(path_to_file, encoding="utf-8") as f:  # Открываем файл и читаем строки
                logger.info(f"Открываем файл {path_to_file} и читаем строки")

                first_char = f.read(1)
                if not first_char:
                    logger.info(f"Файл {path_to_file} пустой, возвращен пустой список.")
                    print("Файл пустой")
                    return []

                f.seek(0)  # перемещаем указатель чтения/записи в начало файла
                dicts_of_transactions = csv.DictReader(f, delimiter=';') # читаем CSV-файл и создаем словари из строк файла

                # Складываем словари в список
                for row in dicts_of_transactions:
                    list_of_transactions.append(row)
                print(type(list_of_transactions))
                return list_of_transactions

        else:
            logger.info(f"Файл {path_to_file} не Excel файл, функция read_Excel_file возвратила пустой список.")
            print("Это не Excel файл")
            return []

    except FileNotFoundError as ex:
        logger.error(f"Файл {path_to_file} не найден. Произошла ошибка: {ex}")
        print(f"Файл {path_to_file} не найден")
        return []

    except Exception as ex:
        logger.error(f"Это общее исключение.{ex}")
        print(f"Это общее исключение.{ex}")

    # return []

# print(read_Excel_file(path_to_file="../data/transactions_excel.xlsx"))
# print(read_Excel_file(path_to_file="../data/empty.xlsx"))  # вызов функции для пустого файла
# print(read_Excel_file(path_to_file="../data/operations.json")) # вызов функции с не Excel файлом
# print(read_Excel_file(path_to_file="transactions_excel.xlsx"))  # вызов функции, если путь до файла указан не верно