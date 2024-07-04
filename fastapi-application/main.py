import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import router as api_router
from core.config import settings
from core.models import db_helper
from core.models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    yield
    # Shutdown
    await db_helper.dispose()
    
main_app = FastAPI(
    lifespan=lifespan,
)
main_app.include_router(
    api_router,
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )