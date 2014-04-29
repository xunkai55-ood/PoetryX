from .chchar import *

def sentences(pc):
    '''
    Input: Content of poetry
    Output: A list of sentence, splitted by full breakings
    '''

    split_on_list = lambda lst, b: [x for y in lst for x in y.split(b)]
    psl = [pc]
    for b in brk:
        psl = split_on_list(psl, b)
    return [x for x in psl if len(x)]

def sentence_len_tuple(pc):
    '''
    Input: Content of poetry
    Output: sentences length tuple (SLT)
    '''

    return tuple(map(len, sentences(pc)))