# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from MyDocument import MyDocument
import os
import sys


input_xml_path = sys.argv[1]
#input_xml_path = 'data/result_50.xml'
tree = ET.parse(input_xml_path)
root = tree.getroot()

all_documents = []

out_file = open('out/out.txt', 'w+')
for document in root.iter('document'):
    #deleting unnecessary frames
    for frames in document.findall('frames'):
        for frame in frames.findall('frame'):
            #print(frame.attrib['class'])
            #class_name = frame.attrib['class'].encode('windows-1251')#.encode('utf-8')
            class_name = frame.attrib['class']
            #print(class_name)
            if class_name not in ['crime', 'объект: противозаконная деятельность'.decode('utf-8'), 'события: противозаконная деятельность'.decode('utf-8'),
                                  'объект: конфликты'.decode('utf-8'), 'личное взаимодействие: физическое насилие'.decode('utf-8')]:
                frames.remove(frame)

    doc = MyDocument(document)
    doc.analyseEntities()

    police = doc.getPoliceList()
    crime = doc.getCrimeList()
    victim = doc.getVictimList()
    undefined = doc.getUndefinedList()

    #print('================')
    #print( len( doc.entities) )

    for el in police:
        out_file.write( str(el.entity_type) + '|' + el.id + "\n")
        #print(el.word)
    for el in victim:
        #print(el.word)
        out_file.write( str(el.entity_type) + '|' + el.id + "\n")
    for el in crime:
        #print(el.word)
        out_file.write( str(el.entity_type) + '|' + el.id + "\n")

    for el in undefined:
        #print(el.word)
        out_file.write( str(el.entity_type) + '|' + el.id + "\n")

out_file.close()

print( os.path.dirname( __file__ ) + '/out/out.txt')
