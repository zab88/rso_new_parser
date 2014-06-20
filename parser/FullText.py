# -*- coding: utf-8 -*-
import pymorphy2
import nltk
from Token import Token

class FullText(object):
    #!text
    hl_text = None
    tokens = []
    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

    def __init__(self, text):
        self.text = text

        # chars = self.text.split("")
        chars = list(self.text)
        current_word = u''
        current_offset = 0
        for k, char in enumerate(chars):
            if char in list(self.symbols):
                current_word += char
            elif char in [u' ', u"\n"] and current_word != u'':
                self.tokens.append(Token(current_word, current_offset))
                current_word = ''
                current_offset = k+1


        # tokens = nltk.word_tokenize(text)
        #
        # for token in tokens:
        #     self.tokens.append( Token(token) )

    def hl_01(self):
        for token in reversed(self.tokens):
            if hasattr(token, "is_anim") and token.is_anim is True:
                self.make_html(token)
        self.write_html()

    def make_html(self, token, color="red"):
        if self.hl_text is None:
            self.hl_text = self.text

        point_start = token.offset
        point_end = token.offset + token.length
        # print(token.word_origin)
        # print(self.hl_text[point_start:point_end])
        # print(point_start, point_end)

        #self.hl_text = self.hl_text.decode('utf-8')
        self.hl_text = self.hl_text[:point_start] + "<b>" + self.hl_text[point_start:point_end] + "</b>" + self.hl_text[point_end:]
        #self.hl_text = self.hl_text.encode('utf-8')

    def write_html(self):
        f = open("out.html", "w+")
        f.write(self.hl_text.encode('utf-8'))
        f.close()



