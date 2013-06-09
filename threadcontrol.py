#!/usr/bin/python
"""

    thread control to major Tom

    

"""

from Queue import Queue
from global_sets import tControl

class threadControl():
    def __init__( self ):
        self.listThread=[]
        self.queueGet = Queue()
        self.queueTelnet = Queue()
        self.listlog=[] #for every index --> Value[0] = thread name, value[1] = subject, value[2] = command, value[3] = state
        print("thread control started")

    def append_and_start_thread(self, thread):
        if thread_name is "None":
            print("ERROR - name cannot be 'None', therefore thread not initiated\ntry another name")
            return

        self.listThread.append( thread, thread_name )
        self.listThread[-1].setName( thread_name )
        self.listThread[-1].setDaemon( True )
        self.listThread[-1].start()

        sbjctCmmnd = self.listThread[-1].subject, self.listThread[-1].command
        self.dictWork[thread_name] = sbjctCmmnd

    def get_thread_index (self, thread_name ):
        maxLenght = len(self.listThread)
        i = 0
        while ( i <= maxLenght ):
            if ( self.listThread[i].getName == thread_name ):
                return i
            i += 1
        #TODO anounce error
        return -1

    def check_thread_status(self, thread_name ):

        index = get_thread_index( thread_name )
    
        if ( index is not -1):
            return self.listThread[index].get_status()
        else:
            #TODO print error
            pass

    def check_get_thread_subject(self, thread_name ):

        index = get_thread_index( thread_name )
    
        if ( index is not -1):
            return self.listThread[index].get_subject()
        else:
            #TODO print error
            pass

    def check_get_thread_command(self, thread_name ):

        index = get_thread_index( thread_name )
    
        if ( index is not -1):
            return self.listThread[index].get_command()
        else:
            #TODO print error
            pass
    def check_thread_log_status(self, thread_name ):
        #determine if a thread has finished
            
        #return true or false #TODO add a check using the logcent data
        pass


    def update_listLog( self, thread_name ):
        i = get_thread_index( thread_name )

        nmSbjctCmmnd = thread_name, self.listThread[i].get_subject(), self.listThread[i].get_command(), self.listThread[i].get_status()

        self.listLog.append(nmSbjctCmmnd)
    
        print("added a new entry in the log")

    def Gather_last_log( self, subject, command ):
        m = len( self.listLog )

        i = m - 1

        while i >= 0 :

            if ( self.listLog[i][1] is subject ) and ( self.listLog[i][2] is command ) and ( self.listLog[i][3] is "done" ):
                return self.listLog[i][0] #returns the thread name
            i -= 1
        print ("none found!")
        return -1

    #FOR FUCK SAKE! this is the utmost stupid crap I ever programmed, just add a new "name" variable in the init of the thread! a one liner change! YOU STUPID FUCK!
    """ 
    def request_name(self, subject, command, status):
        global tControl
        listsubj = []
        listcommand = []

        i = 1 #because index 0 is timeFrame
        while i <= 4
            if tControl.threadList[i].subject is subject
                listsubj.append( i )
            i += 1

        for i in len(listsubj)
            if tControl.threadList[i].command is command
                listcommand.append( i )

        for i in len(listcommand)
            if tControl.threadList[i].status is status
                return tControl.threadList[i].getName
    """

    """
    this should lock thread in case they share the subject, 
    this is useful because we don't control the state of the subject directly
    and we don't want the subject to lock off.
    """
    def determine_get_threads_priority ():
        pass


        
