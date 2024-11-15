from sqlalchemy.orm import sessionmaker
from app.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

async_engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session