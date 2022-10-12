import pymongo
DB_URL="mongodb://aonu:aonu@cluster0-shard-00-00.bty5q.mongodb.net:27017,cluster0-shard-00-01.bty5q.mongodb.net:27017,cluster0-shard-00-02.bty5q.mongodb.net:27017/test?replicaSet=atlas-n4iwun-shard-0&ssl=true&authSource=admin"
# client = pymongo.MongoClient(DB_URL)
# DB_URL = "mongodb://localhost:27017"

def property_db():
    client = pymongo.MongoClient(DB_URL)
    db = client['property']
    return db

def user_db():
    client = pymongo.MongoClient(DB_URL)
    db = client['property']
    return db
