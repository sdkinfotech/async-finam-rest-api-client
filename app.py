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

# Загрузка переменных окружения из файла .env для безопасного хранения и доступа к чувствительным данным.
load_dotenv()

# Главная асинхронная функция, которая использует вышеописанные функции для выполнения асинхронных запросов.
async def main():
    """
    Главная функция, демонстрирующая использование клиента API для отправки асинхронных запросов.
    Создает экземпляр клиента API, используя значения из переменных окружения и настроек,
    а затем последовательно вызывает функции для проверки токена доступа,
    запроса информации о дневных и интрадейных свечах.
    """
    API_TOKEN = os.getenv("API_TOKEN")
    TRANSAQ_TOKEN = os.getenv("TRANSAQ_TOKEN")
    client = TradeAPIClient(api_token=API_TOKEN, api_url=settings.API_URL)

    # Тестирование методов класса TradeAPIClient
    # Раскомментируйте нужные для проверки работоспособности кода
   
    # Запрос GET Проверка доступности API TOKEN
    # await examples.check_token(client)
    
    # Запрос GET информация о дневных свечах
    # await examples.fetch_day_candles(client)
    
    # Запрос GET информация о интрадейных свечах
    # await examples.fetch_intraday_candles(client)
    
    # Запрос GET информация о портфеле клиента 
    # await examples.fetch_portfolio(client, TRANSAQ_TOKEN)
    
    # Запрос информации по тикеру
    # await examples.fetch_securities(client)
   
    # Запрос POST поручение на размещение ордера
    # await examples.place_order(client=client, client_id=TRANSAQ_TOKEN)

    # Запрос GET информация о размещенных, отмененных, исполненных ордерах
    # await examples.get_orders(client=client, clieclent_id=TRANSAQ_TOKEN)

    # Запрос DELETE снятие ордера по номеру транзакции
    await examples.delete_order(client=client, client_id=TRANSAQ_TOKEN, transaction_id=40481018)
    

# Проверка, запущен ли скрипт непосредственно, и, если да, запуск главной функции.
if __name__ == "__main__":
    asyncio.run(main())