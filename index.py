'''
S.T.E.V.E. Main Core
index.py, because I'm used to web design
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import config, check, console, sys, update, os

print "S.T.E.V.E."

ucheck = update.updatecheck()
if ucheck == "Update":
    update = True
else:
    update = False

login = config.basicvar()
emailbg = check.emailcheck(login)
emailbg.daemon = True
emailbg.start()
print "E-mail service started!"
txtbg = check.txtcheck()
txtbg.daemon = True
txtbg.start()
print "Text service started!"
try:
    consolebg = console.console()
    print "All systems are go!"
    consolebg.start()
except SystemExit:
    if update == True:
        os.spawnlp(os.P_NOWAIT, "python.exe", "update.py")
        sys.exit()
    elif update == False:
        sys.exit()