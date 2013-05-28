#!/usr/bin/python

"""
this file defines de superclass for all devices that play any role within the system
this superclass will direct two subclasses, masters and slaves, the master class will have a companion whioch will be the super-master (definning a centralized system) which in the future is deemed to dissapear, enabling the sharing of power among all the master in fornt of the slaves.
"""

class Device (object):
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.syncStamp = 0 # this should be changed
        pass

    def run(self):
        init_syncStamp()
        pass

    def get_name(self):
        return self.name

    def set_name(self, newName):
        self.name = newName

    def get_host(self):
        return self.host

    def set_host(self, newHost):
        self.host = newHost

    def get_port(self):
        return self.port

    def set_port(self, newPort):
        self.port = newPort

    def get_syncStamp(self):
        return self.syncStamp

    def set_syncStamp(self, newSyncStamp):
        self.syncStamp = newSyncStamp

    def request_syncronitzation(self, serveDevice):
        #requests syncStamp syncronitzation with a another device
        pass

    def serve_syncronitzation(self, requestDevice):
        #serve the syncStamp syncronitzation requested by another device
        pass

    def init_syncStamp(self):
        try:
            if self.owner:
                request_syncronitzation(self, self.owner)
        except:
            pass

class Master(Device):
    def __init__(self, name, host, port):
        #while slaves might have a master or several masters have none
        super(Device, self).__init__(name, host, port)
        self.slaveList = []
        self.knownMastersList = []

    def run(self):
        super(Device, self).run()
        pass

    def get_slave_names(self):
        for i in sorted(self.slavelist.keys()):
            print(i)

    def append_slave(self, slaveName):
        self.slaveList.append(slaveName)

    def check_slave(self, enquiredSlave):
        #checks if the enquired slaver is his slave
        pass

class SuperMaster(Master):
    def __init__(self, name, host, port):
        super(Master, self).__init__(name, host, port)

    def run(self):
        super(Master, self).run()
        generate_syncStamp()

    def generate_syncStamp(self):
        pass

    def organize_system(self):
        pass


class Slave(Device):
    def __init__(self, name, host, port, owner):
        super(Device, self).__init__(name, host, port)
        self.owner = owner
        self.masterList = []

    def run(self):
        super(Device, self).run()
        pass

    def get_owner(self):
        return self.owner 
        #this should be looked upeon for the case where there are several masters for the same slave

    def set_owner(self):
        self.owner = owner

    def get_master_names(self):
        for i in sorted(self.masterlist.keys()):
            print(i)

    def append_master(self, masterName):
        self.masterList.append(masterName)
        pass

    def check_owner(self, enquiringOwner):
        #checks if the enquiring owner is his owner
        pass

    

#EOF
