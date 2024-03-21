"""
Модуль примеров использования запросов 
из приложения async-finam-rest-api-client
для работы с Trade API Finam
Разработчик https://github.com/sdkinfotech
Репозиторий https://github.com/sdkinfotech/async-finam-rest-api-client.git
"""

# Асинхронная функция для проверки токена доступа.
async def check_token(client):
    """
    Асинхронный запрос к API для проверки валидности токена доступа.
    Аргументы:
    - client: экземпляр клиента API, через который производится запрос.
    Выводит в консоль результат проверки токена доступа.
    """
    token_check = await client.check_access_token()
    print(f"Проверка токена доступа: {token_check}")

# Асинхронная функция для запроса информации о дневных свечах.
async def fetch_day_candles(client):
    """
    Запрос информации о дневных свечах для заданного инструмента и временного периода.
    Аргументы:
    - client: экземпляр клиента API, используемый для выполнения запроса.
    Выводит в консоль полученные данные о свечах.
    """
    day_candles_info = await client.get_day_candles(
        security_board="TQBR",  # Режим торговой площадки.
        security_code="GAZP",   # Тикер инструмента.
        time_frame="D1",        # Временной интервал (D1 - один день).
        interval_from="2024-03-01",  # Начальная дата интервала.
        interval_to="2024-03-21",    # Конечная дата интервала.
        interval_count=0       # Количество запрашиваемых свечей (0 означает все доступные).
    )
    print(f"Информация о дневных свечах: {day_candles_info}")

# Асинхронная функция для запроса информации о интрадейных свечах.
async def fetch_intraday_candles(client):
    """
    Запрос информации о интрадейных свечах за заданный временной интервал.
    Аргументы:
    - client: экземпляр клиента API для отправки запроса.
    Выводит в консоль полученные данные о интрадейных свечах.
    """
    intraday_candles_info = await client.get_intraday_candles(
        security_board="TQBR",  # Режим торговой площадки.
        security_code="SBER",   # Тикер интсрумента.
        time_frame="M1",        # Временной интервал (M1 - одна минута).
        interval_from="2024-03-01T09:00:00",  # Время начала интервала.
        interval_to="2024-03-01T18:00:00",    # Время окончания интервала.
        interval_count=0        # Количество запрашиваемых свечей (0 означает все доступные).
    )
    print(f"Информация о интрадейных свечах: {intraday_candles_info}")

# Асинхронная функция для запроса информации о портфеле TRANSAQ
async def fetch_portfolio(client, client_id):
    """
    Запрос информации о портфеле с использованием предоставленного client_id.
    
    :param client: Экземпляр клиента API, используемый для выполнения запроса.
    :param client_id: Идентификатор клиента для запроса портфеля.
    """
    portfolio_info = await client.get_portfolio(client_id)
    print(f"Информация о портфеле: {portfolio_info}")

# Асинхронная функция для запроса информации об инструментах
async def fetch_securities(client, board="TQBR", seccode="GAZP"):
    """
    Запрос информации о ценных бумагах на указанной торговой площадке и с определенным кодом.
    
    :param client: Экземпляр клиента API, используемый для выполнения запроса.
    :param board: Режим торговой площадки.
    :param seccode: Код ценной бумаги.
    """
    securities_info = await client.get_securities(board=board, seccode=seccode)
    print(f"Информация о ценных бумагах: {securities_info}")

# Асинхронная функция для размещения ордера
async def place_order(client, client_id):
    """
    Размещение ордера на покупку или продажу
    :param client: Экземпляр клиента API, используемый для выполнения запроса.
    :param client_id: ключ API в данном случае TRANSAQ_TOKEN
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
    # Размещение ордера
    order_response = await client.place_order(order_data)
    print("Ответ на размещение ордера:", order_response)

async def get_orders(client, client_id):
    """
    Асинхронная функция для получения списка ордеров.
    Демонстрирует работу с асинхронным методом get_orders

    :param client: Экземпляр клиента API, используемый для выполнения запроса.
    :param client_id: Идентификатор клиента.
    """
    # Получим все возможные варианты ордеров для примера
    orders_response = await client.get_orders(
        client_id=client_id, 
        include_matched=True, 
        include_canceled=True, 
        include_active=True
        )
    
    print("Ответ на запрос списка ордеров:", orders_response)

# Асинхронная функция для снятия ордера
async def delete_order(client, client_id, transaction_id=0):
    """
    Асинхронная функция, демонстрирующая снятие ордера
    по идентификатору транзакции, присваиваемому при размещении.

    :param client: Экземпляр клиента API, используемый для выполнения запроса.
    :param client_id: Идентификатор клиента.
    :paran transaction_id: Идентификатор транзакции размещенного ордера
    """
    # Указать тут номер транзакции размещенного ордера
    cancellation_response = await client.cancel_order(client_id=client_id, transaction_id=transaction_id)
    print(f"Ответ на запрос об отмене ордера: {cancellation_response}")