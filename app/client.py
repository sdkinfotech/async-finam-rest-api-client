import aiohttp #  для асинхронных HTTP-запросов

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