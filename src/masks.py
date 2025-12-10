import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: принимает номер карты в виде целого числа
    :return: возвращает замаскированный номер карты - маску в виде строки формата XXXX XX** **** XXXX.
    """
    logger.info(f'Начала выполняться функция get_mask_card_number')
    if card_number > 0:
        card_number_str = str(card_number)  # меняем тип c числа на строку
        if len(card_number_str) == 16:
            mask = card_number_str[:6] + "**" + "****" + card_number_str[-4:]  # формируем маску
            logger.info(
                f'Функция get_mask_card_number возвращает маску номера карты в виде строки формата XXXX XX** **** XXXX')
            return " ".join(
                mask[i: i + 4] for i in range(0, len(mask), 4))  # возвращаем в заданном шаблоне по 4 символа
        else:
            logger.info(f'Функция get_mask_card_number возвращает сообщение "Введено не 16 цифр"')
            return "Введено не 16 цифр"
    else:
        logger.info(f'Функция get_mask_card_number возвращает сообщение "Введено число < 0"')
        return "Введено число < 0"


def get_mask_account(account_number: int) -> str:
    """
    Функция маскировки номера банковского счета
    :param account_number: принимает номер счета в виде целого числа
    :return: возвращает замаскированный номер счета - маску в виде строки формата ** XXXX.
    """
    logger.info(f'Начала выполняться функция get_mask_account')
    if account_number > 0:
        account_number_str = str(account_number)  # меняем тип c числа на строку
        if len(account_number_str) > 6:
            masked = "** " + account_number_str[-4:]  # формируем маску
            logger.info(
                f'Функция get_mask_account возвращает замаскированный номер счета - маску в виде строки формата ** XXXX')
            return masked
        else:
            logger.info(f'Функция get_mask_account возвращает сообщение "Введено меньше 6 цифр"')
            return "Введено меньше 6 цифр"
    else:
        logger.info(f'Функция get_mask_account возвращает сообщение "Введено число < 0"')
        return "Введено число < 0"

# print(get_mask_card_number(1234567891234567)) # Введено число 16 цифр
# print(get_mask_card_number(123456789)) # Введено число не 16 цифр
# print(get_mask_card_number(-123456789)) # Введено число < 0
#
# print(get_mask_account(123456789)) # Введено число больше 6 цифр
# print(get_mask_account(12345)) # Введено число меньше 6 цифр
# print(get_mask_account(-12345)) # Введено число < 0
