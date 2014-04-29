# -*-coding: utf-8-*-

__author__ = "zxk"

from .config import default_config as config

import os
import codecs
import json

from pymongo import MongoClient
mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx

def run():
    fn = input("Specify the ci-pai-alias document > ")
    f = codecs.open(fn, "r", "utf-8")
    lines = f.readlines()
    f.close()
    cpad = {} # ci pai alias dictionary
    for line in lines:
        lst = [x.strip() for x in line.split("、")]
        for pai in lst:
            if pai in cpad:
                cpad[pai].extend(set(lst)) # need to remove duplication
            else:
                cpad[pai] = lst[ : ]

    for key in list(cpad.keys()):
        alias = list(set(cpad[key]))
        t = {}
        t["词牌名"] = key
        t["全部别名"] = alias
        mongo.ci_pai_alias.insert(t)

if __name__ == "__main__":
    run()
