from pymongo import MongoClient

#connect to the mongo client
client = MongoClient("mongodb+srv://utkarshrasal12:goodwish12@cluster0.n2908.mongodb.net/mongo_database?retryWrites=true&w=majority")

#connect to the database.....(the database will automatically be created for the name you give)
db = client.mongo_database

#connect to the collection.....(the collection will automatically be created for the name you give)
collection_name = db['mongo_collection']




