from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.schemas.country import Country, CountryCreate
from app.crud.country import create_country, get_countries, get_country_by_code

router = APIRouter()

@router.post("/countries/", response_model=Country)
def create_country(country: CountryCreate, db: Session = Depends(get_db)):
    return create_country(db=db, country=country)

@router.get("/countries/", response_model=list[Country])
def read_countries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_countries(db=db, skip=skip, limit=limit)

@router.get("/countries/{code}", response_model=Country)
def read_country(code: str, db: Session = Depends(get_db)):
    db_country = get_country_by_code(db=db, code=code)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country