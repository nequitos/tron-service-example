
from src.depends import uow


async def main():
    await uow.metadata_drop()
    await uow.metadata_create()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())