'''
S.T.E.V.E. Command Parser
Builtin S.T.E.V.E. commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

from config import googlevar
from cv import CaptureFromCAM, QueryFrame, SaveImage
from gvoice import GoogleVoiceLogin, TextSender

def picture():
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

def txt(number, txt):
    glogin = googlevar()
    gv_login = GoogleVoiceLogin(glogin[0], glogin[1])
    text_sender = TextSender(gv_login)
    text_sender.text = txt
    text_sender.send_text(number)
    if text_sender.response:
        return "OK"
    else:
        return

if __name__ == '__main__':
    print "Not to be called directly."