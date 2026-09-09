import logging

from fastapi import FastAPI

from app.api.endpoints import router
from app.config.main import config


def create_app() -> FastAPI:
    logging.basicConfig(
        level=config.app.log_level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    application = FastAPI(
        title=config.app.title,
        version=config.app.version,
        debug=config.app.debug,
    )
    application.include_router(router)
    return application


app = create_app()
