from fastapi import APIRouter

from core.config import settings

from .auth_api import auth_router
from .contacts_api import contacts_router
from .categories_api import categories_router



router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(
    auth_router,
    prefix="/auth",
)

router.include_router(
    categories_router,
    prefix=settings.api.categories,
)

router.include_router(
    contacts_router,
    prefix=settings.api.contacts,
)