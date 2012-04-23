'''
S.T.E.V.E. Additional Commands Parser
For all of the extra commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
'''

'''
A Quick Note on the Additional Commands

Additional commands are the equivalent of plugins or mods; they allow you to add additional
functionality to the program (S.T.E.V.E.). For an example of how to make an additional
command, take a look at examples/plugin/plugin.py. For instructions on how to use a plugin,
look at examples/plugin/readme.txt.
'''

import os
from plugins import *

def parse(data, sender, format):
    var = []
    if len(os.listdir("plugins")) == 1:
        return "Error: not a valid command."
    else:
        return