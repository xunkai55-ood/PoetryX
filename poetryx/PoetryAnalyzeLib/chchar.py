brk_1 = list('.。?？！!；;：:')
brk_2 = list(',，、')
brk = brk_1 + brk_2

def is_breaking(c):
    return c in brk

ch_interval = [("\u4E00", "\u9FFF"),
    ("\u2E80", "\u2FFF"),
    ("\u31C0", "\u31EF"),
    ("\u3400", "\u4DBF"),
    ("\uF900", "\uFAFF"),
    ("\U00020000", "\U0002FA1F")]

def is_ch(c):
    for inv in ch_interval:
        if inv[0] <= c and c <= inv[1]:
            return True
    return False

ignorables = list("<《(（）)》>『』「」")

def is_ignorable(c):
    return c in ignorables