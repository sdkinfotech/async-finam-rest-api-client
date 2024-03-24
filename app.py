"""
Приложение для работы с TRADE API FINAM
Разработчик https://github.com/sdkinfotech
Репозиторий https://github.com/sdkinfotech/async-finam-rest-api-client.git
"""

import asyncio
from dotenv import load_dotenv
import os
from app.client import TradeAPIClient
import app.settings as settings

load_dotenv()

async def main():

    API_TOKEN = os.getenv("API_TOKEN")
    TRANSAQ_TOKEN = os.getenv("TRANSAQ_TOKEN")
    client = TradeAPIClient(api_token=API_TOKEN, api_url=settings.API_URL)

    # Проверка доступности токена
    response = await client.check_access_token()
    print(response)

if __name__ == "__main__":
    asyncio.run(main())