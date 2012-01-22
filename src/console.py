'''
S.T.E.V.E. Console
Interactive command-line console
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import threading, sys, platform
import interfaces.emailmod as emailmod
import interfaces.txtmod as txtmod
import parsers.cmdparser as cmdparser
import parsers.searchparser as searchparser
from getpass import getuser

class console(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print
        print "Type help for a list of commands."
        while True:
            con = raw_input("S.T.E.V.E. > ")
            if con == "help":
                print "info - Shows current stats on S.T.E.V.E."
                print "picture - I'll take a picture and send it to a specified address."
                print "whoareyou - I'll tell you who I am."
                print "whoami - I'll tell you who you are."
                print "text - I'll send a text message for you."
                print "g - I'll Google that for you."
            elif con == "info":
                print "S.T.E.V.E. Statistics"
                print
                print "Operating System: " + platform.system() + " " + platform.release()
                print "Network Name: " + platform.node()
            elif con == "picture":
                cmdparser.picture()
                eaddress = raw_input("Email address to send to (Press Enter for no email) > ")
                if eaddress == "":
                    pass
                else:
                    emailmod.sendattach(eaddress, None, None, "image.jpg")
            elif con == "whoareyou":
                cmdparser.whoareyou("console")
            elif con == "text":
                number = raw_input("Phone number to send to (ex. 5555551234) > ")
                txt = raw_input("Message to send (can be over 160 characters) > ")
                if len(txt) > 160:
                    print "Message is " + str(len(txt)) + " characters."
                    q = raw_input("Would you still like to send the message (Y/n) >")
                    if q == "y" or "yes" or "":
                        txtmod.send(number, txt)
                        print "Message sent."
                    else:
                        print "Message not sent."
                else:
                    txtmod.send(number, txt)
                    print "Message sent."
            elif con == "whoami":
                print "Your name is probably " + getuser() + "."
                print "If you did not already know this, then that is a problem."
            elif con == "g":
                term = raw_input("Term to search for > ")
                res = searchparser.g(term)
                print "Top result is:"
                print res[0]
                print res[1]
                print res[2]
            elif con == "exit":
                sys.exit()
            else:
                print "Not a vaild command."