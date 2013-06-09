#!/usr/bin/python
"""

    this get functionality was extracted from some answers in stackoverflow.com:

    http://stackoverflow.com/questions/2467609/using-wget-via-python

    from ansewers: 

    5 - by McJeff
    5.1 - by disfated

"""

import sys
import threading
import urllib
#from Queue import Queue
import logging
from global_sets import tControl
from msg import print_CASUAL, print_ERROR, print_DEBUG



class Downloader( threading.Thread ):
    def __init__( self, queue, owner, name ):
        threading.Thread.__init__( self )
        self.queue = queue
        self.name = name
        self.subject = "None"
        self.command = "None"
        self.status = "idle"
        self.owner = owner #this allows the thread to remember who called it,
                           #therefore letting the print messages know who did it

        tControl.update_listLog( self.name )

    def run( self ):
        while True:
            task = self.queue.get()
            if task is not None:
                self.status = "working"
            else:
                self.status = "idle"
                

            if not task.url:
                print_WARNING(self.owner, "ERROR! Cannot download " + task.url + " !" )
                return
            else:
                print_DEBUG(self.owner, "url is: " + task.url)
            if task.filename is None:
                print_DEBUG(self.owner, "downloading but not saving!")
                #TODO figure out how to retrieve a file through url but not save it.
                """
                try:
                    urllib.urlretrieve(task.url, filename=task.filename)
                except Exception, e:
                    #logging.warn("error downloading %s: %s" % (download_url, e))
                    print_WARNING(self.owner, "error downloading %s: %s" % (download_url, e))
                """
            else:
                print_DEBUG(self.owner, "downloading the file named " + task.filename + "!")
                self.subject = task.subject
                try:
                    urllib.urlretrieve(task.url, filename=task.filename)
                    
                    print_DEBUG(self.owner, task.filename + " downloaded from " + task.url)
                except Exception, e:
                    #logging.warn("error downloading %s: %s" % (download_url, e))
                    print_WARNING(self.owner, "error downloading %s: %s" % (download_url, e))
                    self.status = "failed"
                    tControl.update_listLog( self.name )
            print_DEBUG(self.owner, self.name + "done!") #debug
            #we don¡t change the subject but we change the status this serves 
            #the purpose of remainig who we were downloading from
            self.status = "done"
            tControl.update_listLog( self.name )
            self.queue.task_done()

            #TODO bind it with the logging system
        """
        this serves the purpose to control different get systems by 
        retruning the subject that every get thread is working to.

        this means to which url the get thread is attempting to download from

        it could return "None" in that case the thread is nogt working on anything
        """
        def get_subject( self ):
            return self.subject

        def get_command( self ):
            return self.command
    
        def get_status( self ):
            return self.status

        def update_dictWork(self):
            
            
            
if __name__ == '__main_':
    print("\nyou attempted to operate this file directly\nbut his file isn't meant to operate on it's own,\n\nplease before proceeding read first the README file.\n")
#EOF
