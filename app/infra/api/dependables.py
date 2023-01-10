from starlette.requests import Request

from app.core.facade import StoreServiceCore


def get_core(request: Request) -> StoreServiceCore:
    core: StoreServiceCore = request.app.state.core
    return core
