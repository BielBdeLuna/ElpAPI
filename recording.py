#!/usr/bin/python

"""
this file controls the recording aspect of the camera
there is two types of recording:
in-camera
off-camera

in-camera is controled via telnetlib

all code by Biel B. de Luna

this file is under GPLv3
"""

import os, telnetlib

ROOT_PATH = "" # path = ROOT_PATH + rel_path (the real deal here is the "rel_path")
               # ROOT_PATH is the root path inside the HDD on the camera, 
               # it should be indpenendent than the one used by the computer as a part of the destine folder path
"""
the script that checks th current status of camogm
"""
def camogm_check(self):
    """
    self.tn = telnetlib.Telnet(self.HOST)

    tn.read_until("login: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write('ps | grep "camogm"')
    tn.write('echo "status; exif 1; format=jpeg;status=/var/tmp/camogm.status" > /var/state/camogm_cmd')
    # ^^^^ probably needs to be changed to only read the status
    tn.read_until("status") #I need to find a way to gather the status
    """
    self.TNET_COMMANDS_QUEUE.put("write", 'ps | grep "camogm"')
    self.TNET_COMMANDS_QUEUE.put("write", 'echo "status; exif 1; format=jpeg;status=/var/tmp/camogm.status" > /var/state/camogm_cmd')
    # ^^^^ probably needs to be changed to only read the status
    self.TNET_COMMANDS_QUEUE.put("read_until", "status")

"""
the script that makes camogm start recording
"""
def camogm_record_start(self):
    if not self.RDY_STATE:
        print("ERROR! you can't start recording without setting up the recording session before!")
        return
    self.REC_STATE = True
    pass

"""
the script that makes camogm stop recording
"""
def camogm_record_stop(self):
    self.REC_STATE = False
    pass

"""
the script that setups camogm, 
sets the wanted the file name
sets the relative path starting from the ROOT_PATH in the HDD on camera
sets the container format from the filename
sets up the lentgh (infinite or something closer)
"""
def camogm_setup(self, filename, rel_path):

    if self.REC_STATE:
        print("ERROR! stop recording before changein anything!")
        return
    else:
        self.RDY_STATE = False
        #TODO let's extract the container from the filename
        #TODO lentgh should be infinite
        #TODO rel_path should be a relative path from an specific path selected inside the HDD, which is ROOT_PATH

        path = os.path.join(ROOT_PATH, rel_path)

        self.RDY_STATE = True
        pass


if __name__ == '__main_':
    print("\nyou attempted to operate this file directly\nbut his file isn't meant to operate on it's own,\n\nplease before proceeding read first the README file.\n")
#EOF   
