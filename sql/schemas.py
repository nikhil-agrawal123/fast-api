from pydantic import BaseModel

class Trying(BaseModel):
    title: str
    date: int