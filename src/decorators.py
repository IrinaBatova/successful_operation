import functools

# Декоратор log
def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_message = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"
                raise
            finally:
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
        return wrapper
    return decorator

# Пример использования
@log(filename="mylog.txt")
def my_function(x, y):
    return x / y

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

# # Пример использования, если filename не задан, логи выводятся в консоль
# @log()
# def my_function(x, y):
#     return x / y

# Вызов функции
try:
    my_function(3, 0)
except ZeroDivisionError:
    pass