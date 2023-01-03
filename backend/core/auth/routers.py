"""
Register and authentication related routers
"""
from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.get("/")
async def test_router():
    return {"message": "Hello World Bogdan"}
