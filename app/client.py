import sys
from pathlib import Path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
import aiohttp
import logging  
from pydantic import ValidationError
from models.check_token_model import TokenValidationResponse

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