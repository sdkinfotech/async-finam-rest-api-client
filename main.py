
import asyncio # для асинхронных приложений
from dotenv import load_dotenv # для загрузки переменных окружения из .env файла.
import os # для работы с операционной системой, включая переменные окружения.
from app.client import TradeAPIClient # для взаимодействия с Trade API Finam.
import app.settings as settings # Импорт настроек приложения

# Загрузка переменных окружения из файла .env
load_dotenv()  

# Определение асинхронной главной функции main.
async def main():
    """
    Главная асинхронная функция для проверки работы клиента API, 
    включая запрос информации о дневных свечах.
    Эта функция демонстрирует два основных использования клиента: проверку токена
    и получение информации о дневных свечах для заданного инструмента.
    """
    # Получение токена API из переменных окружения.
    API_TOKEN = os.getenv("API_TOKEN")
    # Создание экземпляра клиента API с использованием токена и URL из настроек.
    client = TradeAPIClient(api_token=API_TOKEN, api_url=settings.API_URL)
    
    # Выполнение запроса проверки токена доступа и вывод ответа.
    token_check = await client.check_access_token()
    print(f"Проверка токена доступа: {token_check}")

    # Параметры запроса информации о дневных свечах.
    security_board = "TQBR"  # Режим торговой площадки.
    security_code = "GAZP"   # Тикер трейдовой бумаги.
    time_frame = "D1"        # Временной интервал для свечей.
    interval_from = "2024-03-01"  # Начальная дата интервала.
    interval_to = "2024-03-21"    # Конечная дата интервала.
    interval_count = 0       # Количество запрашиваемых свечей (0 для всех доступных).
    
    # Выполнение запроса получения информации о дневных свечах и вывод ответа.
    day_candles_info = await client.get_day_candles(
        security_board=security_board, 
        security_code=security_code, 
        time_frame=time_frame, 
        interval_from=interval_from, 
        interval_to=interval_to, 
        interval_count=interval_count
    )
    print(f"Информация о дневных свечах: {day_candles_info}")

# Проверка, что скрипт запущен как основная программа, и запуск асинхронной функции main.
if __name__ == "__main__":
    asyncio.run(main())