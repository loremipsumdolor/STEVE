'''
S.T.E.V.E. Built-in Commands Parser
Parses messages for the builtin commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
'''

import config
import platform
import urllib2
import os
import addlparser
import interfaces.txtmod as txtmod
from getpass import getuser
from win32api import InitiateSystemShutdown
from cv import CaptureFromCAM, QueryFrame, SaveImage

class msgparse():
    def __init__(self):
        self.stats = config.statsvar()

    def interpret(self, data, format):
        if format == "email" or format == "txt" or format == "console":
            var = []
            var.append(data)
            var.append(format)
            return var
        else:
            return "Error: Input not in understandable format."

    def parse(self, data, sender, format):
        var = []
        if data.find("steve info") != -1 or data == "info":
            pllist = []
            with open("aplist.txt") as f:
                for line in f:
                    pllist.append(line.rstrip('\n')[:-3])
            if format == "email":
                var.extend(["text", sender, "S.T.E.V.E. Info", "S.T.E.V.E is running version %s." % self.stats[0]])
            if format == "txt":
                var.extend([sender, "S.T.E.V.E version %s" % self.stats[0]])
            if format == "console":
                ghurl = urllib2.urlopen("https://api.github.com/")
                var.append("S.T.E.V.E Info")
                var.append("--------------")
                var.append("Revision Number: %s" % self.stats[0])
                var.append("Operating System: %s %s" %
                           (platform.system(), platform.release()))
                var.append("Network Name: %s" % platform.node())
                var.append("GitHub Requests Remaining: %s/%s" %
                           (str(ghurl.headers['X-RateLimit-Remaining']),
                            str(ghurl.headers['X-RateLimit-Limit'])))
                var.append("Plugins: %s" % str(pllist).strip("[]"))
                ghurl.close()
            return var
        elif data.find("steve picture") != -1 or data == "picture":
            capture = CaptureFromCAM(0)
            frame = QueryFrame(capture)
            SaveImage('image.jpg', frame)
            if format == "email":
                var.extend(["attach", sender, None,
                            "Image taken successfully.", "image.jpg"])
                return var
            elif format == "txt":
                var.extend([sender, "Image taken successfully."])
                return var
            elif format == "console":
                return "Image taken successfully."
        elif data.find("steve whoareyou") != -1 or data == "whoareyou":
            if format == "email":
                var.extend(["text", sender, None])
                var.append("I am S.T.E.V.E. This stands for Super Traversing \
                Enigmatic Voice-controlled Engine. Most of my coding was \
                written by Jacob Turner. However, there's parts of me written \
                by other people, but all of my code is open source, so no \
                worries there.")
            elif format == "txt":
                var.append(sender)
                var.append("I am S.T.E.V.E. This stands for Super Traversing \
                Enigmatic Voice-controlled Engine.")
            elif format == "console":
                var = []
                var.append("                     hhhhhhh     hhhhhhhhhh     hhhhhhhh                          ")
                var.append("                   hh       hhhhhh         hhhhhh       hh                        ")
                var.append("                  hhh       hhhh             hhh        hh                        ")
                var.append("                  hhh       hhh               hhh       hh                        ")
                var.append("                   hh     hh      hh     hh     hhh     hh                        ")
                var.append("                     hhhhhhh      MN     MN     hhhhhhhh                          ")
                var.append("                          hh      MN     MN     hhh                               ")
                var.append("                         h                        h                               ")
                var.append("                       hhh                         hhh                            ")
                var.append("                     hh                              hhh                          ")
                var.append("                     hh                              hhh                          ")
                var.append("                     hh                              hhh                          ")
                var.append("                     hh           mmmmmmmmmh         hhh                          ")
                var.append("                       hh         mmmmmmmmmh       hhh                            ")
                var.append("                        hh                         hh                             ")
                var.append("                          hhhhh               hhhhh                               ")
                var.append("                               hhhhhhhhhhhhhhh                                    ")
                var.append("")
                var.append("")
                var.append("")
                var.append("         ooooooo     oooooos     ooooooo      oos ooo      oooooos                ")
                var.append("         oos          soos       ooo          oos ooo      oos                    ")
                var.append("         ooossss       oo        ooossss      oos ooo      oossss                 ")
                var.append("             soo       oo        ooo          oos ooo      oos                    ")
                var.append("         ssssooo ss    oo    ss  ooossss  ss  oossooo ss   oosssss  ss            ")
                var.append("")
                var.append("I am S.T.E.V.E. This stands for Super Traversing Enigmatic Voice-controlled Engine.")
                var.append("Most of my coding was written by Jacob Turner. However, there's parts of me written")
                var.append("by other people, but all of my code is open source, so no worries there.")
            return var
        elif data.find("steve whoami") != -1 or data.find("whoami") != -1:
            if format == "email":
                var.extend(["text", sender, None, "Your name is probably %s. If you did not already know this, then that is a problem." % getuser()])
            elif format == "txt":
                var.extend([sender, "Your name is probably %s. If you did not already know this, then that is a problem." % getuser()])
            elif format == "console":
                var.extend(["Your name is probably %s. If you did not already know this, then that is a problem." % getuser()])
            return var
        elif data.find("steve shutdown") != -1 or data == "shutdown":
            if os.name() == 'nt':
                InitiateSystemShutdown()
            elif os.name() == 'linux':
                os.system('shutdown -h now')
        elif data.find("steve restart") != -1 or data == "restart":
            if os.name() == 'nt':
                InitiateSystemShutdown(None, None, 0, True, True)
            elif os.name() == 'linux':
                os.system('restart now')
        elif data.find("steve text") != -1 or data == "text":
            self.data = data.lstrip("text ")
            self.num = data.split(" ")[0]
            if format == "email":
                var.extend(["text", sender, None, "You can send your own \
                email-to-text to them."])
            elif format == "txt":
                var.extend([sender, "You have a phone, send your own text!"])
            elif format == "console":
                if len(self.data) > 160:
                    txt = [''.join(x) for x in zip(*[list(self.data[z::160])
                                                     for z in range(160)])]
                    for x in txt:
                        txtmod.send(txt[x], self.num)
                else:
                    txtmod.send(self.data, self.num)
                return "Message sent."
            return var
        else:
            parse = addlparser.parse(data, sender, format)
            return parse

if __name__ == '__main__':
    print "Not to be called directly."