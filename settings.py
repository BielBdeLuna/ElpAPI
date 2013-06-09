#!/usr/bin/python
"""
this file is GPLv3

and was written by Biel Bestue

v 2.0
"""

import os, subprocess, telnetlib, urllib, logging
from global_sets import tControl
from tools import camera_get_download, XML_2_dict
from msg import print_CASUAL, print_ERROR, print_DEBUG
import xml.etree.ElementTree as ElTree
import task

def get_string_parameter(self,parameter,destinePath,fileName):
    os.chdir(destinePath)
    subject = "http://"+self.HOST
    command = "/parsedit.php?immediate&" + parameter
    camera_get_download(self, action="get", owner=self, subject=subject, command=command, fileName=fileName)

def get_list_parameters(self,parameters,destinePath,fileName):
    os.chdir(destinePath)
    subject = "http://"+self.HOST
    parmLine="&"
    i = 0
    maxLength = len(parameters)
    for i in range (maxLength):
        parmLine = parmLine + parameters[i] + "&"
        i = i + 1
    print_DEBUG(self,"parmLine is:" + parmLine) #debug
    command = "/parsedit.php?immediate" + parmLine
    camera_get_download(self, action="get", owner=self, subject=subject, command=command, fileName=fileName)

def get_dictionary_parameters(self,parameters,destinePath,fileName):
    os.chdir(destinePath)
    subject = "http://"+self.HOST
    keyList = parameters.keys() # values get ignored and only a key list remains, in order to gather new values
    parmLine="&"
    i = 0
    maxLength = len(keyList)
    for i in range (maxLength):
        parmLine = parmLine + keyList[i] + "&"
        i = i + 1
    print_DEBUG(self,"parmLine is:" + parmLine) #debug
    command = "/parsedit.php?immediate" + parmLine
    camera_get_download(self, action="get", owner=self, subject=subject, command=command, fileName=fileName)
    """    
    url = "http://"+self.HOST+"/parsedit.php?immediate"+parmLine
    filename = str(fileName)+".xml"
    if not fileName:
        try:
            print("downloading nothing!")
            urllib.urlretrieve(url)
        except Exception, e:
            logging.warn("error downloading %s: %s" % (url, e))
    else:
        try:
            print("downloading a file named " + filename + "!")
            urllib.urlretrieve(url, filename=filename)
        except Exception, e:
            logging.warn("error downloading %s: %s" % (url, e))
    """ 

def get_xml_parameters(self,parameters,destinePath,fileName):
    pass #TODO - add the possibility to extract parameters dict from an XML file and get them from the camera

def set_dictionary_parameters(self,parameters):
    subject = "http://"+self.HOST
    command = "/parsedit.php?immediate"
    parmValStringList = ""
    for key in sorted(parameters.keys()):
        parmValStringList = parmValStringList +"&" + key + "=" + parameters[key]
    print_DEBUG(self,"Line sent: " + subject + command + parmValStringList) #debug
    camera_get_download(self, action="set", owner=self, subject=subject, command=command, fileName=None)

def set_xml_parameters(self, XMLparmFile):

    changes = False
    error = False
    currentParmsDic = {}
    sendParmsDic = {}
    maxLengthWan = 0
    maxLengthCam = 0
    subject = "http://"+self.HOST
    command = "/parsedit.php?immediate"
    
    try:
        tree = ElTree.parse(XMLparmFile)
        root = tree.getroot()
    except:
        print_ERROR(self,"Something went wrong while parsing " + XMLparmFile)
        error = True
    else:
        for child in tree.iter():
            for c in child:
                self.SETTINGS_DIC[c.tag] = c.text
                print_DEBUG(self,"implanted parameter '" + c.tag + "' as " + c.text + " in the camera's settings dictionary") #debug
    
    keyListWan = self.SETTINGS_DIC.keys()

    if error is not True:

        get_dictionary_parameters(self,self.SETTINGS_DIC,self.SETTINGS_PATH,"camera_settings")
       
        #FIXME - this only works on the initial ocasion
        global tControl            
        """
        while self.DOWNLOAD_QUEUE.get() is not None:
        
            print("waiting waiting waiting")
            tControl.threadList[0].wait_for_tick()
            print("this shouldn't be printing")
        """
        print("lineal failing") #FIXME erase this debug line
        return #FIXME erase this debug line
        
        try:
            tree = ElTree.parse(os.path.join(DESTPATH,"camera_settings.xml"))
            root = tree.getroot()
        except:
            print_ERROR(self,"Something went wrong while parsing 'camera_settings.xml'")
            error = True
        else:
            for child in tree.iter():
                for c in child:
                    currentParmsDic[c.tag] = c.text

        keyListCam = currentParmsDic.keys()

    if error is not True:

        wanVal = ""
        camVal = ""
        w = 0
        maxLengthWan = len(keyListWan)
        #print_DEBUG(self,"'maxLengthWan' is: " + str(maxLengthWan)) #debug
        maxLengthCam = len(keyListCam)
        #print_DEBUG(self,"'maxLengthCam' is: " + str(maxLengthCam)) #debug
        for w in range(maxLengthWan):
            wanVal = keyListWan[w]
            c = 0
            for c in range(maxLengthCam):
                camVal = keyListCam[c]
                if wanVal is camVal:
                    if self.SETTINGS_DIC[wanVal] is currentParmsDic[camVal]:
                        print_DEBUG(self,wanVal + " is " + self.SETTINGS_DIC[wanVal] + " on both dictionaries")
                        break
                    else:
                        #TODO add a pooliong system, which will allow multi-threading
                        sendParmsDic[wanVal] = self.SETTINGS_DIC[wanVal]
                        changes = True
            c = c + 1
        w = w + 1

    else:
        print_ERROR(self,"The process failed and will end unsuccessfully")
        return

    if changes:
        set_dictionary_parameters(sendParmsDic)
        """
        while ???:
            wait_next_frame
        """
        print_CASUAL(self,"All new values uploaded to the camera")
    else:
        print_CASUAL(self,"No values uploaded to the camera")

    #set_parameters(self.SETTINGS_DIC)
    
    if self.SETTINGS_DIC["AUTOEXP_ON"] is 1:
        self.AUTO_EXP_STATE = False
    else:
        self.AUTO_EXP_STATE = True

    if self.SETTINGS_DIC["WB_EN"] is 1:
        self.AUTO_WB_STATE = False
    else:
        self.AUTO_WB_STATE = True
    
"""
sets up the necessary parameters in the camera's internal settings dictionary, in order to use it, instead of XMLs
"""
def setup_settings_dictionary(self, parameters):
    #TODO the camera's internal dictionary is feed from the wanted XML settings 
    XML_2_dict(os.path.join(self.SETTINGS_PATH,self.SETTINGS_FILE),self.SETTINGS_DIC)
    print_DEBUG(self,"rejoice! the camera's internal settings dictionary has been created!")

"""
implants a settings parameter along it's associated value to the camera's internal settings dictionary
"""
def implant_parmameter_settings_dictionary(self, parm, val):
    for k in sorted(self.SETTINGS_DIC.keys()):
        if k is parm:
            if self.SETTINGS_DIC[parm] is val:
                print_DEBUG(self,parm + " is already in the dictionary and contains the same value: " + val)
                return
    self.SETTINGS_DIC[parm] = val

"""
gathers a settings property from the camera's internal settings dictionary
"""
def gather_settings_dictionary_parameter(self, parm):
    for k in sorted(self.SETTINGS_DIC.keys()):
        if k is parm:
            return self.SETTINGS_DIC[parm]
    print_ERROR(self,"couldn't find '" + parm + "' in the internal settings dictionary!")

if __name__ == '__main_':
    print("\nyou attempted to operate this file directly\nbut his file isn't meant to operate on it's own,\n\nplease before proceeding read first the README file.\n")
#EOF
