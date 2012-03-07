'''
S.T.E.V.E. Text Message Parser
Parses text messages for commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import parsers.cmdparser as cmdparser
import parsers.apiparser as apiparser

def parse(data):
    var = []
    fromnum = data[1]
    if data[0].find("steve picture") != -1:
        cmdparser.picture()
        var.append("image")
        var.append(fromnum)
        return var
    elif data[0].find("steve shutdown") != -1:
        cmdparser.shutdown()
    elif data[0].find("steve restart") != -1:
        cmdparser.restart()
    elif data[0].find("steve search") != -1:
        term = data[0].split(" ")
        search = apiparser.ddg(term[2])
        var.append("text")
        var.append(" ".join(search))
        var.append(fromnum)
        return var
    elif data[0].find("steve shorten") != -1:
        term = data[0].split(" ")
        url = apiparser.shorten(term[2])
        var.append("text")
        var.append(url)
        var.append(fromnum)
        return var
    else:
        return "None"

if __name__ == '__main__':
    print "Not to be called directly."