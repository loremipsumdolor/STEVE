'''
S.T.E.V.E. Updater
Keeps the code current
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
'''

import urllib
import json
import config

def currentcommit():
    clist = urllib.urlopen("https://api.github.com/repos/loremipsumdolor/S.T.E.V.E./commits")
    j = json.load(clist)
    return j[00]['sha']

def update():
    print "Updating S.T.E.V.E. to %s..." % currentcommit()
    stats = config.statsvar()
    clist = urllib.urlopen("https://api.github.com/repos/loremipsumdolor/S.T.E.V.E./commits")
    jclist = json.load(clist)
    for x in jclist:
        if jclist[x]['sha'] == stats[0]:
            commitsnum = x
            break
        else:
            pass
    for x in range(commitsnum):
        commit = urllib.urlopen("https://api.github.com/repos/loremipsumdolor/S.T.E.V.E./commits/", ccommit)
        jcommit = json.load(commit)
        for x in jcommit:
            urllib.urlretrieve(jcommit[x]["raw_url"], jcommit[x]["filename"])
    config.changecommit(jclist[00]['sha'])

def updatecheck():
    stats = config.statsvar()
    ccommit = currentcommit()
    if stats[0] != ccommit:
        return "Update"
    else:
        return

if __name__ == '__main__':
    stats = config.statsvar()
    ccommit = currentcommit()
    print "The current commit is " + ccommit + "."
    if stats[0] != ccommit:
        print "A new version of S.T.E.V.E. is available!"
        print "This revision: " + stats[0]
        print "Current revision: " + ccommit
        yn = raw_input("Update? (Yes/no) > ")
        if yn == "yes" or "Yes" or "":
            update()
            raw_input("Successfully updated!")
        else:
            pass
    else:
        raw_input("You are already using the most current version.")