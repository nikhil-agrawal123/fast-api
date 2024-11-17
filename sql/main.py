from fastapi import FastAPI, HTTPException,Depends,status,Response,HTTPException
from . import schemas, models
from .database import engine, session_loacal
from sqlalchemy.orm import Session
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Create all tables
try:
    models.Base.metadata.create_all(engine)
    logger.info("Tables created successfully")
except Exception as e:
    logger.error(f"Error creating tables: {e}")

def get_db():
    db = session_loacal()
    try:
        yield db
    finally:
        db.close()

@app.post('/trying',status_code=status.HTTP_202_ACCEPTED)
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
        logger.error(f"Error creating trying: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@app.get('/trying',status_code=status.HTTP_200_OK)
def get_info(db: Session = Depends(get_db)):
    try:
        data = db.query(models.Trying).all()
        return data
    except Exception as e:
        logger.error('could not get data from the database')

@app.delete('/blog/{id}',status_code=status.HTTP_200_OK)
def delete(id,db:Session = Depends(get_db)):
    try:
        data = db.query(models.Trying).filter(models.Trying.id == id).delete(synchronize_session=False)
        db.commit()
        return 'succesfully deleted'
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='index not found')
    
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,db:Session = Depends(get_db),request = schemas.Trying):
    data = db.query(models.Trying).filter(models.Trying.id == id).update()

@app.get('/trying/{id}',status_code=200)
def get_id_info(id,response:Response, db:Session = Depends(get_db)):
    try:
        data = db.query(models.Trying).filter(models.Trying.id == id).first()
        return data
    finally:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='id does not exist') #better way to raise exceptions on the api