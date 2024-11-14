from sqlalchemy import CHAR, Column, DECIMAL, Enum, Integer, SmallInteger, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'

    Code = Column(CHAR(3), primary_key=True, server_default=text("''"))
    Name = Column(CHAR(52), nullable=False, server_default=text("''"))
    Continent = Column(Enum('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America'),
                       nullable=False, server_default=text("'Asia'"))
    Region = Column(CHAR(26), nullable=False, server_default=text("''"))
    SurfaceArea = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    IndepYear = Column(SmallInteger)
    Population = Column(Integer, nullable=False, server_default=text("'0'"))
    LifeExpectancy = Column(DECIMAL(3, 1))
    GNP = Column(DECIMAL(10, 2))
    GNPOld = Column(DECIMAL(10, 2))
    LocalName = Column(CHAR(45), nullable=False, server_default=text("''"))
    GovernmentForm = Column(CHAR(45), nullable=False, server_default=text("''"))
    HeadOfState = Column(CHAR(60))
    Capital = Column(Integer)
    Code2 = Column(CHAR(2), nullable=False, server_default=text("''"))