from mycroft import MycroftSkill, intent_file_handler
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import parakimo
import time
import getpass
import os


class CiscoSsh(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ssh.cisco.intent')

     UN = raw_input("Username : ")
     PW = getpass.getpass("Password : ")

     twrssh = paramiko.SSHClient()
     twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     twrssh.connect(192.168.0.1, port=22, username=UN, password=PW)
     remote = twrssh.invoke_shell()
     remote.send('term len 0\n')
     time.sleep(1)

     remote.send("reload")
     remote.send("y")

 def handle_ssh_cisco(self, message):
        self.speak_dialog('ssh.cisco')


def create_skill():
    return CiscoSsh()

