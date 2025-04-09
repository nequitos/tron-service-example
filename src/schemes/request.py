
from .base import Validator
from uuid import UUID
from datetime import datetime


class RequestCreateScheme(Validator):
    bandwidth: int
    energy: int
    trx_balance: float


class RequestScheme(RequestCreateScheme):
    id: int
    uuid: UUID
    date: datetime


class RequestReadScheme(Validator):
    page: int
    per_page: int