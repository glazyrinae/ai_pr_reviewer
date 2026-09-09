"""Конфигурация сервиса: TOML как основной источник, переменные окружения — поверх него.

Окружение стоит перед файлом намеренно: config.toml лежит в репозитории и монтируется
в контейнер, поэтому всё, что зависит от стенда, переопределяется переменными вида
APP__ENVIRONMENT (двойное подчёркивание = вложенность).
"""

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class AppSettings(BaseModel):
    """Параметры самого процесса: как называемся и сколько логируем."""

    title: str = "AI PR Reviewer"
    version: str = "0.1.0"


class Config(BaseSettings):
    """Корень конфигурации: секции повторяют config.toml один в один."""

    model_config = SettingsConfigDict(
        toml_file="config/settings/config.toml",
        extra="ignore",
    )

    app: AppSettings = AppSettings()

    @classmethod
    def load(cls) -> "Config":
        return cls()

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            TomlConfigSettingsSource(settings_cls),
        )


config = Config.load()
