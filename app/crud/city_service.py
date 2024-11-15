from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.city_schema import City, CityCreate

async def create_city(db: AsyncSession, city: CityCreate):
    db_city = City(**city.model_dump())
    db.add(db_city)
    await db.commit()
    await db.refresh(db_city)
    return db_city

async def get_cities(db: AsyncSession, skip: int = 0, limit: int = 10):
    return await db.query(City).offset(skip).limit(limit).all()

async def get_city_by_id(db: AsyncSession, id: int):
    return await db.query(City).filter(City.ID == id).first()

async def get_cities_by_country(db: AsyncSession, country_code: str, skip: int = 0, limit: int = 10):
    return await db.query(City).filter(City.CountryCode == country_code).offset(skip).limit(limit).all()

async def get_cities_by_district(db: AsyncSession, district: str, country_code: str, skip: int = 0, limit: int = 10):
    return await db.query(City).filter(City.District == district and City.CountryCode == country_code).offset(skip).limit(limit).all()

async def get_cities_by_name(db: AsyncSession, name: str, skip: int = 0, limit: int = 10):
    return await db.query(City).filter(City.Name == name).offset(skip).limit(limit).all()