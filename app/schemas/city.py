from pydantic import BaseModel

class CityBase(BaseModel):
    Name: str
    CountryCode: str
    District: str
    Population: int

class CityCreate(CityBase):
    pass

class City(CityBase):
    ID: int

    class Config:
        from_attributes = True
