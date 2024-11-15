from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.city_schema import City, CityCreate
from app.crud.city_service import create_city, get_cities, get_cities_by_country, get_cities_by_district, get_cities_by_name, get_city_by_id

router = APIRouter()

@router.post("/cities/", response_model=City)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    return create_city(db=db, city=city)

@router.get("/cities/", response_model=list[City])
def read_cities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_cities(db=db, skip=skip, limit=limit)

@router.get("/cities/{id}", response_model=City)
def read_city(id: int, db: Session = Depends(get_db)):
    db_city = get_city_by_id(db=db, id=id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

@router.get("/cities/name/{name}", response_model=list[City])
def read_cities_by_name(name: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_cities = get_cities_by_name(db=db, name=name, skip=skip, limit=limit)
    if db_cities is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_cities

@router.get("/cities/country/{code}", response_model=list[City])
def read_cities_by_country(code: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_cities = get_cities_by_country(db=db, country_code=code, skip=skip, limit=limit)
    if db_cities is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_cities

@router.get("/cities/district/{district}/{code}", response_model=list[City])
def read_cities_by_district(district: str, code: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_cities = get_cities_by_district(db=db, district=district, country_code=code, skip=skip, limit=limit)
    if db_cities is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_cities