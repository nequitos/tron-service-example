
from src.frameworks.tron import TronFramework, TAddress
from src.depends import uow, Request
from src.schemes.request import RequestCreateScheme


tron = TronFramework()


async def create(addr: str | TAddress):
    repository = uow[Request]

    scheme = await tron.get_response_form(addr)
    endpoint = await repository.create(scheme)

    assert scheme == endpoint


if __name__ == "__main__":
    import asyncio

    asyncio.run(create("TTzPiwbBedv7E8p4FkyPyeqq4RVoqRL3TW"))




