from pydantic import BaseModel
from typing import List, Optional


class ScaleNumber(BaseModel):
    """
    Представляет число с масштабом. Используется для точного представления финансовых данных,
    где 'num' это значение, а 'scale' определяет количество знаков после запятой.
    """
    num: int
    scale: int


class IntradayCandle(BaseModel):
    """
    Описывает финансовую свечу для интрадейных данных. Содержит информацию о времени ('timestamp'),
    ценах открытия ('open'), закрытия ('close'), максимальной ('high') и минимальной ('low'), 
    а также объем торгов ('volume').
    """
    timestamp: str
    open: ScaleNumber
    close: ScaleNumber
    high: ScaleNumber
    low: ScaleNumber
    volume: int


class IntradayData(BaseModel):
    """
    Содержит массив финансовых свечей ('candles') в ответе от API для интрадейных данных.
    """
    candles: List[IntradayCandle]


class Error(BaseModel):
    """
    Описывает структуру сообщения об ошибке с кодом ('code'), сообщением ('message') и дополнительными данными ('data').
    """
    code: str
    message: str
    data: str


class IntradayCandlesResponse(BaseModel):
    """
    Корневая модель ответа от API для интрадейных свечей, включающая в себя либо данные с финансовыми свечами ('data'),
    либо информацию об ошибке ('error'). Оба поля являются опциональными, так как зависят от результата запроса.
    """
    error: Optional[Error]
    data: Optional[IntradayData]