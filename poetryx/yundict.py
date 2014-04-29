from __future__ import division

__author__ = "zxk"

from .config import default_config as config
from pymongo import MongoClient

class YunDict(object):

    def __init__(self):
        mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx
        self.dict = mongo.yd_ci_lin    

    def query_char(self, c):
        rst = self.dict.find_one({u"字": c})[u"韵列表"]
        
        # append other information
        for each in rst:
            if each[u"声"] in list(u"上去入"):
                each[u"平仄"] = u"仄"
            else:
                each[u"平仄"] = u"平"

    def reorganize(self, cysd):
        '''
        Reorganize the distribution of yuns to the distribution of each attributes.
        cys: char's yuns distribution
        '''
        rst = {}
        targets = [u"韵", u"部", u"声"]
        for each in targets:
            rst[each] = []
            cands = [y[each] for y, p in cysd]
            cands = list(set(cands))
            for cand in cands:
                pc = 0
                for y, p in cysd:
                    if y[each] == cand:
                        pc += p
                rst[each].append((cand, pc))
        return rst

    def process(self, sentence, raw = False):
        '''
        return type:
            [yun_of_char_distribution]

        yun_of_char_distribution:
            [(yun, probability)]
        '''

        # Naive method
        rst = []
        for c in sentence:
            q = self.query_char(c)
            rst.append(zip(q, [1 / len(q)] * len(q)))
        if raw:
            return rst
        else:
            return map(self.reorganize, rst)

        
