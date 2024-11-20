from .database import Base
from sqlalchemy import Column, String, Integer

class Trying(Base):
    __tablename__ = 'trying'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date = Column(Integer)

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer,primary_key=True,index = True)
    name = Column(String)
    password = Column(String)