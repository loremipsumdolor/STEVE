'''
S.T.E.V.E. API Command Parser
For commands that require API keys
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import urllib2, config

def getkeys():
    return config.apivar()

def shorten(url):
    apikeys = getkeys()
    if apikeys[0] == None:
        return "Error: Cannot complete function due to missing username/API key for bit.ly."
    else:
        url = url.replace(":", "%3A").replace("/", "%2F")
        short = urllib2.urlopen("https://api-ssl.bitly.com/v3/shorten?login=" + apikeys[0] + "&apiKey=" + apikeys[1] + "&longUrl=" + url + "&format=txt")
        con = short.read()
        short.close()
        return con.rstrip("\n")

if __name__ == '__main__':
    print "Not to be called directly."