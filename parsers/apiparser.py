'''
S.T.E.V.E. API Command Parser
For commands that depend on APIs/websites
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import urllib2, config, json, decimal

def shorten(url):
    apikeys = config.apivar()
    if apikeys[0] or apikeys[1] == None:
        return "Error: Cannot complete function due to missing username/API key for bit.ly."
    else:
        url = url.replace(":", "%3A").replace("/", "%2F")
        short = urllib2.urlopen("https://api-ssl.bitly.com/v3/shorten?login=" + apikeys[0] + "&apiKey=" + apikeys[1] + "&longUrl=" + url + "&format=txt")
        con = short.read()
        short.close()
        return con.rstrip("\n")

def ghproj(proj, user):
    var = []
    try:
        infourl = urllib2.urlopen("https://api.github.com/repos/" + user + "/" + proj)
    except:
        return "Error: Invalid project name or username."
    j = json.load(infourl)
    var.append(proj.capitalize() + " by " + user) #Name and user
    var.append(j["description"]) #Description
    var.append(j["homepage"]) #Homepage
    var.append("Created on: " + j["created_at"].split("T")[0]) #Create date
    var.append("Written in: " + j["language"]) #Language
    var.append(str(j["watchers"]) + " watchers") #Watchers
    var.append(str(j["forks"]) + " forks") #Forks
    return var

def ghuser(user):
    var = []
    try:
        infourl = urllib2.urlopen("https://api.github.com/users/" + user)
    except:
        return "Error: Invalid username."
    j = json.load(infourl)
    var.append(user + " (" + str(j["name"]) + ")") #Username (Name)
    var.append("Email: " + j["email"]) #Email
    var.append("Website/Blog: " + j["blog"]) #Website
    var.append("Location: " + j["location"]) #Location
    var.append("Registered on: " + j["created_at"].split("T")[0]) #Create date
    var.append(str(j["public_repos"]) + " public repositories") #Repos
    var.append(str(j["followers"]) + " followers") #Followers
    return var

def weather(city, state):
    apikeys = config.apivar()
    if apikeys[2] == None:
        return "Error: Cannot complete function due to missing API key for Wunderground."
    var = []
    wurl = urllib2.urlopen("http://api.wunderground.com/api/" + apikeys[2] + "/geolookup/conditions/forecast/q/" + state + "/" + city + ".json")
    j = json.load(wurl)
    var.append(city.capitalize() + ", " + state.capitalize())
    var.append("Current Conditions: " + j["current_observation"]["weather"])
    var.append("Temperature: " + j["current_observation"]["temperature_string"])
    var.append("Humidity: " + j["current_observation"]["relative_humidity"])
    var.append("Wind: " + j["current_observation"]["wind_string"])
    var.append("Dewpoint: " + j["current_observation"]["dewpoint_string"])
    return var

def ddg(term):
    var = []
    search_results = urllib2.urlopen('http://api.duckduckgo.com/?q=' + term + '&format=json')
    j = json.load(search_results)
    var.append(j["AbstractSource"])
    var.append(j["Definition"])
    var.append(j["AbstractURL"])
    return var

def currency(num, output):
    var = []
    rates = urllib2.urlopen("https://raw.github.com/currencybot/open-exchange-rates/master/latest.json")
    j = json.load(rates)
    amount = decimal.Decimal(num)*decimal.Decimal(j["rates"][output])
    var.append(j["license"])
    var.append(str(decimal.Decimal(amount).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN)) + " " + output.upper())
    return var

if __name__ == '__main__':
    print "Not to be called directly."