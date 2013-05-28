#!/usr/bin/python
"""

    this scri initiates the time system, 
    it works in a tick counter fashion, 
    where time intervals arbit the development of the program
    it might serve in the future as the infraestructure for timed events

    it is inspired in the quake/doom engines

    time in miliseconds extreacted form a comentary at stackoverflow.com

    

"""

import threading
import time

DEFAULT_FREQUENCY = 16.66 # frequency in miliseconds --> 60fps

class timed_event:
    def __init__ (self, event_name=None):
        self.name = event_name if event_name is not None else randomize_name()
    def run(self):
        pass

    def get_name():
        return self.name

    def randomize_name():
        return "randomized named... NOT!" #TODO add a randomizer here

class Timeframe(threading.Thread):
    def __init__ (self, frequency=None):
        threading.Thread.__init__(self)
        self.frequency=frequency if frequency is not None else DEFAULT_FREQUENCY #frequency is in miliseconds seconds
        self.last_time = time.time()
        self.timed_events = []
        #self.count_tick =  unsigned long(0)
        self.run()

    def run(self):
        standard_sleep_time = float (self.frequency) / 1000 #convert the frequency to seconds
        #print("here starts the time loop, standard loop time is: " + str(standard_sleep_time))
        while True: 
            current_time = time.time()
            if len(self.timed_events) is 0:
                sleep_time = standard_sleep_time
            else:
                for event in self.timed_events:
                    event.run()
                sleep_time = self.get_time_for_next_tick()
    
            time.sleep(sleep_time)
            #self.count_tick = self.count_tick + 1
            self.last_time = current_time
            #print("time elapsed = " + str(self.last_time - time.time()))
            

    def get_tick_count(self):
        return self.count_tick

    def get_time_for_next_tick(self):
        current_time = time.time()
        delta = current_time-self.last_time
        return ((float(DEFAULT_FREQUENCY) / 1000) - delta)

    def add_event(self, event):
        self.timed_events.append(event)

    def sub_event(self, event_name):
        for event in self.timed_events:
            if event.get_name() is event_name:
                i = event.index()
                self.timed_events[i].pop()
                print ("event " + event_name + " substracted!")
                return
        print ("event " + event_name + " not found!")
        return

    def list_timed_event_names (self):
        for event in self.timed_events:
            print (event.get_name())

    def wait_for_tick(self):
        time.sleep(self.getTimeForNextTick())
