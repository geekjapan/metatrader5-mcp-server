from fastapi import APIRouter, Depends

from metatrader_client import MT5Client

router = APIRouter(prefix="/api/v1/positions", tags=["positions"])


def get_client(client: MT5Client = Depends()):
    return client


@router.get("")
def all_positions(client: MT5Client = Depends(get_client)):
    return client.order.get_all_positions()
