'''
Store poetry records from text-based system to mongo.
'''

__author__ = "zxk"
from config import default_config as config

import os
import codecs
import json

from pymongo import MongoClient
mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx

def run():
    fn = input("Specify the yun-dict document > ")
    f = open(fn, "r")
    dic = json.load(f)
    for each in dic:
        t = {}
        t['char'] = each
        t['yuns'] = dic[each]
        mongo.yd_ci_lin.insert(t)