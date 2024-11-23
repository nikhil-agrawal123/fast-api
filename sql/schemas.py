from pydantic import BaseModel,Field

class Trying(BaseModel):
    title: str
    date: int

class User(BaseModel):
    user_name : str
    password: str

class User_show(BaseModel):
    user_name:str = Field(alias='name')
    class Config():
        from_attributes = True

class show(Trying):
    user_show: User_show
    class Config():
        from_attributes = True 