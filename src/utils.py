import json
import logging

from src import external_api

from pathlib import Path
log_path = Path(__file__).parent.parent / "logs" / "utils.log"

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(path_to_file: str) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях. Если файл
    пустой, содержит не список или не найден, функция возвращает пустой список.
    :param path_to_file: путь до JSON-файла
    :return: список
    """

    logger.info("Начала выполняться функция read_json_file")
    try:
        with open(path_to_file, encoding="utf-8") as f:  # Открываем файл и читаем строки
            logger.info(f"Открываем файл {path_to_file} и читаем строки")
            first_char = f.read(1)
            if not first_char:
                logger.info(f"Файл {path_to_file} пустой, возвращен пустой список.")
                print(f"Файл {path_to_file} пустой")
                return []
            f.seek(0)  # перемещаем указатель чтения/записи в начало файла
            list_of_transactions = json.load(f)
            if type(list_of_transactions) is list:
                logger.info("Функция read_json_file возвратила список словарей с данными о финансовых транзакциях.")
                return list_of_transactions
            else:
                logger.info(
                    f"Файл {path_to_file} не содержит список, функция read_json_file возвратила пустой список."
                )
                print(f"Файл {path_to_file} не содержит список")
                return []

    except FileNotFoundError as ex:
        logger.error(f"Файл {path_to_file} не найден. Произошла ошибка: {ex}")
        print(f"Файл {path_to_file} не найден")
        return []

    except json.JSONDecodeError as ex:
        logger.error(f"Ошибка декодирования JSON-файла {path_to_file} : {ex}")
        print(f"Ошибка декодирования JSON-файла {path_to_file} : {ex}")

    except Exception as ex:
        logger.error(f"Это общее исключение.{ex}")
        print(f"Это общее исключение.{ex}")

    return []


def transaction_amount(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях
    :param transaction: принимает на вход словарь с данными о транзакции
    :return: возвращает сумму транзакции (ключ amount) в рублях, тип данных float
    """

    logger.info("Начала выполняться функция transaction_amount")
    try:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            logger.info("Получаем сумму транзакции в рублях")
            amount_rub = float((transaction.get("operationAmount")).get("amount"))  # получаем сумму в рублях

        else:
            logger.info("Получаем сумму транзакции не в рублях")
            amount_no_rub = (transaction.get("operationAmount")).get("amount")  # получаем сумму не в рублях
            currency = ((transaction.get("operationAmount")).get("currency")).get("code")  # получаем тип валюты
            # Вызываем функцию конвертации валюты
            logger.info(f"Конвертируем сумму транзакции в {currency} в рубли")
            amount_rub = external_api.currency_conversion(amount_no_rub, currency)

        logger.info(f"Функция transaction_amount возвратила сумму транзакции {amount_rub} в рублях.")
        return amount_rub

    except KeyError as ex:
        logger.error(f"Запрошенный ключ не найден в словаре. Произошла ошибка: {ex}")
        raise KeyError(f"Запрошенный ключ не найден в словаре. {ex}")

    except ValueError as ex:
        logger.error(f"Не удалось преобразовать сумму в число. Произошла ошибка: {ex}")
        raise ValueError(f"Не удалось преобразовать сумму в число. Произошла ошибка: {ex}")

    except Exception as ex:
        logger.error(f"Это общее исключение. Произошла ошибка: {ex}")
        raise Exception(f"Это общее исключение. Произошла ошибка: {ex}")

if __name__ == "__main__":
    file_path = str(Path(__file__).parent.parent / "data")
    print(read_json_file(path_to_file=f"{file_path}/operations.json"))
    print(read_json_file(path_to_file=f"{file_path}/empty.json"))  # вызов функции для пустого файла
    print(read_json_file(path_to_file=f"{file_path}/not_list.json"))  # вызов функции для файла, содержащего не список
    print(read_json_file(path_to_file="operations.json"))  # вызов функции, если путь до файла указан не верно
