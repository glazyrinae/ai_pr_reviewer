from fastapi import APIRouter

from app.ai.llm import LLMClient
from app.api.schemas import HealthResponse
from app.config.main import config

router = APIRouter()
llm_client = LLMClient()


@router.get("/health", response_model=HealthResponse, tags=["service"])
def health() -> HealthResponse:
    return HealthResponse(
        api_status="ok",
        llm_status="ok" if llm_client.check() else "error",
        service=config.app.title,
        version=config.app.version,
        debug=config.app.debug,
    )
