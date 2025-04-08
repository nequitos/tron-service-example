
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)
from sqlalchemy import (
    BigInteger,
    String,
    Uuid
)

from uuid import uuid4, UUID


__all__ = [
    "Base",
    "Wallet"
]


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Wallet(Base):
    __tablename__ = "wallet"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    uuid: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), default=uuid4, unique=True)

