from fastapi import FastAPI
from app.routers import country_router

app = FastAPI()

app.include_router(country_router.router, prefix="/api", tags=["Country"])