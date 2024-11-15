from pydantic import BaseModel

class CountryLanguageBase(BaseModel):
    CountryCode: str
    Language: str
    IsOfficial: str
    Percentage: float

class CountryLanguageCreate(CountryLanguageBase):
    pass

class CountryLanguage(CountryLanguageBase):
    class Config:
        from_attributes = True
