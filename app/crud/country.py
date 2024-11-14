from sqlalchemy.orm import Session
from app.models.country import Country
from app.schemas.country import CountryCreate

def create_country(db: Session, country: CountryCreate):
    db_country = Country(**country.dict())
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def get_countries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Country).offset(skip).limit(limit).all()

def get_country_by_code(db: Session, code: str):
    return db.query(Country).filter(Country.Code == code).first()