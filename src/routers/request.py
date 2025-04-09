
from typing import Annotated, Union

from tronpy.async_tron import TAddress

from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
    Response,
    Form
)

from src.depends import (
    get_tron_framework,
    uow,
    RequestRepository,
    TronFramework,
    Request, get_request_repository
)
from src.schemes.request import *


router = APIRouter(
    prefix="/request"
)


@router.post(
    ""
)
async def create(
    address: Annotated[str, Form()],
    framework: TronFramework = Depends(get_tron_framework),
    repository: RequestRepository = Depends(get_request_repository)
) -> int:
    endpoint = await framework.get_response_form(address)
    endpoint = await repository.create(endpoint)

    if endpoint is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error on server"
        )

    return status.HTTP_200_OK


@router.get(
    "",
    response_model=list[RequestScheme]
)
async def read(
    page: int = 0,
    per_page: int = 0,
    repository: RequestRepository = Depends(get_request_repository)
) -> list[RequestScheme]:
    scheme = RequestReadScheme(
        page=page, per_page=per_page
    )
    endpoint = await repository.read(scheme)

    if endpoint is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error on server"
        )

    return endpoint