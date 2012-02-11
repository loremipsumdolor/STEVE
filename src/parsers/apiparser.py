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
        bitlyurl = "https://api-ssl.bitly.com/v3/shorten?login=" + apikeys[0] + "&apiKey=" + apikeys[1] + "&longUrl=" + url + "&format=txt"
        short = urllib2.urlopen(bitlyurl)
        con = short.read()
        short.close()
        return con.rstrip("\n")

def ghproj(proj, user):
    i = []
    try:
        infourl = urllib2.urlopen("https://api.github.com/repos/" + user + "/" + proj)
    except:
        return "Error: Invalid project name or username."
    j = json.load(infourl)
    i.append(proj.capitalize() + " by " + user) #Name and user
    i.append(j["description"]) #Description
    i.append(j["homepage"]) #Homepage
    i.append("Created on: " + j["created_at"].split("T")[0]) #Create date
    i.append("Written in: " + j["language"]) #Language
    i.append(str(j["watchers"]) + " watchers") #Watchers
    i.append(str(j["forks"]) + " forks") #Forks
    return i

def ghuser(user):
    i = []
    try:
        infourl = urllib2.urlopen("https://api.github.com/users/" + user)
    except:
        return "Error: Invalid username."
    j = json.load(infourl)
    i.append(user + " (" + str(j["name"]) + ")") #Username (Name)
    i.append("Email: " + j["email"]) #Email
    i.append("Website/Blog: " + j["blog"]) #Website
    i.append("Location: " + j["location"]) #Location
    i.append("Registered on: " + j["created_at"].split("T")[0]) #Create date
    i.append(str(j["public_repos"]) + " public repositories") #Repos
    i.append(str(j["followers"]) + " followers") #Followers
    return i

if __name__ == '__main__':
    print "Not to be called directly."