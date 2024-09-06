import pymongo

import json

import copy

from config import config

import requests

import bson

from bson.json_util import dumps as bson_dumps, loads as bson_loads


def get_connection():
    client = pymongo.MongoClient(config.URL)
    return client


def set_item(client, database, collection, query, new):
    database_item = client[database]
    collection_item = database_item[collection]
    collection_item.update_one(query, new)


def get_item(client, database, collection, query):
    database_item = client[database]
    collection_item = database_item[collection]
    item = collection_item.find_one(query)
    item = copy.deepcopy(item)
    try:
        del item["_id"]
    except TypeError:
        return {"error": "Could not find"}

    return item


def get_items(client, database, collection, query):
    database_item = client[database]
    collection_item = database_item[collection]
    items = collection_item.find(query)
    all = []

    for item in items:
        itemi = copy.deepcopy(item)
        del itemi["_id"]
        all.append(itemi)

    return all


def get_id(collection):
    if config.AM_I_ID_SERVER:

        with open("ids.json", "r") as f:
            data = json.load(f)

        Id = data[collection]["id"]

        with open("ids.json", "w") as f:
            data[collection]["id"] = int(Id) + 1
            json.dump(data, f)
    else:
        try:
            Id = requests.get(f"{config.MAIN_ID_SERVER}/id/{collection}")
            Id.raise_for_status()
        except:
            raise ConnectionError("Could not get response from main server")
        else:
            Id = Id.text

    return Id


def create_item(client, database, collection, item):
    database_item = client[database]
    collection_item = database_item[collection]
    item["ID"] = get_id(collection)
    collection_item.insert_one(item)

    return item["ID"]


def get_all(client, database, collection):
    database_item = client[database]
    collection_item = database_item[collection]
    all = []
    for item in collection_item.find():
        itemi = copy.deepcopy(item)
        del itemi["_id"]
        all.append(itemi)

    return all
