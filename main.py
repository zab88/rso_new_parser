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
    doc = MyDocument(document)
    doc.analyseEntities()
    police = doc.getPoliceList()
    crime = doc.getCrimeList()
    victim = doc.getVictimList()

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

out_file.close()

print( os.path.dirname( __file__ ) + '/out/out.txt')
    #json.dump(victim, "out.json")


#     attribute = entity.find('attributes')
#     original = entity.find('original')
#     if attribute is None:
#         continue
#
#     # print(attribute.text)
#     if 'Semantic=Person;' in attribute.text:
#         # print entity.attrib['id']
#         # print(attribute.text)
#         all_persons[entity.attrib['id']] = original.text
#     elif 'Person:' in entity.attrib['type']:
#         all_persons[entity.attrib['id']] = original.text
#
# for p in all_persons:
#     print(p)