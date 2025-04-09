
from typing import AsyncGenerator

from contextlib import asynccontextmanager

from tronpy.async_tron import AsyncTron, TAddress
from tronpy.keys import to_base58check_address, to_hex_address

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
            address = to_base58check_address(address)
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
