
from tronpy.async_tron import AsyncTron


class TronFramework:
    def __init__(
        self,
        client: AsyncTron
    ) -> None:
        if client is None:
            raise ConnectionError

        self._client = client

    async def get_response_form(self, address: str):
        pass
