list_of_dictionaries_user = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> list:

    new_list_of_dictionaries = []

    for element in list_of_dictionaries:
        if element.get("state") == state:
            new_list_of_dictionaries.append(element)
        elif element.get("state") != "EXECUTED":
            new_list_of_dictionaries.append(element)

    return new_list_of_dictionaries


print(filter_by_state(list_of_dictionaries_user, state = "CANCELED"))
