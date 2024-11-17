from .database import Base
from sqlalchemy import Column,String,Integer

class trying(Base):
    __tablename__ = 'trying'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    date = Column(Integer)