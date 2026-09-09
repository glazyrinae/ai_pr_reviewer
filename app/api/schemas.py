from typing import Literal

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    api_status: Literal["ok"] = Field(description="Процесс отвечает")
    llm_status: str = Field(description="Ответ от LLM")
    service: str = Field(description="Имя сервиса из конфига")
    version: str = Field(description="Версия сервиса")
    debug: bool = Field(description="Режим отладки")
