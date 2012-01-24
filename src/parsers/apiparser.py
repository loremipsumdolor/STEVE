'''
S.T.E.V.E. API Command Parser
For commands that require API keys
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import urllib2, config, json

def shorten(url):
    apikeys = config.apivar()
    if apikeys[0] == None:
        return "Error: Cannot complete function due to missing username/API key for bit.ly."
    else:
        url = url.replace(":", "%3A").replace("/", "%2F")
        short = urllib2.urlopen("https://api-ssl.bitly.com/v3/shorten?login=" + apikeys[0] + "&apiKey=" + apikeys[1] + "&longUrl=" + url + "&format=txt")
        con = short.read()
        short.close()
        return con.rstrip("\n")

def github(proj, user):
    i = []
    try:
        infourl = urllib2.urlopen("https://api.github.com/repos/" + user + "/" + proj)
    except:
        return "Error: Invalid project name or username."
    j = json.load(infourl)
    i.append(proj.capitalize() + " by " + user) #Name and user
    i.append(str(j["description"])) #Description
    i.append(str(j["homepage"])) #Homepage
    i.append("Created on: " + str(j["created_at"].split("T")[0])) #Create date
    i.append("Written in: " + str(j["language"])) #Language
    i.append(str(j["watchers"]) + " watchers") #Watchers
    i.append(str(j["forks"]) + " forks") #Forks
    return i

if __name__ == '__main__':
    print "Not to be called directly."