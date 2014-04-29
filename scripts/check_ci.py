# -*-coding: utf-8 -*-

'''
A terminal intereactive script to check all ci in db.
'''

__author__ = "zxk"

from .config import default_config as config
from . import utils

import os
import codecs
import json

from pymongo import MongoClient
mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx

def get_plist():
    return mongo.poetry.find({"ci": 1})

def is_suspect(p):
    '''Check if p is suspect, which means p may not be used.'''

    '''
    # Step.1 two adjoining breakings
    # This part should move to another module
    prev_brk = True
    for c in p["content"]:
        if prev_brk and utils.is_breaking(c):
            return True
        elif utils.is_breaking(c):
            prev_brk = True
        else:
            prev_brk = False
    '''

    # Step.2 just like an poetry
    # TBD
    pass

def run():
    for each in get_plist():
        if is_suspect(each):
            os.system("clear")
            print(each["subject"])
            print(each["a_info"])
            print("====================")
            print(each["content"])
            print("====================")
            if len(input("remove?").strip()) == 0:
                mongo.poetry.remove({"_id": each["_id"]})

if __name__ == "__main__":
    run()