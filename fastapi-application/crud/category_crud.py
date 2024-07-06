from core.models import Categories

from fastapi import HTTPException
from fastapi import status

from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession



async def get_all_getegories(session: AsyncSession):
    query = select(Categories).order_by(Categories.id)
    result = await session.scalars(query)
    return result.all()

async def get_category_by_id(id: id, session: AsyncSession):
    query = select(Categories).where(Categories.id == id)
    result = await session.scalar(query)

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="error: category with given id not found")

    return result

async def add_new_category(label: str, session: AsyncSession):
    query = select(Categories).where(Categories.label == label)
    result = await session.scalar(query)
    
    if result is None:
        new = Categories(label=label)
        session.add(new)
        await session.commit()
        return new
    
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="error: category already exists")
    
async def update_category(id: int, label: str, session: AsyncSession):
    query = select(Categories).where((Categories.label == label) )
    result = await session.scalar(query)

    if result is not None:
        HTTPException(status_code=status.HTTP_409_CONFLICT, detail="error: category already exists")

    query = select(Categories).where(Categories.id == id)
    result = await session.scalar(query)

    if result is not None:
        result.label = label
        await session.commit()
        return result
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="error: category with given id not found")

async def delete_category(id: int, session: AsyncSession):
    query = delete(Categories).where(Categories.id == id)
    result = await session.execute(query)    
    await session.commit()
    
    return {"id": id}