# -*- coding: utf-8 -*-

__author__ = "zxk"

from .config import default_config as config
from . import utils

import os
import codecs
import json
import re

from pymongo import MongoClient
mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT).poetryx

from . import tag_ci_pai
from . import poetry_char_count
from . import ci_lin_extractor
from . import alias2mongo

def fix(half):
    rec = re.compile(r"&#[0-9]{1,10};")
    rst = rec.findall(half)
    if len(rst):
        for each in rst:
            num = int(each[2:-1])
            half = half.replace(each, chr(num))
    return half

def fix2(raw):
    rec = re.compile("（.*?）", re.DOTALL)
    half = rec.sub("", raw)
    rec = re.compile(r"&#[0-9]{1,10};")
    rst = rec.findall(half)
    if len(rst):
        for each in rst:
            num = int(each[2:-1])
            half = half.replace(each, chr(num))
    rst = ""
    for each in half:
        if each >= '\U00002C00' or each == '\u25a1':
            rst += each
    return rst

def get_inner(line):
    rec = re.compile(r"'.*?'", re.DOTALL)
    try:
        x = rec.findall(line)[0]
    except:
        return ""
    else:
        return x[1:-1]

def db_write(syid, d, a, s, p, raw):
    t = {
        "搜韵id": syid,
        "朝代": d,
        "作者名": a,
        "来源": "搜韵网",
        "题目": s,
        "内容": p,
        "raw_data": raw
    }
    mongo.poetry.insert(t)
def main(f):

    dynasty = ""
    author = ""
    subject = ""
    poem = ""
    rp = ""
    cnt = 0

    for rline in f:
        line = fix(rline)
        if line.find("<Dynasties>") >= 0:
            pass
        elif line.find("<Dynasty name") >= 0:
            dynasty = get_inner(line)
        elif line.find("<Authors>") >= 0:
            pass
        elif line.find("<Author name") >= 0:
            author = get_inner(line)
        elif line.find("<Poems>") >= 0:
            pass
        elif line.find("<Poem subject") >= 0:
            subject = get_inner(line)
        elif line.find("</Poem>") >= 0:
            cnt += 1
            if cnt >= start:
                db_write(cnt, dynasty, author, subject, poem, rp)
            poem = ""
            rp = ""
            pass
        elif line.find("</Poems>") >= 0:
            pass
        elif line.find("</Author>") >= 0:
            pass
        elif line.find("</Authors>") >= 0:
            pass
        elif line.find("</Dynasty>") >= 0:
            pass
        elif line.find("</Dynasties>") >= 0:
            pass
        else:
            poem = poem + fix2(rline)
            rp = rp + rline

def rebuild_poetry():
    fn = input("Specify db.txt here > ")
    f = codecs.open(fn, "r", "utf-8")
    main(f)
    f.close()
    poetry_char_count.run()
    tag_ci_pai.run()

if "__main__" == __name__:
    alias2mongo.run()
    # ci_lin_extractor.run() 
    # need to do that manually. Redirect input from log.
    rebuild_poetry()