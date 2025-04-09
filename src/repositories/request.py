
from src.types.repository import (
    Repository,
    T,
    ABC
)

from sqlalchemy import (
    insert,
    select
)

from src.schemes.request import RequestScheme
from src.utils import get_paginated_data



class RequestRepository(Repository[T], ABC):
    async def create(self, scheme: T) -> T:
        stmt = insert(self._relation).values(
            bandwidth=scheme.bandwidth,
            energy=scheme.energy,
            trx_balance=scheme.trx_balance
        )

        async with self._session() as session:
            await session.execute(stmt)
            await session.commit()

        return scheme

    async def read(self, scheme: T) -> T | None:
        async with self._session() as session:
            paginated_data = await get_paginated_data(
                session=session,
                relation=self._relation,
                page=scheme.page,
                per_page=scheme.per_page
            )
            return [
                RequestScheme(
                    id=i.id,
                    uuid=i.uuid,
                    bandwidth=i.bandwidth,
                    energy=i.energy,
                    trx_balance=i.trx_balance,
                    date=i.date
                )
                for i in paginated_data
            ]

    async def update(self, scheme: T) -> T:
        pass

    async def delete(self, scheme: T) -> T:
        pass