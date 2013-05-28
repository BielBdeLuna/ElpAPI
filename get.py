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
from Queue import Queue
import logging
from msg import print_CASUAL, print_ERROR, print_DEBUG

class get_task:
    def __init__(self, url_to_retrieve, save_file_name):
        self.url = url_to_retrieve
        self.filename = save_file_name

class Downloader(threading.Thread):
    def __init__(self, queue, owner):
        threading.Thread.__init__(self)
        self.queue = queue
        self.owner = owner #this allows the thread to remember who called it,
                           #therefore letting the print messages know who did it

    def run(self):
        while True:
            #download_url = self.queue.get()
            
            task = self.queue.get()

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
                try:
                    urllib.urlretrieve(task.url, filename=task.filename)
                    print_DEBUG(self.owner, task.filename + " downloaded from " + task.url)
                except Exception, e:
                    #logging.warn("error downloading %s: %s" % (download_url, e))
                    print_WARNING(self.owner, "error downloading %s: %s" % (download_url, e))
            print_DEBUG(self.owner,"we don't wait2!") #debug
            self.queue.task_done()

            #TODO bind it with the logging system
            
if __name__ == '__main_':
    print("\nyou attempted to operate this file directly\nbut his file isn't meant to operate on it's own,\n\nplease before proceeding read first the README file.\n")
#EOF
