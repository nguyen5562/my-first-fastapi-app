from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.schemas.country_schema import CountryCreate, CountryUpdate
from app.models.country_model import Country

async def create_country(db: AsyncSession, country: CountryCreate):
    db_country = Country(**country.model_dump())
    db.add(db_country)
    await db.commit()
    await db.refresh(db_country)
    return db_country

async def get_countries(db: AsyncSession, skip: int = 0, limit: int = 10):
    query = select(Country).offset(skip).limit(limit)
    result = await db.execute(query)
    data = result.scalars().all()
    if data is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return data

async def get_country_by_code(db: AsyncSession, code: str):
    query = select(Country).filter(Country.Code == code)
    result = await db.execute(query)
    data = result.scalars().first()
    if data is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return data

async def update_country(db: AsyncSession, country: CountryUpdate, code: str):
    db_country = await get_country_by_code(db=db, code=code)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    for key, value in country.model_dump().items():
        if value is not None:
            setattr(db_country, key, value)
    await db.commit()
    await db.refresh(db_country)
    return db_country

async def delete_country(db: AsyncSession, code: str):
    db_country = await get_country_by_code(db=db, code=code)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    await db.delete(db_country)
    await db.commit()
    return True