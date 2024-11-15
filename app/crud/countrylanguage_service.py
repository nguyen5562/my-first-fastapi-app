from sqlalchemy.orm import Session
from app.schemas.countrylanguage_schema import CountryLanguageCreate, CountryLanguage

async def create_countrylanguage(db: Session, countrylanguage: CountryLanguageCreate):
    db_countrylanguage = CountryLanguage(**countrylanguage.model_dump())
    db.add(db_countrylanguage)
    await db.commit()
    await db.refresh(db_countrylanguage)
    return db_countrylanguage

async def get_countrylanguages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(CountryLanguage).offset(skip).limit(limit).all()

async def get_countrylanguage_by_country(db: Session, code: str, skip: int = 0, limit: int = 10):
    return db.query(CountryLanguage).filter(CountryLanguage.CountryCode == code).offset(skip).limit(limit).all()