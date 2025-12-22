import logging

from pathlib import Path
log_path = Path(__file__).parent.parent / "logs" / "masks.log"

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: принимает номер карты в виде целого числа
    :return: возвращает замаскированный номер карты - маску в виде строки формата XXXX XX** **** XXXX.
    """
    try:
        logger.info("Начала выполняться функция get_mask_card_number")
        if card_number > 0:
            card_number_str = str(card_number)  # меняем тип c числа на строку
            if len(card_number_str) == 16:
                mask = card_number_str[:6] + "**" + "****" + card_number_str[-4:]  # формируем маску
                mask_template = " ".join(mask[i: i + 4] for i in range(0, len(mask), 4))  # шаблон по 4 символа
                logger.info(f"Функция get_mask_card_number возвращает маску номера карты {mask_template}")
                return mask_template
            else:
                logger.info('Функция get_mask_card_number возвращает сообщение "Введено не 16 цифр"')
                return "Введено не 16 цифр"
        else:
            logger.info('Функция get_mask_card_number возвращает сообщение "Введено число < 0"')
            return "Введено число < 0"

    except TypeError as ex:
        logger.error(f"Номер карты не целое число. Произошла ошибка: {ex}")
        return f"Номер карты не целое число. Произошла ошибка: {ex}"

    except Exception as ex:
        logger.error(f"Это общее исключение. Произошла ошибка: {ex}")
        return f"Это общее исключение. Произошла ошибка: {ex}"


def get_mask_account(account_number: int) -> str:
    """
    Функция маскировки номера банковского счета
    :param account_number: принимает номер счета в виде целого числа
    :return: возвращает замаскированный номер счета - маску в виде строки формата ** XXXX.
    """
    try:
        logger.info("Начала выполняться функция get_mask_account")
        if account_number > 0:
            account_number_str = str(account_number)  # меняем тип c числа на строку
            if len(account_number_str) > 6:
                masked = "** " + account_number_str[-4:]  # формируем маску
                logger.info(f"Функция get_mask_account возвращает замаскированный номер счета {masked}")
                return masked
            else:
                logger.info('Функция get_mask_account возвращает сообщение "Введено меньше 6 цифр"')
                return "Введено меньше 6 цифр"
        else:
            logger.info('Функция get_mask_account возвращает сообщение "Введено число < 0"')
            return "Введено число < 0"

    except TypeError as ex:
        logger.error(f"Номер счета не целое число. Произошла ошибка: {ex}")
        return f"Номер карты не целое число. Произошла ошибка: {ex}"

    except Exception as ex:
        logger.error(f"Это общее исключение. Произошла ошибка: {ex}")
        return f"Это общее исключение. Произошла ошибка: {ex}"


# print(get_mask_card_number(1234567891234567))  # Введено число 16 цифр
# print(get_mask_card_number(123456789))  # Введено число не 16 цифр
# print(get_mask_card_number(-123456789))  # Введено число < 0
# print(get_mask_card_number('1234567891234567'))  # Введено не целое число
#
# print(get_mask_account(123456789))  # Введено число больше 6 цифр
# print(get_mask_account(12345))  # Введено число меньше 6 цифр
# print(get_mask_account(-12345))  # Введено число < 0
# print(get_mask_account('123456789'))  # Введено не целое число
