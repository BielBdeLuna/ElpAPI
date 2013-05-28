#!/usr/bin/python

"""
this script controls the telnet communication beyween the devices and the program

all code by Biel B. de Luna

this file is under GPLv3
"""

import sys, telnetlib
#import ElpAPI.core as camera
import threading

CAMERA_DELAY = 1 #second

class TnetCom(threading.Thread):

    def __init__(self, device, queue):
        #super(TnetCom, self).__init__()
        threading.Thread.__init__(self)
        self.device = device
        self.commandQueue = queue

    def run(self):
        self.TNET = telnetlib.Telnet(self.device.HOST)
        self.TNET.read_until("login: ")
        self.TNET.write(self.device.USERNAME + "\n")
        if self.device.PASSWORD:
            self.TNET.read_until("Password: ")
            self.TNET.write(self.device.PASSWORD + "\n")
        print("Telnet started!")
        #TODO bind it with the logging system

    def WorkItGodDamnIt(self):
        command_type, command_order = self.commandQueue.get()
        if command_type == "write":
            self.TNET.write(command_order + "\n")
        elif command_type == "read_until":
            self.TNET.read_until(command_order)
        
        if command_type == "wait":
            self.TNET.read_until(sleep(command_order))
        else:
            sleep(CAMERA_DELAY)    


if __name__ == '__main_':
    print("\nyou attempted to operate this file directly\nbut his file isn't meant to operate on it's own,\n\nplease before proceeding read first the README file.\n")
#EOF
