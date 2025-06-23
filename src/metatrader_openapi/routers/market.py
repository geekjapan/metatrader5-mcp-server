from fastapi import APIRouter, Depends

from metatrader_client import MT5Client

router = APIRouter(prefix="/api/v1/market", tags=["market"])


def get_client(client: MT5Client = Depends()):
    return client


@router.get("/symbols")
def symbols(client: MT5Client = Depends(get_client)):
    return client.market.get_symbols()
