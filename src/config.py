'''
S.T.E.V.E. Configuration File Parser
Based on http://stackoverflow.com/a/3446232 by Zimm3r
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import os.path
from ConfigParser import RawConfigParser
from ConfigParser import Error

def configvar():
    parser = RawConfigParser()
    fileopen = open("config.ini")
    if fileopen.read().startswith("\xef\xbb\xbf"):
        print
        print "Error: File saved as Unicode."
        print "To fix: Resave config.ini as ASCII."
        raw_input()
    try:
        results = parser.read("config.ini")
    except Error, msg:
        print "Error: Cannot parse file."
        print "Reason: Please see error message."
        print msg
    else:
        if results == []:
            print "Error: Could not load config.ini."
            if not os.path.exists("config.ini"):
                print
                print "Reason: config.ini does not exist."
                print "To fix: Rerun index.py."
                raw_input()
            else:
                print
                print "Reason: Unknown."
                raw_input()
        else:
            sections = parser.sections()
            sections.sort()
            login = []
            for s in sections:
                if parser.has_option(s, "emailaddress"):
                    if parser.get(s, "emailaddress") == 'test@example.com':
                        print
                        print "Error: Default value detected."
                        print "To fix: Edit value 'emailaddress' in config.ini."
                        raw_input()
                    else:
                        login.append(parser.get(s, "emailaddress"))
                else:
                    print
                    print "Error: Email address not found."
                    print "To fix: Edit value 'emailaddress' in config.ini."
                    raw_input()
                if parser.has_option(s, "password"):
                    if parser.get(s, "password") == 'password':
                        print
                        print "Error: Default value detected."
                        print "To fix: Edit value 'password' in config.ini."
                        raw_input()
                    else:
                        login.append(parser.get(s, "password"))
                else:
                    print
                    print "Error: Password not found."
                    print "To fix: Edit value 'password' in config.ini."
                    raw_input()
                if parser.has_option(s, "imapserver"):
                    if parser.get(s, "imapserver") == '':
                        server = parser.get(s, "emailaddress").split("@")
                        login.append('imap.' + server[1].strip("'"))
                        login.append(True)
                    else:
                        login.append(parser.get(s, "imapserver"))
                if parser.has_option(s, "smtpserver"):
                    if parser.get(s, "smtpserver") == '':
                        server = parser.get(s, "emailaddress").split("@")
                        login.append('smtp.' + server[1].strip("'"))
                        login.append(True)
                    else:
                        login.append(parser.get(s, "smtpserver"))
            return login

if __name__ == '__main__':
    print "S.T.E.V.E. Configuration Values"
    login = configvar()
    print "Email Address: " + login[0]
    #print "Password: " + login[1]
    print "Password: Not displayed for security reasons."
    print "To display password, please uncomment line 90 and comment lines 91-92."
    print "IMAP Server: " + login[2]
    print "SMTP Server: " + login[4]
    raw_input("Press Enter to exit... (don't question it)")