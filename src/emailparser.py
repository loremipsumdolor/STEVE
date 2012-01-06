'''
S.T.E.V.E. Email Parser
Parses Email messages for commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import email, cmdparser

def parse(data):
    var = []
    body = email.message_from_string(data)
    payload = body.get_payload()
    parsedmsg = payload[0].get_payload()
    fromemail = body["Return-Path"].strip("<>")
    check = parsedmsg.find("steve picture")
    if check != -1:
        cmdparser.picture()
        var.append("image.jpg")
        var.append(fromemail)
        return var
    else:
        return "None"

if __name__ == '__main__':
    print "Not to be called directly."