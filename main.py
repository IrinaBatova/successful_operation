from src import processing, widget, generators, decorators

# Домашняя работа к уроку 9.2 Основы Git

# Запрос типа и номера карты, или счета и его номера у пользователя
card_or_account_number_user = input("Введите тип карты и её номер или слово 'Счет' и его номер :  ")

print(widget.mask_account_card(card_or_account_number_user))

# Запрос пользователя ввести дату
date_user = input("Введите дату:  ")

print(widget.get_date(date_user))


# Домашняя работа к уроку 10.1 Продвинутый Git

# Список словарей
list_of_dictionaries_user = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Вызов функции filter_by_state отбора словарей по значению ключа "state"
print(processing.filter_by_state(list_of_dictionaries_user))
print(processing.filter_by_state(list_of_dictionaries_user, state="CANCELED"))

# Вызов функции sort_by_date сортировки словарей по значению ключа "date"
print(processing.sort_by_date(list_of_dictionaries_user))
print(processing.sort_by_date(list_of_dictionaries_user, ascending=False))


# Домашняя работа к уроку 11.1 Включения и генераторы

# Список словарей
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

# Вызов функции filter_by_currency
usd_transactions = generators.filter_by_currency(transactions, "USD")
try:
    for _ in range(5):
        print(next(usd_transactions))
except StopIteration:
    print("Достигнут конец итератора")


# Вызов функции transaction_descriptions
descriptions = generators.transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


# Вызов функции card_number_generator
usd_transactions = generators.card_number_generator(9999999999999997, 9999999999999999)
for transaction in usd_transactions:
    print(transaction)

# Домашняя работа к уроку 11.2 Декораторы


# Пример использования декоратора log, если filename задан, логи выводятся в файл mylog.txt
@decorators.log(filename="../mylog.txt")
def my_function_1(x, y):
    return x / y


# Пример использования декоратора log, если filename не задан, логи выводятся в консоль
@decorators.log()
def my_function_2(x, y):
    return x + y


my_function_1(10, 5)
my_function_2(10, 5)
