from pathlib import Path
from src import utils, data_import, masks, generators, processing, widget


# 1. Выбор файла определённого типа, содержащего данные о транзакциях
print(
    "\nПрограмма: Привет! Добро пожаловать в программу работы\n"
    "с банковскими транзакциями.\n"
    "\nВыберите необходимый пункт меню:\n"
    "1. Получить информацию о транзакциях из JSON-файла\n"
    "2. Получить информацию о транзакциях из CSV-файла\n"
    "3. Получить информацию о транзакциях из XLSX-файла\n"
)

menu_item = input("Пользователь:  ") # ответ пользователя
menu_item = menu_item.replace(" ", "") # убираем пробелы, если они есть

while menu_item != "1" and menu_item != "2" and menu_item != "3":  # проверяем символы в строке
    print("\nПрограмма: Пункт меню выбран не корректно. Введите 1 или 2 или 3.\n")
    menu_item = input("Пользователь:  ")  # запрос пункта меню
    menu_item = menu_item.replace(" ", "")  # убираем пробелы, если они есть

# 1.1 Создаём путь к директории "data", находящейся в той же директории, что и текущий модуль
file_path = str(Path(__file__).parent / "data")  # метод .parent возвращает родительскую директорию текущего файла

list_transactions = []
if menu_item == "1":
    print("\nПрограмма: Для обработки выбран JSON-файл.\n")
    list_transactions = utils.read_json_file(path_to_file=f"{file_path}/operations.json")
elif menu_item == "2":
    print("\nПрограмма: Для обработки выбран CSV-файл.\n")
    list_transactions = data_import.read_csv_file(path_to_file=f"{file_path}/transactions.csv")
elif menu_item == "3":
    print("\nПрограмма: Для обработки выбран XLSX-файл.\n")
    list_transactions = data_import.read_excel_file(path_to_file=f"{file_path}/transactions_excel.xlsx")


# 2. Выбор статуса транзакции для сортировки
print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
      "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")

status = input("Пользователь:  ") # ответ пользователя
status = status.upper().replace(" ", "") # приводим к верхнему регистру и убираем пробелы, если они есть

while status != "EXECUTED" and status != "CANCELED" and status != "PENDING":  # проверяем выбранный статус
    print(f"\nПрограмма: Статус операции '{status}' недоступен.\n")
    print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
          "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n")
    status = input("Пользователь:  ")  # ответ пользователя
    status = status.upper().replace(" ", "") # приводим к верхнему регистру и убираем пробелы, если они есть

print(f'\nПрограмма: Операции отфильтрованы по статусу "{status}".\n')
list_status = processing.filter_by_state(list_transactions, state=status)

# 2.1 Транзакции с заданным статусом отсутствуют.
if not list_status:
    print(f'Программа: Не найдено ни одной транзакции со статусом "{status}"\n')
    print("Программа завершила работу")
else:
    # 3. Выбор настроек сортировки транзакций (по дате и по возрастанию/по убыванию)
    print("Программа: Отсортировать операции по дате? Да/Нет\n")
    user_date = input("Пользователь:  ") # ответ пользователя
    user_date = user_date.lower().replace(" ", "")  # приводим к нижнему регистру и убираем пробелы, если они есть

    while user_date != "да" and user_date != "нет":  # проверяем выбранную сортировку
        print(f'\nПрограмма: Ответ "{user_date}" не корректен. Введите "Да" или "Нет"\n')
        user_date = input("Пользователь:  ")  # ответ пользователя
        user_date = user_date.lower().replace(" ", "")  # приводим к нижнему регистру и убираем пробелы, если они есть

    user_sorting = ""
    if user_date == "да":
        print("\nПрограмма: Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n")
        user_sorting = input("Пользователь:  ") # ответ пользователя
        user_sorting = user_sorting.lower().replace(" ", "")  # приводим к нижнему регистру и убираем пробелы, если они есть

        while user_sorting != "повозрастанию" and user_sorting != "поубыванию":  # проверяем выбранную сортировку
            print(f'\nПрограмма: Ответ "{user_sorting}" не корректен. Введите "по возрастанию" или "по убыванию"\n')
            user_sorting = input("Пользователь:  ")  # ответ пользователя
            user_sorting = user_sorting.lower().replace(" ", "")  # приводим к нижнему регистру и убираем пробелы, если они есть

    if user_date == "да" and user_sorting == "поубыванию":
        list_status_data = processing.sort_by_date(list_status)
    elif user_date == "да" and user_sorting == "повозрастанию":
        list_status_data = processing.sort_by_date(list_status, ascending=False)
    else:
        list_status_data = list_status


    # 4. Отбор только рублевых транзакций
    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет\n")
    user_currency = input("Пользователь:  ") # ответ пользователя
    user_currency = user_currency.lower().replace(" ", "")  # приводим к нижнему регистру и убираем пробелы, если они есть

    while user_currency != "да" and user_currency != "нет":  # проверяем выбранную сортировку
        print(f'\nПрограмма: Ответ "{user_currency}" не корректен. Введите "Да" или "Нет"\n')
        user_currency = input("\nПользователь:  ")  # ответ пользователя
        user_currency = user_currency.lower().replace(" ", "")  # приводим к нижнему регистру и убираем пробелы, если они есть

    if user_currency == "да":
        list_status_data_currency = list(generators.filter_by_currency(list_status_data, "RUB"))
    else:
        list_status_data_currency = list_status_data

    # 4.1 Транзакции с рублевой валютой отсутствуют.
    if not list_status_data_currency:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n"
              "Программа завершила работу\n")
    else:
        # 5. Отбор транзакций по определенному слову в описании
        print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        by_user_word = input("Пользователь:  ") # ответ пользователя
        by_user_word = by_user_word.lower().replace(" ", "")  # приводим к нижнему регистру и убираем пробелы, если они есть

        while by_user_word != "да" and by_user_word != "нет":  # проверяем выбранную сортировку
            print(f'\nПрограмма: Ответ "{by_user_word}" не корректен. Введите "Да" или "Нет"\n')
            by_user_word = input("Пользователь:  ")  # ответ пользователя
            by_user_word = by_user_word.lower().replace(" ", "")  # приводим к нижнему регистру и убираем пробелы, если они есть

        if by_user_word == "да":
            print('Программа: Введите слово для отбора, например;\n'
                  '"Перевод организации", "Перевод с карты на карту", "Открытие вклада"\n')
            user_word = input("\nПользователь:  ")  # ответ пользователя
            final_list = processing.process_bank_search(list_status_data_currency, user_word)
        else:
            final_list = list_status_data_currency

        # 5.1 Транзакции с заданным для отбора словом отсутствуют.
        if not final_list:
            print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n"
                  "Программа завершила работу\n")
        else:
            print("\nПрограмма: Распечатываю итоговый список транзакций...\n")

            # 6. Вывод отобранных транзакций
            print(f"Всего банковских операций в выборке: {len(final_list)}\n")
            descriptions = generators.transaction_descriptions(final_list)

            for transaction in final_list:
                date_transactions = widget.get_date(transaction["date"])
                description = transaction["description"]
                check_from = widget.mask_account_card(str(transaction.get("from", "")))
                check_to = widget.mask_account_card(str(transaction.get("to", "")))

                # Проверяем check_from на истинность (не пустое значение)
                check_transactions = f"{check_from} -> {check_to}" if check_from else check_to

                amount_key = "operationAmount" if menu_item == "1" else "amount" # ключ суммы
                currency_key = "currency" if menu_item == "1" else "currency_name" # ключ валюты
                sum_transactions = transaction[amount_key]["amount"]
                currency = transaction[amount_key][currency_key]

                print(
                    f"{date_transactions} {description}\n{check_transactions}\nСумма: {sum_transactions} {currency}\n")


    # Файл JSON
    # [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
    #   'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},
    #   'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}]

    # Файл CSV
    # {'id': '307426', 'state': 'CANCELED', 'date': '2023-08-17T22:30:01Z', 'amount': '13875', 'currency_name': 'Ruble',
    #  'currency_code': 'RUB', 'from': 'American Express 1495416283887670', 'to': 'Mastercard 5120967507423143',
    #  'description': 'Перевод с карты на карту'}

    # Файл XLSX
    # [{'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0,
    #   'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
    #   'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'}]

    # Программа:
    # Всего банковских операций в выборке: 4
    #
    # 08.12.2019 Открытие вклада
    # Счет **4321
    # Сумма: 40542 руб.
    #
    # 12.11.2019 Перевод с карты на карту
    # MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
    # Сумма: 130 USD
    #
    # 18.07.2018 Перевод организации
    # Visa Platinum 7492 65** **** 7202 -> Счет **0034
    # Сумма: 8390 руб.
    #
    # 03.06.2018 Перевод со счета на счет
    # Счет **2935 -> Счет **4321
    # Сумма: 8200 EUR
