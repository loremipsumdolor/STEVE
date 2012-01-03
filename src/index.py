'''
S.T.E.V.E. Main Core
index.py, because I'm used to web design
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import emailmod, time, emailparser, config

print "S.T.E.V.E."
login = config.configvar()
ea = login[0]
pw = login[1]
imap = login[2]
smtp = login[4]
if login[3] == True:
    print
    print "WARNING: IMAP server assumed to be " + login[2] + "."
    print "If this is incorrect, please stop S.T.E.V.E. and change the"
    print "value 'smtpserver'."
if login[5] == True:
    print
    print "WARNING: SMTP server assumed to be " + login[4] + "."
    print "If this is incorrect, please stop S.T.E.V.E. and change the"
    print "value 'smtpserver'."
#Main loop
while True:
    data = emailmod.retrieve(ea, pw, imap)
    if data != None:
        parse = emailparser.parse(data)
        if parse[0] == "image.jpg":
            emailmod.sendattach(parse[1], None, None, parse[0])
        else:
            time.sleep(10)
    else:
        time.sleep(10)