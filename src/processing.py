def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> list:
    """
    Функция отбора словарей по значению ключа "state":
    - param list_of_dictionaries: принимает список словарей;
    - param state: не обязательный, принимает опционально значение для ключа state (по умолчанию 'EXECUTED');
    - return: возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
     выбранному значению.
     """

    new_list_of_dictionaries = []

    for element in list_of_dictionaries:
        if element.get("state") == state:
            new_list_of_dictionaries.append(element)
    return new_list_of_dictionaries


def sort_by_date(list_of_dictionaries: list, ascending: bool = True) -> list:
    """
    Функция сортировки словарей по значению ключа "date":
    - param list_of_dictionaries: принимает список словарей;
    - param ascending: необязательный параметр, задающий порядок сортировки (по умолчанию — убывание);
    - return: возвращает новый список словарей, отсортированный по дате (date).
    """

    list_of_dictionaries.sort(key=lambda x: x.get("date", 0), reverse=ascending)

    return list_of_dictionaries


# Вызов функции отбора словарей по значению ключа "state"

# list_of_dictionaries = [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 594226727, "state": "CANCELED", "date": ""},
#     ]
#
#
# print(filter_by_state(list_of_dictionaries))
# print(filter_by_state(list_of_dictionaries, state="CANCEL"))
# print(sort_by_date(list_of_dictionaries))
# print(sort_by_date(list_of_dictionaries, ascending=False))
