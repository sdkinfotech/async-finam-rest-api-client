from pydantic import BaseModel
from typing import List, Optional


class ScaleNumber(BaseModel):
    """
    Представляет число с масштабом. Используется для точного представления финансовых данных,
    где 'num' это значение, а 'scale' определяет количество знаков после запятой.
    """
    num: int
    scale: int


class Candle(BaseModel):
    """
    Описывает финансовую свечу для дневных данных. Содержит информацию о ценах открытия ('open'),
    закрытия ('close'), максимальной ('high') и минимальной ('low'), а также объем торгов ('volume') за
    определенную дату ('date').
    """
    date: str
    open: ScaleNumber
    close: ScaleNumber
    high: ScaleNumber
    low: ScaleNumber
    volume: int


class Data(BaseModel):
    """
    Содержит массив финансовых свечей ('candles') в ответе от API.
    """
    candles: List[Candle]


class Error(BaseModel):
    """
    Описывает структуру сообщения об ошибке с кодом ('code'), сообщением ('message') и дополнительными данными ('data').
    """
    code: str
    message: str
    data: str


class DayCandlesResponse(BaseModel):
    """
    Корневая модель ответа от API, включающая в себя либо данные с финансовыми свечами ('data'),
    либо информацию об ошибке ('error'). Оба поля являются опциональными, так как зависят от результата запроса.
    """
    error: Optional[Error]
    data: Optional[Data]