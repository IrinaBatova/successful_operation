def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> list:
    """Функция отбора словарей по значению ключа "state":
    - param list_of_dictionaries: принимает список словарей;
    - param state: не обязательный, принимает опционально значение для ключа state (по умолчанию 'EXECUTED');
    - return: возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
     выбранному значению."""

    new_list_of_dictionaries = []

    for element in list_of_dictionaries:
        if element.get("state") == state:
            new_list_of_dictionaries.append(element)
    return new_list_of_dictionaries


def sort_by_date(list_of_dictionaries: list, ascending: bool = True) -> list:
    """Функция сортировки словарей по значению ключа "date":
    - param list_of_dictionaries: принимает список словарей;
    - param ascending: необязательный параметр, задающий порядок сортировки (по умолчанию — убывание);
    - return: возвращает новый список словарей, отсортированный по дате (date)."""

    list_of_dictionaries.sort(key=lambda x: x.get("date", 0), reverse=ascending)

    return list_of_dictionaries
