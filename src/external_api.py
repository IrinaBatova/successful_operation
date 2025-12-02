import os
from dotenv import load_dotenv
import requests
import json


def currency_conversion(amount: str, currency: str) -> float:
    """
    Функция для конвертации валюты.
    - param amount: принимает сумму транзакции в виде строки;
    - param currency: принимает тип валюты транзакции в виде строки;
    - return: возвращает сумму транзакции в рублях.
    """

    try:
        load_dotenv()
        api_key = os.getenv('API_KEY')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        payload = {}
        headers = {"apikey": f"{api_key}"}

        response = requests.request("GET", url=url, headers=headers, data=payload)
        # status_code = response.status_code
        # result = response.text # {"message":"You have exceeded your daily\/monthly API rate limit.
        # Please review and upgrade your subscription plan at https:\/\/promptapi.com\/subscriptions to continue."}

        result = json.loads(response.text)
        amount_rub = float(result['result'])
        # print(type(amount_rub))

        return amount_rub

    except requests.exceptions.RequestException as e:
        print(f"HTTP ошибка: {e.response.status_code} - {e.response.reason}")
        print(f"Сообщение об ошибке: {e}")

    except json.JSONDecodeError as e:
        print("Ошибка декодирования. Invalid result.")
        print(f"Сообщение об ошибке: {e.msg}")
        print(f"Строка: {e.lineno}, колонка: {e.colno}")

    except TypeError:
        print("The object type is not serializable in JSON format.")

    except Exception as e:
        print(f"Ошибка {e}")
        print(result)


#print(currency_conversion("8221.37", "USD"))
