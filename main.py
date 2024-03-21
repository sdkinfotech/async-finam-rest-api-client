import asyncio
from dotenv import load_dotenv
import os
from app.client import TradeAPIClient  # Импортируйте вашего клиента API соответственно
import app.settings as settings

load_dotenv()  # Загрузите переменные среды

async def main():
    """
    Главная асинхронная функция для проверки работы клиента API.
    """
    API_TOKEN = os.getenv("API_TOKEN")
    # Используйте переменную окружения для токена
    client = TradeAPIClient(api_token=API_TOKEN, api_url=settings.API_URL)
    token_check = await client.check_access_token()
    print(token_check)

if __name__ == "__main__":
    asyncio.run(main())