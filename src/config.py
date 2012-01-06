'''
S.T.E.V.E. Configuration File Parser
Based on http://stackoverflow.com/a/3446232 by Zimm3r
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import os.path, sys
from ConfigParser import RawConfigParser
from ConfigParser import Error

def basicvar():
    parser = RawConfigParser()
    fileopen = open("config.ini")
    if fileopen.read().startswith("\xef\xbb\xbf"):
        print
        print "Error: File saved as Unicode."
        print "To fix: Resave config.ini as ASCII."
        raw_input()
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
                print
                print "Reason: config.ini does not exist."
                print "To fix: Rerun index.py."
                raw_input()
                sys.exit()
            else:
                print
                print "Reason: Unknown."
                raw_input()
                sys.exit()
        else:
            sections = parser.sections()
            login = []
            if parser.has_option(sections[0], "emailaddress"):
                if parser.get(sections[0], "emailaddress") == 'test@example.com':
                    print
                    print "Error: Default value detected."
                    print "To fix: Edit value 'emailaddress' in config.ini."
                    raw_input()
                    sys.exit()
                else:
                    login.append(parser.get(sections[0], "emailaddress"))
            else:
                print
                print "Error: Email address not found."
                print "To fix: Edit value 'emailaddress' in config.ini."
                raw_input()
                sys.exit()
            if parser.has_option(sections[0], "password"):
                if parser.get(sections[0], "password") == 'password':
                    print
                    print "Error: Default value detected."
                    print "To fix: Edit value 'password' in config.ini."
                    raw_input()
                    sys.exit()
                else:
                    login.append(parser.get(sections[0], "password"))
            else:
                print
                print "Error: Password not found."
                print "To fix: Edit value 'password' in config.ini."
                raw_input()
                sys.exit()
            if parser.has_option(sections[0], "imapserver"):
                if parser.get(sections[0], "imapserver") == '':
                    server = parser.get(sections[0], "emailaddress").split("@")
                    login.append('imap.' + server[1].strip("'"))
                    login.append(True)
                else:
                    login.append(parser.get(sections[0], "imapserver"))
                    login.append(False)
            if parser.has_option(sections[0], "smtpserver"):
                if parser.get(sections[0], "smtpserver") == '':
                    server = parser.get(sections[0], "emailaddress").split("@")
                    login.append('smtp.' + server[1].strip("'"))
                    login.append(True)
                else:
                    login.append(parser.get(sections[0], "smtpserver"))
                    login.append(False)
            return login

def googlevar():
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
            glogin = []
            if parser.has_option(sections[1], "gusername"):
                if parser.get(sections[1], "gusername") == 'test@gmail.com':
                    print
                    print "Error: Default value detected."
                    print "To fix: Edit value 'username' in config.ini."
                    raw_input()
                    sys.exit()
                else:
                    glogin.append(parser.get(sections[1], "gusername"))
            else:
                print
                print "Error: Google username not found."
                print "To fix: Edit value 'gusername' in config.ini."
                raw_input()
                sys.exit()
            if parser.has_option(sections[1], "gpassword"):
                if parser.get(sections[1], "gpassword") == 'gpassword':
                    print
                    print "Error: Default value detected."
                    print "To fix: Edit value 'gpassword' in config.ini."
                    raw_input()
                    sys.exit()
                else:
                    glogin.append(parser.get(sections[1], "gpassword"))
            else:
                print
                print "Error: Google password not found."
                print "To fix: Edit value 'gpassword' in config.ini."
                raw_input()
                sys.exit()
            return glogin

if __name__ == '__main__':
    print "S.T.E.V.E. Configuration Values"
    login = basicvar()
    print "Email Address: " + login[0]
    #print "Password: " + login[1]
    print "Password: Not displayed for security reasons."
    print "To display password, please uncomment line 152 and comment lines 153-154."
    if login[3] == True:
        print "WARNING: IMAP server assumed to be " + login[2] + "."
        print "If this is incorrect, please stop S.T.E.V.E. and change the"
        print "value 'smtpserver'."
    if login[5] == True:
        print "SMTP Server: " + login[4]
        print "WARNING: SMTP server assumed to be " + login[4] + "."
        print "If this is incorrect, please stop S.T.E.V.E. and change the"
        print "value 'smtpserver'."
    else:
        print "SMTP Server: " + login[3]
    glogin = googlevar()
    print "Google Username: " + glogin[0]
    #print "Google Password: " + glogin[1]
    print "Password: Not displayed for security reasons."
    print "To display password, please uncomment line 170 and comment lines 171-172."
    raw_input("Press Enter to exit... (don't question it)")
    sys.exit()