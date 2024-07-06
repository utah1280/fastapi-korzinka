from typing import List

from fastapi import Depends
from fastapi import APIRouter

from crud import category_crud as c
from auth.utils_jwt import get_payload
from core.models import db_helper
from core.schemas import category_schemas

from sqlalchemy.ext.asyncio import AsyncSession



categories_router = APIRouter(tags=["Categories"])

@categories_router.get("/get-categories", response_model=List[category_schemas.CategoryResponse])
async def get_categories(
    credentials: dict = Depends(get_payload),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    result = await c.get_all_getegories(session=session)
    return result

@categories_router.get("/get-categories/{id}", response_model=category_schemas.CategoryResponse)
async def get_categories_by_id(
    id: int,
    credentials: dict = Depends(get_payload),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.get_category_by_id(id, session=session)    
    return result

@categories_router.post("/new-category", response_model=category_schemas.CategoryResponse)
async def add_new_category(
    label: str,
    credentials: dict = Depends(get_payload),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.add_new_category(label, session=session)
    return result

@categories_router.patch("/update-category/{id}", response_model=category_schemas.CategoryIdResponse)
async def update_category(
    id: int,
    label: str,
    credentials: dict = Depends(get_payload),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.update_category(id, label=label, session=session)
    return result

@categories_router.delete("/delete-category/{id}", response_model=category_schemas.CategoryIdResponse)
async def delete_category(
    id: int,
    credentials: dict = Depends(get_payload),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.delete_category(id, session=session)
    return result