# -*- coding: utf-8 -*-
from PersonDict import PersonDict

class MyEntity(object):
    entity = None
    entity_type = 1 # 1-crime, 2-police, 3-victim

    TYPE_CRIME = 1
    TYPE_POLICE = 2
    TYPE_VICTIM = 3

    word = ''
    word_norm = ''
    id = None

    def __init__(self, entity):
        self.entity = entity
        self.id = self.entity.attrib['id'].encode('utf-8')

        # attribute = entity.find('attributes')
        self.word = entity.find('original')
        self.word = self.word.text.encode('utf-8')

        self.word_norm = entity.find('name')
        self.word_norm = self.word_norm.text.encode('utf-8')
        # grammar = entity.find('grammar')

        self._checkPolice()
        self._checkVictim()

    def _checkPolice(self):
        #e_word = self.word.encode()
        if 'ПОЛИЦ' in self.word:
            self.entity_type = self.TYPE_POLICE
        else:
            pd = PersonDict()
            if pd.isPolice(self.word_norm) == True:
                self.entity_type = self.TYPE_POLICE

    def _checkVictim(self):
        pd = PersonDict()
        #print(self.word_norm)
        if True == pd.isVictim(self.word_norm):
            self.entity_type = self.TYPE_VICTIM

    def _checkSynonym(self):
        pass

    def _checkRelationship(self):
        pass