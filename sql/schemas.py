from pydantic import BaseModel,Field

class Trying(BaseModel):
    title: str
    date: int

class User(BaseModel):
    user_name : str
    password: str
class show(Trying):
    class Config():
        from_attributes = True 

class User_show(BaseModel):
    user_name:str = Field(alias='name')
    class Config():
        from_attributes = True