from pydantic import BaseModel
from typing import List, Optional

class ScaleNumber(BaseModel):
    """
    Представляет число с масштабом, используемое для точного представления финансовых данных,
    где числовое значение (num) сопровождается масштабом (scale), указывающим на количество знаков после запятой.

    Attributes:
        num (int): Числовое значение.
        scale (int): Количество знаков после запятой.
    """
    num: int  # Числовое значение
    scale: int  # Масштаб, количество знаков после запятой

class IntradayCandle(BaseModel):
    """
    Описывает одну финансовую свечу для интрадейных данных, включая информацию о времени, ценах открытия, 
    закрытия, максимальной и минимальной ценах, а также объеме торгов.

    Attributes:
        timestamp (str): Временная метка свечи.
        open (ScaleNumber): Цена открытия.
        close (ScaleNumber): Цена закрытия.
        high (ScaleNumber): Максимальная цена.
        low (ScaleNumber): Минимальная цена.
        volume (int): Объем торгов.
    """
    timestamp: str  # Временная метка
    open: ScaleNumber  # Цена открытия
    close: ScaleNumber  # Цена закрытия
    high: ScaleNumber  # Максимальная цена
    low: ScaleNumber  # Минимальная цена
    volume: int  # Объем торгов

class IntradayData(BaseModel):
    """
    Содержит список финансовых свечей для интрадейных данных.

    Attributes:
        candles (List[IntradayCandle]): Список финансовых свечей.
    """
    candles: List[IntradayCandle]  # Список финансовых свечей

class Error(BaseModel):
    """
    Предоставляет структуру для сообщения об ошибке, содержащую код ошибки, текстовое сообщение 
    и любые дополнительные данные, связанные с ошибкой.

    Attributes:
        code (str): Код ошибки.
        message (str): Сообщение об ошибке.
        data (str): Дополнительные данные об ошибке.
    """
    code: str  # Код ошибки
    message: str  # Сообщение об ошибке
    data: str  # Дополнительные данные об ошибке

class IntradayCandlesResponse(BaseModel):
    """
    Представляет корневой объект ответа API для запроса интрадейных свечей, содержащий либо данные свечей,
    либо информацию об ошибке.

    Attributes:
        error (Optional[Error]): Опциональное поле с информацией об ошибке.
        data (Optional[IntradayData]): Опциональное поле с данными о свечах.
    """
    error: Optional[Error]  # Информация об ошибке, если таковая присутствует
    data: Optional[IntradayData]  # Данные о свечах, если запрос был успешным