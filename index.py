'''
S.T.E.V.E. Main Core
index.py, because I'm used to web design
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
'''

import config
import check
import console
import plgverify
import os
import sys
import update

print "S.T.E.V.E."

ucheck = update.updatecheck()
settings = config.settingsvar()
if ucheck == "Update":
    print
    print "An update is available!"
    if settings[0] == True:
        print "The update will be applied on exit."
        print
        update = True
    else:
        print "You will be asked to update on exit."
        print
        update = True
else:
    update = False

emailbg = check.emailcheck()
emailbg.daemon = True
emailbg.start()
print "E-mail service started!"
txtbg = check.txtcheck()
txtbg.daemon = True
txtbg.start()
print "Text service started!"
plgverify = plgverify.plgverify()
print "Plugins have been verified!"
consolebg = console.console()
print "All systems are go!"
consolebg.run()
if update == True and settings[0] == True:
    os.spawnl(os.P_NOWAIT, "python.exe update.py")
    sys.exit()
if update == True and settings[0] == False:
    upyn = raw_input("Would you like to update? (Yes/no)")
    if upyn == "Yes" or "Y":
        os.spawnl(os.P_NOWAIT, "python.exe update.py")
        sys.exit()
    else:
        sys.exit()
elif update == False:
    sys.exit()