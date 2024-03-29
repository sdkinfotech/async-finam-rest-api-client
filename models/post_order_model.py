from pydantic import BaseModel
from typing import Optional

class OrderPlacementResponse(BaseModel):
    """
    Модель данных для ответа на размещение ордера.

    Атрибуты:
        clientId (str): Идентификатор клиента.
        transactionId (int): Идентификатор транзакции.
        securityCode (str): Код безопасности.
        error (Optional[str]): Ошибка, если такая имеется.
    """
    clientId: str
    transactionId: int
    securityCode: str
    error: Optional[str] = None