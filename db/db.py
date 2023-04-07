import pymongo

def get_connection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    return myclient