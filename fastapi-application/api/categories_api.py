from typing import List

from fastapi import status
from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException

from crud import category_crud as c
from core.models import db_helper
from core.schemas import category_schemas

from sqlalchemy.ext.asyncio import AsyncSession



categories_router = APIRouter(tags=["Categories"])

@categories_router.get("/get-categories", response_model=List[category_schemas.CategoryResponse])
async def get_categories(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.get_all_getegories(session=session)
    return result

@categories_router.get("/get-categories/{id}", response_model=category_schemas.CategoryResponse)
async def get_categories_by_id(
    id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.get_category_by_id(id, session=session)    
    return result

@categories_router.post("/new-category", response_model=category_schemas.CategoryResponse)
async def add_new_category(
    label: str,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.add_new_category(label, session=session)

    return result

@categories_router.patch("/update-category/{id}", response_model=category_schemas.CategoryIdResponse)
async def update_category(
    id: int,
    label: str,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.update_category(id, label=label, session=session)
    
    return result

@categories_router.delete("/delete-category/{id}", response_model=category_schemas.CategoryIdResponse)
async def delete_category(
    id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    result = await c.delete_category(id, session=session)
    
    return result