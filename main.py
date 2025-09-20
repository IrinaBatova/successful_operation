from src import widget

# Запрос типа и номера карты или счета и его номера пользователя
card_or_account_number_user = input("Введите тип карты и её номер или слово 'Счет' и его номер :  ")

print(widget.mask_account_card(card_or_account_number_user))

# Запрос пользователя ввести дату
date_user = input("Введите дату:  ")

print(widget.get_date(date_user))
