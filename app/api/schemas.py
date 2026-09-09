from typing import Literal

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: Literal["ok"] = Field(description="Процесс отвечает")
    service: str = Field(description="Имя сервиса из конфига")
    version: str= Field(description="Версия сервиса")
    debug: bool = Field(description="Режим отладки")
