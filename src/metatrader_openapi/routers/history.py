from datetime import datetime

from fastapi import APIRouter, Depends

from metatrader_client import MT5Client

router = APIRouter(prefix="/api/v1/history", tags=["history"])


def get_client(client: MT5Client = Depends()):
    return client


@router.get("/deals")
def deals(from_date: datetime, to_date: datetime, client: MT5Client = Depends(get_client)):
    return client.history.get_deals(from_date, to_date)


@router.get("/orders")
def orders(from_date: datetime, to_date: datetime, client: MT5Client = Depends(get_client)):
    return client.history.get_orders(from_date, to_date)
