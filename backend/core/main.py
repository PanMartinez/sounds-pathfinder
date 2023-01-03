"""
Entrypoint for core API.
"""
from fastapi import FastAPI
from core.common.routers import app_routers
from core.common.middlewares import app_middlewares

# We are starting core
app = FastAPI()

# Here we register routers from all apps
for router in app_routers:
    app.include_router(router)

# The same goes for middlewares
for middleware in app_middlewares:
    app.add_middleware(middleware)

