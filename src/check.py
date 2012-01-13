'''
S.T.E.V.E. Background Checkers
All of the background processes
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import threading
import interfaces.emailmod as emailmod
import interfaces.txtmod as txtmod
import parsers.emailparser as emailparser
import parsers.txtparser as txtparser
from time import sleep

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