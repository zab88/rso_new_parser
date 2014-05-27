# -*- coding: utf-8 -*-
import pymysql
import pymorphy2
import nltk
import string

import functions
import os

all_files = os.listdir('mvd_texts/')

file = open('count_animacy.txt', 'w+')
for ttt in all_files:
    fff = open('mvd_texts/' + ttt, 'r')
    r = fff.read()
    fff.close()

    animate_num = 0
    not_animate_num = 0

    text = r.decode('windows-1251')
    #text = text.encode('utf-8')
    tokens = nltk.word_tokenize(text)
    tokens = [i for i in tokens if ( i not in string.punctuation )]

    for word in tokens:
        print(word)
        is_animate, is_noun = functions.isAnimateNoun2(word)
        if is_noun:
            if is_animate:
                animate_num += 1
                file.write(word.encode('utf-8') + "\n")
            else:
                not_animate_num += 1

    # file.write(r[2].decode('utf-8')+' nouns:'+(animate_num) + '/' + (animate_num+not_animate_num) )
    # file.write(r[2].encode('utf-8')+' nouns:'+str(animate_num).encode('utf-8') + '/' + str(animate_num+not_animate_num).encode('utf-8') )
    # file.write(r[2]+' nouns:'+str(animate_num) + '/' + str(animate_num+not_animate_num) )
    # file.write("\n")
    #print(tokens[0])
    # exit()
file.close()
print(not_animate_num)
print(animate_num)