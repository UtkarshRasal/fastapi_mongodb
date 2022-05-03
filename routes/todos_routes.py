from fastapi import APIRouter

from models.todos_models import Todo
from config.database import collection_name

from schemas.todos_schemas import todo_serializer, todos_serializer

from bson import objectid


api_router = APIRouter()


@api_router.post('/')
async def create_todo(todo: Todo):
    _id = collection_name.insert_one(dict(todo))
    _todo = todos_serializer(collection_name.find({"_id": _id.inserted_id}))

    return {
        'data': todo
    }

@api_router.get('/')
async def get_todos():
    todos = todos_serializer(collection_name.find())

    return todos