'''
S.T.E.V.E. Email Module
The primary Email message exchange
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
'''

import imaplib
import smtplib
from os.path import basename
from ssl import SSLError
from config import basicvar
from string import join
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email import Encoders, message_from_string

def retrieve():
    login = basicvar()
    if login[2] != False:
        try: acct = imaplib.IMAP4_SSL(login[2])
        except SSLError: acct = imaplib.IMAP4(login[2])
    else:
        try: acct = imaplib.IMAP4_SSL(login[3])
        except SSLError: acct = imaplib.IMAP4(login[3])
    acct.login(login[0], login[1])
    acct.select()
    typ, data = acct.search(None, 'UNSEEN')
    data = str(data).strip("'[]").split(" ")
    msgs = []
    if data != ['']:
        for x in range(len(data)):
            typ, msg = acct.fetch(data[x], '(RFC822)')
            a = message_from_string(msg[0][1])
            b = a["Return-Path"].strip("<>")
            a = a.get_payload()
            if type(a) is not str:
                a = a[0].get_payload()
            if a.find('steve') != -1:
                msgs.append((a, b))
                acct.store(data[x], '+FLAGS', '\\Seen')
            else:
                pass
        acct.close()
        acct.logout()
        return msgs
    else:
        acct.close()
        acct.logout()
        return msgs

def send(toea, subject, text):
    login = basicvar()
    if subject != None: pass
    if text != None: pass
    body = join((
        "From: %s" % login[0],
        "To: %s" % toea,
        "Subject: %s" % subject ,
        "",
        text
        ), "\r\n")
    if login[4] != False:
        try:
            mail = smtplib.SMTP_SSL(login[4])
        except SSLError:
            mail = smtplib.SMTP(login[4])
    else:
        try:
            mail = smtplib.SMTP_SSL(login[5])
        except SSLError:
            mail = smtplib.SMTP(login[5])       
    mail.login(login[0], login[1])
    mail.sendmail(login[0], toea, body)
    mail.quit()

def sendattach(toea, subject, text, f):
    login = basicvar()
    msg = MIMEMultipart()
    msg['From'] = login[0]
    msg['To'] = toea
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach( MIMEText(text) )
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(f,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="%s"' % basename(f))
    msg.attach(part)
    if login[4] != False:
        try:
            mail = smtplib.SMTP_SSL(login[4])
        except SSLError:
            mail = smtplib.SMTP(login[4])
    else:
        try:
            mail = smtplib.SMTP_SSL(login[5])
        except SSLError:
            mail = smtplib.SMTP(login[5]) 
    mail.login(login[0], login[1])
    mail.sendmail(login[0], toea, msg.as_string())
    mail.close()

if __name__ == '__main__':
    print "Not to be called directly."