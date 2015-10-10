'''
bit.ly plugin for S.T.E.V.E.
Code by Jacob Turner; released under the MIT license
'''

'''
        if data.find("steve shorten") != -1 or data.find("shorten") != -1:
            term = data.split(" ")
            if format == "email" or format == "text":
                nurl = bitly.bitly(term[2])
            else:
                nurl = bitly.bitly(term[1])
            if format == "email":
                var.append("text")
                var.append(sender)
                var.append(None)
                var.append(nurl)
            elif format == "txt":
                var.append(sender)
                var.append(nurl)
            elif format == "console":
                return nurl
'''

import urllib2
import config

def bitly(url):
    cfg = config.othersvar("bitly.ini", ["bitlyusername", "bitlykey"])
    if cfg[0] == None or cfg[1] == None:
        return "Error: Cannot complete function due to missing username/API key for bit.ly."
    else:
        url = url.replace(":", "%3A").replace("/", "%2F")
        apiurl = "https://api-ssl.bitly.com/v3/shorten?login=%s&apiKey=%s&longUrl=%s&format=txt" % (cfg[0], cfg[1], url)
        short = urllib2.urlopen(apiurl)
        nurl = short.read().rstrip("\n")
        short.close()
        return nurl