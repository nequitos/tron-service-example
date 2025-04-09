
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select, Sequence


async def get_paginated_data(
    session: AsyncSession,
    relation: DeclarativeAttributeIntercept,
    *,
    page: int,
    per_page: int
) -> Sequence:
    offset = (page - 1) * per_page
    stmt = select(relation).offset(offset).limit(per_page)
    result = await session.execute(stmt)

    return result.scalars().all()