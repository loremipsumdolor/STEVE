'''
S.T.E.V.E. Main Core
index.py, because I'm used to web design
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import config, update, check

print "S.T.E.V.E."

ucheck = update.check()
if ucheck == 'Update':
    print
    print "There is an update available for S.T.E.V.E.!"
    print "Please go to http://bit.ly/steveupdate for"
    print "more details."

login = config.basicvar()
emailbg = check.emailcheck(login)
emailbg.start()
print "E-mail service started!"
txtbg = check.txtcheck()
txtbg.start()
print "Text service started!"
consolebg = check.console()
print "All systems are go!"
consolebg.start()