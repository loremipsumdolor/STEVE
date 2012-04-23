'''
S.T.E.V.E. Console
Interactive command-line console
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
'''

import threading
import cmdparser

class console(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.msgparse = cmdparser.msgparse()

    def run(self):
        print
        print "Type help for a list of commands."
        while True:
            con = raw_input("S.T.E.V.E. > ")
            if con == "help":
                with open('consolehelp.txt') as consolehelp:
                    for line in sorted(consolehelp):
                        print line.rstrip('\n')
            elif con == "exit":
                break
            else:
                interpret = self.msgparse.interpret(con, "console")
                parse = self.msgparse.parse(interpret[0], interpret[1], interpret[1])
                if type(parse) is list:
                    for x in range(len(parse)):
                        print parse[x]
                elif type(parse) is str:
                    print parse
                elif type(parse) is int:
                    print str(parse)
                elif interpret[0] == "":
                    pass
                else:
                    print "Error: Invalid results."

if __name__ == '__main__':
    print "Not to be called directly."