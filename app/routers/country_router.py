from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.country_schema import CountryResponse, CountryCreate
from app.crud.country_service import create_country, get_countries, get_country_by_code, update_country, delete_country

router = APIRouter()

@router.post("/countries/", response_model=CountryResponse)
async def create(country: CountryCreate, db: AsyncSession = Depends(get_db)):
    return await create_country(db=db, country=country)

@router.get("/countries/", response_model=list[CountryResponse])
async def read_all(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_countries(db=db, skip=skip, limit=limit)

@router.get("/countries/{code}", response_model=CountryResponse)
async def read(code: str, db: AsyncSession = Depends(get_db)):
    return await get_country_by_code(db=db, code=code)

@router.put("/countries/{code}", response_model=CountryResponse)
async def update(code: str, country: CountryCreate, db: AsyncSession = Depends(get_db)):
    return await update_country(db=db, country=country, code=code)

@router.delete("/countries/{code}", response_model=bool)
async def delete(code: str, db: AsyncSession = Depends(get_db)):
    return await delete_country(db=db, code=code)