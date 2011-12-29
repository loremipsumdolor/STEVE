'''
S.T.E.V.E. Main Core
index.py, because I'm used to web design
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import emailmod, time, emailparser, config

login = config.configvar()
ea = login[0]
pw = login[1]
imap = login[2]
smtp = login[3]

#Main loop
while True:
    data = emailmod.retrieve(ea, pw, imap)
    if data != None:
        emailparser.parse(data)
    else:
        time.sleep(10)