'''
S.T.E.V.E. Console
Interactive command-line console
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import threading, platform, urllib2, sys
import interfaces.emailmod as emailmod
import interfaces.txtmod as txtmod
import parsers.cmdparser as cmdparser
from getpass import getuser
from config import statsvar
from Tkinter import Tk

class console(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.basic = cmdparser.basiccmd()
        self.api = cmdparser.apicmd()

    def run(self):
        print
        print "Type help for a list of commands."
        while True:
            con = raw_input("S.T.E.V.E. > ")
            if con == "help":
                consolehelp = open('consolehelp.txt', 'r')
                for line in sorted(consolehelp):
                    print line.rstrip('\n')
            elif con == "info":
                stats = statsvar()
                print "S.T.E.V.E. Info"
                print "---------------"
                print "Revision Number: " + stats[0]
                print "Operating System: " + platform.system() + " " + platform.release()
                print "Network Name: " + platform.node()
                ghurl = urllib2.urlopen("https://api.github.com/")
                print "GitHub Requests Remaining: " + str(ghurl.headers['X-RateLimit-Remaining']) + "/" + str(ghurl.headers['X-RateLimit-Limit'])
            elif con == "picture":
                self.basic.picture()
                eaddress = raw_input("Email address to send to (Press Enter for no email) > ")
                if eaddress == "":
                    pass
                else:
                    emailmod.sendattach(eaddress, None, None, "image.jpg")
                    print "E-mail sent."
            elif con == "whoareyou":
                self.basic.whoareyou("console")
            elif con == "weather":
                city = raw_input("City > ")
                state = raw_input("State > ")
                cc = self.api.weather(city, state)
                for x in range(len(cc)):
                    print cc[x]
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
            elif con == "search":
                term = raw_input("Term to search for > ")
                res = self.api.search(term)
                print "Top result is from:" + res[0]
                print res[1]
                print res[2]
            elif con == "shorten":
                url = raw_input("URL to shorten (Do not include http://) > ")
                nurl = self.api.shorten("http://" + url)
                cb = Tk()
                cb.withdraw()
                cb.clipboard_clear()
                cb.clipboard_append(nurl)
                cb.destroy()
                print nurl
                print "URL copied to clipboard."
            elif con == "currency":
                num = raw_input("Amount > ")
                output = raw_input("3 letter name of currency to convert to (e.g USD) > ")
                convert = self.api.currency(num, output)
                for x in range(len(convert)):
                    print convert[x]
            elif con == "github":
                type = raw_input("Project or user > ")
                if type == "project":
                    proj = raw_input("Name of project > ")
                    name = raw_input("Username of project owner > ")
                    info = self.api.ghproj(proj, name)
                    if isinstance(info, list) == True:
                        for x in range(len(info)):
                            print info[x]
                    else:
                        print info
                elif type == "user":
                    name = raw_input("Username > ")
                    info = self.api.ghuser(name)
                    if isinstance(info, list) == True:
                        for x in range(len(info)):
                            print info[x]
                    else:
                        print info
                else:
                    print "Error: Not a valid selection."
            elif con == "exit":
                break
            else:
                print "Not a valid command."

if __name__ == '__main__':
    print "Not to be called directly."