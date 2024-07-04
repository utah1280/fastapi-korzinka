from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Categories

async def get_all_categories(session: AsyncSession):
    stmt = select(Categories).order_by(Categories.id)
    result = await session.scalars(stmt)
    return result.all()