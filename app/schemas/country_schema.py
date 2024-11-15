from pydantic import BaseModel
from typing import Optional

from app.models.country_model import Country

class CountryBase(BaseModel):
    Code: str
    Name: str
    Continent: str
    Region: str
    SurfaceArea: float
    IndepYear: Optional[int]
    Population: int
    LifeExpectancy: Optional[float]
    GNP: Optional[float]
    GNPOld: Optional[float]
    LocalName: str
    GovernmentForm: str
    HeadOfState: Optional[str]
    Capital: Optional[int]
    Code2: str

class CountryCreate(CountryBase):
    pass

class CountryUpdate(CountryBase):
    Code: Optional[str]
    Name: Optional[str]
    Continent: Optional[str]
    Region: Optional[str]
    SurfaceArea: Optional[float]
    IndepYear: Optional[int]
    Population: Optional[int]
    LifeExpectancy: Optional[float]
    GNP: Optional[float]
    GNPOld: Optional[float]
    LocalName: Optional[str]
    GovernmentForm: Optional[str]
    HeadOfState: Optional[str]
    Capital: Optional[str]
    Code2: Optional[str]

class CountryResponse(CountryBase):
    class Config:
        from_attributes = True
