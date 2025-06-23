from fastapi import APIRouter, Depends

from metatrader_client import MT5Client

router = APIRouter(prefix="/api/v1/accounts", tags=["accounts"])


def get_client(client: MT5Client = Depends()):
    return client


@router.get("/info")
def account_info(client: MT5Client = Depends(get_client)):
    return client.account.get_account_info()
