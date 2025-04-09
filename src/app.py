
from fastapi import FastAPI
from .routers import *


app = FastAPI()
app.include_router(request_router)
