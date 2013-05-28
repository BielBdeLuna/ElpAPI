#!/usr/bin/python

"""
this file is GPLv3

and was written by Biel Bestue with help from Carlos Padial with the XML parsing

v 1.0
"""
import xml.etree.ElementTree as ElTree
from xml.dom.minidom import parseString
from msg import print_CASUAL, print_ERROR, print_DEBUG

def XML_2_string_data(xml_file):
    try:
        file = open(xml_file)
        data = file.read()
        file.close()
        return data
    except IOError:
        print_ERROR(self,"No XML file found!")
        return -1

def XML_2_str_parm(xml_file, parameter):
    xml_data = get_XML_data(xml_file)
    if xml_data == -1:
        print_ERROR(self,"Couldn't get any parameter because coudln't found the file")
        return -1
    dom = parseString(xml_data)
    value = dom.getElementsByTagName(parameter)[0].childNodes[0]
    parameter = int(value.nodeValue)
    return parameter
    #TODO return -2 if the parameter couldn't be found

def XML_2_dict(file, dic):
    tree = ElTree.parse(file)
    root = tree.getroot()

    for child in tree.iter():
        #print("child.tag is: " + child.tag + " and child.text is: " + child.text)
        for c in child:
            print_DEBUG(self,"c.tag is: " + c.tag + " and c.text is: " + c.text)
            dic[c.tag] = c.text
            #c.tag  --> parm
            #c.text --> value

def XML_2_list(file, lst):
    tree = ElTree.parse(file)
    root = tree.getroot()
    i = 0
    for child in tree.iter():
        #print("child.tag is: " + child.tag + " and child.text is: " + child.text)
        for c in child:
            lst[i] = c.tag
            i = i + 1
