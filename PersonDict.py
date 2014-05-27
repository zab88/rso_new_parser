# -*- coding: utf-8 -*-

class PersonDict(object):

    crime_synonym = []
    police_synonym = ['сотрудник']
    victim_synonym = ['ПОТЕРПЕВШИЙ', "ПОТЕРПЕВШАЯ", "ПОТЕРПЕВШИЕ"]

    def isCrime(self, word):
        for w in self.crime_synonym:
            if w == word:
                return True
        return False

    def isPolice(self, word):
        for w in self.police_synonym:
            if w == word:
                return True
        return False

    def isVictim(self, word):
        for w in self.victim_synonym:
            if w == word:
                return True
        return False

    def getCrimeSynonyms(self):
        return self.crime_synonym

    def getPoliceSynonyms(self):
        return self.police_synonym

    def getVictimSynonyms(self):
        return self.victim_synonym