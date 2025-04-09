
from typing import Annotated, TypeVar, Any

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker
)
from .base import (
    Base,
    Request
)

from .request import RequestRepository


__all__ = [
    "UoW",
    "Request",
    "RequestRepository"
]

T = TypeVar(
    "T",
    bound=Annotated[
        AsyncEngine,
        Any
    ]
)
K = TypeVar(
    "K",
    bound=Annotated[
        type,
        Any,
        Request
    ]
)
V = TypeVar(
    "V",
    bound=Annotated[
        type,
        Any,
        RequestRepository
    ]
)


class UoW[T, K, V]:
    def __init__(
        self,
        engine: T
    ) -> None:
        self._engine = engine
        self.__session = async_sessionmaker(bind=engine)
        self.__repositories = {}

    def __setitem__(
        self,
        relation: K,
        repository: V
    ) -> None:
        if relation not in self.__repositories:
            self.__repositories[relation] = repository(
                session=self.__session,
                relation=relation
            )

    def __getitem__(self, relation: K) -> V:
        return self.__repositories[relation]

    def __delitem__(self, relation: K) -> None:
        del self.__repositories[relation]

    async def metadata_create(self):
        async with self._engine.begin() as core:
            await core.run_sync(Base.metadata.create_all)

    async def metadata_drop(self):
        async with self._engine.begin() as core:
            await core.run_sync(Base.metadata.drop_all)