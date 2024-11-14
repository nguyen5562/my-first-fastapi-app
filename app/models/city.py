from sqlalchemy import CHAR, Column, ForeignKey, Integer, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.models.country import Country

Base = declarative_base()

class City(Base):
    __tablename__ = 'city'

    ID = Column(Integer, primary_key=True)
    Name = Column(CHAR(35), nullable=False, server_default=text("''"))
    CountryCode = Column(ForeignKey('country.Code'), nullable=False, index=True, server_default=text("''"))
    District = Column(CHAR(20), nullable=False, server_default=text("''"))
    Population = Column(Integer, nullable=False, server_default=text("'0'"))

    country = relationship(Country)