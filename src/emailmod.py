'''
S.T.E.V.E. Email Module
The primary Email message exchange
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import imaplib, smtplib, os.path, ssl, config
from string import join
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email import Encoders

def retrieve(ea, pw, imap):
    try:
        acct = imaplib.IMAP4_SSL(imap)
    except ssl.SSLError:
        acct = imaplib.IMAP4(imap)
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

def send(toea, subject, text):
    login = config.basicvar()
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
    try:
        mail = smtplib.SMTP_SSL(login[4])
    except ssl.SSLError:
        mail = smtplib.SMTP(login[4])
    mail.login(login[0], login[1])
    mail.sendmail(login[0], toea, body)
    mail.quit()

def sendattach(toea, subject, text, f):
    login = config.basicvar()
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
    try:
        mail = smtplib.SMTP_SSL(login[4])
    except ssl.SSLError:
        mail = smtplib.SMTP(login[4])
    mail.login(login[0], login[1])
    mail.sendmail(login[0], toea, msg.as_string())
    mail.close()

if __name__ == '__main__':
    print "Not to be called directly."