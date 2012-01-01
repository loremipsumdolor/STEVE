'''
S.T.E.V.E. Command Parser
Builtin S.T.E.V.E. commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

from VideoCapture import Device

def picture():
    eye = Device()
    eye.saveSnapshot("image.jpg", timestamp=3, boldfont=1)
    return

if __name__ == '__main__':
    print "Not to be called directly."