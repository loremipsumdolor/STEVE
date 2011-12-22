'''
S.T.E.V.E. Configuration File Parser
Based on http://stackoverflow.com/a/3446232 by Zimm3r
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''
import sys
import os.path
from ConfigParser import RawConfigParser as ConfParser
from ConfigParser import Error

def configvar():
    parser = ConfParser()
    fileopen = open("config.ini")
    if fileopen.read().startswith("\xef\xbb\xbf"):
        print "Error: File saved as Unicode."
        print "To fix: Resave config.ini as ASCII."
        sys.exit()
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
                print "Reason: config.ini does not exist."
                print "To fix: Rerun index.py."
                sys.exit()
            else:
                print "Reason: Unknown."
                sys.exit()
        else:
            sections = parser.sections()
            sections.sort()
            login = []
            for s in sections:
                if parser.has_option(s, "emailaddress"):
                    if parser.get(s, "emailaddress") == 'test@example.com':
                        print "Error: Default values detected."
                        print "To fix: Edit values in config.ini."
                        sys.exit()
                    else:
                        login.append(parser.get(s, "emailaddress"))
                        email = parser.get(s, "emailaddress")
                else:
                    print "Error: Email address not found."
                    print "To fix: Edit values in config.ini."
                    sys.exit()
                if parser.has_option(s, "password"):
                    if parser.get(s, "password") == 'password':
                        print "Error: Default values detected."
                        print "To fix: Edit values in config.ini."
                        sys.exit()
                    else:
                        login.append(parser.get(s, "password"))
                else:
                    print "Error: Password not found."
                    print "To fix: Edit values in config.ini."
                    sys.exit()
                if parser.has_option(s, "fbemail"):
                    if parser.get(s, "fbemail") == 'example@m.facebook.com':
                        print "Error: Default values detected."
                        print "To fix: Edit values in config.ini."
                        sys.exit()
                    else:
                        login.append(parser.get(s, "fbemail"))
                else:
                    print "Error: Facebook email not found."
                    print "To fix: Edit values in config.ini."
                    sys.exit()
                if parser.has_option(s, "imapserver"):
                    if parser.get(s, "imapserver") == '':
                        server = email.split("@")
                        login.append(server[1])
                        print "WARNING: IMAP server assumed to be imaparser." + server[1] + "."
                        print "If this is incorrect, please stop S.T.E.V.E. and change the"
                        print "value 'imapserver'."
                    else:
                        login.append(parser.get(s, "imapserver"))
                if parser.has_option(s, "smtpserver"):
                    if parser.get(s, "smtpserver") == '':
                        server = email.split("@")
                        login.append(server[1])
                        print "WARNING: SMTP server assumed to be smtparser." + server[1] + "."
                        print "If this is incorrect, please stop S.T.E.V.E. and change the"
                        print "value 'smtpserver'."
                    else:
                        login.append(parser.get(s, "smtpserver"))
            return login

if __name__ == '__main__':
    print "S.T.E.V.E. Configuration Values"
    parser = ConfParser()
    fileopen = open("config.ini")
    if fileopen.read().startswith("\xef\xbb\xbf"):
        print "Error: File saved as Unicode."
        print "To fix: Resave config.ini as ASCII."
        sys.exit()
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
                print "Reason: config.ini does not exist."
                print "To fix: Rerun index.py."
                sys.exit()
            else:
                print "Reason: Unknown."
                sys.exit()
        else:
            sections = parser.sections()
            sections.sort()
            for s in sections:
                if parser.has_option(s, "emailaddress"):
                    print "Email Address: " + parser.get(s, "emailaddress")
                if parser.has_option(s, "password"):
                    #print "Password: " + parser.get(s, "password")
                    print "Password: Not displayed for security reasons."
                    print "To display password, please uncomment line 126 and comment lines 127-128."
                if parser.has_option(s, "fbemail"):
                    print "Facebook Email Address: " + parser.get(s, "fbemail")
                    print "NOTE: Facebook email should be the mobile Facebook email address."
                if parser.has_option(s, "imapserver"):
                    print "IMAP Server: " + parser.get(s, "imapserver")
                if parser.has_option(s, "smtpserver"):
                    print "SMTP Server: " + parser.get(s, "smtpserver")
    raw_input("Press Enter to exit... (don't question it)")