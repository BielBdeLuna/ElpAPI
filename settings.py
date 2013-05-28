#!/usr/bin/python
"""
this file is GPLv3

and was written by Biel Bestue

v 2.0
"""

import os, subprocess, telnetlib
from tools import camera_wget_download
from msg import print_CASUAL, print_ERROR, print_DEBUG

def get_string_parameter(self,parameter,destinePath,fileName):
    self.DWN_STATE = True
    os.chdir(destinePath)
    camera_wget_download(self,parameter,fileName)
    self.DWN_STATE = False

def get_list_parameters(self,parameters,destinePath,fileName):
    self.DWN_STATE = True
    os.chdir(destinePath)
    parmLine="&"
    i = 0
    maxLength = len(parameters)
    for i in range (maxLength):
        parmLine = parmLine + parameters[i] + "&"
        i = i + 1
    print_DEBUG(self,"parmLine is:" + parmLine) #debug
    camera_wget_download(self,parmLine,fileName)
    self.DWN_STATE = False

def get_dictionary_parameters(self,parameters,destinePath,fileName):
    self.DWN_STATE = True
    os.chdir(destinePath)
    keyList = parameters.keys() # values get ignored and only a key list remains, in order to gather new values
    parmLine="&"
    i = 0
    maxLength = len(keyList)
    for i in range (maxLength):
        parmLine = parmLine + keyList[i] + "&"
        i = i + 1
    print_DEBUG(self,"parmLine is:" + parmLine) #debug
    camera_wget_download(self,parmLine,fileName)
    self.DWN_STATE = False

def get_xml_parameters(self,parameters,destinePath,fileName):
    pass #TODO - add the possibility to extract parameters dict from an XML file and get them from the camera

def set_dictionary_parameters(self,parameters):
    self.DWN_STATE = True
    parmValStringList = "&"
    for key in sorted(parameters.keys()):
        parmValStringList = parmValStringList + key + "=" + parameters[key] + "&"
    camera_wget_download(self,parmValStringList,None)
    self.DWN_STATE = False

def set_xml_parameters(self,parameters):
    pass #TODO - add the possibility to extract parameters dict from an XML file and set them in the camera
'''
def set_dictionary_telNet_parameters(self, parameters):
    self.DWN_STATE = True
    tn = telnetlib.Telnet(self.HOST)
    for key in sorted(parameters.keys()):
        tn.write(key + "=" + parameters[key] + "\n") #TODO - check if you can set parameters via telNet in the cam
    tn.close()
    self.DWN_STATE = False
'''   
