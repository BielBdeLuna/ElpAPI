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
#                    * v 0.5 *                   #
#                                                #
##################################################
"""

import random
import settings
from msg import print_CASUAL, print_ERROR, print_DEBUG

DEFAULT_HOST = "192.168.1.9"
DEFAULT_PORT = "554"
DEFAULT_STILLS_PORT = "8081"

DicDevicesColours = {}

class core(object):
    
    """
    every camera is an object, this objects autocompletes with default values if non are given
    """
    def __init__ (self, host=None, port=None, stlport=None):
                 
        self.HOST = host if host is not None else DEFAULT_HOST
        self.PORT = port if port is not None else DEFAULT_PORT
        self.STLPORT = stlport if stlport is not None else DEFAULT_STILLS_PORT

        self.USERNANE = "root"
        self.PASSWORD = "pass"
        self.DWN_STATE = False
        self.REC_STATE = False
        self.RDY_STATE = False

        self.MSG_COLOUR = 0 #initiate with white
        self.MSG_NODEBUG = False
        
        #try to assing the correct colour to the camera name:
        
        if len(DicDevicesColours) is 0:
            colourChosed = self.MSG_COLOUR #with only one camera, camera name always stay in white in messages
        elif len(DicDevicesColours) is 8:
            print_CASUAL(self,"STOP TRYING TO CONNECT CAMERAS TO THIS COMPUTER! are you mad?!")
        elif len(DicDevicesColours) > 7:
            colourChosed = random.randrange(0,7,1)
        else:
            breaker = False
            while True:
                colourChosed = random.randrange(0,7,1)
                for k in DicDevicesColours:
                    if colourChosed == DicDeviceColours[k]:
                        breaker = True
                        break
                if breaker:
                    break
        
        DicDevicesColours[self.HOST] = colourChosed
        
        self.MSG_COLOUR = colourChosed

        #colour assigned
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
    def get_parameters(self,parameters,destinePath,fileName):
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
    def set_parameters(self,parameters):
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

#EOF
