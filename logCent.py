#!/usr/bin/python

"""
this file is GPLv3

written by Biel B. de Luna 

this file controls the centralised logging system, every object should have the capacity to handle their local logging system which should consist of different styles of logging: error logging, get logging, telnet logging, changes logging

this file though keeps records of all changes in all devices using the API, therfore it's useful for debugging purposes

it describes both the method of saving the logs, and the method to display them

v 0.1
"""
#style possibilities  
DEBUG   =   0
CASUAL  =   1
WARNING =   2              
ERROR   =   3
FREEWILL=   4 #if we detect that the devices reacted and change soemthing on their own

#environment
INCODE  =   0   #logs from the code itself
GET     =   1
TELNET  =   2



class log:
    def __init__(self, owner, time, style, environment, message):
        self.owner = owner
        self.time = time
        self.style = style
        self.envirnoment = environment
        self.message = message

class change_state_log(log):
    def __init__(self, action, subject, command, state):
        super(Device, self).__init__(owner, time, style, environment, message):
        self.action = action
        self.subject = subject
        self.command = command
        self.state = state
        

class logCenter:
    def __init__ (self):
        
        self.LOG_DIC = {}

    def set_new_entry(self, owner, style, time, msg):
        #self.LOG_DIC[owner] = style, time, msg
        pass

    def get_entry_by_style ( self, owner, style):
        # TODO get all the log entries from the owner, by style order
        pass

    def get_entry_by_owner(self, owner):
        #TODO get
        pass

if __name__ == '__main_':
    print("\nyou attempted to operate this file directly\nbut his file isn't meant to operate on it's own,\n\nplease before proceeding read first the README file.\n")
#EOF
