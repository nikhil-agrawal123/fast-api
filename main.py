from fastapi import FastAPI
from typing import Optional
import uvicorn
from pydantic import BaseModel
from typing import Optional

class something(BaseModel):
    title:str
    body:str 
    published:bool
    address:Optional[str]

class info(BaseModel):
    name:str
    age:int
    about:str
    working_professional:bool
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'nikhil'}}

@app.get('/about')
def about():
    return 'Hello welcome to my first api'

@app.get('/names/{id}')
def names(id):
    return {'name' : id}

@app.get('/names/{id}/age')
def age(id):
    return {'names':{id:{'age':18}}}

@app.get('/howdy')
def test(limit=10,published:bool = True,sort:Optional[str] = None):
    if published:
        return f'{limit} of the docs from db'
    else:
        return 'nothing to show'
    
@app.post('/something')
def something(request:something):
    return {'data':f'something is created with the title {request.title}'}

@app.post('/info')
def info(request:info):
    return f'hello {request.name}'

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=9000)