"""
From here we will be serving routers from all apps
"""
from core.auth.routers import auth_router

app_routers = [auth_router,]
