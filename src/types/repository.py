
from abc import abstractmethod, ABC
from typing import TypeVar, Annotated

from pydantic._internal._model_construction import ModelMetaclass

from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    AsyncEngine
)


T = TypeVar(
    "T",
    bound=Annotated[
        AsyncEngine,
        async_sessionmaker[AsyncSession],
        ModelMetaclass,
        DeclarativeAttributeIntercept
    ]
)


class Repository[T](ABC):
    @abstractmethod
    def __init__(
        self,
        session: T,
        relation: T
    ) -> None:
        self._session = abs(session)
        self._relation = abs(relation)

    @abstractmethod
    async def create(self, scheme: T) -> T:
        pass

    @abstractmethod
    async def read(self, scheme: T) -> T:
        pass

    @abstractmethod
    async def update(self, scheme: T) -> T:
        pass

    @abstractmethod
    async def delete(self, scheme: T) -> T:
        pass