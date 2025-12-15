import unittest
import pandas as pd
from io import BytesIO
from unittest.mock import mock_open, patch, MagicMock

from src.data_import import read_csv_file, read_excel_file

# Тестирование функции read_csv_file

# Создаем объекты, которые будут представлять замоканные версии функции open
mock_file = mock_open(read_data='id,amount\n1,100')
mock_file_empty = mock_open(read_data='')

# Создаем объект, для создания фейкового итератора для имитации ответа функции DictReader
mock_data = [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z;16210'},
             {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z;29740'}]

# Проверяем, что функция возвращает список словарей
@patch("builtins.open", mock_file)
def test_read_csv_file_() -> None:
    with patch("csv.DictReader", return_value=iter(mock_data)):
        assert read_csv_file("./data/transactions.csv") == mock_data


# Проверяем, что функция возвращает пустой список, если файл пуст
@patch("builtins.open", mock_file_empty)
def test_read_csv_file_1() -> None:
    with patch("csv.DictReader", return_value=iter(mock_data)):
        assert read_csv_file("./data/empty.csv") == []


# Проверяем, что функция возвращает пустой список, если тип файла не .csv
@patch("builtins.open", mock_file)
def test_read_csv_file_2() -> None:
    with patch("csv.DictReader", return_value=iter(mock_data)):
        assert read_csv_file("./data/operations.json") == []


# Проверяем, что функция возвращает пустой список, если файл не найден
@patch("builtins.open", mock_file)
def test_read_csv_file_3() -> None:
    with patch("csv.DictReader", side_effect=FileNotFoundError):
        assert read_csv_file("transactions.csv") == []


# Тестирование функции read_excel_file

# Создаем объект, список словарей
mock_data_list = [{'id': '650703', 'state': 'EXECUTED'}, {'id': '3598919', 'state': 'EXECUTED'}]

# Создаем объект DataFrame
mock_data_df = pd.DataFrame({'id': ['650703', '3598919'], 'state': ['EXECUTED', 'EXECUTED']})
mock_data_empty = pd.DataFrame() # Пустой DataFrame

# Используем BytesIO для создания буфера в памяти
excel_buffer = BytesIO()

# Записываем DataFrame в BytesIO как в Excel-файл
with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
    mock_data_df.to_excel(writer, index=False)

# Получаем данные из BytesIO
excel_data = excel_buffer.getvalue()

# Создаем объекты, которые будет представлять замоканные версии функции open
mock_file = mock_open(read_data=excel_data)
mock_file_empty = mock_open(read_data='')

# Проверяется, что функция возвращает список словарей
@patch("builtins.open", mock_file)
def test_read_excel_file_() -> None:
    with patch("pandas.read_excel", return_value=mock_data_df):
        assert read_excel_file("./data/transactions_excel.xlsx") == mock_data_list


# Проверяется, что функция возвращает пустой список, если файл пуст
@patch("builtins.open", mock_file_empty)
def test_read_excel_file_1() -> None:
    with patch("pandas.read_excel", return_value=mock_data_empty):
        assert read_excel_file("./data/empty.xlsx") == []


# Проверяется, что функция возвращает пустой список, если тип файла не .xlsx
@patch("builtins.open", mock_file)
def test_read_excel_file_2() -> None:
    with patch("pandas.read_excel", return_value=mock_data_df):
        assert read_excel_file("./data/operations.json") == []


# Проверяется, что функция возвращает пустой список, если файл не найден
@patch("builtins.open", mock_file)
def test_read_excel_file_3() -> None:
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        assert read_excel_file("transactions_excel.xlsx") == []


# if __name__ == "__main__":
#     unittest.main()
