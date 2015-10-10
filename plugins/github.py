'''
GitHub plugin for S.T.E.V.E.
Code by Jacob Turner; released under the MIT license
'''

'''
        elif data.find("steve ghuser") != -1 or data.find("ghuser") != -1:
            term = data.split(" ")
            if format == "email" or format == "text":
                info = github.ghuser(term[2])
            else:
                info = github.ghuser(term[1])
            if format == "email":
                var.append("text")
                var.append(sender)
                var.append(term[2])
                if type(info) is dict:
                    var.append("%s has %s public repos." % (term[2],
                               str(info["public_repos"])))
                else:
                    var.append(info)
                return var
            elif format == "txt":
                var.append(sender)
                if type(info) is dict:
                    var.append("%s has %s public repos." % (term[2],
                               str(info["public_repos"])))
                else:
                    var.append(info)
                return var
            elif format == "console":
                if type(info) is dict:
                    var.append("%s (%s)" % (term[1], str(info["name"])))
                    var.append("Email: %s" % info["email"])
                    var.append("Website/Blog: %s" % info["blog"])
                    var.append("Location: %s" % info["location"])
                    var.append("Registered on: %s" % info["created_at"].split("T")[0])
                    var.append("%s public repositories" % str(info["public_repos"]))
                    var.append("%s followers" % str(info["followers"]))
                else:
                    var.append(info)
                return var
        elif data.find("steve ghproj") != -1 or data.find("ghproj") != -1:
            term = data.split(" ")
            if format == "email" or format == "text":
                info = github.ghproj(term[2], term[3])
            else:
                info = github.ghproj(term[1], term[2])
            if format == "email":
                var.append("text")
                var.append(sender)
                var.append("%s by %s" % (term[2].capitalize(), term[3]))
                if type(info) is dict:
                    var.append("%s by %s - %s" % (term[2].capitalize(), term[3],
                               info["description"]))
                else:
                    var.append(info)
                return var
            elif format == "txt":
                var.append(sender)
                if type(info) is dict:
                    var.append("%s by %s - %s" % (term[2].capitalize(), term[3],
                               info["description"]))
                else:
                    var.append(info)
                return var
            elif format == "console":
                if type(info) is dict:
                    var.append("%s by %s" % (term[1].capitalize(), term[2]))
                    var.append(info["description"])
                    var.append(info["homepage"])
                    var.append("Created on: %s" % info["created_at"].split("T")[0])
                    var.append("Written in: %s" % info["language"])
                    var.append("%s watchers" % str(info["watchers"]))
                    var.append("%s forks" % str(info["forks"]))
                    return var
                else:
                    return info
'''

import json
import urllib2

def ghuser(user):
    url = "https://api.github.com/users/%s" % user
    info = json.load(urllib2.urlopen(url))
    try:
        if info["message"] == "Not Found":
            return "Error: Invalid project name or username."
    except:
        return info

def ghproj(project, user):
    url = "https://api.github.com/repos/%s/%s" % (user, project)
    info = json.load(urllib2.urlopen(url))
    try:
        if info["message"] == "Not Found":
            return "Error: Invalid project name or username."
    except:
        return info