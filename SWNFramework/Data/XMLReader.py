'''
Created on 30/giu/2011

@author: massi
'''

from xml.dom.minidom import *
from PySide.QtCore import QDir
import string
import os

def getText(baseNode):
    rc = []
    for node in baseNode.childNodes:
        if node.nodeType == node.TEXT_NODE or node.nodeType == node.CDATA_SECTION_NODE :
            rc.append(node.data)
    return ''.join(rc)

def __parseTable (element):
    res = []
    for tag in element.getElementsByTagName("entry"):
        t = {
             'min' : int(tag.attributes['min'].value),
             'max' : int(tag.attributes['max'].value),
             'label' : tag.attributes['label'].value
             }
        res.append(t)
    return res
    
def __parseTable1 (element):
    res = []
    for tag in element.getElementsByTagName("entry"):
        t = {
             'min' : int(tag.attributes['min'].value),
             'max' : int(tag.attributes['max'].value),
             'minval' : int(tag.attributes['minval'].value),
             'maxval' : int(tag.attributes['maxval'].value),
             'label' : tag.attributes['label'].value
             }
        res.append(t)
    return res

def __parseTags (dom):
    res = {}
    for tag in dom.getElementsByTagName("Tag"):
        a = { 
             'name': string.strip( getText(tag.getElementsByTagName("Name")[0])),
             'description': string.strip( getText(tag.getElementsByTagName("Description")[0])),
             'enemies': string.strip( getText(tag.getElementsByTagName("Enemies")[0])),
             'friends': string.strip( getText(tag.getElementsByTagName("Friends")[0])),
             'things': string.strip( getText(tag.getElementsByTagName("Things")[0])),
             'places': string.strip( getText(tag.getElementsByTagName("Places")[0])),
             'complications': string.strip( getText(tag.getElementsByTagName("Complications")[0]))
             }
        res [a['name']] = a
    return res

def ReadTagsFromConfiguration():
    try:
        map = {}
        dom_file = os.path.join(QDir.currentPath(),"Data","swn_tag_data.xml")
        print "fetching data from ", dom_file
        dom = parse(dom_file)
        map["Tags"] = __parseTags(dom)
        map["Atmosphere"] = __parseTable(dom.getElementsByTagName("Atmosphere")[0])        
        map["Biosphere"] = __parseTable(dom.getElementsByTagName("Biosphere")[0])
        map["Tech"] = __parseTable(dom.getElementsByTagName("Tech")[0])
        map["Temperature"] = __parseTable(dom.getElementsByTagName("Temperature")[0])
        map["Population"] = __parseTable1(dom.getElementsByTagName("Population")[0])
        return map
    except Exception as inst:
        print "Some error occurred: %s", inst
        return None


if __name__ == '__main__':
    pass
