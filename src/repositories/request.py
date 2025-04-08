
from src.types.repository import (
    Repository,
    T,
    ABC
)

from sqlalchemy import (
    insert,
    select
)


class RequestRepository(Repository[T], ABC):
    async def create(self, scheme: T) -> T:
        stmt = insert(self._relation).values(
            bandwidth=scheme.bandwidth,
            energy=scheme.energy,
            trx_balance=scheme.trx_balance
        )

        async with self._session() as session:
            await session.execute(stmt)

        return scheme

    async def read(self, scheme: T) -> T | None:
        stmt = select(self._relation).order_by(
            self._relation.id
        ).limit(scheme.limit).offset(scheme.start)

        async with self._session() as session:
            result = await session.execute(stmt)

            if result is not None:
                return result.scalars()

    async def update(self, scheme: T) -> T:
        pass

    async def delete(self, scheme: T) -> T:
        pass