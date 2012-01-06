'''
S.T.E.V.E. Update Module
Updates the program with each commit
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import feedparser, os.path
from time import strftime, localtime

def check():
    feed = feedparser.parse('https://github.com/loremipsumdolor/S.T.E.V.E./commits/master.atom')
    cdate = str(feed.entries[0].updated)
    ccontent = feed.entries[0].content
    ccontent = ccontent[0].value
    clist = ccontent.split('\n')
    if clist[0].strip('<pre> m') == "README":
        check = clist[1].split('/')
        tcheck = strftime("%Y-%m-%dT%H:%M:%S-08:00", localtime(os.path.getmtime(check[1])))
        if cdate != tcheck:
            return 'Update'
        else:
            return
    else:
        check = clist[0].split('/')
        tcheck = strftime("%Y-%m-%dT%H:%M:%S-08:00", localtime(os.path.getmtime(check[1])))
        if cdate != tcheck:
            return 'Update'
        else:
            return

if __name__ == '__main__':
    print check()