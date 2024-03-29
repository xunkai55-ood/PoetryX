# -*-coding: utf-8-*-


__author__ = "zxk"

from pymongo import MongoClient
from .config import default_config as config

class PoetryDao(object):

    def __init__(self):
        self.mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx

    def find_by_ci_pai(self, pai, permit_alias = False):
        '''
        Input: One Ci Pai name
        Output: If `select_alias` is True, return poems with potential alias of Ci Pai queryed.
        '''

        if permit_alias == False:
            rst = self.mongo.poetry.find({"词牌名": pai})
        else:
            al = self.mongo.ci_pai_alias.find({"词牌名": pai})
            if len(al) == 0:
                return []
            al = al[0]["全部别名"]
            rst = self.mongo.poetry.find({"词牌名": {"$in": al}})
        return [x for x in rst]

