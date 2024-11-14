import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from alembic import command
from alembic.config import Config

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Chạy migrations khi ứng dụng khởi động
    run_migrations()
    yield  # Chờ ứng dụng hoạt động
    # Tắt ứng dụng (có thể dọn dẹp tài nguyên ở đây nếu cần)
    print("Shutting down...")

# Khởi tạo ứng dụng với lifespan handler
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI project with Alembic!"}