# -*- coding: utf-8 -*-
from PersonDict import PersonDict

class MyEntity(object):
    entity = None
    entity_type = 0 # 1-crime, 2-police, 3-victim, 0-undefined
    slot_name = None

    TYPE_UNDEFINED = 0
    TYPE_CRIME = 1
    TYPE_POLICE = 2
    TYPE_VICTIM = 3

    word = ''
    word_norm = ''
    word_offset = ''
    word_length = ''
    id = None
    relation_words = []

    crime_slot_names = ['person_object', 'Object1', 'Obj1', 'object1']
    victim_slot_names = ['person_subject']
    police_slot_names = []

    def __init__(self, entity):
        self.entity = entity
        self.entity_type = self.TYPE_UNDEFINED
        self.id = self.entity.attrib['id'].encode('utf-8')

        # attribute = entity.find('attributes')
        self.word = entity.find('original')
        self.word = self.word.text.encode('utf-8')

        word_norm = entity.find('name')
        self.word_norm = word_norm.text.encode('utf-8')
        #set offset and length
        if word_norm.attrib.get('offset') is not None:
            self.word_offset = word_norm.attrib['offset']
            self.word_length = word_norm.attrib['length']
            #print(self.word_offset)
        # grammar = entity.find('grammar')

        relations_xml = entity.findall('relationship')
        for r_xml in relations_xml:
            r_word = r_xml.attrib['entity']
            # print(r_word)
            self.relation_words.append(r_word.encode('utf-8'))

        self._checkPolice()
        self._checkVictim()
        self._checkCrime()

    def setSlotName(self, slot_name):
        #print(slot_name)
        self.slot_name = slot_name

    def _checkPolice(self):
        #e_word = self.word.encode()
        if 'ПОЛИЦ' in self.word:
            self.entity_type = self.TYPE_POLICE
        else:
            pd = PersonDict()
            # if pd.isPolice(self.word_norm, self.relation_words) == True:
            if pd.isPolice(self.word_norm) == True:
                self.entity_type = self.TYPE_POLICE

    def _checkVictim(self):
        pd = PersonDict()
        #print(self.word_norm)
        if True == pd.isVictim(self.word_norm, self.relation_words):
            self.entity_type = self.TYPE_VICTIM

    def _checkCrime(self):
        pd = PersonDict()
        if True == pd.isCrime(self.word_norm, self.relation_words):
            self.entity_type = self.TYPE_CRIME

    def _checkSlotName(self):
        if self.slot_name is None: return

        if self.slot_name in self.crime_slot_names:
            self.setEntityType(self.TYPE_CRIME)
        elif self.slot_name in self.victim_slot_names:
            self.setEntityType(self.TYPE_VICTIM)
        elif self.slot_name in self.police_slot_names:
            self.setEntityType(self.TYPE_POLICE)

    def _checkSynonym(self):
        pass

    def _checkRelationship(self):
        pass

    def setEntityType(self, type):
        self.entity_type = type