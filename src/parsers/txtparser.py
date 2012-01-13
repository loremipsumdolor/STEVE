'''
S.T.E.V.E. Text Message Parser
Parses text messages for commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import cmdparser

def parse(data):
    var = []
    fromnum = data[1]
    if data[0].find("steve picture") != -1:
        cmdparser.picture()
        var.append("image.jpg")
        var.append(fromnum)
        return var
    elif data[0].find("steve shutdown") != -1:
        cmdparser.shutdown()
    elif data[0].find("steve restart") != -1:
        cmdparser.restart()
    else:
        return "None"

if __name__ == '__main__':
    print "Not to be called directly."