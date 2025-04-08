
from fastapi import FastAPI
from uvicorn import Server, Config

from routers import *
from config import HOST, PORT


app = FastAPI()
app.include_router(request_router)


async def main():
    config = Config("app:app", host=HOST, port=PORT, log_level="debug", timeout_notify=30)
    server = Server(config=config)

    await server.serve()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())