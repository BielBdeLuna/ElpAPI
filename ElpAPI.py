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
#               * Biel B. de Luna *              #
#                                                #
#                    * v 0.7 *                   #
#                                                #
##################################################
"""

import random, os
import threading
from Queue import Queue

from Devices import Slave
import get, settings, telnet, recording
from msg import print_CASUAL, print_ERROR, print_DEBUG

DEFAULT_HOST = "192.168.0.9"
DEFAULT_NAME = "Elphel camera"
DEFAULT_OWNER = "ElpAPI GUI"
DEFAULT_USERNAME = "root"
DEFAULT_PASSWORD = "pass"
DEFAULT_PORT = "554"
DEFAULT_STILLS_PORT = "8081"
DEFAULT_SETTINGS_FILE = "wanted_settings.xml"
DEFAULT_SETTINGS_PATH = os.path.expanduser("~/")+"elphel" #TODO - make it so all OS can get the correct path
DEFAULT_ROOT_PATH = os.path.expanduser("~/")+"elphel" #TODO - make it so all OS can get the correct path

#DicDevicesColours = {}

class elphelCam(Slave):


    """
    every camera is an object, this objects autocompletes with default values if non are given
    """
    def __init__ (self, host=None, port=None, stillport=None, root_path=None, settingsFile=None, name=None, owner=None, username=None, password=None):
       
        self.HOST = host if host is not None else DEFAULT_HOST
        self.NAME = name if name is not None else DEFAULT_NAME
        self.OWNER = owner if owner is not None else DEFAULT_OWNER
        self.PORT = port if port is not None else DEFAULT_PORT
        self.STILLPORT = stillport if stillport is not None else DEFAULT_STILLS_PORT

        self.USERNAME = username if username is not None else DEFAULT_USERNAME
        self.PASSWORD = password if password is not None else DEFAULT_PASSWORD

        #super(Slave, self).__init__(name=self.NAME, host=self.HOST, port=self.PORT, owner=self.OWNER)
        super(Slave, self).__init__(name=self.NAME, host=self.HOST, port=self.PORT)

        self.DWN_STATE = False
        self.REC_STATE = False
        self.RDY_STATE = False
        #self.MSG_DEVICE_COLOUR = 0 #initiate with white
        self.MSG_DEBUG_LEVEL = 0 #change for -1 if you want to avoid any debug messages

        self.ROOT_PATH = root_path if root_path is not None else DEFAULT_ROOT_PATH
        self.SETTINGS_FILE = settingsFile if settingsFile is not None else DEFAULT_SETTINGS_FILE
        self.SETTINGS_PATH = DEFAULT_SETTINGS_PATH
        self.SETTINGS_DIC = {}
        self.ERROR_LOG = ""
        self.AUTO_CONFIG = True
        self.AUTO_EXP_STATE = True #the dafault beheviour
        self.AUTO_WB_STATE = True #the dafault beheviour

        """
        #try to assing the correct colour to the camera name:
        print_CASUAL(self, "DicDevicesColours is: " + str(DicDevicesColours))
        if len(DicDevicesColours) is 0:
            #with only one camera, camera name always stay in white in messages
            colourChosed = self.MSG_DEVICE_COLOUR 
        elif len(DicDevicesColours) is 8:
            print_CASUAL(self,"STOP TRYING TO CONNECT CAMERAS TO THIS COMPUTER! are you mad?!")
            colourChosed = random.randrange(0,7,1)
        else:
            colourChosed = random.randrange(0,7,1)
            
        else:
            breaker = False
            while True:
                colourChosed = random.randrange(0,7,1)
                for k in DicDevicesColours:
                    if colourChosed == DicDevicesColours[k]:
                        breaker = True
                        break
                if breaker:
                    break
        
        print_CASUAL(self, "DicDevicesColours is: " + str(DicDevicesColours))
        if DicDevicesColours[self.HOST] is not colourChosed:
            DicDevicesColours[self.HOST] = colourChosed
        else:
            pass
        self.MSG_DEVICE_COLOUR = colourChosed
        #colour assigned
        """

        self.DOWNLOAD_QUEUE = Queue()
        self.DOWNLOAD_LOG = ""
        self.TNET_COMMANDS_QUEUE = Queue()
        self.TNET_OUTPUT_LOG = ""
        self.THREADS = []
    
        #self.THREADS.append(telnet.TnetCom(self,self.TNET_COMMANDS_QUEUE))
        #self.THREADS[-1].start()
        #TODO indentify this last thread!

        self.THREADS.append(get.Downloader(self.DOWNLOAD_QUEUE, self))
        self.THREADS[-1].setDaemon(True)
        self.THREADS[-1].start()
        self.THREADS[-1].setName("get")

        #autosetup the camera
        self.set_custom_XML_settings(os.path.join(self.SETTINGS_PATH, self.SETTINGS_FILE))

    def run(self):
        super(self, self).run()
        pass

        
    """
    object destroyer, in case of ending the ussage of a camera, currently it doesn't do anything
    """
    def __del__ (self):
        #clear meomory from somewhere if needed
        #TODO add a method to kill all the threads when killing this object
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
    sets up camogm for recording in-camera
    """
    def camogm_setup(self):
        pass

    """
    starts recording
    """
    def camogm_rec_start(self):
        pass

    """
    stops recording
    """
    def camogm_rec_stop(self):
        pass

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
    implants a parameter along it's associated value to the camera's settings dictionary
    """
    def implant_camera_setting(self, parm, val):
        self.DIC_SETTINGS[parm] = val
        print_DEBUG(self,"parm '" + parm + "' implanted as '" + val + "' in the camera's settings dictionary") #debug

    """
    set's up the camera according to a given XML parameter file
    """
    def set_custom_XML_settings(self, XMLparmFile):
        print_CASUAL(self, "setting the custom XML settings file '" + XMLparmFile + "' in camera")        
        settings.set_xml_parameters(self, XMLparmFile)

    def get_error_log(self):
        return self.ERROR_LOG
    def get_telnet_log(self):
        return self.TNET_OUTPUT_LOG
    def get_get_log(self):
        return self.DOWNLOAD_LOG

            
if __name__ == '__main_':
    print("\nyou attempted to operate this file directly\nbut his file isn't meant to operate on it's own,\n\nplease before proceeding read first the README file.\n")
#EOF
