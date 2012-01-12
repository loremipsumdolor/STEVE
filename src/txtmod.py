'''
S.T.E.V.E. Texting Module
The primary text message exchange
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import lib.BeautifulSoup as BeautifulSoup
from config import googlevar
from lib.gvoice import Voice
from lib.gvoice.util import input, Message

def retrieve():
    glogin = googlevar()
    voice = Voice()
    voice.login(glogin[0], glogin[1])
    voice.sms()
    msgitems = []
    tree = BeautifulSoup.BeautifulSoup(voice.sms.html)
    conversations = tree.findAll("div",attrs={"id" : True},recursive=False)
    for conversation in conversations :
        rows = conversation.findAll(attrs={"class" : "gc-message-sms-row"})
        for row in rows :
            msgitem = {"id" : conversation["id"]}
            spans = row.findAll("span",attrs={"class" : True}, recursive=False)
            for span in spans :
                cl = span["class"].replace('gc-message-sms-', '')
                msgitem[cl] = (" ".join(span.findAll(text=True))).strip()
            msgitems.append(msgitem)
    val = []
    for x in range(len(msgitems)):
        msg = msgitems[x].values()
        if msg[0].find('steve') != -1:
            val.append(msg[0])
            val.append(msg[1].strip(":+"))
        else:
            pass
    e = voice.sms().messages
    for message in voice.sms().messages:
        message.delete()
    return val

def send(number, txt):
    glogin = googlevar()
    voice = Voice()
    voice.login(glogin[0], glogin[1])
    voice.send_sms(number, txt)
    return "OK"

if __name__ == '__main__':
    print "Not to be called directly."