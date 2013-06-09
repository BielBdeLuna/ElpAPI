#!/usr/bin/python

"""
this file is GPLv3

and was written by Biel Bestue

v 3.0
"""

import os
import timeframe
import ElpAPI
from global_sets import tControl
from timeframe import Timeframe
from msg import print_CASUAL, print_ERROR, print_DEBUG

HOST = "elphel"
DESTPATH = os.path.expanduser("~/")+"elphel" #TODO - make it so all OS can get the correct path

def main():
    global tControl
    tControl.append_and_start_thread(Timeframe(), "Time Frame system")
       
    camera = ElpAPI.elphelCam(host=HOST,root_path=DESTPATH)

def close():
    pass
    """
    timeframe.destroy()
    camera.destroy()
    """

if __name__ == "__main__":
    main()	
