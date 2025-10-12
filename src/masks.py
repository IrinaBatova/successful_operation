def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: принимает номер карты в виде целого числа
    :return: возвращает замаскированный номер карты - маску в виде строки формата XXXX XX** **** XXXX.
    """
    if card_number > 0:
        card_number_str = str(card_number)  # меняем тип c числа на строку
        if len(card_number_str) == 16:
            mask = card_number_str[:6] + "**" + "****" + card_number_str[-4:]  # формируем маску
            return " ".join(
                mask[i:i + 4] for i in range(0, len(mask), 4)
            )  # возвращаем в заданном шаблоне по 4 символа
        else:
            return "Введено не 16 цифр"
    else:
        return "Введено число < 0"


def get_mask_account(account_number: int) -> str:
    """
    Функция маскировки номера банковского счета
    :param account_number: принимает номер счета в виде целого числа
    :return: возвращает замаскированный номер счета - маску в виде строки формата ** XXXX.
    """
    if account_number > 0:
        account_number_str = str(account_number)  # меняем тип c числа на строку
        if len(account_number_str) > 6:
            masked = "** " + account_number_str[-4:]  # формируем маску
            return masked
        else:
            return "Введено меньше 6 цифр"
    else:
        return "Введено число < 0"


# print(get_mask_card_number(12))
# rint(get_mask_account(1225633222))
