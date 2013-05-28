#!/usr/bin/python

"""
this file is GPLv3

and was written by Biel Bestue 
inspired partially by Aleksey Rembish example @ https://github.com/don-ramon/colorprint and other examples in forums

v 1.0.1
"""

import time
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

def IPnDATE(self):
    return prCol.GREEN + "[ " + prCol.BOLD + gatherColor(self) + self.HOST + prCol.GREEN + " @ " + prCol.STANDARD + time.strftime("%H:%M:%S") + prCol.GREEN + " ] "

def print_ERROR(self, msg):
    print(IPnDATE(self) + prCol.RED + msg + prCol.STANDARD)
    #TODO add a logging system so error logs get printed in a file autmatically

def print_DEBUG(self, msg):
    if self.MSG_NODEBUG:
        pass
    else:
        print(IPnDATE(self) + prCol.MAGENTA + msg + prCol.STANDARD)

def print_CASUAL(self, msg):
    print(IPnDATE(self) + prCol.BLUE + msg + prCol.STANDARD)
