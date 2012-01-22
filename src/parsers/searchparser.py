'''
S.T.E.V.E. Search Parser
It's like cmdparser.py but for your searches
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

from lib.google.search import GoogleSearch, SearchError

def g(term):
    try:
        gs = GoogleSearch(term)
        gs.results_per_page = 1
        results = gs.get_results()
        var = []
        for res in results:
            var.append(res.title.encode("utf8"))
            var.append(res.desc.encode("utf8"))
            var.append(res.url.encode("utf8"))
        return var 
    except SearchError, e:
        return "Search failed: %s" % e