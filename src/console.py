'''
S.T.E.V.E. Console
Interactive command-line console
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import threading, sys, platform, urllib2, os
import interfaces.emailmod as emailmod
import interfaces.txtmod as txtmod
import parsers.cmdparser as cmdparser
import parsers.apiparser as apiparser
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
                consolehelp = open('consolehelp.txt', 'r')
                for line in consolehelp:
                    print line.strip('\n')
            elif con == "info":
                print "Operating System: " + platform.system() + " " + platform.release()
                print "Network Name: " + platform.node()
                ghurl = urllib2.urlopen("https://api.github.com/")
                x = ghurl.headers['X-RateLimit-Remaining']
                print "GitHub Requests Remaining: " + str(x)
            elif con == "picture":
                cmdparser.picture()
                eaddress = raw_input("Email address to send to (Press Enter for no email) > ")
                if eaddress == "":
                    pass
                else:
                    emailmod.sendattach(eaddress, None, None, "image.jpg")
            elif con == "whoareyou":
                cmdparser.whoareyou("console")
            elif con == "weather":
                city = raw_input("City > ")
                state = raw_input("State > ")
                cc = apiparser.weather(city, state)
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
                res = apiparser.ddg(term)
                print "Top result is from:" + res[0]
                print res[1]
                print res[2]
            elif con == "shorten":
                url = raw_input("URL to shorten (Do not include http://) > ")
                nurl = apiparser.shorten("http://" + url)
                if os.name == "nt":
                    import win32clipboard, win32con
                    win32clipboard.OpenClipboard()
                    win32clipboard.EmptyClipboard()
                    win32clipboard.SetClipboardData(win32con.CF_TEXT, nurl)
                    win32clipboard.CloseClipboard()
                    print "URL copied to clipboard."
                else:
                    print nurl
            elif con == "github":
                type = raw_input("Project or user > ")
                if type == "project":
                    proj = raw_input("Name of project > ")
                    name = raw_input("Username of project owner > ")
                    info = apiparser.ghproj(proj, name)
                    if isinstance(info, list) == True:
                        for x in range(len(info)):
                            print info[x]
                    else:
                        print info
                elif type == "user":
                    name = raw_input("Username > ")
                    info = apiparser.ghuser(name)
                    if isinstance(info, list) == True:
                        for x in range(len(info)):
                            print info[x]
                    else:
                        print info
                else:
                    print "Error: Not a valid selection."
            elif con == "exit":
                sys.exit()
            else:
                print "Not a vaild command."