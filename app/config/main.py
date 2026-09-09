from pathlib import Path

from pydantic import BaseModel, SecretStr
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class AppSettings(BaseModel):
    title: str = "AI PR Reviewer"
    version: str = "0.1.0"
    debug: bool = False
    log_level: str = "INFO"


class LLMSettings(BaseModel):
    base_url: str = ""
    api_key: SecretStr = SecretStr("")
    model: str = ""
    timeout: int = 60


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        toml_file=Path(__file__).parent / "settings" / "config.toml",
        env_nested_delimiter="__",
        extra="ignore",
    )

    app: AppSettings = AppSettings()
    llm: LLMSettings = LLMSettings()

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
        return (env_settings, TomlConfigSettingsSource(settings_cls))


config = Config.load()
