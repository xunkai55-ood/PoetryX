# -*-coding: utf-8 -*-

'''
Extract Ci Lin Zheng Yun from docs of sou-yun.
'''

__author__ = "zxk"

yd = {}

import codecs
f = codecs.open("stash/ci_lin_zheng_yun.txt", "r", "utf-8")

from pymongo import MongoClient
from config import default_config as config

mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx

cnn = set(list("一二三四五六七八九十"))

leftling = set(list("[(（"))
rightling = set(list("])）"))

def add_to_yd(c, y, b, s):
    if c in yd:
        yd[c].append({"韵": y, "部": b, "声": s})
    else:
        yd[c] = [{"韵": y, "部": b, "声": s}]
    print(c, y, b, s, yd[c])

def run():
    bu = ""
    sheng = ""
    yun = ""
    ling = 0

    lines = f.readlines()
    for line in lines:

        line = line.strip()
        if len(line) == 0:
            continue

        if line[0] == "注":
            continue

        if line[0] == "其":
            continue

        if line[0] == "第":
            bu = line
        else:
            if line[0] in cnn:
                print(line)
                print(bu)
                sheng = input()
                for u in range(len(line)):
                    if not (line[u] in cnn):
                        yun = line[ : u + 1]
                        line = line[u + 1 : ]
                        break

            for each in line:
                if each in leftling:
                    ling += 1
                elif each in rightling:
                    ling -= 1
                elif ling == 0:
                    add_to_yd(each, yun, bu, sheng)

    for each in yd:
        t = {}
        t['字'] = each
        t['韵列表'] = yd[each]
        mongo.yd_ci_lin.insert(t)

if __name__ == "__main__":
    run()


