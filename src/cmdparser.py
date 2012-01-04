'''
S.T.E.V.E. Command Parser
Builtin S.T.E.V.E. commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

import cv

def picture():
    capture = cv.CaptureFromCAM(0)
    frame = cv.QueryFrame(capture)
    cv.SaveImage('image.jpg', frame)

if __name__ == '__main__':
    print "Not to be called directly."