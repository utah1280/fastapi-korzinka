from sqlalchemy import select
from sqlalchemy import delete
from core.models import Categories
from sqlalchemy.ext.asyncio import AsyncSession

async def get_all_getegories(session: AsyncSession):
    query = select(Categories).order_by(Categories.id)
    result = await session.scalars(query)
    return result.all()

async def get_category_by_id(id: id, session: AsyncSession):
    query = select(Categories).where(Categories.id == id)
    result = await session.scalar(query)

    if result is None:
        return "error: category with given id is not found"

    return result

async def add_new_category(label: str, session: AsyncSession):
    query = select(Categories).where(Categories.label == label)
    result = await session.scalar(query)
    
    if result is None:
        new = Categories(label=label)
        session.add(new)
        await session.commit()
        return new
    
    return "error: category already exists"
    
async def update_category(id: int, label: str, session: AsyncSession):
    query = select(Categories).where((Categories.label == label) )
    result = await session.scalar(query)

    if result is not None:
        return "error: category already exists"

    query = select(Categories).where(Categories.id == id)
    result = await session.scalar(query)

    if result is not None:
        result.label = label
        await session.commit()
        return result
    
    return "error: category with given id is not found"

async def delete_category(id: int, session: AsyncSession):
    query = delete(Categories).where(Categories.id == id)
    result = await session.execute(query)    
    await session.commit()
    
    return {"id": id}