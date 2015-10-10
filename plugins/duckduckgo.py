'''
DuckDuckGo plugin for S.T.E.V.E.
Code by Jacob Turner; released under the MIT license
'''

'''
        elif data.find("steve search") != -1 or data.find("search") != -1:
            term = data.split(" ")
            if format == "email" or format == "text":
                result = duckduckgo.ddg(term[2])
            else:
                result = duckduckgo.ddg(term[1])
            if format == "email":
                var.append("text")
                var.append(sender)
                var.append(term[2])
                var.append("%s - %s - %s" % (result["AbstractSource"],
                           result["Definition"], result["AbstractURL"]))
            elif format == "txt":
                var.append(sender)
                var.append("%s - %s - %s" % (result["AbstractSource"],
                           result["Definition"], result["AbstractURL"]))
            elif format == "console":
                var.append("The top result is from: %s" % result["AbstractSource"])
                var.append(result["Definition"])
                var.append(result["AbstractURL"])
            return var
'''

import json
import urllib2

def ddg(term):
    url = 'http://api.duckduckgo.com/?q=%s&format=json' % term
    result = json.load(urllib2.urlopen(url))
    return result