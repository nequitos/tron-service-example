
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import URL

from src.enums.tron import Network
from src.frameworks import *
from src.repositories import *
from .config import *


# --- Database initialize --- #
postgres_url = URL.create(
    "postgresql+asyncpg",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    database=POSTGRES_DATABASE
)
engine = create_async_engine(url=postgres_url)
uow = UoW(engine=engine)

# --- Repositories initialize --- #
uow[Request] = RequestRepository

# --- Frameworks initialize --- #
tron_framework = TronFramework()


def get_tron_framework() -> TronFramework:
    return tron_framework

def get_request_repository() -> RequestRepository:
    return uow[Request]

