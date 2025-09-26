from src import processing, widget

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

# Вызов функции отбора словарей по значению ключа "state"
print(processing.filter_by_state(list_of_dictionaries_user))
print(processing.filter_by_state(list_of_dictionaries_user, state="CANCELED"))

# Вызов функции сортировки словарей по значению ключа "date"
print(processing.sort_by_date(list_of_dictionaries_user))
print(processing.sort_by_date(list_of_dictionaries_user, ascending=False))
