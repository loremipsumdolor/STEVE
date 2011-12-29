'''
S.T.E.V.E. Email Parser
Parses Email messages for commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import email, cmdparser, emailmod

def parse(msg):
    body = email.message_from_string(msg)
    pl = body.get_payload()
    parsedmsg = pl[0].get_payload().split()
    check = parsedmsg.find("steve picture")
    if check != -1:
        cmdparser.picture()