import unittest
from unittest.mock import mock_open, patch

from src.utils import read_json_file, transaction_amount

# Тестирование функции read_json_file

# Создаем объект, который будет представлять замоканную версию функции open
mock_file = mock_open(read_data='[{"id": 1, "amount": 100}]')


# Проверяется, что функция возвращает список словарей
@patch("builtins.open", mock_file)
def test_read_json_file_() -> None:
    with patch("json.load", return_value=[{"id": 1, "amount": 100}]):
        assert read_json_file("./data/operations.json") == [{"id": 1, "amount": 100}]


# Проверяется, что функция возвращает пустой список, если список словарей в файле пуст
@patch("builtins.open", mock_file)
def test_read_json_file_1() -> None:
    with patch("json.load", return_value=[]):
        assert read_json_file("./data/operations.json") == []


# Проверяется, что функция возвращает пустой список, если файл содержит не список
@patch("builtins.open", mock_file)
def test_read_json_file_2() -> None:
    with patch("json.load", return_value={"id": 1, "amount": 100}):
        assert read_json_file("./data/operations.json") == []


# Проверяется, что функция возвращает пустой список, если файл не найден
@patch("builtins.open", mock_file)
def test_read_json_file_3() -> None:
    with patch("json.load", return_value=None):
        assert read_json_file("./data/operations.json") == []


# Тестирование функции transaction_amount


# Проверяется, что функция корректно обрабатывает транзакцию с валютой в "RUB"
def test_transaction_amount_rub(transactions_utils_rub: dict) -> None:
    assert transaction_amount(transactions_utils_rub) == 31957.58


# Проверяется, что функция корректно обрабатывает транзакцию с валютой в "USD"
@patch("src.external_api.currency_conversion", return_value=75.0)
def test_transaction_amount_usd(transactions_utils_usd: dict) -> None:
    assert transaction_amount(transactions_utils_usd) == 75.0


# Проверяется, что функция корректно выбрасывает исключения
class TestTransactionAmount(unittest.TestCase):

    def test_key_error(self) -> None:
        transaction: dict = {"operationAmount": {}}  # Здесь отсутствует ключ 'amount'
        with self.assertRaises(KeyError):
            transaction_amount(transaction)

    def test_value_error(self) -> None:
        transaction = {"operationAmount": {"amount": "not_a_number", "currency": {"code": "RUB"}}}
        with self.assertRaises(ValueError):
            transaction_amount(transaction)


if __name__ == "__main__":
    unittest.main()
