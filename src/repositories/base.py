
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)
from sqlalchemy import (
    BigInteger,
    Integer,
    Uuid,
    Float,
    DateTime
)

from datetime import datetime
from uuid import uuid4, UUID


__all__ = [
    "Base",
    "Request"
]


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Request(Base):
    __tablename__ = "request"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    uuid: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), default=uuid4, unique=True)

    bandwidth: Mapped[int] = mapped_column()
    energy: Mapped[int] = mapped_column()
    trx_balance: Mapped[float] = mapped_column(Float)
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now())
