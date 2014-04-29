# -*- coding: utf-8 -*-

brk_1 = list(u'.。?？！!；;：:')
brk_2 = list(u',，、')
brk = brk_1 + brk_2

def is_breaking(c):
    return c in brk

ch_interval = [(u"\u4E00", u"\u9FFF"),
               (u"\u2E80", u"\u2FFF"),
               (u"\u31C0", u"\u31EF"),
               (u"\u3400", u"\u4DBF"),
               (u"\uF900", u"\uFAFF"),
               (u"\U00020000", u"\U0002FA1F")]

def is_ch(c):
    for inv in ch_interval:
        if inv[0] <= c and c <= inv[1]:
            return True
    return False

ignorables = list(u"<《(（）)》>『』「」")

def is_ignorable(c):
    return c in ignorables