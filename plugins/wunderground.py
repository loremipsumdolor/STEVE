'''
Wunderground plugin for S.T.E.V.E.
Code by Jacob Turner; released under the MIT license
'''

'''
        elif data.find("steve weather") != -1 or data.find("weather") != -1:
            term = data.split(" ")
            if format == "email" or format == "text":
                info = wunderground.wg(term[2], term[3])
            else:
                info = wunderground.wg(term[1], term[2])
            if format == "email":
                var.append("text")
                var.append(sender)
                var.append("%s, %s" % (term[2].capitalize(), term[3].capitalize()))
                if type(info) is dict:
                    var.append("%s, %s is currently %s." % (term[2].capitalize(),
                               term[3].capitalize(),
                               info["current_observation"]["temperature_string"]))
                else:
                    var.append(info)
                return var
            elif format == "txt":
                var.append(sender)
                if type(info) is dict:
                    var.append("%s, %s is currently %s." % (term[2].capitalize(),
                               term[3].capitalize(),
                               info["current_observation"]["temperature_string"]))
                else:
                    var.append(info)
                return var
            elif format == "console":
                if type(info) is dict:
                    var.append("%s, %s" % (term[1].capitalize(), term[2].capitalize()))
                    var.append("Current Conditions: %s" %
                               info["current_observation"]["weather"])
                    var.append("Temperature: %s" %
                               info["current_observation"]["temperature_string"])
                    var.append("Humidity: %s" %
                               info["current_observation"]["relative_humidity"])
                    var.append("Wind: %s" %
                               info["current_observation"]["wind_string"])
                    var.append("Dewpoint: %s" %
                               info["current_observation"]["dewpoint_string"])
                    return var
                else:
                    return info
'''

import json
import urllib
import config

def wg(city, state):
    cfg = config.othersvar("wunder.ini", ["wunderkey"])
    if cfg[0] == None:
        return "Error: Cannot complete function due to missing username/API key for Wunderground."
    url = "http://api.wunderground.com/api/%s/geolookup/conditions/forecast/q/%s/%s.json" % (cfg[0], state, city)
    info = json.load(urllib.urlopen(url))
    try:
        if info["error"]["type"] == "querynotfound":
            return "Error: Invalid city or state."
    except:
        return info