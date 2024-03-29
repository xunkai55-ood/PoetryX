

__author__ = "zxk"

from .config import default_config as config
from pymongo import MongoClient

class YunDict(object):

    def __init__(self):
        mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx
        self.dict = mongo.yd_ci_lin    

    def query_char(self, c):
        rst = self.dict.find_one({"字": c})["韵列表"]
        
        # append other information
        for each in rst:
            if each["声"] in list("上去入"):
                each["平仄"] = "仄"
            else:
                each["平仄"] = "平"

        return rst

    def reorganize(self, cysd):
        '''
        Reorganize the distribution of yuns to the distribution of each attributes.
        cys: char's yuns distribution
        '''
        rst = {}
        targets = ["韵", "部", "声", "平仄"]
        for each in targets:
            rst[each] = {}
            for y, p in cysd:
                if y[each] in rst[each]:
                    rst[each][y[each]] += p
                else:
                    rst[each][y[each]] = p
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
            rst.append(list(zip(q, [1 / len(q)] * len(q))))
        if raw:
            return rst
        else:
            return list(map(self.reorganize, rst))

        
