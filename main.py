import os
current_directory = os.getcwd()
print(current_directory)

from src import masks

card_number_user = input("Введите номер карты:  ")  # запрос номера карты пользователя
card_number_user = card_number_user.replace(" ", "")  # убираем пробелы, если они есть

while not card_number_user.isdigit() or len(card_number_user) != 16:  # проверяем, что символы в строке цифры и их 16
    print("Номер карты должен содержать 16 цифр")
    card_number_user = input("Введите номер карты:  ")  # запрос номера карты пользователя
    card_number_user = card_number_user.replace(" ", "")  # убираем пробелы, если они есть

card_number_user_int = int(card_number_user)  # меняем тип на целочисленный

print(masks.get_mask_card_number(card_number_user_int))


account_number_user = input("Введите номер счета:  ")  # запрос номера счета пользователя
account_number_user = str(account_number_user).replace(" ", "")  # убираем пробелы, если они есть

while (
    not account_number_user.isdigit() or len(account_number_user) < 6
):  # проверяем, что символы в строке цифры и их не < 6
    print("Номер счета должен содержать минимум 6 цифр")
    account_number_user = input("Введите номер счета:  ")  # запрос номера карты пользователя
    account_number_user = str(account_number_user).replace(" ", "")  # убираем пробелы, если они есть

account_number_user_int = int(account_number_user)  # меняем тип на целочисленный

print(masks.get_mask_account(account_number_user_int))
