import functools, datetime


# Декоратор log
def log(filename=None):
    """
    Декоратор с параметрами: внешняя функция
    :param filename: Необязательный аргумент, который определяет куда будут записываться логи (в файл или в консоль):
        - если filename задан, логи записываются в указанный файл;
        - если filename не задан, логи выводятся в консоль.
    :return: Возвращает внутренний декоратор - decorator
    """

    def decorator(func):
        """
        Декоратор: внутренняя функция
        :param func: принимает любую функцию, которую нужно декорировать
        :return: возвращает функцию-обертку: wrapper
        """

        @functools.wraps(func)  # декоратор передает метаданные (имя функции, docstring)
        # от декорируемой функции в функцию-обертку.
        def wrapper(*args, **kwargs):  # функция-обертка
            log_message_1 = ""
            log_message_2 = ""
            log_message_3 = ""
            log_message_4 = ""
            log_message_err = ""
            try:
                start_time = datetime.datetime.now()
                #log_message_1 = f"[{start_time}] Starting function '{func.__name__}' with arguments {args} and {kwargs}"
                result = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                log_message_1 = f"[{start_time}] Starting function '{func.__name__}' with arguments {args} and {kwargs}"
                log_message_2 = f"[{end_time}] Finished function '{func.__name__}' with result {result}"
                log_message_3 = f"{func.__name__} ok."
                log_message_4 = f"Function execution time: {(end_time - start_time).total_seconds()} seconds"
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_message_err = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"
                raise
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message_err + "\n" + log_message_1 + "\n" + log_message_2 + "\n" + log_message_3 + "\n" + log_message_4 + "\n")
                else:
                    print(log_message_err + "\n" + log_message_1 + "\n" + log_message_2 + "\n" + log_message_3 + "\n" + log_message_4)

        return wrapper

    return decorator

#
# # Пример использования декоратора log, если filename задан, логи выводятся в файл mylog.txt
# @log(filename="../mylog.txt")
# def my_function_1(x, y):
#     return x / y
#
#
# # Пример использования декоратора log, если filename не задан, логи выводятся в консоль
# @log()
# def my_function_2(x, y):
#     return x + y
#
#
# my_function_1(10, 5)
# my_function_2(10, 5)
