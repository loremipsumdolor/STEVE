'''
S.T.E.V.E. Configuration File Parser
For that config.ini file
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
Based on http://stackoverflow.com/a/3446232 by Zimm3r
'''

import os.path, sys, inspect, update
from ConfigParser import RawConfigParser, Error

def testconfig():
    parser = RawConfigParser()
    fileopen = open("config.ini")
    if fileopen.read().startswith("\xef\xbb\xbf"):
        print
        print "Error: File saved as Unicode."
        raw_input("To fix: Resave config.ini as ASCII.")
        sys.exit()
    try:
        results = parser.read("config.ini")
    except Error, msg:
        print "Error: Cannot parse file."
        print "Reason: Please see error message."
        raw_input(msg)
        sys.exit()
    else:
        if results == []:
            print "Error: Could not load config.ini."
            if not os.path.exists("config.ini"):
                print "Reason: config.ini does not exist."
                raw_input("To fix: Rerun index.py.")
                sys.exit()
            else:
                raw_input("Reason: Unknown.")
                sys.exit()
        else:
            return

def basicvar():
    testconfig()
    parser = RawConfigParser()
    results = parser.read("config.ini")
    sections = parser.sections()
    login = []
    if parser.has_option(sections[0], "emailaddress"):
        if parser.get(sections[0], "emailaddress") == 'test@example.com':
            print
            print "Error: Default value detected."
            raw_input("To fix: Edit value 'emailaddress' in config.ini.")
            sys.exit()
        else:
            login.append(parser.get(sections[0], "emailaddress"))
    else:
        print
        print "Error: Email address not found."
        raw_input("To fix: Add value 'emailaddress' to config.ini.")
        sys.exit()
    if parser.has_option(sections[0], "password"):
        if parser.get(sections[0], "password") == 'password':
            print
            print "Error: Default value detected."
            raw_input("To fix: Edit value 'password' in config.ini.")
            sys.exit()
        else:
            login.append(parser.get(sections[0], "password"))
    else:
        print
        print "Error: Password not found."
        raw_input("To fix: Add value 'password' to config.ini.")
        sys.exit()
    if parser.has_option(sections[0], "imapserver"):
        if parser.get(sections[0], "imapserver") == '':
            server = parser.get(sections[0], "emailaddress").split("@")
            login.append('imap.' + server[1].strip("'"))
            login.append(True)
        else:
            login.append(parser.get(sections[0], "imapserver"))
            login.append(False)
    else:
        print
        print "Error: IMAP server not found."
        raw_input("To fix: Add value 'imapserver' to config.ini.")
        sys.exit()
    if parser.has_option(sections[0], "smtpserver"):
        if parser.get(sections[0], "smtpserver") == '':
            server = parser.get(sections[0], "emailaddress").split("@")
            login.append('smtp.' + server[1].strip("'"))
            login.append(True)
        else:
            login.append(parser.get(sections[0], "smtpserver"))
            login.append(False)
    else:
        print
        print "Error: SMTP server not found."
        raw_input("To fix: Add value 'smtpserver' to config.ini.")
        sys.exit()
    return login

def googlevar():
    testconfig()
    parser = RawConfigParser()
    results = parser.read("config.ini")
    sections = parser.sections()
    glogin = []
    if parser.has_option(sections[1], "gusername"):
        if parser.get(sections[1], "gusername") == 'test@gmail.com':
            print
            print "Error: Default value detected."
            raw_input("To fix: Edit value 'username' in config.ini.")
            sys.exit()
        else:
            glogin.append(parser.get(sections[1], "gusername"))
    else:
        print
        print "Error: Google username not found."
        raw_input("To fix: Add value 'gusername' to config.ini.")
        sys.exit()
    if parser.has_option(sections[1], "gpassword"):
        if parser.get(sections[1], "gpassword") == 'gpassword':
            print
            print "Error: Default value detected."
            raw_input("To fix: Edit value 'gpassword' in config.ini.")
            sys.exit()
        else:
            glogin.append(parser.get(sections[1], "gpassword"))
    else:
        print
        print "Error: Google password not found."
        raw_input("To fix: Add value 'gpassword' to config.ini.")
        sys.exit()
    if parser.has_option(sections[1], "gvoicenum"):
        if parser.get(sections[1], "gvoicenum") == '5555551234':
            print
            print "Error: Default value detected."
            raw_input("To fix: Edit value 'gvoicenum' in config.ini.")
            sys.exit()
        else:
            glogin.append(parser.get(sections[1], "gvoicenum"))
    else:
        print
        print "Error: Google Voice Number not found."
        raw_input("To fix: Add value 'gvoicenum' to config.ini.")
        sys.exit()
    return glogin

def apivar():
    testconfig()
    parser = RawConfigParser()
    results = parser.read("config.ini")
    sections = parser.sections()
    apivar = []
    if parser.has_option(sections[2], "bitlyusername"):
        if parser.get(sections[2], "bitlyusername") == '':
            apivar.append(None)
        else:
            apivar.append(parser.get(sections[2], "bitlyusername"))
    else:
        print
        print "Error: bit.ly username not found."
        raw_input("To fix: Add value 'bitlyusername' to config.ini.")
        sys.exit()
    if parser.has_option(sections[2], "bitlykey"):
        if parser.get(sections[2], "bitlykey") == '':
            apivar.append(None)
        else:
            apivar.append(parser.get(sections[2], "bitlykey"))
    else:
        print
        print "Error: bit.ly key not found."
        raw_input("To fix: Add value 'bitlykey' to config.ini.")
        sys.exit()
    if parser.has_option(sections[2], "wunderkey"):
        if parser.get(sections[2], "wunderkey") == '':
                apivar.append(None)
        else:
            apivar.append(parser.get(sections[2], "wunderkey"))
    else:
        print
        print "Error: Wunderground key not found."
        raw_input("To fix: Add value 'wunderkey' to config.ini.")
        sys.exit()
    return apivar

def statsvar():
    testconfig()
    parser = RawConfigParser()
    results = parser.read("config.ini")
    sections = parser.sections()
    statsvar = []
    if parser.has_option(sections[3], "commit"):
        if parser.get(sections[3], "commit") == '':
            parser.set(sections[3], "commit", update.currentcommit())
            print "WARNING: Most recent commit was the assumed for value 'commit'."
            print "This can be ignored if this the first run. If not, please"
            print "download the newest version as soon as possible."
        else:
            statsvar.append(parser.get(sections[3], "commit"))
    else:
        print
        print "Error: Commit not found."
        raw_input("To fix: Add value 'commit' to config.ini.")
        sys.exit()
    return statsvar

def changecommit(ccommit):
    testconfig()
    parser = RawConfigParser()
    results = parser.read("config.ini")
    sections = parser.sections()
    parser.set(sections[3], "commit", ccommit)
    return

def lineno():
    return int(inspect.currentframe().f_back.f_lineno)

if __name__ == '__main__':
    login = basicvar()
    glogin = googlevar()
    apikeys = apivar()
    stats = statsvar()
    print "S.T.E.V.E. Configuration Values"
    print
    print "Basic Configuration Values"
    print "Email Address: " + login[0]
    #print "Password: " + login[1]
    print "Password: Not displayed for security reasons."
    print "To display password, please uncomment line " + str(lineno()-2) + " and comment lines " + str(lineno()-1) + "-" + str(lineno()) + "."
    if login[3] == True:
        print "IMAP Server: " + login[2]
        print "Warning: IMAP server is an assumed value."
        print "To fix: Edit value 'imapserver' in config.ini."
    else:
        print "IMAP Server: " + login[2]
    if login[5] == True:
        print "SMTP Server: " + login[4]
        print "Warning: SMTP server is an assumed value."
        print "To fix: Edit value 'smtpserver' in config.ini."
    else:
        print "SMTP Server: " + login[4]
    print
    print "Google Configuration Values"
    print "Google Username: " + glogin[0]
    #print "Google Password: " + glogin[1]
    print "Password: Not displayed for security reasons."
    print "To display password, please uncomment line " + str(lineno()-2) + " and comment lines " + str(lineno()-1) + "-" + str(lineno()) + "."
    print "Google Voice #: (" + glogin[2][:3] + ") " + glogin[2][3:6] + "-" + glogin[2][-4:]
    print
    print "API Keys"
    print "bit.ly: " + str(apikeys[0]) + "/" + str(apikeys[1])
    print "Wunderground: " + str(apikeys[2])
    print
    print "Other Statistics"
    print "Commit: " + statsvar[0]
    raw_input("Press Enter to quit...")
    sys.exit()