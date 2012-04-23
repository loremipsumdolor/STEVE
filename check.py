'''
S.T.E.V.E. Background Checkers
All of the background processes
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
'''

import threading
import cmdparser
import config
import interfaces.emailmod as emailmod
import interfaces.txtmod as txtmod
from time import sleep

class emailcheck(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.msgparse = cmdparser.msgparse()
        self.login = config.basicvar()
        if self.login[3] == True:
            print
            print "WARNING: IMAP server assumed to be " + self.login[2] + "."
            print "If this is incorrect, please stop S.T.E.V.E. and change the"
            print "value 'smtpserver'."
        if self.login[5] == True:
            print
            print "WARNING: SMTP server assumed to be " + self.login[4] + "."
            print "If this is incorrect, please stop S.T.E.V.E. and change the"
            print "value 'smtpserver'."
    def run(self):
        while True:
            self.data = emailmod.retrieve()
            if self.data != [] or self.data != None:
                for x in range(len(self.data)):
                    self.interpret = self.msgparse.interpret(self.data[x],
                                                             "email")
                    if self.interpret != None:
                        self.data = self.interpret[0]
                        self.sender = self.interpret[1]
                        self.parse = self.msgparse.parse(self.data,
                                                         self.sender, "email")
                        self.method = self.parse[0]
                        self.toea = self.parse[1]
                        self.subject = self.parse[2]
                        self.text = self.parse[3]
                        if self.method == "attach":
                            self.attach = self.parse[4]
                            emailmod.sendattach(self.toea, self.subject,
                                                self.text, self.attach)
                        elif self.method == "text":
                            emailmod.send(self.toea, self.subject, self.text)
                        else:
                            sleep(10)
                    else:
                        sleep(10)
            else:
                sleep(10)

class txtcheck(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.msgparse = cmdparser.msgparse()
    def run(self):
        while True:
            self.data = txtmod.retrieve()
            if self.data != []:
                for x in range(len(self.data)):
                    self.interpret = self.msgparse.interpret(self.data[x],
                                                             "txt")
                    if self.interpret != None:
                        self.data = self.interpret[0]
                        self.sender = self.interpret[1]
                        self.parse = self.msgparse.parse(self.data,
                                                         self.sender, "txt")
                        
                        self.tonum = self.parse[0]
                        self.msg = self.parse[1]
                        if len(self.parse[1]) > 160:
                            txt = [''.join(x) for x in zip(*[list(self.msg
                                                                  [z::160])
                                                    for z in range(160)])]
                            for x in txt:
                                txtmod.send(txt[x], self.tonum)
                        else:
                            txtmod.send(self.tonum, self.msg)
                    else:
                        sleep(10)
            else:
                sleep(10)

if __name__ == '__main__':
    print "Not to be called directly."