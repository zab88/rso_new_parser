# -*- coding: utf-8 -*-
from MyEntity import MyEntity
import itertools

class MyDocument(object):

    document = None
    entities = []
    all_slots = []

    all_persons = {}

    def __init__(self, document):
        self.setDocument(document)
        self.entities = []
        self.all_slots = []
        self.all_persons = {}

    def setDocument(self, document):
        self.document = document

    def analyseEntities(self):
        all_entities = self.document.iter('entity')
        self.all_slots = self.document.iter('slot')

        for entity in all_entities:
            attribute = entity.find('attributes')
            original = entity.find('original')
            grammar = entity.find('grammar')
            # if attribute is None:
            #     attribute = object
            #     attribute.text = ''

            # print(attribute.text)
            if (attribute is not None and 'Semantic=Person;' in attribute.text) \
                or ('Person:' in entity.attrib['type']) \
                or grammar.attrib['SpeechPart'] == 'Pronoun':

                new_entity = MyEntity(entity)
                slot_name = self.findSlotName(new_entity.word_offset, new_entity.word_length)
                if slot_name is not None:
                    new_entity.setSlotName(slot_name)
                    print(slot_name)

                self.entities.append( new_entity )
                self.all_persons[entity.attrib['id']] = original.text



        #print(len(self.entities))
        #print(self.all_persons)
        # !!!
        # for p in self.all_persons:
        #     print(p)

        #ok we load all entities, let's analyse them

    def findSlotName(self, offset, length):
        if offset == '': return None
        # print(offset, length)

        all_slots_backup, self.all_slots = itertools.tee(self.all_slots)
        for slot in all_slots_backup:
            # print(offset, length, slot.attrib['offset'], slot.attrib['length'])

            if slot.attrib['offset'] == offset and slot.attrib['length'] == length:
                return slot.attrib['name']
        return None

    def getPoliceList(self):
        police_list = [e for e in self.entities if e.entity_type==e.TYPE_POLICE]
        return police_list

    def getCrimeList(self):
        police_list = [e for e in self.entities if e.entity_type==e.TYPE_CRIME]
        return police_list

    def getVictimList(self):
        police_list = [e for e in self.entities if e.entity_type==e.TYPE_VICTIM]
        return police_list

    def getUndefinedList(self):
        undefined_list = [e for e in self.entities if e.entity_type==e.TYPE_UNDEFINED]
        return undefined_list