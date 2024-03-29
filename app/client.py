import sys
from pathlib import Path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
import aiohttp
import logging  
from pydantic import ValidationError
from models.check_access_token_model import TokenValidationResponse
from models.day_candles_model import DayCandlesResponse
from models.intraday_candles_model import IntradayCandlesResponse
from models.post_order_model import OrderPlacementResponse
from models.get_orders_model import OrdersResponse

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('app.log',encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Создание обработчика для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Форматирование для обработчиков лога
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class TradeAPIClient:
    """
    Клиент для взаимодействия с Trade API Finam.
    Позволяет выполнять асинхронные запросы к API для проверки токенов доступа.
    """
    def __init__(self, api_token: str, api_url: str):
        """
        Инициализация клиента API.
        """
        self.base_url = api_url
        self.headers = {"accept": "application/json", "X-Api-Key": api_token}

    async def check_access_token(self) -> TokenValidationResponse:
        """
        Асинхронно проверяет валидность токена доступа.
        """
        url = f"{self.base_url}/access-tokens/check"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as response:
                    response_json = await response.json()
                    try:
                        return TokenValidationResponse(**response_json)
                    except ValidationError as e:
                        logger.error("Ошибка валидации данных: %s", e.json())
                        raise
        except aiohttp.ClientError as e:
            logger.error("Ошибка при выполнении запроса к API: %s", str(e))
            raise
        except Exception as e:
            logger.error("Неожиданная ошибка: %s", str(e))
            raise
    
    async def get_day_candles(self, security_board: str, security_code: str, time_frame: str, interval_from: str, interval_to: str) -> DayCandlesResponse:
        """
        Асинхронно запрашивает данные о дневных свечах для определенного инструмента и периода времени.
        :param security_board: Доска торгов (например, 'TQBR').
        :param security_code: Код ценной бумаги (например, 'GAZP').
        :param time_frame: Таймфрейм ('D1' для дневных свеч).
        :param interval_from: Начальная дата интервала.
        :param interval_to: Конечная дата интервала.
        :return: Экземпляр DayCandlesResponse с данными о свечах.
        """
        url = f"{self.base_url}/day-candles?SecurityBoard={security_board}&SecurityCode={security_code}&TimeFrame={time_frame}&Interval.From={interval_from}&Interval.To={interval_to}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as response:
                    response_json = await response.json()
                    try:
                        return DayCandlesResponse(**response_json)
                    except ValidationError as e:
                        logger.error("Ошибка валидации данных: %s", e.json())
                        raise
        except aiohttp.ClientError as e:
            logger.error("Ошибка при выполнении запроса к API: %s", str(e))
            raise
        except Exception as e:
            logger.error("Неожиданная ошибка: %s", str(e))
            raise    

    async def get_intraday_candles(self, security_board: str, security_code: str, time_frame: str, interval_from: str, interval_to: str) -> IntradayCandlesResponse:
        """
        Асинхронно запрашивает данные об интрадейных свечах для определенного инструмента и периода времени.
        :param security_board: Доска торгов (например, 'TQBR').
        :param security_code: Код ценной бумаги (например, 'GAZP').
        :param time_frame: Таймфрейм для интрадейных свеч ('M1', 'M5', 'M15', 'M30', 'H1').
        :param interval_from: Начальная дата и время интервала в формате ISO 8601.
        :param interval_to: Конечная дата и время интервала в формате ISO 8601.
        :return: Экземпляр CandlesResponse с данными о свечах.
        """
    
        url = f"{self.base_url}/intraday-candles?SecurityBoard={security_board}&SecurityCode={security_code}&TimeFrame={time_frame}&Interval.From={interval_from}&Interval.To={interval_to}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as response:
                    response_json = await response.json()
                    try:
                        return IntradayCandlesResponse(**response_json)
                    except ValidationError as e:
                        logger.error("Ошибка валидации данных: %s", e.json())
                        raise
        except aiohttp.ClientError as e:
            logger.error("Ошибка при выполнении запроса к API: %s", str(e))
            raise
        except Exception as e:
            logger.error("Неожиданная ошибка: %s", str(e))
            raise

    async def place_order(self, order_data: dict) -> OrderPlacementResponse:
        """
        Асинхронный метод для размещения ордера на покупку или продажу.

        :param order_data: Словарь с данными ордера.
        :return: Экземпляр OrderPlacementResponse с результатом размещения ордера.
        """
        url = f"{self.base_url}/orders"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=self.headers, 
                                        json=order_data,   
                                        ssl=False) as response:  
                    if response.status == 200:
                        response_json = await response.json()
                        return OrderPlacementResponse(**response_json['data'])
                    else:
                        error_message = await response.text()
                        logger.error("Ошибка при размещении ордера: %s", error_message)
                        raise Exception("Ошибка при размещении ордера: " + error_message)
        except aiohttp.ClientError as e:
            logger.error("Ошибка при выполнении запроса к API: %s", str(e))
            raise
        except Exception as e:
            logger.error("Неожиданная ошибка: %s", str(e))
            raise

    async def get_orders(self, client_id: str, include_matched: bool = True, include_canceled: bool = True, include_active: bool = True) -> OrdersResponse:
        """
        Асинхронная функция для получения списка ордеров.
        Возвращает экземпляр OrdersResponse с данными о списке ордеров.

        :param client_id: Идентификатор клиента.
        :param include_matched: Включать ли исполненные ордера в ответ.
        :param include_canceled: Включать ли отмененные ордера.
        :param include_active: Включать ли активные ордера.
        :return: Экземпляр OrdersResponse с результатами запроса.
        """
        url = f"{self.base_url}/orders?clientId={client_id}&includeMatched={include_matched}&includeCanceled={include_canceled}&includeActive={include_active}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers, ssl=False) as response:  # SSL-проверка отключена для упрощения примера
                    if response.status == 200:
                        response_json = await response.json()
                        return OrdersResponse(**response_json)
                    else:
                        error_message = await response.text()
                        logger.error("Ошибка при получении списка ордеров: %s", error_message)
                        raise Exception("Ошибка при получении списка ордеров: " + error_message)
        except aiohttp.ClientError as e:
            logger.error("Ошибка при выполнении запроса к API: %s", str(e))
            raise
        except Exception as e:
            logger.error("Неожиданная ошибка: %s", str(e))
            raise