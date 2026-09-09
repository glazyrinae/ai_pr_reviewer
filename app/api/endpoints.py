from fastapi import APIRouter

from app.api.schemas import HealthResponse
from app.config import config

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["service"])
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=config.app.title,
        version=config.app.version,
        debug=config.app.debug,
    )
