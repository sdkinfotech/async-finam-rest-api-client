"""
Асинхронный клиент API для взаимодействия с Trade API Finam.

Этот модуль предоставляет асинхронный клиент API, который может использоваться
для выполнения различных API запросов к Trade API Finam,
включая проверку токенов доступа и другие операции торговли и управления портфелем.

Примеры включают асинхронную отправку запросов для получения информации о свечах,
заказах и операциях со стоп-заявками.
"""

import aiohttp
class TradeAPIClient:
    """
    Клиент для взаимодействия с Trade API Finam.
    Позволяет выполнять асинхронные запросы к API для проверки токенов доступа.
    """
    
    def __init__(self, api_token: str, api_url: str):
        """
        Инициализация клиента API.
        :param api_token: Ключ API для доступа к сервису.
        """
        self.base_url = api_url
        self.headers = {"accept": "text/plain", "X-Api-Key": api_token}

    async def check_access_token(self) -> str:
        """
        Асинхронная проверка токена доступа.
        :return: Ответ сервера о состоянии токена.
        """
        url = f"{self.base_url}/access-tokens/check"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                # Возможна обработка статуса ответа, например, response.status
                return await response.text()
