'''
test1.py

test PoetryAnalyzeLib.basic and the module framework
'''

import poetryx.PoetryAnalyzeLib as PAL
from poetryx import YunDict, PoetryDao

yun_dict = YunDict()
poetry_dao = PoetryDao()

plist = poetry_dao.find_by_ci_pai("十六字令")
print(len(plist))
print(plist[0])
pc = plist[0]["内容"]
print(PAL.sentences(pc))
print(PAL.sentence_len_tuple(pc))

for each in PAL.sentences(pc):
    print(each)
    print(yun_dict.process(each))

