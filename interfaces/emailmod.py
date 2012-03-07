'''
S.T.E.V.E. Email Module
The primary Email message exchange
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import imaplib, smtplib, os.path, ssl
from config import basicvar
from string import join
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email import Encoders

def retrieve():
    login = basicvar()
    if login[2] != False:
        try:
            acct = imaplib.IMAP4_SSL(login[2])
        except ssl.SSLError:
            acct = imaplib.IMAP4(login[2])
    else:
        try:
            acct = imaplib.IMAP4_SSL(login[3])
        except ssl.SSLError:
            acct = imaplib.IMAP4(login[3])
    acct.login(login[0], login[1])
    acct.select()
    typ, data = acct.search(None, 'UNSEEN')
    if data != ['']:
        typ, msg = acct.fetch(data[0], '(RFC822)')
        a = data[0], msg[0][1]
        if a[1].find('steve') != -1:
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

def send(toea, subject, text):
    login = basicvar()
    if subject != None:
        pass
    if text != None:
        pass
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
        except ssl.SSLError:
            mail = smtplib.SMTP(login[4])
    else:
        try:
            mail = smtplib.SMTP_SSL(login[5])
        except ssl.SSLError:
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
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)
    if login[4] != False:
        try:
            mail = smtplib.SMTP_SSL(login[4])
        except ssl.SSLError:
            mail = smtplib.SMTP(login[4])
    else:
        try:
            mail = smtplib.SMTP_SSL(login[5])
        except ssl.SSLError:
            mail = smtplib.SMTP(login[5]) 
    mail.login(login[0], login[1])
    mail.sendmail(login[0], toea, msg.as_string())
    mail.close()

if __name__ == '__main__':
    print "Not to be called directly."