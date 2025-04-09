
from uvicorn import Config, Server
from src.config import HOST, PORT

from src import app



async def main():
    config = Config("src.app:app", host=HOST, port=PORT, log_level="debug")
    server = Server(config=config)

    await server.serve()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())