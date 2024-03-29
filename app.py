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
import app.examples as examples

load_dotenv()

async def main():

    API_TOKEN = os.getenv("API_TOKEN")
    TRANSAQ_TOKEN = os.getenv("TRANSAQ_TOKEN")
    client = TradeAPIClient(api_token=API_TOKEN, api_url=settings.API_URL)

    # Проверка доступности токена
    await examples.check_access_token(client=client)

    # Проверка запроса дневных свечей
    await examples.check_day_candles(client=client)

    # Проверка запроса интадейных свечей
    await examples.check_intraday_candles(client=client)

    # Проверка размещения ордера
    await examples.place_order(client=client, client_id=TRANSAQ_TOKEN)

    # Проверка размещенных одеров
    await examples.check_orders(client=client, client_id=TRANSAQ_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())