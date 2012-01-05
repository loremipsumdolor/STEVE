'''
S.T.E.V.E. Speech Module
Interface to Windows Speech SDK
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import speechlib, time, cmdparser

speechlib.say("Welcome to the STEVE Interface Engine Voice Module")
time.sleep(3)
speechlib.say("Say help for a list of commands")
#speechlib.say("You said %s" % input)
while True:
    speechlib.say("Please say a command.")
    spk = speechlib.input()
    if spk == "help":
        speechhelp = open('speechhelp.txt', 'r')
        for line in speechhelp:
            speechlib.say(line.strip('\n'))
            time.sleep(1)
    elif spk == "who are you":
        speechlib.say(cmdparser.whoareyou("speech"))
    else:
        speechlib.say("That is not a valid command.")