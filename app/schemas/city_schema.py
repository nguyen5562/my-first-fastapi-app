from pydantic import BaseModel

class CityBase(BaseModel):
    ID: int
    Name: str
    CountryCode: str
    District: str
    Population: int

class CityCreate(CityBase):
    pass

class City(CityBase):
    class Config:
        from_attributes = True
