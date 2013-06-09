class task(): #this might be useful for telnet and as a base
    def __init__(self, subject, command):
        self.subject = subject
        self.command = command

class task_get(task):
    def __init__(self, subject, command, save_file_name):
        super(task, self).__init__(subject, command)
        #self.subject = subject
        #self.command = command
        self.url = self.subject + self.command
        self.filename = save_file_name

if __name__ == '__main_':
    print("\nyou attempted to operate this file directly\nbut his file isn't meant to operate on it's own,\n\nplease before proceeding read first the README file.\n")
#EOF
