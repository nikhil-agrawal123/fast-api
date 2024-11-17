from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DATABASE_URL_1 = 'sqlite:///./try.db'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL_1, connect_args={'check_same_thread': False})

session_loacal = sessionmaker(autocommit=False, bind=engine, autoflush=False)

Base = declarative_base()