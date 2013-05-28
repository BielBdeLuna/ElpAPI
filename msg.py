#!/usr/bin/python

"""
this file is GPLv3

written by Biel B. de Luna 
inspired partially by Aleksey Rembish example @ https://github.com/don-ramon/colorprint and other examples in forums

v 1.0.2
"""

import time
import logCent
class prCol:

    STANDARD =  '\033[0m'
    BOLD =   '\033[1m'
    BLAND =  '\033[2m'
    UNDERLINE =  '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    CONCEALED = '\033[8m'
    GRAY =  '\033[90m'  
    RED =    '\033[91m'
    GREEN =  '\033[92m'
    YELLOW = '\033[93m'
    BLUE =   '\033[94m'
    MAGENTA = '\033[95m'
    CYAN =  '\033[96m'
    WHITE = '\033[97m'

    def disable(self):
        self.STANDARD = ''
        self.BOLD = ''
        self.BLAND = ''
        self.UNDERLINE = ''
        self.BLINK = ''
        self.REVERSE = ''
        self.CONCEALED = ''
        self.GRAY = ''
        self.RED = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.BLUE = ''
        self.MAGENTA = ''
        self.CYAN = ''
        self.WHITE = ''

def gatherColor(self): #TODO resolve the self reference
    if self.MSG_DEVICE_COLOUR is 0:
        return prCol.WHITE
    elif self.MSG_DEVICE_COLOUR is 1:
        return prCol.GRAY
    elif self.MSG_DEVICE_COLOUR is 2:
        return prCol.RED
    elif self.MSG_DEVICE_COLOUR is 3:
        return prCol.GREEN
    elif self.MSG_DEVICE_COLOUR is 4:
        return prCol.YELLOW
    elif self.MSG_DEVICE_COLOUR is 5:
        return prCol.BLUE
    elif self.MSG_DEVICE_COLOUR is 6:
        return prCol.MAGENTA
    elif self.MSG_DEVICE_COLOUR is 7:
        return prCol.CYAN

def IPnDATE(self, timeHMS):
    return prCol.GREEN + "[ " + prCol.BOLD + gatherColor(self) + self.HOST + prCol.GREEN + " @ " + prCol.STANDARD + timeHMS + prCol.GREEN + " ] "

def print_ERROR(self, msg):
    timeHMS = time.strftime("%H:%M:%S")
    final_msg = IPnDATE(self, timeHMS) + prCol.RED + msg + prCol.STANDARD
    #self.ERROR_LOG = self.ERROR_LOG + final_msg + "\n"  
    print(final_msg)
    #logCent.logCenter.set_new_entry(self, ERROR, timeHMS, msg)
    
def print_DEBUG(self, msg, level=0):
    level = level if level is not 0 else level is 0
    timeHMS = time.strftime("%H:%M:%S")

    if self.MSG_DEBUG_LEVEL is -1:
        pass
    else:
        if self.MSG_DEBUG_LEVEL <= level:
            
            #TODO test if msg is an array if so, print it accordingly
            """
            if 
                print(IPnDATE(self))
                for t in range(msg):
                    print(prCol.MAGENTA + t + "\n")
                print(prCol.STANDARD)
            else:
            """
            print(IPnDATE(self, timeHMS) + prCol.MAGENTA + msg + prCol.STANDARD)
        else:
            pass
    #log it anyway
    #logCent.logCenter.set_new_entry(self, DEBUG, timeHMS, msg) 

def print_CASUAL(self, msg):
    timeHMS = time.strftime("%H:%M:%S")
    print(IPnDATE(self, timeHMS) + prCol.BLUE + msg + prCol.STANDARD)
    #logCent.logCenter.set_new_entry(self, CASUAL, timeHMS, msg)

def print_WARNING(self, msg):
    timeHMS = time.strftime("%H:%M:%S")
    final_msg = IPnDATE(self, timeHMS) + prCol.YELLOW + msg + prCol.STANDARD
    #self.ERROR_LOG = self.ERROR_LOG + final_msg + "\n"  
    print(final_msg)
    #logCent.logCenter.set_new_entry(self, WARNING, timeHMS, msg)

if __name__ == '__main_':
    print("\nyou attempted to operate this file directly\nbut his file isn't meant to operate on it's own,\n\nplease before proceeding read first the README file.\n")
#EOF
