import pytest, re

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Тестирование функции filter_by_currency

# Проверяется, что функция корректно фильтрует транзакции по заданной валюте
def test_filter_by_currency(transactions: list, transaction_usd_1: list, transaction_usd_2: list, transaction_usd_3: list) -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == transaction_usd_1
    assert next(usd_transactions) == transaction_usd_2
    assert next(usd_transactions) == transaction_usd_3


# Проверяется, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют
def test_filter_by_currency_no_transactions(transactions: list) -> None: # транзакции в заданной валюте отсутствуют
    eur_transactions = filter_by_currency(transactions, "EUR")
    try:
        next(eur_transactions)
        assert False, "Должно было быть выброшено исключение StopIteration"
    except StopIteration:
        assert True


# Проверяется, что генератор не завершается ошибкой при обработке пустого списка
def test_filter_by_currency_empty_list(transactions: list) -> None: # пустой список транзакций
    eur_transactions = filter_by_currency([], "EUR")
    try:
        next(eur_transactions)
        assert False, "Должно было быть выброшено исключение StopIteration"
    except StopIteration:
        assert True


# Тестирование функции transaction_descriptions

# Проверка, что функция возвращает корректные описания для каждой транзакции
def test_transaction_descriptions(transactions: list) -> None:
    key_transactions = transaction_descriptions(transactions)
    assert next(key_transactions) == "Перевод организации"
    assert next(key_transactions) == "Перевод со счета на счет"
    assert next(key_transactions) == "Перевод со счета на счет"
    assert next(key_transactions) == "Перевод с карты на карту"
    assert next(key_transactions) == "Перевод организации"


#Проверка работы функции с пустым списком транзакций
def test_transaction_descriptions_(transactions: list) -> None:
    key_transactions = transaction_descriptions([])
    try:
        next(key_transactions)
        assert False, "Должно было быть выброшено исключение StopIteration"
    except StopIteration:
        assert True


# Тестирование функции card_number_generator

# Проверка, что генератор выдает правильные номера карт в заданном диапазоне
@pytest.mark.parametrize("start, stop", [(0, 1)])
def test_card_number_generator_1(start: int, stop: int) -> None:
    formatted_number = card_number_generator(start, stop)
    assert next(formatted_number) == "0000 0000 0000 0000"
    assert next(formatted_number) == "0000 0000 0000 0001"


# Проверяет, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.
@pytest.mark.parametrize("start, stop", [(9999999999999997, 9999999999999999)])
def test_card_number_generator_2(start: int, stop: int) -> None:
    formatted_number = card_number_generator(start, stop)
    assert next(formatted_number) == "9999 9999 9999 9997"
    assert next(formatted_number) == "9999 9999 9999 9998"
    assert next(formatted_number) == "9999 9999 9999 9999"


# Проверка, что генератор выдает правильные номера карт в заданном диапазоне
@pytest.mark.parametrize("start, stop", [(1, 2)])
def test_card_number_generator_3(start: int, stop: int) -> None:
    formatted_number = card_number_generator(start, stop)
    card_number = str(next(formatted_number))
    pattern = r"^\d{4} \d{4} \d{4} \d{4}$"
    try:
        if re.match(pattern, card_number):
            print("Корректный формат номера карты")
        else:
            print("Некорректный формат номера карты")
    except AssertionError:
        print("Assertion Error")

