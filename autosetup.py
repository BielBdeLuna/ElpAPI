#!/usr/bin/python

"""
this file is GPLv3

and was written by Biel Bestue with help from Carlos Padial with the XML parsing

v 2.0
"""

import os
import xml.etree.ElementTree as ElTree
import ElpAPI
from msg import print_CASUAL, print_ERROR, print_DEBUG
#import autoKillSwitch, autoResolution, autoColour #TODO not yet, not yet

HOST = "elphel"
DESTPATH = os.path.expanduser("~/")+"elphel" #TODO - make it so all OS can get the correct path

def setupCamera():
    changes = False
    error = False
    wantedParmsDic = {}
    cameraParmsDic = {}
    sendParmsDic = {}
    maxLengthWan = 0
    maxLengthCam = 0

    #autoKillSwitch.go() #TODO all this stuff is reserverd for the future
    #autoResolution.go() #TODO the same above
    #autoColourt.go() #TODO add a colour selection system, the same above
    try:
        camera
    except NameError:
        camera = ElpAPI.core(HOST) #creates camera only if it doesn't exists before
    else:
        print_CASUAL(camera,"'camera' object already created")


    try:
        tree = ElTree.parse(os.path.join(DESTPATH,"wanted_settings.xml"))
        root = tree.getroot()
    except:
        print_ERROR(camera,"Something went wrong while parsing 'wanted_settings.xml'")
        error = True
    else:
        for child in tree.iter():
            for c in child:
                wantedParmsDic[c.tag] = c.text
        #created a dictionary from known sources.
        keyListWan = wantedParmsDic.keys()


    camera.get_parameters(wantedParmsDic,DESTPATH,"camera_settings") 
    #download the camera settings using the dictionary as a reference.
    try:
        tree = ElTree.parse(os.path.join(DESTPATH,"camera_settings.xml"))
        root = tree.getroot()
        print_DEBUG(camera,"'tree' is:" + str(tree)) #debug
        print_DEBUG(camera,"'root' is" + str(root)) #debug
    except:
        print_ERROR(camera,"Something went wrong while parsing 'camera_settings.xml'")
        error = True
    else:
        for child in tree.iter():
            for c in child:
                cameraParmsDic[c.tag] = c.text
        #created a new dictionary with the settings the camera is using.
        keyListCam = cameraParmsDic.keys()


    if error is not True: 
        
        wanVal = ""
        camVal = ""
        w = 0
        maxLengthWan = len(keyListWan)
        print_DEBUG(camera,"'maxLengthWan' is: " + str(maxLengthWan)) #debug
        maxLengthCam = len(keyListCam)
        print_DEBUG(camera,"'maxLengthCam' is: " + str(maxLengthCam)) #debug
        for w in range(maxLengthWan):
            wanVal = keyListWan[w]
            c = 0
            for c in range(maxLengthCam):
                camVal = keyListCam[c]
                if (wanVal == camVal):
                    if (wantedParmsDic[wanVal] == cameraParmsDic[camVal]):
                        print_DEBUG(camera,wanVal + " is " + wantedParmsDic[wanVal] + " on both dictionaries")
                        break
                    else:
                        #TODO add a pooliong system, which will allow multi-threading
                        sendParmsDic[wanVal] = wantedParmsDic[wanVal]
                        changes = True
                c = c + 1
            w = w + 1
    else:
        print_ERROR(camera,"The process failed and will end unsuccessfully")
        return

    if changes:
        camera.set_parameters(sendParmsDic)
        print_CASUAL(camera,"All new values uploaded to the camera")
    else:
        print_CASUAL(camera,"No values uploaded to the camera")

def main():
    setupCamera()

if __name__ == "__main__":
    main()	
