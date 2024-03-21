# Импорт необходимых модулей:
# asyncio для создания и управления асинхронными задачами,
# dotenv для работы с переменными окружения,
# os для доступа к функциональности операционной системы,
# TradeAPIClient для взаимодействия с Trade API Finam,
# settings для доступа к настройкам приложения, таким как URL API.
import asyncio
from dotenv import load_dotenv
import os
from app.client import TradeAPIClient
import app.settings as settings

# Загрузка переменных окружения из файла .env для безопасного хранения и доступа к чувствительным данным.
load_dotenv()

# Асинхронная функция для проверки токена доступа.
async def check_token(client):
    """
    Асинхронный запрос к API для проверки валидности токена доступа.
    Аргументы:
    - client: экземпляр клиента API, через который производится запрос.
    Выводит в консоль результат проверки токена доступа.
    """
    token_check = await client.check_access_token()
    print(f"Проверка токена доступа: {token_check}")

# Асинхронная функция для запроса информации о дневных свечах.
async def fetch_day_candles(client):
    """
    Запрос информации о дневных свечах для заданного инструмента и временного периода.
    Аргументы:
    - client: экземпляр клиента API, используемый для выполнения запроса.
    Выводит в консоль полученные данные о свечах.
    """
    day_candles_info = await client.get_day_candles(
        security_board="TQBR",  # Режим торговой площадки.
        security_code="GAZP",   # Тикер трейдовой бумаги.
        time_frame="D1",        # Временной интервал (D1 - один день).
        interval_from="2024-03-01",  # Начальная дата интервала.
        interval_to="2024-03-21",    # Конечная дата интервала.
        interval_count=0       # Количество запрашиваемых свечей (0 означает все доступные).
    )
    print(f"Информация о дневных свечах: {day_candles_info}")

# Асинхронная функция для запроса информации о интрадейных свечах.
async def fetch_intraday_candles(client):
    """
    Запрос информации о интрадейных свечах за заданный временной интервал.
    Аргументы:
    - client: экземпляр клиента API для отправки запроса.
    Выводит в консоль полученные данные о интрадейных свечах.
    """
    intraday_candles_info = await client.get_intraday_candles(
        security_board="TQBR",  # Режим торговой площадки.
        security_code="SBER",   # Тикер трейдовой бумаги.
        time_frame="M1",        # Временной интервал (M1 - одна минута).
        interval_from="2024-03-01T09:00:00",  # Время начала интервала.
        interval_to="2024-03-01T18:00:00",    # Время окончания интервала.
        interval_count=0        # Количество запрашиваемых свечей (0 означает все доступные).
    )
    print(f"Информация о интрадейных свечах: {intraday_candles_info}")

# Асинхронная функция для запроса информации о портфеле TRANSAQ
async def fetch_portfolio(client, client_id):
    """
    Запрос информации о портфеле с использованием предоставленного client_id.
    
    :param client: Экземпляр клиента API, используемый для выполнения запроса.
    :param client_id: Идентификатор клиента для запроса портфеля.
    """
    portfolio_info = await client.get_portfolio(client_id)
    print(f"Информация о портфеле: {portfolio_info}")

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

    # await check_token(client)
    # await fetch_day_candles(client)
    # await fetch_intraday_candles(client)
    await fetch_portfolio(client, TRANSAQ_TOKEN)

# Проверка, запущен ли скрипт непосредственно, и, если да, запуск главной функции.
if __name__ == "__main__":
    asyncio.run(main())