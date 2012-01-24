'''
S.T.E.V.E. Email Parser
Parses Email messages for commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import email
import parsers.cmdparser as cmdparser
import parsers.searchparser as searchparser
import parsers.apiparser as apiparser

def parse(data):
    var = []
    body = email.message_from_string(data)
    payload = body.get_payload()
    if type(payload) is not str:
        parsedmsg = payload[0].get_payload()
    fromemail = body["Return-Path"].strip("<>")
    if parsedmsg.find("steve picture") != -1:
        cmdparser.picture()
        var.append("attach")
        var.append("image.jpg")
        var.append(fromemail)
        return var
    elif parsedmsg.find("steve shutdown") != -1:
        cmdparser.shutdown()
    elif parsedmsg.find("steve restart") != -1:
        cmdparser.restart()
    elif parsedmsg.find("steve g") != -1:
        term = parsedmsg.split(" ")
        search = searchparser.g(term[2])
        var.append("text")
        var.append(" ".join(search))
        var.append(fromemail)
        return var
    elif parsedmsg.find("steve shorten") != -1:
        term = parsedmsg.split(" ")
        url = apiparser.shorten(term[2])
        var.append("text")
        var.append(url)
        var.append(fromemail)
        return var
    else:
        return "None"

if __name__ == '__main__':
    print "Not to be called directly."