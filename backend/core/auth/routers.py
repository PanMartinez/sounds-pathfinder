"""
Register and authentication related routers
"""
from fastapi import APIRouter, Depends

from core.config.settings import Settings, get_settings

auth_router = APIRouter()


@auth_router.get("/version")
async def version_router(settings: Settings = Depends(get_settings)):

    return {'version': settings.VERSION}
