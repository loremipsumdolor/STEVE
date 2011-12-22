'''
S.T.E.V.E. Main Core
Part of the S.T.E.V.E Core
index.py, because I'm used to web design
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import emailmod, time, emailparser, config

login = config.configvar()
ea = login[0].strip("'")
pw = login[1].strip("'")
fbea = login[2].strip("'")
imap = login[3].strip("'")
smtp = login[4].strip("'")

#Main loop
while True:
    check = emailmod.check(ea, pw, imap)
    if check == 'OK':
        data = emailmod.retrieve(ea, pw, imap)
        if data != None:
            init = emailparser.init(data)
        else:
            time.sleep(10)
    elif check == 'None':
        time.sleep(10)
