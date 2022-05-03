from fastapi import APIRouter

from models.todos_models import Todo
from config.database import collection_name

from schemas.todos_schemas import todo_serializer, todos_serializer

from bson import ObjectId


api_router = APIRouter()

#post
@api_router.post('/')
async def create_todo(todo: Todo):
    id = collection_name.insert_one(dict(todo))
    _todo = todos_serializer(collection_name.find({"id": id.inserted_id}))

    return {
        'data': todo
    }

#retrieve
@api_router.get('/')
async def get_todos():
    todos = todos_serializer(collection_name.find())

    return todos

# update
@api_router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(todo)
    })
    return todos_serializer(collection_name.find({"_id": ObjectId(id)}))

# delete
@api_router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}