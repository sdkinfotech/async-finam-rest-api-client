import aiohttp #  для асинхронных HTTP-запросов
import json # для работы с размещением ордера в формате json

# Определяем класс TradeAPIClient, который будет клиентом API.
class TradeAPIClient:
    """
    Клиент для взаимодействия с Trade API Finam.
    Позволяет выполнять асинхронные запросы к API для проверки токенов доступа.
    """
    
    # Конструктор класса, принимает два параметра: токен API и базовый URL API.
    def __init__(self, api_token: str, api_url: str):
        """
        Инициализация клиента API.
        :param api_token: Ключ API для доступа к сервису.
        :param api_url: Базовый URL API, к которому будут отправляться запросы.
        """
        # Сохраняем полученные значения в атрибутах объекта класса.
        self.base_url = api_url
        self.headers = {"accept": "text/plain", "X-Api-Key": api_token}

    # Асинхронный метод для проверки токена доступа.
    async def check_access_token(self) -> str:
        """
        Асинхронная проверка токена доступа.
        Возвращает ответ сервера о состоянии токена в текстовом формате.
        """
        # Формируем полный URL для запроса, добавляя к базовому URL путь к эндпоинту.
        url = f"{self.base_url}/access-tokens/check"
        # Создаем асинхронную сессию запросов.
        async with aiohttp.ClientSession() as session:
            # Отправляем GET-запрос, используя сессию и указанные заголовки.
            async with session.get(url, headers=self.headers) as response:
                # Возвращаем текст ответа сервера.
                return await response.text()
    
    # Асинхронный метод для получения информации о дневных свечах.
    async def get_day_candles(
            self, 
            security_board: str, 
            security_code: str, 
            time_frame: str, 
            interval_from: str, 
            interval_to: str, 
            interval_count: int) -> str:
        """
        Асинхронный запрос информации о дневных свечах.
        Принимает параметры запроса и возвращает ответ сервера с данными о свечах в текстовом формате.
        """
        # Формируем URL запроса, включая необходимые параметры как часть строки запроса (query string).
        url = (f"{self.base_url}/day-candles?SecurityBoard={security_board}&"
               f"SecurityCode={security_code}&TimeFrame={time_frame}&Interval.From={interval_from}&"
               f"Interval.To={interval_to}&Interval.Count={interval_count}")
        # Отправляем асинхронный GET-запрос с указанными параметрами и заголовками.
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                # Возвращаем текстовый ответ сервера.
                return await response.text()

    # Асинхронный метод для получения информации о внутридневных свечах.        
    async def get_intraday_candles(
            self, 
            security_board: str, 
            security_code: str, 
            time_frame: str, 
            interval_from: str, 
            interval_to: str, 
            interval_count: int) -> str:
        """
        Асинхронный запрос информации о интрадейных свечах.
        :param security_board: Режим торгов. (format:CLASS_NAME)
        :param security_code: Тикер инструмента. (format:TIKER_NAME)
        :param time_frame: Временной интервал (format:M1;M15;M30;H1).
        :param interval_from: Дата и время начала. (format:yyyy-mm-ddTHH:MM:SS)
        :param interval_to: Дата и время окончания. (format:yyyy-mm-ddTHH:MM:SS)
        :param interval_count: Количество запрашиваемых свечей. (format:int>0)
        :return: Ответ сервера с данными о свечах в текстовом формате.
        """
        # URL может потребовать изменения в зависимости от конечного API для интрадейных свечей
        url = (f"{self.base_url}/intraday-candles?SecurityBoard={security_board}&"
               f"SecurityCode={security_code}&TimeFrame={time_frame}&Interval.From={interval_from}&"
               f"Interval.To={interval_to}&Interval.Count={interval_count}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                return await response.text()
            
    # Асинхронный метод для получения информации о портфеле  
    async def get_portfolio(
            self, 
            client_id, 
            include_currencies=True, 
            include_money=True, 
            include_positions=True, 
            include_max_buy_sell=True) -> str:
        """
        Асинхронный запрос информации о портфеле.
        :param client_id: Идентификатор клиента для запроса портфеля.
        :return: Ответ сервера с данными о портфеле в текстовом формате.
        """
        url = (f"{self.base_url}/portfolio?ClientId={client_id}&"
               f"Content.IncludeCurrencies={str(include_currencies).lower()}&"
               f"Content.IncludeMoney={str(include_money).lower()}&"
               f"Content.IncludePositions={str(include_positions).lower()}&"
               f"Content.IncludeMaxBuySell={str(include_max_buy_sell).lower()}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                return await response.text()
    
    # Асинхронный метод для получения информации об инструментах          
    async def get_securities(self, board, seccode) -> str:
        """
        Асинхронный запрос информации об инструментах.

        :param board: Режим торговой площадки.
        :param seccode: Код ценной бумаги.
        :return: Ответ сервера с данными о запрошенных инструментах в текстовом формате.
        """
        url = f"{self.base_url}/securities?Board={board}&Seccode={seccode}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                return await response.text()
    
    # Асинхронный метод для размещения ордера
    async def place_order(self, order_data: dict) -> str:
        """
        Асинхронный метод для размещения ордера на покупку или продажу.

        :param order_data: Словарь с данными ордера.
        :return: Ответ сервера на запрос о размещении ордера.
        """
        url = f"{self.base_url}/orders"
        async with aiohttp.ClientSession() as session:
            # Используем параметр json= для автоматической сериализации и установки нужного Content-Type
            async with session.post(url, headers=self.headers, 
                                    json=order_data,   # Изменено с data на json
                                    ssl=False) as response:  # SSL-проверка отключена для упрощения примера
                return await response.text()

    # Асинхронный метод для получения информации об ордерах   
    async def get_orders(self, client_id: str, include_matched: bool, include_canceled: bool, include_active: bool) -> str:
        """
        Асинхронный метод для получения списка ордеров.

        :param client_id: Идентификатор клиента.
        :param include_matched: Включить исполненные ордера в ответ.
        :param include_canceled: Включить отмененные ордера в ответ.
        :param include_active: Включить активные ордера в ответ.
        :return: Ответ сервера на запрос о списка ордеров.
        """
        url = f"{self.base_url}/orders"
        # Преобразование булевых значений в строки
        params = {
            "ClientId": client_id,
            "IncludeMatched": str(include_matched).lower(),
            "IncludeCanceled": str(include_canceled).lower(),
            "IncludeActive": str(include_active).lower()
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers, params=params) as response:
                return await response.text()
    
    # Асинхронный метод для снятия ордера по транзакции           
    async def cancel_order(self, client_id: str, transaction_id: int) -> str:
        """
        Асинхронный метод для отмены ордера по идентификатору транзакции.

        :param client_id: Идентификатор клиента.
        :param transaction_id: Идентификатор транзакции ордера, который нужно отменить.
        :return: Ответ сервера на запрос об отмене ордера.
        """
        url = f"{self.base_url}/orders?ClientId={client_id}&TransactionId={transaction_id}"
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=self.headers) as response:
                return await response.text()