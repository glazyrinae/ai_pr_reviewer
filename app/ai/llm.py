import logging

import requests

from app.config.main import LLMSettings, config

logger = logging.getLogger(__name__)


class LLMClient:
    def __init__(self, settings: LLMSettings | None = None) -> None:
        self._settings = settings or config.llm

    def check(self) -> bool:
        try:
            response = requests.get(
                f"{self._settings.base_url}/models",
                headers={"Authorization": f"Bearer {self._settings.api_key.get_secret_value()}"},
                timeout=self._settings.timeout,
            )
            response.raise_for_status()
        except requests.RequestException:
            logger.warning("LLM недоступна: %s", self._settings.base_url, exc_info=True)
            return False

        models = {item.get("id") for item in response.json().get("data", [])}
        if self._settings.model not in models:
            logger.warning("Модель %s не найдена у провайдера", self._settings.model)
            return False

        return True
