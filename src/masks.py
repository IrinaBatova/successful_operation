def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: принимает номер карты в виде целого числа
    :return: возвращает замаскированный номер карты - маску в виде строки формата XXXX XX** **** XXXX.
    """

    card_number_str = str(card_number)  # меняем тип c числа на строку
    mask = card_number_str[:6] + "**" + "****" + card_number_str[-4:]  # формируем маску
    return " ".join(mask[i : i + 4] for i in range(0, len(mask), 4))  # возвращаем в заданном шаблоне по 4 символа


def get_mask_account(account_number: int) -> str:
    """
    Функция маскировки номера банковского счета
    :param account_number: принимает номер счета в виде целого числа
    :return: возвращает замаскированный номер счета - маску в виде строки формата ** XXXX.
    """

    account_number_str = str(account_number)  # меняем тип c числа на строку
    masked = "**" + account_number_str[-4:]  # формируем маску

    return masked
