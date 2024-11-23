from fastapi import FastAPI, HTTPException,Depends,status,HTTPException
from . import schemas, models
from .database import engine, session_loacal
from sqlalchemy.orm import Session
from passlib.context import CryptContext


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = session_loacal()
    try:
        yield db
    finally:
        db.close()

@app.post('/trying',status_code=status.HTTP_202_ACCEPTED,tags=['trying'])
def create_trying(request: schemas.Trying, db: Session = Depends(get_db)):
    try:
        new_trying = models.Trying(
            title=request.title,
            date=request.date
        )
        db.add(new_trying)
        db.commit()
        db.refresh(new_trying)
        return new_trying
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@app.get('/trying',status_code=status.HTTP_200_OK,tags=['trying'])
def get_info(db: Session = Depends(get_db)):
    try:
        data = db.query(models.Trying).all()
        return data
    except Exception as e:
        return 'Could not load database'

@app.delete('/blog/{id}',status_code=status.HTTP_200_OK,tags=['blog'])
def delete(id,db:Session = Depends(get_db)):
    try:
        data = db.query(models.Trying).filter(models.Trying.id == id).delete(synchronize_session=False)
        db.commit()
        return 'succesfully deleted'
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='index not found')
    
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blog'])
def update(id,request:schemas.Trying,db:Session = Depends(get_db)):
    data = db.query(models.Trying).filter(models.Trying.id == id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no data with the provided index')
    data.update(title = request.title())
    db.commit()

    return 'updated sucussefully'

@app.get('/trying/{id}',status_code=200, response_model=schemas.show,tags=['trying'])
def get_id_info(id, db:Session = Depends(get_db)):
    try:
        data = db.query(models.Trying).filter(models.Trying.id == id).first()
        return data
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='id does not exist') #better way to raise exceptions on the api

pwd = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

@app.post('/user',status_code=status.HTTP_200_OK,tags=['user'])
def users(request : schemas.User,db:Session = Depends(get_db)):
    hashed = pwd.hash(request.password)
    user_info = models.User(
        name = request.user_name,
        password = hashed
    )
    db.add(user_info)
    db.commit()
    db.refresh(user_info)
    return 'succesful'

@app.get('/user/{id}',status_code=status.HTTP_200_OK,response_model=schemas.User_show,tags=['user'])
def get_user(id:int,db:Session = Depends(get_db)):
    try:
        data = db.query(models.User).filter(models.User.id == id).first()
        return data
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='id does not exist')