#!/usr/bin/python
# -*- coding: utf-8 -*-

from AWNDatabaseManagement import wn

def Temp():
    for word,ids  in sorted(wn.get_words(False)):
        print word, ids

def getSynonyms(word):
    synsets = wn.get_synsetids_from_word(word)
    synonyms = []
    for s in synsets:
        synonyms =  wn._items[s].getLinks()

    strList = []
    for i in range(len(synonyms)):
        strList.append(wn._items[synonyms[i][0][1]].getName())
    return strList

def ToList(lis):
    return [[''.join(list(i))] for i in lis]

def Group(dic, keys):
    sents = []
    dic[keys[0]] = ToList(dic[keys[0]])
    q = 0
    str = ''
    for i in dic[keys[0]]:
        for j in range(len(keys) - 1):
            for k in dic[keys[j + 1]]:
                for w in i:
                    str = w + ' ' + k
                    sents.append(str)
            str = ''
            i = sents
            sents = []
        dic[keys[0]][q] = i
        q = q + 1
    return dic


sent = u' إِسَاءَة جَمِيل َبَقِيَ فَضِيلَة قِطّ'
lis = sent.split()

# print lis

dic = {}

for i in lis:
    X =  getSynonyms(i)
    if len(X) != 0:
        dic[i] = X
    else:
        dic[i] = [i]
res =  Group(dic,lis)[u'إِسَاءَة']

for i in res:
    for word in i:
        print word
# Temp()
