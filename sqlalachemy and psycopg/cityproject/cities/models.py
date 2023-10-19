from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm  import declarative_base
from sqlalchemy import MetaData 
# from cityproject.cities.apps import CitiesConfig
from engine import session,engine
metadata=MetaData(schema='public')
Base = declarative_base(metadata=metadata)


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    population = Column(Integer)


metadata.create_all(engine)
