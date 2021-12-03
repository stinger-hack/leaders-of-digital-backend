from fastapi import FastAPI

from .info import info_router
from .login import login_router
from .chat import chat_router
from .feed import feed_router
from .showcase import showcase_router
from settings import PREFIX


def setup_routes(app: FastAPI) -> None:
    app.include_router(info_router)
    app.include_router(chat_router)
    app.router.prefix = PREFIX
    app.include_router(login_router)
    app.include_router(feed_router)
    app.include_router(showcase_router)

