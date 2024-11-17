from fastapi import FastAPI
from . import schemas,models
from .database import engine,session_loacal
from sqlalchemy.orm import Session
from fastapi import Depends

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = session_loacal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create():
    return 'creating'

@app.post('/info')  
def info(request:schemas.inp,db:Session = Depends(get_db)):
    new_info = models.trying(title=request.title,date = request.date)
    db.add(new_info)
    db.commit()
    db.refresh(new_info)
    return new_info