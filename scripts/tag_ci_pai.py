# -*-coding: utf-8 -*-

'''
Tag ci pai for all poetry
'''

__author__ = "zxk"

import codecs
from pymongo import MongoClient
from config import default_config as config

mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx

def run():
    plist = mongo.poetry.find()

    cpnlist = []
    for each in mongo.ci_pai_alias.find():
        cpnlist.append(each["词牌名"])
    cpnset = set(cpnlist)

    for each in plist:
        sub = each["题目"]
        for i in reversed(list(range(len(sub)))):
            if sub[ : i + 1] in cpnset:
                mongo.poetry.update(
                    {"_id": each["_id"]},
                    {"$set": {"词牌名": sub[ : i + 1], "词": 1}}
                )
                print(sub[ : i + 1])

if __name__ == "__main__":
    run()