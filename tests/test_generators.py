import pytest

from src.generators import filter_by_currency


# С применением фикстур
def test_filter_by_currency(transactions: list, transaction_1: list, transaction_2: list) -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == transaction_1
    assert next(usd_transactions) == transaction_2

def test_filter_by_currency_no_transactions(list_transactions): # транзакций с заданной валютой нет
    eur_transactions = filter_by_currency(list_transactions, "EUR")
    try:
        next(eur_transactions)
        assert False, "Должно было быть выброшено исключение StopIteration"
    except StopIteration:
        assert True

# def test_filter_by_currency(transactions: list, new_transactions: list) -> None:
#     usd_transactions = filter_by_currency(transactions, "USD")
#     assert next(usd_transactions) == 1

    # expected_usd_transactions = new_transactions
    # actual_usd_transactions = filter_by_currency(transactions, "USD")
    # expected_usd_transactions == actual_usd_transactions

    # try:
    #     for _ in range(5):
    #         print(next(usd_transactions))
    # except StopIteration:
    #     print("Достигнут конец итератора")
    # assert filter_by_currency(transactions) == new_transactions

