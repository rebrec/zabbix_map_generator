#!/usr/bin/python

#

from lxml import etree as ET
from Settings import Settings as S
from Disposer import Disposer

if __name__ == '__main__':
    print ("****************************************")
    print("Marge de Gauche : %s" % S.marginleft)
    print("Marge du Haut : %s" % S.margintop)
    print("Espacement horizontal : %s" % S.spacex)
    print("Espacement vertical : %s" % S.spacey)
    print("Fichier de sortie : %s" % S.outputfile)
    print ("****************************************")
disposer = Disposer()
tree = ET.parse('map.xml')
root = tree.getroot()
submaps = tree.findall('.//selement')
mylist = []
# Build a list of labels (=each icon on the map)
for element in submaps:
    elementname = element.find('label').text
    print(elementname)
    mylist.append(elementname)
# Sort this list
mylist = sorted(mylist)
print('*' * 25)
# For each element of the sorted list, get the xmlnode associated and generate x,y coordinates
for e in mylist:
    if e != "SDIS" :
        found = [
                 element for element in submaps.__iter__() 
                    if element.find('label').text == e
                ]
        res = disposer.getNextPosition()
        x = found[0].find('x')
        y = found[0].find('y')
        x.text = str(res[0])
        y.text = str(res[1])

tree.write(S.outputfile)


