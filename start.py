#!/usr/bin/python

"""
this file is GPLv3

author Biel B. de Luna

v 1.0
"""

import os
import ElpAPI
from msg import print_CASUAL, print_ERROR, print_DEBUG

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

    try:
        camera
    except NameError:
        camera = ElpAPI.core(HOST) #creates camera only if it doesn't exists before
    else:
        print_CASUAL(camera, "'camera' object already created")

def main():
    setupCamera()

if __name__ == "__main__":
    main()	
