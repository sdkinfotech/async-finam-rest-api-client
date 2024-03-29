"""
Модуль `examples.py` предоставляет набор асинхронных функций для демонстрации взаимодействия с API через клиента.
Каждая функция в этом модуле предназначена для выполнения конкретного типа запроса к API и демонстрации обработки ответа.

Включает в себя функции:
- `check_access_token(client)`: Проверяет валидность токена доступа, используемого клиентом для работы с API.
  При успешной проверке выводит полученный от API ответ.

- `check_day_candles(client)`: Запрашивает у API данные о дневных свечах для указанного инструмента.
  Использует параметры, такие как доска торгов, код ценной бумаги, таймфрейм, начальную и конечную даты.
  В случае успеха выводит полученные данные о свечах.

- `check_intraday_candles(client)`: Выполняет запрос к API для получения данных об интрадейных свечах в рамках 
  заданного краткосрочного временного интервала. Подобно функции для дневных свечей, выводит данные о свечах 
  при успешном ответе от API.

"""

async def check_access_token(client):
    """
    Асинхронно выполняет запрос к API для проверки доступности токена и выводит результат.
    """
    try:
        response = await client.check_access_token()
        print("Результат проверки токена:")
        print(response)
    except Exception as e:
        print(f"Возникла ошибка при проверке токена: {e}")
        

async def check_day_candles(client):
    """
    Асинхронно выполняет запрос к API для получения дневных свечей и выводит результат.
    """
    
    security_board = "TQBR"
    security_code = "GAZP"
    time_frame = "D1"
    interval_from = "2024-03-10"
    interval_to = "2024-03-11"

    try:
        response = await client.get_day_candles(
            security_board=security_board,
            security_code=security_code,
            time_frame=time_frame,
            interval_from=interval_from,
            interval_to=interval_to
        )
        print("Успешный ответ от API:")
        print(response)
    except Exception as e:
        print(f"Возникла ошибка при запросе: {e}")

async def check_intraday_candles(client):
    """
    Асинхронно выполняет запрос к API для получения интрадейных свечей и выводит результат.
    """
    security_board = "TQBR"
    security_code = "GAZP"
    time_frame = "M1"
    interval_from = "2024-03-04T12:22:40Z"  
    interval_to = "2024-03-04T12:23:40Z"  
    try:
        response = await client.get_intraday_candles(
            security_board=security_board,
            security_code=security_code,
            time_frame=time_frame,
            interval_from=interval_from,
            interval_to=interval_to
        )
        print("Успешный ответ от API:")
        print(response)
    except Exception as e:
        print(f"Возникла ошибка при запросе: {e}")

async def place_order(client, client_id):
    """
    Асинхронно размещает ордер на покупку или продажу.

    :param client: Экземпляр клиента API, используемый для выполнения запроса.
    :param client_id: Ключ API в данном случае TRANSAQ_TOKEN.
    """
    # Создание данных ордера для примера
    order_data = {
        "clientId": client_id,
        "securityBoard": "TQBR",
        "securityCode": "VTBR",
        "buySell": "Buy",
        "quantity": 1,
        "useCredit": False,
        "price": 0.012485,
        "property": "PutInQueue",
        "condition": {
            "type": "Bid",
            "price": 0.012485,
            "time": None
        },
        "validBefore": {
            "type": "TillEndSession",
            "time": None
        }
    }
    try:
        # Размещение ордера
        order_response = await client.place_order(order_data)
        print("Ответ на размещение ордера:", order_response)
    except Exception as e:
        print("Ошибка при размещении ордера:", e)