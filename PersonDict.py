# -*- coding: utf-8 -*-

class PersonDict(object):

    crime_synonym = ['ГРАБИТЕЛЬ', "ГРАБИТЕЛИ", "ПОДОЗРЕВАЕМЫЙ", "МОШЕННИК", "НАРКОТОРГОВЕЦ", "ОБВИНЯЕМЫЙ", "ПРЕСТУПНИК",
                     "ПРЕСТУПНИК", "ОСУЖДЕННЫЙ", "ОРГАНИЗОВАННАЯ ГРУППА", "ОБВИНЯЕМЫЙ", "ЧЛЕН ГРУППЫ", "ГРУППА",
                     "НАРКОТОРГОВЕЦ", "ЗАДЕРЖАННЫЙ", "ВОЗМУТИТЕЛЬ СПОКОЙСТВИЯ", "ФИГУРАНТ", "БАНДИТ", "УБИЙЦА",
                     "ВИНОВНЫЙ", "ГЛАВАРЬ ГРУППИРОВКИ КИЛЛЕРОВ", "КИЛЛЕР", "КРИМИНАЛЬНЫЙ АВТОРИТЕТ", "ПРИСПЕШНИК",
                     "СООБЩНИК", "БАНДА", "ЧЛЕН ГРУППИРОВКИ", "КИЛЛЕР ЗАВЬЯЛОВА ДМИТРИЯ", "ПРЕДПОЛАГАЕМЫЙ КИЛЛЕР ГРУППИРОВКИ",
                     "ГЛАВАРЬ ГРУППИРОВКИ КИЛЛЕРА", "ХУЛИГАН"]
    police_synonym = ['СОТРУДНИК', 'СТРАЖА', "СОТРУДНИК ПОЛИЦИИ", "СЫЩИК", "СЛЕДОВАТЕЛЬ", "ИСПАНСКИЙ СЫЩИК",
                      "СОТРУДНИК ИСПРАВИТЕЛЬНОЙ КОЛОНИИ", "СУД", "ПОЛИЦЕЙСКИЙ", "СЛЕДСТВЕННО-ОПЕРАТИВНАЯ ГРУППА",
                      "КИНОЛОГ", "ОПЕРАТИВНИК УГОЛОВНОГО РОЗЫСКА", "СОТРУДНИК ГИБДД", "НАРЯД ПОЛИЦИИ",
                      "ЗАМНАЧАЛЬНИКА КРИМИНАЛЬНОЙ ПОЛИЦИИ СИГУЛДА", "МЕСТНЫЙ РАЗБОЙНИК", "ОБНАГЛЕВШАЯ ШПАНА", ]
    victim_synonym = ['ПОТЕРПЕВШИЙ', "ПОТЕРПЕВШАЯ", "ПОТЕРПЕВШИЕ", "ЖЕРТВА"]

    police_relations = ['ЗАДЕРЖАЛИ', 'ПРИБЫВШИЕ', 'РАСКРЫТЫ', 'ЗАДЕРЖАЛ', 'ЭКСТРЕННО', 'ПОЛИЦИИ' 'СОТРУДНИКИ', 'ЛИКВИДИРОВАЛИ']
    crime_relations = ['УБИТЬ', "УКРАСТЬ"]
    victim_relations = []

    def isCrime(self, word, relations = []):
        #print(word)
        for w in self.crime_synonym:
            if w == word:
                #print word + " CRIME!"
                return True
        for relation in relations:
            for crime_relation in self.crime_relations:
                if relation == crime_relation:
                    #print word + " CRIME!"
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