
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import URL

from tronpy.async_tron import (
    AsyncTron,
    AsyncHTTPProvider
)

from src.repositories import UoW
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

# --- Tron initialize --- #
provider = AsyncHTTPProvider(
    TRON_PROVIDER_URI
)
tron_client = AsyncTron(
    provider=provider
)
