from src import masks

def mask_account_card(card_or_account_number: str) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_or_account_number: принимает тип и номер карты или счета в виде строки
    :return: возвращает замаскированный номер карты или счета, маску в виде строки формата:
     тип карты(счет) XXXX XX** **** XXXX. Если card_or_account_number пустая строка,
     возвращается пустая строка
    """
    # Создаем пустые списки
    card_or_account = []
    number = []

    if card_or_account_number == "":
        return ""
    else:
        # Разделяем текст и цифры по спискам
        for symbol in card_or_account_number:
            if symbol.isdigit():
                number.append(symbol)
            else:
                card_or_account.append(symbol)

        card_or_account_str = "".join(card_or_account)  # преобразуем список с текстом в строку

        # В зависимости от того, номер счета или номер карты разделяем по маскам
        if card_or_account_str == "Счет " or card_or_account_str == "Счет":
            if number:
                number_str = masks.get_mask_account("".join(number))
                # number_str = masks.get_mask_account(int("".join(number)))
            else:
                number_str = ""
        else:
            if number:
                number_str = masks.get_mask_card_number("".join(number))
            else:
                number_str = ""

        return card_or_account_str + number_str


def get_date(data: str) -> str:
    """
    Функция переформатирования даты
    :param data: принимает дату в виде строки - 2024-03-11T02:26:18.671407
    :return: возвращает переформатированную дату - в виде строки формата "ДД.ММ.ГГГГ" ( "11.03.2024" ).
    """

    if data == "":
        return "Вы ничего не ввели"
    else:
        formatted_date = data[8:10] + "." + data[5:7] + "." + data[:4]
        return formatted_date
