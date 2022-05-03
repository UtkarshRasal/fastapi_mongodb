from fastapi import FastAPI
from routes.todos_routes import api_router

app = FastAPI()

app.include_router(api_router)


