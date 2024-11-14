from fastapi import FastAPI
from app.routers import countries

app = FastAPI()

app.include_router(countries.router, prefix="/api", tags=["country"])