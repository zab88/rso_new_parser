# -*- coding: utf-8 -*-

class PersonDict(object):

    crime_synonym = []
    police_synonym = []
    victim_synonym = []

    def getCrimeSynonyms(self):
        return self.crime_synonym

    def getPoliceSynonyms(self):
        return self.police_synonym

    def getVictimSynonyms(self):
        return self.victim_synonym