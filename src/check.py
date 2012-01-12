'''
S.T.E.V.E. Background Checkers
All of the background processes
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import threading, cmdparser
import emailparser, emailmod
import txtmod, txtparser
from time import sleep
from getpass import getuser

class emailcheck(threading.Thread):
    def __init__(self, login):
        threading.Thread.__init__(self)
        self.ea = login[0]
        self.pw = login[1]
        self.imap = login[2]
        if login[3] == True:
            self.smtp = login[4]
            print
            print "WARNING: IMAP server assumed to be " + login[2] + "."
            print "If this is incorrect, please stop S.T.E.V.E. and change the"
            print "value 'smtpserver'."
        else:
            self.smtp = login[3]
        if login[5] == True:
            print
            print "WARNING: SMTP server assumed to be " + login[4] + "."
            print "If this is incorrect, please stop S.T.E.V.E. and change the"
            print "value 'smtpserver'."
    def run(self):
        while True:
            self.data = emailmod.retrieve(self.ea, self.pw, self.imap)
            if self.data != None:
                self.parse = emailparser.parse(self.data)
                if self.parse[0] == "image.jpg":
                    emailmod.sendattach(self.parse[1], None, None, self.parse[0])
                else:
                    sleep(10)
            else:
                sleep(10)

class txtcheck(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            self.data = txtmod.retrieve()
            if self.data != []:
                self.parse = txtparser.parse(self.data)
                if self.parse[0] == "image.jpg":
                    txtmod.send(self.parse[1], "Image taken successfully.")
                else:
                    sleep(10)
            else:
                sleep(10)

class console(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print
        print "Type help for a list of commands."
        while True:
            con = raw_input("S.T.E.V.E. > ")
            if con == "help":
                print "picture - I'll take a picture and send it to a specified address."
                print "whoareyou - I'll tell you who I am."
                print "whoami - I'll tell you who you are."
                print "text - I'll send a text message for you."
                print
            elif con == "picture":
                cmdparser.picture()
                eaddress = raw_input("Email address to send to (Press Enter for no email) > ")
                if eaddress == "":
                    pass
                else:
                    emailmod.sendattach("image.jpg", None, None, eaddress)
            elif con == "whoareyou":
                cmdparser.whoareyou("console")
            elif con == "text":
                number = raw_input("Phone number to send to (ex. 5555551234) > ")
                txt = raw_input("Message to send (160 characters or less) > ")
                if len(txt) <= 160:
                    txtmsg = txtmod.send(number, txt)
                    if txtmsg == "OK":
                        print "Message sent successfully."
                    else:
                        print "Message sent unsuccessfully."
                else:
                    print "Message too long (" + str(len(txt)) + " chars)."
            elif con == "whoami":
                print "Your name is probably " + getuser() + "."
                print "If you did not already know this, then that is a problem."
            elif con == "exit":
                exit()
            else:
                print "Not a vaild command."