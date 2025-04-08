
from typing import AsyncGenerator

from contextlib import asynccontextmanager

from tronpy.async_tron import AsyncTron, TAddress

from src.schemes.request import RequestCreateScheme
from src.enums.tron import Network



class TronFramework:
    def __init__(
        self,
        network: Network | str = Network.NILE
    ) -> None:
        self._network = network

    async def get_response_form(self, address: TAddress | str) -> RequestCreateScheme:
        async with self.context() as client:
            trx_balance = await client.get_account_balance(addr=address)
            bandwidth = await client.get_bandwidth(addr=address)
            contract = await client.get_contract(addr=address)

            return RequestCreateScheme(
                bandwidth=bandwidth,
                energy=contract.origin_energy_limit,
                trx_balance=float(trx_balance)
            )

    @asynccontextmanager
    async def context(self) -> AsyncGenerator[AsyncTron]:
        client = AsyncTron(network=self._network)
        try:
            yield client
        finally:
            await client.close()


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    framework = TronFramework()
    result = loop.run_until_complete(framework.get_response_form(
        "TTJT3rGxcJLrHrjVj9iZR2BCXpWtt3t3t3"
    ))
    print(result)
