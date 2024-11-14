from pydantic import BaseModel
from typing import Optional

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

class Country(CountryBase):
    class Config:
        from_attributes = True
