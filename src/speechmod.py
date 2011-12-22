'''
S.T.E.V.E. Speech Module
Interface to Windows Speech SDK
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''
import speechlib, time

speechlib.say("Welcome to the STEVE Interface Engine Voice Module")
time.sleep(3)
'''
Calendar events
'''
speechlib.say("Please say a command, or say help for a list of commands")
#speechlib.say("You said %s" % input)
while True:
    speechlib.say("Please say a command")
    spk = speechlib.input()
    if spk == "help":
        speechlib.say("There are a number of commands the STEVE Interface Engine Voice Module understands")
        time.sleep(1)
        speechlib.say("Note that these commands are not permanent, and may change")
        time.sleep(1)
        speechlib.say("help - this list of commands")
        time.sleep(1)
        speechlib.say("check port - will test for a connection between the computer and the Internet on a specific port")
        time.sleep(1)
        speechlib.say("start minecraft - starts the local minecraft server")
        time.sleep(1)
        speechlib.say("Note that these commands are not permanent, and may change")
        time.sleep(1)
    if input == "turn off":
        pass
    
if __name__ == '__main__':
    print "Not to be called directly."