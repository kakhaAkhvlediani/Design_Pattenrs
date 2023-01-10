from fastapi import FastAPI

from app.core.facade import StoreServiceCore
from app.infra.api.receipt_api import receipt_api
from app.infra.api.report_api import report_api
from app.infra.SQLlite import SQLiteStoreRepository


def setup() -> FastAPI:
    app = FastAPI()

    app.include_router(receipt_api)
    app.include_router(report_api)

    store_repository = SQLiteStoreRepository()

    app.state.core = StoreServiceCore.create(store_repository=store_repository)

    return app
