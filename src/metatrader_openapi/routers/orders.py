from fastapi import APIRouter, Depends

from metatrader_client import MT5Client
from metatrader_client.types import OrderType

router = APIRouter(prefix="/api/v1/orders", tags=["orders"])


def get_client(client: MT5Client = Depends()):
    return client


@router.post("/market")
def market_order(symbol: str, volume: float, order_type: OrderType, client: MT5Client = Depends(get_client)):
    return client.order.place_market_order(symbol, volume, order_type)
