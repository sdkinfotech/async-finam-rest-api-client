# TRADE API FINAM

## TREE представление проекта
- `async-finam-rest-api-client` корневой каталог
    - `/app/` каталог плиложения
        - `clinet.py` модуль для взаимодействия с API
        - `examples.py` модуль с описанием примеров
        - `settings.py` модуль для конфигурации клиента

    - `/models/` каталог со схемами представления данных
        - `check_access_token_model` модуль для представления данных ответа на запрос проверки ключа
        - `day_candles_model.py` модуль для представления данных дневных свечей
        - `intraday_candles_model.py` модуль для представления данных интрадейных свечей
        - `post_order_model.py` модуль для представления данных ответа на размещение ордера
        - `get_orders_model.py` модуль для представления данных ответа на запрос списка ордеров
    
    - `app.py` модуль для запуска приложения
    - `README.MD` файл с описанием приложения
    - `requirements.txt` файл с описанием зависимостей


## DEV в разработке

### Описание схем
- **Статус**: `В работе`
- **Каталог**: `/models` **OK**
    -**Модуль**: `check_access_token_model.py` **OK**
    -**Модуль**: `day_candles_model.py` **OK**
    -**Модуль**: `intraday_candles_model.py` **OK**
        - Класс `TradeAPIClient`, **OK**
            - Метод: `check_access_token`. **OK**
            - Метод: `get_day_candles` **OK**
            - Метод: `get_intraday_candles` **OK**
            - Метод: `place_order` **OK**
            - Метод: `get_orders **OK**

## REFACTORING - изменения, улучшения, дополнения

### Обработка ошибок
- **Статус**: `Выполнено`
- **Модуль**: `/client.py`
    - Добавлена обработка ошибок в класс `TradeAPIClient`.

### Логирование
- **Статус**: `Ожидает окончания разработки зависимых методов`
- **Модуль**: `/client.py`
    - Класс `TradeAPIClient`.
        - Метод: `check_access_token:` **OK**
        - Метод: `get_day_candles` **OK**
        - Метод: `get_intraday_candles` **OK**
        - Метод: `place_order` **ОК**
        - Метод: `get_orders **OK**

### Обработка Responce Code=200
- **Статус**: `Запланировано`
- **Модуль**: `/client.py`