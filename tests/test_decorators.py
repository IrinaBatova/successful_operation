import pytest
from src.decorators import log


# Проверяется вывод log-сообщений в файл mylog.txt:
def test_log_file():
    @log(filename="../mylog.txt")
    def my_function_1(x, y):
        return x - y

    result = my_function_1(10, 5)
    with open("../mylog.txt", "r") as file:
        log_content = file.read()
    assert "my_function_1 ok." in log_content
    assert result == 5

# Проверяется вывод log-сообщений об ошибке в файл mylog.txt:
def test_log_file_error():
    @log(filename="../mylog.txt")
    def my_function_2(x: float, y: float) -> float:
        return x / y

    with pytest.raises(Exception, match="division by zero"):
        my_function_2(10, 0)

    with open("../mylog.txt", "r") as file:
        log_content = file.read()
    assert "my_function_2 error: ZeroDivisionError. Inputs: (10, 0), {}" in log_content


# Проверяется вывод log-сообщений в консоль:
def test_log_console(capsys):
    @log()
    def my_function_3(x, y):
        return x / y

    result = my_function_3(20, 2)
    log_console = capsys.readouterr()
    string = str(log_console.out)
    assert "my_function_3 ok." in string
    assert result == 10

# Проверяется вывод log-сообщений об ошибке в консоль:
def test_log_console_error():
    @log()
    def my_function_4(x: int, y: int) -> int:
        return x / y

    with pytest.raises(Exception, match="division by zero"):
        my_function_4(10, 0)
        log_console = capsys.readouterr()
        string = str(log_console.out)
        assert "my_function_4 error: ZeroDivisionError. Inputs: (10, 0), {}" in string
