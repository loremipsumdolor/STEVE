'''
S.T.E.V.E. Configuration File Parser
For that config.ini file
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
Based on http://stackoverflow.com/a/3446232 by Zimm3r
'''

import os.path
import sys
import inspect
import update
from messages import errors
from ConfigParser import RawConfigParser, Error

def testconfig():
    parser = RawConfigParser()
    fileopen = open("config.ini")
    if fileopen.read().startswith("\xfe\xff\x00"):
        raise errors.ConfigUni()
    try:
        results = parser.read("config.ini")
    except Error, msg:
        print msg
        raise errors.CantParseConfig()
    else:
        if results == []:
            print "Error: Could not load config.ini."
            if not os.path.exists("config.ini"):
                configlist = ["[Basic]", "emailaddress = test@example.com",
                              "password = password", "smtpserver =",
                              "imapserver =", "[Google]",
                              "gusername = test@gmail.com",
                              "gpassword = gpassword",
                              "gvoicenum = 5555551234",
                              "[Settings]", "autoupdate = False",
                              "#DO NOT EDIT BEYOND THIS LINE", "[Stats]",
                              "commit ="]
                with open("config.ini", "w") as config:
                    for x in configlist:
                        config.write(x)
                print "Reason: config.ini did not exist."
                raise errors.NewConfig()
            else:
                raise errors.Unknown()
        else:
            return

def testotherconfig(conf):
    parser = RawConfigParser()
    fileopen = open("plugins/%s" % conf)
    if fileopen.read().startswith("\xfe\xff\x00"):
        raise errors.ConfigUni()
    try:
        results = parser.read("plugins/%s" % conf)
    except Error, msg:
        print msg
        raise errors.CantParseConfig()
    else:
        if results == []:
            print "Error: Could not load %s." % conf
            if not os.path.exists("plugins/%s" % conf):
                raise errors.FileNotFound()
            else:
                raise errors.Unknown()
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
            raise errors.DefaultValue("emailaddress")
        else:
            login.append(parser.get(sections[0], "emailaddress"))
    else:
        raise errors.ValueNotFound("emailaddress")
    if parser.has_option(sections[0], "password"):
        if parser.get(sections[0], "password") == 'password':
            raise errors.DefaultValue("password")
        else:
            login.append(parser.get(sections[0], "password"))
    else:
        raise errors.ValueNotFound("password")
    if parser.has_option(sections[0], "imapserver"):
        if parser.get(sections[0], "imapserver") == '':
            server = parser.get(sections[0], "emailaddress").split("@")
            login.append('imap.' + server[1].strip("'"))
            login.append(True)
        else:
            login.append(parser.get(sections[0], "imapserver"))
            login.append(False)
    else:
        raise errors.ValueNotFound("imapserver")
    if parser.has_option(sections[0], "smtpserver"):
        if parser.get(sections[0], "smtpserver") == '':
            server = parser.get(sections[0], "emailaddress").split("@")
            login.append('smtp.' + server[1].strip("'"))
            login.append(True)
        else:
            login.append(parser.get(sections[0], "smtpserver"))
            login.append(False)
    else:
        raise errors.ValueNotFound("smtpserver")
    return login

def googlevar():
    testconfig()
    parser = RawConfigParser()
    results = parser.read("config.ini")
    sections = parser.sections()
    glogin = []
    if parser.has_option(sections[1], "gusername"):
        if parser.get(sections[1], "gusername") == 'test@gmail.com':
            raise errors.DefaultValue("gusername")
        else:
            glogin.append(parser.get(sections[1], "gusername"))
    else:
        raise errors.ValueNotFound("gusername")

    if parser.has_option(sections[1], "gpassword"):
        if parser.get(sections[1], "gpassword") == 'gpassword':
            raise errors.DefaultValue("gpassword")
        else:
            glogin.append(parser.get(sections[1], "gpassword"))
    else:
        raise errors.ValueNotFound("gpassword")

    if parser.has_option(sections[1], "gvoicenum"):
        if parser.get(sections[1], "gvoicenum") == '5555551234':
            raise errors.DefaultValue("gvoicenum")
        else:
            glogin.append(parser.get(sections[1], "gvoicenum"))
    else:
        raise errors.ValueNotFound("gvoicenum")
    return glogin

def settingsvar():
    testconfig()
    parser = RawConfigParser()
    results = parser.read("config.ini")
    sections = parser.sections()
    settings = []
    if parser.has_option(sections[2], "autoupdate"):
        settings.append(parser.getboolean(sections[2], "autoupdate"))
    return settings

def statsvar():
    testconfig()
    parser = RawConfigParser()
    results = parser.read("config.ini")
    sections = parser.sections()
    statsvar = []
    if parser.has_option(sections[3], "commit"):
        if parser.get(sections[3], "commit") == '':
            parser.set(sections[3], "commit", update.currentcommit())
            print "WARNING: Most recent commit was assumed for value 'commit'."
            print "This can be ignored if this the first run. If not, please"
            print "download the newest version as soon as possible."
        else:
            statsvar.append(parser.get(sections[3], "commit"))
    else:
        raise errors.ValueNotFound("commit")
    return statsvar

def othersvar(conf, values):
    testotherconfig(conf)
    parser = RawConfigParser()
    results = parser.read("plugins/%s" % conf)
    sections = parser.sections()
    othersvar = []
    for x in range(len(values)):
        if parser.has_option(sections[0], values[x]):
            if parser.get(sections[0], values[x]) == '':
                othersvar.append(None)
            else:
                othersvar.append(parser.get(sections[0], values[x]))
        else:
            raise errors.ValueNotFound(values[x])
    return othersvar

def changecommit(ccommit):
    testconfig()
    parser = RawConfigParser()
    results = parser.read("config.ini")
    sections = parser.sections()
    parser.set(sections[3], "commit", ccommit)
    return

def lineno():
    return inspect.currentframe().f_back.f_lineno

if __name__ == '__main__':
    login = basicvar()
    glogin = googlevar()
    stats = statsvar()
    print "S.T.E.V.E. Configuration Values"
    print
    print "Basic Configuration Values"
    print "Email Address: " + login[0]
    #print "Password: " + login[1]
    print "Password: Not displayed for security reasons."
    print "To display password, uncomment line %s" % str(lineno()-2)
    print "and comment lines %s-%s." % (str(lineno()-1), str(lineno()))
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
    print "To display password, uncomment line %s" % str(lineno()-2)
    print "and comment lines %s-%s." % (str(lineno()-1), str(lineno()))
    print "Google Voice #: (%s) %s-%s" % (glogin[2][:3], glogin[2][3:6],
    glogin[2][-4:])
    print
    print "Other Statistics"
    print "Commit: " + stats[0]
    raw_input("Press Enter to quit...")
    sys.exit()