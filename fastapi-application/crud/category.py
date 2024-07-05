from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import delete
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from core.models import Categories

async def get_all_categories(session: AsyncSession):
    stmt = select(Categories).order_by(Categories.id)
    result = await session.scalars(stmt)
    return result.all()

async def get_category_by_id(id: int, session: AsyncSession):
    stmt = select(Categories).where(Categories.id == id)
    result = await session.scalar(stmt)
    return result

# !TODO
async def new_category(label: str, session: AsyncSession):
    try:
        async with session.begin():
            new_category = Categories(label=label)
            session.add(new_category)
            session.flush()
    except IntegrityError as e:
        await session.rollback()
        raise ValueError(f"Category with label '{label}' already exists") from e
    
    return new_category

# !TODO
async def update_category(id: int, label: str, session: AsyncSession):
    pass

# !TODO   
async def delete_category_by_id(id: int, session: AsyncSession):
    pass