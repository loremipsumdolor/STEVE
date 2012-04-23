'''
S.T.E.V.E. Plugin Verifier
Safeguard for malicious plugins
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
'''

import os
import re

def plgverify():
    aplist = []
    newaplist = []
    files = []
    for file in os.listdir("plugins"):
        if file.endswith('.py'):
            files.append(file)
    files.remove("__init__.py")
    approved = open("aplist.txt", "r+")
    for line in approved:
        aplist.append(line.rstrip("\n"))
    diff_list = []
    for item in files:
        if not item in aplist:
            diff_list.append(item)
    if diff_list != []:
        for item in range(len(diff_list)):
            imports = []
            with open("plugins/%s" % diff_list[item]) as plugin:
                for line in plugin:
                    if re.match("import(.*)", line):
                        imports.append(line.rstrip("\n").split(" ")[1])
            mv = ', '.join(imports)
            print "New plugin found: %s" % diff_list[item]
            print "This plugin requires access to the following libraries:"
            print mv
            while True:
                yn = raw_input("Approve this plugin for use? (Yes/no) > ")
                if yn.capitalize() == "Yes" or "Y" or "":
                    newaplist.append(diff_list[item])
                    print "Plugin %s approved!" % diff_list[item]
                    break
                elif yn.capitalize() == "No" or "N":
                    while True:
                        remyn = raw_input("Remove plugin file? (Yes/no) > ")
                        if remyn.capitalize() == "Yes" or "Y" or "":
                            os.remove("plugins/%s") % diff_list[item]
                            break
                        elif remyn == "No" or "N":
                            break
                        else:
                            print "Not a valid choice."
                else:
                    print "Not a valid choice."
        for item in newaplist:
            approved.write("%s\n" % item)
        approved.close()
        print "Please restart S.T.E.V.E. for plugins to take effect."
        return
    else:
        return

if __name__ == "__main__":
    plgverify()