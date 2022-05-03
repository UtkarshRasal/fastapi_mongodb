from lib2to3.pytree import Base
from pydantic import BaseModel

class Todo(BaseModel):
    name: str
    description: str
    completed: str
    date: str