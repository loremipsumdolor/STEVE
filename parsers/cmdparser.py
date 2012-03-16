'''
S.T.E.V.E. Command Parser
Any and all commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import urllib2, config, json, decimal, os

class basiccmd():
    def picture(self):
        from cv import CaptureFromCAM, QueryFrame, SaveImage
        capture = CaptureFromCAM(0)
        frame = QueryFrame(capture)
        SaveImage('image.jpg', frame)

    def whoareyou(self, caller):
        if caller == "console":
            print "                     hhhhhhh     hhhhhhhhhh     hhhhhhhh                          "
            print "                   hh       hhhhhh         hhhhhh       hh                        "
            print "                  hhh       hhhh             hhh        hh                        "
            print "                  hhh       hhh               hhh       hh                        "
            print "                   hh     hh      hh     hh     hhh     hh                        "
            print "                     hhhhhhh      MN     MN     hhhhhhhh                          "
            print "                          hh      MN     MN     hhh                               "
            print "                         h                        h                               "
            print "                       hhh                         hhh                            "
            print "                     hh                              hhh                          "
            print "                     hh                              hhh                          "
            print "                     hh                              hhh                          "
            print "                     hh           mmmmmmmmmh         hhh                          "
            print "                       hh         mmmmmmmmmh       hhh                            "
            print "                        hh                         hh                             "
            print "                          hhhhh               hhhhh                               "
            print "                               hhhhhhhhhhhhhhh                                    "
            print
            print
            print
            print "         ooooooo     oooooos     ooooooo      oos ooo      oooooos                "
            print "         oos          soos       ooo          oos ooo      oos                    "
            print "         ooossss       oo        ooossss      oos ooo      oossss                 "
            print "             soo       oo        ooo          oos ooo      oos                    "
            print "         ssssooo ss    oo    ss  ooossss  ss  oossooo ss   oosssss  ss            "
            print
            print "I am S.T.E.V.E. This stands for Super Traversing Enigmatic Voice-controlled Engine."
            print "Most of my coding was written by Jacob Turner, the guy behind Squared Pi"
            print "Productions. However, there's parts of me written by other people, but all of my"
            print "code is open source, so no worries there."
        else:
            return "I am S.T.E.V.E. This stands for Super Traversing Enigmatic Voice-controlled Engine. Most of my coding was written by Jacob Turner, the guy behind Squared Pi Productions. However, there's parts of me written by other people, but all of my code is open source, so no worries there."

    def shutdown(self):
        if os.name() == 'nt':
            from win32api import InitiateSystemShutdown
            InitiateSystemShutdown()
        elif os.name() == 'linux':
            os.system('shutdown -h now')
        else:
            return "Shutdown not possible."

    def restart(self):
        if os.name() == 'nt':
            from win32api import InitiateSystemShutdown
            InitiateSystemShutdown(None, None, 0, True, True)
        elif os.name() == 'linux':
            os.system('restart now')
        else:
            return "Shutdown not possible."

class apicmd():
    def __init__(self):
        self.apikeys = config.apivar()
        self.bitlyusername = self.apikeys[0]
        self.bitlykey = self.apikeys[1]
        self.wunderkey = self.apikeys[2]

    def shorten(self, url):
        if self.bitlyusername or self.bitlykey == None:
            return "Error: Cannot complete function due to missing username/API key for bit.ly."
        else:
            url = url.replace(":", "%3A").replace("/", "%2F")
            short = urllib2.urlopen("https://api-ssl.bitly.com/v3/shorten?login=" + self.bitlyusername + "&apiKey=" + self.bitlykey + "&longUrl=" + url + "&format=txt")
            con = short.read()
            short.close()
            return con.rstrip("\n")

    def ghproj(self, proj, user):
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

    def ghuser(self, user):
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

    def weather(self, city, state):
        var = []
        wurl = urllib2.urlopen("http://api.wunderground.com/api/" + self.wunderkey + "/geolookup/conditions/forecast/q/" + state + "/" + city + ".json")
        j = json.load(wurl)
        var.append(city.capitalize() + ", " + state.capitalize())
        var.append("Current Conditions: " + j["current_observation"]["weather"])
        var.append("Temperature: " + j["current_observation"]["temperature_string"])
        var.append("Humidity: " + j["current_observation"]["relative_humidity"])
        var.append("Wind: " + j["current_observation"]["wind_string"])
        var.append("Dewpoint: " + j["current_observation"]["dewpoint_string"])
        return var

    def search(self, term):
        var = []
        search_results = urllib2.urlopen('http://api.duckduckgo.com/?q=' + term + '&format=json')
        j = json.load(search_results)
        var.append(j["AbstractSource"])
        var.append(j["Definition"])
        var.append(j["AbstractURL"])
        return var

    def currency(self, num, output):
        var = []
        rates = urllib2.urlopen("https://raw.github.com/currencybot/open-exchange-rates/master/latest.json")
        j = json.load(rates)
        amount = decimal.Decimal(num)*decimal.Decimal(j["rates"][output])
        var.append(j["license"])
        var.append("$" + num + " is " + str(decimal.Decimal(amount).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN)) + " " + output.upper())
        return var

if __name__ == '__main__':
    print "Not to be called directly."