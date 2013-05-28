#!/usr/bin/python

"""
this file is GPLv3

and was written by Biel Bestue with help from Carlos Padial with the XML parsing

v 2.1
"""

import os
import xml.etree.ElementTree as ElTree
import ElpAPI
from msg import print_CASUAL, print_ERROR, print_DEBUG
#import autoKillSwitch, autoResolution, autoColour #TODO not yet, not yet

HOST1 = "elphel"
HOST2 = "192.168.1.11"
DESTPATH = os.path.expanduser("~/")+"elphel" #TODO - make it so all OS can get the correct path

def setupCamera_1():
    changes = False
    error = False
    wantedParmsDic = {}
    cameraParmsDic = {}
    sendParmsDic = {}
    maxLengthWan = 0
    maxLengthCam = 0

    try:
        camera1
    except NameError:
        camera1 = ElpAPI.core(HOST1) #creates camera only if it doesn't exists before
    else:
        print_CASUAL(camera1,"'camera1' object already created")
    
    try:
        tree = ElTree.parse(os.path.join(DESTPATH,"wanted_settings1.xml"))
        root = tree.getroot()
    except:
        print_ERROR(camera1,"Something went wrong while parsing 'wanted_settings.xml'")
        error = True
    else:
        for child in tree.iter():
            for c in child:
                wantedParmsDic[c.tag] = c.text
        #created a dictionary from known sources.
        keyListWan = wantedParmsDic.keys()

    camera1.get_parameters(wantedParmsDic,DESTPATH,"camera_settings1") 
    #download the camera settings using the dictionary as a reference.
    try:
        tree = ElTree.parse(os.path.join(DESTPATH,"camera_settings1.xml"))
        root = tree.getroot()
        print_DEBUG(camera1,"'tree' is:" + str(tree)) #debug
        print_DEBUG(camera1,"'root' is" + str(root)) #debug
    except:
        print_ERROR(camera1,"Something went wrong while parsing 'camera_settings1.xml'")
        error = True
    else:
        for child in tree.iter():
            for c in child:
                cameraParmsDic[c.tag] = c.text
                camera1.implant_camera_setting(c.tag, c.text)
        #created a new dictionary with the settings the camera is using.7

        #download_settings(camera, wantedParmsDic, cameraParmsDic)
        #download_settings(camera1, wantedParmsDic)
        keyListCam = cameraParmsDic.keys()
        #keyListCam = camera.DIC_SETTINGS.keys()
        #keyListCam = camera1.gather_camera_settings()


    if error is not True: 
        
        wanVal = ""
        camVal = ""
        w = 0
        maxLengthWan = len(keyListWan)
        print_DEBUG(camera1,"'maxLengthWan' is: " + str(maxLengthWan)) #debug
        maxLengthCam = len(keyListCam)
        print_DEBUG(camera1,"'maxLengthCam' is: " + str(maxLengthCam)) #debug
        for w in range(maxLengthWan):
            wanVal = keyListWan[w]
            c = 0
            for c in range(maxLengthCam):
                camVal = keyListCam[c]
                if (wanVal == camVal):
                    if (wantedParmsDic[wanVal] == cameraParmsDic[camVal]):
                        print_DEBUG(camera1,wanVal + " is " + wantedParmsDic[wanVal] + " on both dictionaries")
                        break
                    else:
                        #TODO add a pooliong system, which will allow multi-threading
                        sendParmsDic[wanVal] = wantedParmsDic[wanVal]
                        changes = True
                c = c + 1
            w = w + 1
    else:
        print_ERROR(camera1,"The process failed and will end unsuccessfully")
        return

    if changes:
        camera1.set_parameters(sendParmsDic)
        print_CASUAL(camera1,"All new values uploaded to the camera")
    else:
        print_CASUAL(camera1,"No values uploaded to the camera")


def setupCamera_2():
    changes = False
    error = False
    wantedParmsDic = {}
    cameraParmsDic = {}
    sendParmsDic = {}
    maxLengthWan = 0
    maxLengthCam = 0

    try:
        camera2
    except NameError:
        camera2 = ElpAPI.core(HOST2) #creates camera only if it doesn't exists before
    else:
        print_CASUAL(camera2,"'camera2' object already created")

    try:
        tree = ElTree.parse(os.path.join(DESTPATH,"wanted_settings2.xml"))
        root = tree.getroot()
    except:
        print_ERROR(camera2,"Something went wrong while parsing 'wanted_settings2.xml'")
        error = True
    else:
        for child in tree.iter():
            for c in child:
                wantedParmsDic[c.tag] = c.text
        #created a dictionary from known sources.
        keyListWan = wantedParmsDic.keys()

    camera2.get_parameters(wantedParmsDic,DESTPATH,"camera_settings2") 
    #download the camera settings using the dictionary as a reference.
    try:
        tree = ElTree.parse(os.path.join(DESTPATH,"camera_settings2.xml"))
        root = tree.getroot()
        print_DEBUG(camera2,"'tree' is:" + str(tree)) #debug
        print_DEBUG(camera2,"'root' is" + str(root)) #debug
    except:
        print_ERROR(camera2,"Something went wrong while parsing 'camera_settings2.xml'")
        error = True
    else:
        for child in tree.iter():
            for c in child:
                cameraParmsDic[c.tag] = c.text
                camera2.implant_camera_setting(c.tag, c.text)
        #created a new dictionary with the settings the camera is using.7

        #download_settings(camera, wantedParmsDic, cameraParmsDic)
        #download_settings(camera2, wantedParmsDic)
        keyListCam = cameraParmsDic.keys()
        #keyListCam = camera.DIC_SETTINGS.keys()
        #keyListCam = camera2.gather_camera_settings()


    if error is not True: 
        
        wanVal = ""
        camVal = ""
        w = 0
        maxLengthWan = len(keyListWan)
        print_DEBUG(camera2,"'maxLengthWan' is: " + str(maxLengthWan)) #debug
        maxLengthCam = len(keyListCam)
        print_DEBUG(camera2,"'maxLengthCam' is: " + str(maxLengthCam)) #debug
        for w in range(maxLengthWan):
            wanVal = keyListWan[w]
            c = 0
            for c in range(maxLengthCam):
                camVal = keyListCam[c]
                if (wanVal == camVal):
                    if (wantedParmsDic[wanVal] == cameraParmsDic[camVal]):
                        print_DEBUG(camera2,wanVal + " is " + wantedParmsDic[wanVal] + " on both dictionaries")
                        break
                    else:
                        #TODO add a pooliong system, which will allow multi-threading
                        sendParmsDic[wanVal] = wantedParmsDic[wanVal]
                        changes = True
                c = c + 1
            w = w + 1
    else:
        print_ERROR(camera2,"The process failed and will end unsuccessfully")
        return

    if changes:
        camera2.set_parameters(sendParmsDic)
        print_CASUAL(camera2,"All new values uploaded to the camera")
    else:
        print_CASUAL(camera2,"No values uploaded to the camera")

def setupCameras():
    setupCamera_1()
    setupCamera_2()

def download_settings(cam, parmameters):
#def download_settings(cam, parmameters, settDic):
    cam.get_parameters(parmameters,DESTPATH,"camera_settings") 
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
                #settDic[c.tag] = c.text
                cam.implant_camera_setting(c.tag, c.text)
                #cam.DIC_SETTINGS[c.tag] = c.text   

def check_cam_parameter(cam, parm):
    return cam.gather_one_camera_setting(parm)

def main():
    setupCameras()

if __name__ == "__main__":
    main()	
