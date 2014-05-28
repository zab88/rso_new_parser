# -*- coding: utf-8 -*-

class PersonDict(object):

    crime_synonym = ['ГРАБИТЕЛЬ', "ГРАБИТЕЛИ", "ПОДОЗРЕВАЕМЫЙ", "МОШЕННИК", "НАРКОТОРГОВЕЦ", "ОБВИНЯЕМЫЙ", "ПРЕСТУПНИК"]
    police_synonym = ['СОТРУДНИК']
    victim_synonym = ['ПОТЕРПЕВШИЙ', "ПОТЕРПЕВШАЯ", "ПОТЕРПЕВШИЕ", "ЖЕРТВА"]

    police_relations = ['ЗАДЕРЖАЛИ', 'ПРИБЫВШИЕ', 'РАСКРЫТЫ', 'ЗАДЕРЖАЛ', 'ЭКСТРЕННО', 'ПОЛИЦИИ' 'СОТРУДНИКИ', 'ЛИКВИДИРОВАЛИ']
    crime_relations = ['УБИТЬ', "УКРАСТЬ"]
    victim_relations = []

    def isCrime(self, word, relations = []):
        for w in self.crime_synonym:
            if w == word:
                return True
        for relation in relations:
            for crime_relation in self.crime_relations:
                if relation == crime_relation:
                    return True
        return False

    def isPolice(self, word, relations = []):
        for w in self.police_synonym:
            if w == word:
                return True
        for relation in relations:
            for police_relation in self.police_relations:
                if relation == police_relation:
                    return True
        return False

    def isVictim(self, word, relations = []):
        for w in self.victim_synonym:
            if w == word:
                return True
        for relation in relations:
            for victim_relation in self.victim_relations:
                if relation == victim_relation:
                    return True
        return False


    def getCrimeSynonyms(self):
        return self.crime_synonym

    def getPoliceSynonyms(self):
        return self.police_synonym

    def getVictimSynonyms(self):
        return self.victim_synonym