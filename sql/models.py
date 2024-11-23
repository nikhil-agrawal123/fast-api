from .database import Base
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship

class Trying(Base):
    __tablename__ = 'trying'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date = Column(Integer)

    user_id = Column(Integer,ForeignKey("User.id"))
    user_show = relationship('User' , back_populates='users')

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer,primary_key=True,index = True)
    name = Column(String)
    password = Column(String)

    users = relationship('Trying',back_populates='user_show')