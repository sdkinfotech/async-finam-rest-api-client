from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

class BuySell(str, Enum):
    """
    Энумератор для представления направления ордера: покупка или продажа.
    """
    Buy = "Buy"
    Sell = "Sell"

class Status(str, Enum):
    """
    Энумератор для представления статуса ордера.
    """
    Active = "Active"

class ConditionType(str, Enum):
    """
    Энумератор для типов условий ордера.
    """
    Bid = "Bid"

class ValidBeforeType(str, Enum):
    """
    Энумератор для представления времени действия ордера.
    """
    TillEndSession = "TillEndSession"

class Condition(BaseModel):
    """
    Модель условия ордера, включающая в себя тип условия, цену и время.
    """
    type: ConditionType 
    price: float  
    time: Optional[datetime] = None 

class ValidBefore(BaseModel):
    """
    Модель срока действия ордера.
    """
    type: ValidBeforeType  
    time: Optional[datetime] = None  

class Order(BaseModel):
    """
    Модель ордера, описывающая его основные характеристики, включая условия и срок действия.
    """
   
    orderNo: int = Field(alias='orderNo')
    transactionId: int = Field(alias='transactionId')
    securityCode: str = Field(alias='securityCode')
    clientId: str = Field(alias='clientId')
    status: Status
    buySell: BuySell
    createdAt: Optional[datetime] = None 
    price: float
    quantity: int
    balance: int
    message: str
    currency: str
    condition: Condition
    validBefore: ValidBefore
    acceptedAt: datetime  
    securityBoard: str  
    market: str  

class OrdersData(BaseModel):
    """
    Модель данных ордеров, содержащая информацию о клиенте и список его ордеров.
    """
    clientId: str  
    orders: List[Order]  

class OrdersResponse(BaseModel):
    """
    Модель ответа API по запросу ордеров, включающая данные ордеров или информацию об ошибке.
    """
    data: OrdersData  
    error: Optional[str] = None 

