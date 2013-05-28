#!/usr/bin/python

"""
##################################################
#                                                #
#                       *                        #
#                                                #
#      * welcome to the Elphel python API *      #
#                                                #
#           * This whole API is GPLv3 *          #
#                                                #
#             * Biel Bestue de Luna *            #
#                                                #
#                    * v 0.6 *                   #
#                                                #
##################################################
"""

import random, os
import xml.etree.ElementTree as ElTree
import settings
from msg import print_CASUAL, print_ERROR, print_DEBUG

DEFAULT_HOST = "192.168.1.9"
DEFAULT_PORT = "554"
DEFAULT_STILLS_PORT = "8081"
DEFAULT_PATH = os.path.expanduser("~/")+"elphel" #TODO - make it so all OS can get the correct path
DEFAULT_PARM_FILE = "wanted_settings.xml"

DicDevicesColours = {}

class core(object):
    
    """
    every camera is an object, this objects autocompletes with default values if non are given
    """
    def __init__ (self, host=None, port=None, stlport=None, path=None, parmFile=None):
                 
        self.HOST = host if host is not None else DEFAULT_HOST
        self.PORT = port if port is not None else DEFAULT_PORT
        self.STLPORT = stlport if stlport is not None else DEFAULT_STILLS_PORT
        self.PATH = path if path is not None else DEFAULT_PATH
        self.PARM_FILE = parmFile if parmFile is not None else DEFAULT_PARM_FILE

        

        self.USERNAME = "root"
        self.PASSWORD = "pass"
        self.DWN_STATE = False
        self.REC_STATE = False
        self.RDY_STATE = False
        self.AUTO_EXP_STATE = True #the dafault beheviour
        self.AUTO_WB_STATE = True #the dafault beheviour
        self.AUTO_CONFG = True

        self.MSG_DEVICE_COLOUR = 0 #initiate with white
        self.MSG_NODEBUG = True
        
        self.DIC_SETTINGS = {}
        
        #try to assing the correct colour to the camera name:
        print_CASUAL(self, "DicDevicesColours is: " + str(DicDevicesColours))
        if len(DicDevicesColours) is 0:
            colourChosed = self.MSG_DEVICE_COLOUR #with only one camera, camera name always stay in white in messages
        elif len(DicDevicesColours) is 8:
            print_CASUAL(self,"STOP TRYING TO CONNECT CAMERAS TO THIS COMPUTER! are you mad?!")
        #elif len(DicDevicesColours) > 7:
        else:
            colourChosed = random.randrange(0,7,1)
        """else:
            breaker = False
            while True:
                colourChosed = random.randrange(0,7,1)
                for k in DicDevicesColours:
                    if colourChosed == DicDevicesColours[k]:
                        breaker = True
                        break
                if breaker:
                    break
        """
        print_CASUAL(self, "DicDevicesColours is: " + str(DicDevicesColours))
        if DicDevicesColours[self.HOST] is colourChosed:
            pass
        else:
            DicDevicesColours[self.HOST] = colourChosed
        self.MSG_DEVICE_COLOUR = colourChosed
        #colour assigned

        #settings.set_internal_dictionary(self,os.path.join(self.PATH, self.PARM_FILE))

        #self.set_default_settings("/home/biel/elphel/wanted_settings.xml")
        #self.set_default_settings(os.path.join(self.PATH, self.PARM_FILE))
        

    """
    object destroyer, in case of ending the ussage of a camera, currently it doesn't do anything
    """
    def __del__ (self):
        #clear meomory from somewhere if needed
        pass

    """
    gets parameters from the camera, it accepts a dictionary, a list, or a single string parameter
    in case of a dictionary with a format of: {parameter:value} form factor, the algorithm discard the "values"
    and only calls de camera asking for "parameters".
    """
    def get_parameters(self, parameters, destinePath, fileName):
        if not fileName:
            print_ERROR(self,"You must specify a filename!")
            return

        if type(parameters)==type(dict()):
            settings.get_dictionary_parameters(self,parameters,destinePath,fileName)
        elif type(parameters)==type(list()):
            settings.get_list_parameters(self,parameters,destinePath,fileName)
        elif type(parameters)==type(str()):
            settings.get_string_parameter(self,parameter,destinePath,fileName)
        else:
            print_ERROR(self,"I can't read this parameter, please be more specific!")
            return

    """
    sets parameters to the camera, it only accepts a dict with a format of: {parameter:value} form factor.
    """
    def set_parameters(self, parameters):
        if type(parameters)==type(dict()):
            settings.set_dictionary_parameters(self,parameters)
        elif type(parameters)==type(list()):
            print_ERROR(self,"I need a dictionary of parameters along with it's corresponding values!")
            return
        elif type(parameters)==type(str()):
            print_ERROR(self,"I need a dictionary of parameters along with it's corresponding values!")
            return
        else:
            print_ERROR(self,"I can't read this parameter, please be more specific!")

    """
    gathers all camera settings from the camera's settings dictorinary
    """
    def gather_camera_settings(self):
        return self.DIC_SETTINGS.keys()

    """
    gathers the value of an especific parameter from the camera's settings dictionary
    """
    def gather_one_camera_setting(self, parm):
        #TODO check is this parm exist in the settings dictionary
        return self.DIC_SETTINGS[parm]

    """
    implants a parameter an it's associated value to this camera's settings dictionary
    """
    def implant_camera_setting(self, parm, val):
        self.DIC_SETTINGS[parm] = val

    """
    toggles AUTOEXP an AUTOWB
    """
    def toggleAuto(self):

        #TODO implement some oprotection in case self.DIC_SETTINGS is empty!
        if AUTO_EXP_STATE == True:
            self.DIC_SETTINGS["AUTOEXP_ON"] = 0
            self.AUTO_EXP_STATE = False
        else:
            self.DIC_SETTINGS["AUTOEXP_ON"] = 1
            self.AUTO_EXP_STATE = True

        if self.AUTO_WB_STATE == True:
            self.DIC_SETTINGS["WB_EN"] = 0
            self.AUTO_WB_STATE = False
        else:
            self.DIC_SETTINGS["WB_EN"] = 1
            self.AUTO_WB_STATE = True

    """
    set's up the camera according to a given XML parameter file
    """
    def set_default_settings(self, XMLparmFile):

        import xml.etree.ElementTree as ElTree

        changes = False
        error = False
        currentParmsDic = {}
        sendParmsDic = {}
        maxLengthWan = 0
        maxLengthCam = 0

        self.AUTO_CONFG = True

        

        try:
            print_DEBUG(self,"obre el 'try' amb XMLparmFile:" + XMLparmFile) #debug
            tree = ElTree.parse(XMLparmFile)
            print_DEBUG(self,"crea el 'tree'") #debug
            root = tree.getroot()
            rint_DEBUG(self,"pren l'arrel") #debug
            print_DEBUG(self,"'tree' is:" + str(tree)) #debug
            print_DEBUG(self,"'root' is" + str(root)) #debug
        except:
            print_ERROR(self,"Something went wrong while parsing " + XMLparmFile)
            error = True
        else:
            for child in tree.iter():
                for c in child:
                    self.DIC_SETTINGS[c.tag] = c.text

        keyListWan = self.DIC_SETTINGS.keys()

        if error is not True:

            self.get_parameters(self.DIC_SETTINGS,self.PATH,"camera_settings")

            try:
                tree = ElTree.parse(os.path.join(DESTPATH,"camera_settings.xml"))
                root = tree.getroot()
                print_DEBUG(self,"'tree' is:" + str(tree)) #debug
                print_DEBUG(self,"'root' is" + str(root)) #debug
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
            print_DEBUG(self,"'maxLengthWan' is: " + str(maxLengthWan)) #debug
            maxLengthCam = len(keyListCam)
            print_DEBUG(self,"'maxLengthCam' is: " + str(maxLengthCam)) #debug
            for w in range(maxLengthWan):
                wanVal = keyListWan[w]
                c = 0
                for c in range(maxLengthCam):
                    camVal = keyListCam[c]
                    if (wanVal == camVal):
                        if (self.DIC_SETTINGS[wanVal] == currentParmsDic[camVal]):
                            print_DEBUG(self,wanVal + " is " + self.DIC_SETTINGS[wanVal] + " on both dictionaries")
                            break
                        else:
                            #TODO add a pooliong system, which will allow multi-threading
                            sendParmsDic[wanVal] = self.DIC_SETTINGS[wanVal]
                            changes = True
                    c = c + 1
                w = w + 1

        else:
            print_ERROR(self,"The process failed and will end unsuccessfully")
            return

        if changes:
            set_parameters(sendParmsDic)
            print_CASUAL(self,"All new values uploaded to the camera")
        else:
            print_CASUAL(self,"No values uploaded to the camera")

        #set_parameters(self.DIC_SETTINGS)
    
        if self.DIC_SETTINGS["AUTOEXP_ON"] == 1:
            self.AUTO_EXP_STATE = False
        else:
            self.AUTO_EXP_STATE = True

        if self.DIC_SETTINGS["WB_EN"] == 1:
            self.AUTO_WB_STATE = False
        else:
            self.AUTO_WB_STATE = True

        self.AUTO_CONFG = False
            

#EOF
