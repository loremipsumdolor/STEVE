'''
S.T.E.V.E. Email Module
Part of the S.T.E.V.E Core
Parses Email messages for commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import imaplib, mailer

def check(ea, pw, imap):
    acct = imaplib.IMAP4_SSL(imap)
    acct.login(ea, pw)
    acct.select()
    data = acct.search(None, 'UNSEEN')
    acct.close()
    acct.logout()
    if data != ('OK', ['']):
        return 'OK'
    else:
        return 'None'
    
def retrieve(ea, pw, imap):
    acct = imaplib.IMAP4_SSL(imap)
    acct.login(ea, pw)
    acct.select()
    typ, data = acct.search(None, 'UNSEEN')
    c = []
    for num in data[0].split():
        typ, data = acct.fetch(num, '(RFC822)')
        a = num, data[0][1]
        b = a[1].find('steve')
        if b != -1:
            print a[1]
            c.append(a[1])
        else:
            acct.store(num, '-FLAGS', '\\Seen')
    return c

def send(ea, pw, toea, smtp, subject, body, attach):
    msg = mailer.Message()
    msg.From = ea
    msg.To = toea
    if subject != None:
        msg.Subject = subject
    if body != None:
        msg.Body = body
    if attach != None:
        msg.attach(attach)
    mail = mailer.Mailer(smtp)
    mail.login(ea, pw)
    mail.send(msg)
       
if __name__ == '__main__':
    print "Not to be called directly."