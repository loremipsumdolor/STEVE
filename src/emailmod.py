'''
S.T.E.V.E. Email Module
The primary Email message exchange
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import imaplib, mailer

def retrieve(ea, pw, imap):
    acct = imaplib.IMAP4_SSL(imap)
    acct.login(ea, pw)
    acct.select()
    typ, data = acct.search(None, 'UNSEEN')
    if data != ['']:
        typ, msg = acct.fetch(data[0], '(RFC822)')
        a = data[0], msg[0][1]
        b = a[1].find('steve')
        if b != -1:
            acct.close()
            acct.logout()
            return a[1]
        else:
            acct.store(data[0], '+FLAGS', '\\Seen')
            acct.close()
            acct.logout()
            return None
    else:
        acct.close()
        acct.logout()
        return None

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