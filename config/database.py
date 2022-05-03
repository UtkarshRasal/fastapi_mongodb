from pymongo import MongoClient
from dotenv import dotenv_values


config = dotenv_values(".env")
client = MongoClient("mongodb+srv://utkarshrasal12:goodwish12@cluster0.n2908.mongodb.net/mongo_database?retryWrites=true&w=majority")

db = client.mongo_database

collection_name = db['mongo_collection']




