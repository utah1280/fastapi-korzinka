import uvicorn
from fastapi import FastAPI
from core.config import settings
from core.models import db_helper
from api import router as api_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Sturtup
    yield
    # Shutdown
    await db_helper.dispose()

main_app = FastAPI(
    lifespan=lifespan,
)
main_app.include_router(
    api_router,
)


if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )