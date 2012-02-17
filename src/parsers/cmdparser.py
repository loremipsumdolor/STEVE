'''
S.T.E.V.E. Command Parser
Builtin S.T.E.V.E. commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import os

def picture():
    from cv import CaptureFromCAM, QueryFrame, SaveImage
    capture = CaptureFromCAM(0)
    frame = QueryFrame(capture)
    SaveImage('image.jpg', frame)

def whoareyou(caller):
    if caller == "console":
        print "                          hhhhhhh     hhhhhhhhhh     hhhhhhhh                               "
        print "                        hh       hhhhhh         hhhhhh       hh                             "
        print "                       hhh       hhhh             hhh        hh                             "
        print "                       hhh       hhh               hhh       hh                             "
        print "                        hh     hh      hh     hh     hhh     hh                             "
        print "                          hhhhhhh      MN     MN     hhhhhhhh                               "
        print "                               hh      MN     MN     hhh                                    "
        print "                              h                        h                                    "
        print "                            hhh                         hhh                                 "
        print "                          hh                              hhh                               "
        print "                          hh                              hhh                               "
        print "                          hh                              hhh                               "
        print "                          hh           mmmmmmmmmh         hhh                               "
        print "                            hh         mmmmmmmmmh       hhh                                 "
        print "                             hh                         hh                                  "
        print "                               hhhhh               hhhhh                                    "
        print "                                    hhhhhhhhhhhhhhh                                         "
        print
        print
        print
        print "              ooooooo     oooooos     ooooooo      oos ooo      oooooos                     "
        print "              oos          soos       ooo          oos ooo      oos                         "
        print "              ooossss       oo        ooossss      oos ooo      oossss                      "
        print "                  soo       oo        ooo          oos ooo      oos                         "
        print "              ssssooo ss    oo    ss  ooossss  ss  oossooo ss   oosssss  ss                 "
        print
        print "I am S.T.E.V.E. This stands for Super Traversing Enigmatic Voice-controlled Engine."
        print "Most of my coding was written by Jacob Turner, the guy behind Squared Pi"
        print "Productions. However, there's parts of me written by other people, but all of my"
        print "code is open source, so no worries there."
    else:
        return "I am S.T.E.V.E. This stands for Super Traversing Enigmatic Voice-controlled Engine. Most of my coding was written by Jacob Turner, the guy behind Squared Pi Productions. However, there's parts of me written by other people, but all of my code is open source, so no worries there."

def shutdown():
    os = os.name()
    if os == 'nt':
        from win32api import InitiateSystemShutdown
        InitiateSystemShutdown()
    elif os == 'linux':
        os.system('shutdown -h now')

def restart():
    os = os.name()
    if os == 'nt':
        from win32api import InitiateSystemShutdown
        InitiateSystemShutdown(None, None, 0, True, True)
    elif os == 'linux':
        os.system('restart now')

if __name__ == '__main__':
    print "Not to be called directly."