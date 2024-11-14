from sqlalchemy import CHAR, Column, DECIMAL, Enum, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.models.country import Country

Base = declarative_base()

class Countrylanguage(Base):
    __tablename__ = 'countrylanguage'

    CountryCode = Column(ForeignKey('country.Code'), primary_key=True, nullable=False, index=True, server_default=text("''"))
    Language = Column(CHAR(30), primary_key=True, nullable=False, server_default=text("''"))
    IsOfficial = Column(Enum('T', 'F'), nullable=False, server_default=text("'F'"))
    Percentage = Column(DECIMAL(4, 1), nullable=False, server_default=text("'0.0'"))

    country = relationship(Country)