# -*-coding: utf-8-*-

from __future__ import division
__author__ = "zxk"

from pymongo import MongoClient
from .config import default_config as config

class PoetryDao(object):

    def __init__(self):
        mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx
        self.table = mongo.poetry

    def 