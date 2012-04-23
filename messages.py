'''
S.T.E.V.E. Messages
Messages and errors
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Code and device by Jacob Turner; code released under the MIT license
'''

class messages():
    pass
class errors():
    class ConfigUni(Exception):
        def __str__(self):
            return repr("File incorrectly saved as Unicode, please resave as ASCII.")
    class CantParseConfig(Exception):
        def __str__(self):
            return repr("Cannot parse config.ini. Please see error message.")
    class Unknown(Exception):
        def __str__(self):
            return repr("Unknown error. Please try again.")
    class DefaultValue(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr("Default value detected for %s." % self.value)
    class ValueNotFound(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr("Value %s not found." % self.value)
    class NewConfig(Exception):
        def __str__(self):
            return repr("Please fix the values in config.ini.")
    class FileNotFound(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr("%s does not exist." % self.value)

if __name__ == '__main__':
    print "Not to be called directly."