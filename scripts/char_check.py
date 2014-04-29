'''
This script checks if there exists invalid charachaters.
'''

__author__ = 'zxk'

from config import default_config as config
import utils

import os
import codecs
import json

from pymongo import MongoClient
mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx

def run():
    lst = mongo.poetry.find()
    for each in lst:
        print(each["搜韵id"])
        for c in each["内容"]:
            if not utils.is_ch(c) and not utils.is_breaking(c) and not utils.is_ignorable(c):
                mongo.poetry.update({"_id": each["_id"]}, {"$set": {"不完全": 1}})

    invalids = mongo.poetry.find({"不完全": {"$exists": True}})
    for each in invalids:
        print(each)

if __name__ == "__main__":
    run()
