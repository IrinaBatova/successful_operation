transactions = (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",

                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )


def filter_by_currency(list_transactions: list, currency: str) -> iter:
    """
    Функция возвращает итератор, который поочередно выдает транзакции с заданным типом валюты (например, USD).
    - param list_transactions: принимает список словарей, представляющих транзакции;
    - param currency: принимает тип валюты в виде строки;
    - yield: возвращает итератор, который поочередно выдает транзакции и в них валюта операции соответствует заданной.
    """

    for transaction in list_transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction



# usd_transactions = filter_by_currency(transactions, "USD")
# try:
#     for _ in range(5):
#         print(next(usd_transactions))
# except StopIteration:
#     print("Достигнут конец итератора")



def transaction_descriptions(list_transactions: list) -> iter:
    """
     Функция возвращает описание каждой операции по очереди.
     - param list_transactions: принимает список словарей, представляющих транзакции;;
     - yield: возвращает итератор, который возвращает описание каждой операции по очереди.
     """

    for transaction in list_transactions:
        for key in transaction:
            if key == "description":
                yield transaction[key]


# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(start: int, stop: int) -> iter:
    """
    Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999:
    - param start: принимает целое число, являющееся началом диапазона;
    - param stop: принимает целое число, являющееся концом диапазона;
    - yield: возвращает строку, номер банковской карты в формате XXXX XXXX XXXX XXXX.
    """

    for num in range(start, stop + 1):
        num_str = f"{num:016d}"
        formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted_number


# usd_transactions = card_number_generator(9999999999999997, 9999999999999999)
# for transaction in usd_transactions:
#     print(transaction)
