# -*- coding: utf-8 -*-
from PersonDict import PersonDict

class MyEntity(object):
    entity = None
    entity_type = 1 # 1-crime, 2-police, 3-victim

    TYPE_CRIME = 1
    TYPE_POLICE = 2
    TYPE_VICTIM = 3

    word = ''

    def __init__(self, entity):
        self.entity = entity

        # attribute = entity.find('attributes')
        self.word = entity.find('original')
        self.word = self.word.text.encode('utf-8')
        # grammar = entity.find('grammar')

        self._checkPolice()

    def _checkPolice(self):
        #e_word = self.word.encode()
        if 'ПОЛИЦ' in self.word:
            self.entity_type = self.TYPE_POLICE

    def _checkSynonym(self):
        pass

    def _checkRelationship(self):
        pass