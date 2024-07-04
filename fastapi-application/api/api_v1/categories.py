from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings

from core.schemas.category import (
    CategoryBase,
)

from core.models import db_helper
from crud import category

router = APIRouter(tags=["Categories"])

@router.get("/get-all", response_model=list[CategoryBase])
async def get_categories(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await category.get_all_categories(session=session)
    return result

@router.get("/get-category{id}", response_model=CategoryBase)
async def get_category(
    id,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await category.get_category_by_id(id, session=session)
    return result