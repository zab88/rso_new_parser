# -*- coding: utf-8 -*-
from neo4jrestclient.client import GraphDatabase
import xml.etree.ElementTree as ET

#init
gdb = GraphDatabase("http://localhost:7474/db/data/")
#MATCH (a) OPTIONAL MATCH (a)-[r1]-() DELETE a, r1


input_xml_path = 'data/result_3.xml'
tree = ET.parse(input_xml_path)
root = tree.getroot()

all_documents = []

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

            #try to insert frame in Neo4J
            else:
                o1, o2, ev = None, None, None
                for slot in frame.findall('slot'):
                    if slot.attrib['name'] in ['person_object', 'Object1', 'Obj1', 'object1']: #crime
                        o1 = slot.text
                    if slot.attrib['name'] in ['person_subject', 'Object2']: #victim
                        o2 = slot.text
                    if slot.attrib['name'] in ['Event', 'event']:
                        ev = slot.text
                    # print(slot.attrib['name'])
                    # print(slot.text)
                if o1 is not None and o2 is not None:
                    obj1 = gdb.node(name=o1)
                    obj2 = gdb.node(name=o2)
                    # obj1.labels.add(["Person", "Crime"])
                    # obj2.labels.add(["Person", "Victim"])
                    obj1.labels.add(["Crime"])
                    obj2.labels.add(["Victim"])

                    if ev is not None:
                        obj1.Crime(obj2, event=ev)
                    else:
                        obj1.Crime(obj2)

    #now let's insert all features of document