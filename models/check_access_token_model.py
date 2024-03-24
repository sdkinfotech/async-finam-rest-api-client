from pydantic import BaseModel
from typing import Optional, Any

class TokenValidationResponseData(BaseModel):
    """
    Представление данных токена, полученных в ответе API.

    Эта модель Pydantic описывает структуру данных токена, 
    возвращаемых API при успешной проверке.
    Основывается на том, что ответ содержит 
    идентификатор токена как минимум.

    Атрибуты:
        id (int): Уникальный идентификатор токена доступа.
    """
    id: int

class TokenValidationResponse(BaseModel):
    """
    Модель ответа API на проверку токена доступа.

    Описывает стандартный ответ API на запросы, 
    связанные с токенами доступа, включая проверку валидности токена. 
    Модель содержит информацию о данных токена в случае успешного 
    ответа и ошибке, если проверка не пройдена.

    Атрибуты:
        data (Optional[TokenValidationResponseData]): 
        Данные токена доступа в случае успешной проверки. 
        None, если в ответе нет данных.
        
        error (Optional[Any]): 
        Информация об ошибке, если проверка не пройдена.
        None, если ошибок нет.
    """
    data: Optional[TokenValidationResponseData]
    error: Optional[Any]