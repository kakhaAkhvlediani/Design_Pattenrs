from fastapi import APIRouter, Depends

from app.core.facade import StoreServiceCore
from app.core.store.interactor import XReportResponse
from app.infra.api.dependables import get_core

report_api = APIRouter()


@report_api.get("/report/x_report")
def make_x_report(core: StoreServiceCore = Depends(get_core)) -> XReportResponse:
    return core.make_x_report()
