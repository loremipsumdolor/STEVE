'''
S.T.E.V.E. Search Parser
It's like cmdparser.py but for your searches
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''
import urllib2, json

def ddg(term):
    var = []
    url = 'http://api.duckduckgo.com/?q=' + term + '&format=json'
    search_results = urllib2.urlopen(url)
    j = json.load(search_results)
    var.append(j["AbstractSource"])
    var.append(j["Definition"])
    var.append(j["AbstractURL"])
    return var