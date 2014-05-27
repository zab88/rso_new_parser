import xml.etree.ElementTree as ET
from MyDocument import MyDocument


tree = ET.parse('data/result_50.xml')
root = tree.getroot()

all_documents = []

for document in root.iter('document'):
    doc = MyDocument(document)
    doc.analyseEntities()
    police = doc.getPoliceList()
    crime = doc.getCrimeList()
    victim = doc.getVictimList()

    print('================')
    print( len( doc.entities) )
    for el in police:
        print(el.word)


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