'''
S.T.E.V.E. Command Parser
Part of the S.T.E.V.E Core
Parses for commands from various sources
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

def init(self, data):
    fb = data.find('facebookmail.com')
    if fb != -1:
        return 'fb'
    else:
        em = data.find('steve')
        if em != -1:
            return 'email'
        else:
            pass

if __name__ == '__main__':
    print "Not to be called directly."