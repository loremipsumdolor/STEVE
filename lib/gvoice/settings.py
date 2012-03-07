LOGIN = 'https://accounts.google.com/ServiceLoginAuth?service=grandcentral'
FEEDS = ('inbox', 'starred', 'all', 'spam', 'trash', 'voicemail', 'sms',
        'recorded', 'placed', 'received', 'missed')

BASE = 'https://www.google.com/voice/'
LOGOUT = BASE + 'account/signout'
INBOX = BASE + '#inbox'
DELETE = BASE + 'inbox/deleteMessages/'
MARK = BASE + 'inbox/mark/'
SMS = BASE + 'sms/send/'

XML_RECENT = BASE + 'inbox/recent/'
XML_SMS = XML_RECENT + 'sms/'