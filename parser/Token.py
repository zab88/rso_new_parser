# -*- coding: utf-8 -*-
import pymorphy2
import nltk

#init
morph = pymorphy2.MorphAnalyzer()

class Token(object):
    #!word_origin
    #!offset
    #!length
    #!is_anim

    def __init__(self, word, offset):
        global morph

        self.word_origin = word
        self.offset = offset
        arr = list(self.word_origin)
        self.length = len(arr)

        parsed = morph.parse( self.word_origin )
        # if self.word_origin == u'потерпевший':
        #     for e in parsed:
        #         print(e.tag)
            #print(parsed)
        if len(parsed) > 0:
            parsed = [parsed[0]]#ololo we get only first, sometimes it's bad
            for variant in parsed:
                #if {'NOUN'} in variant.tag:
                if variant.tag.animacy is not None and variant.tag.animacy == "anim": #inan, anim
                    self.is_anim = True

        # parsed = morph.parse(self.word_origin)[0]
        # if parsed is not None:
        #     #searching for subject
        #     if parsed.tag.POS == 'NOUN' and parsed.tag.case == 'nomn':
        #         # print(parsed.normal_form)
        #         subjects.append(parsed.normal_form)
