'''
S.T.E.V.E. Test Plugin
Simple "Hello World!" plugin
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code from An Introduction to Tkinter (http://www.pythonware.com/library/tkinter/introduction/hello-tkinter.htm) Copyright (c) 1999 by Fredrik Lundh
'''

from Tkinter import Tk, Label

def helloworld():
    root = Tk()
    w = Label(root, text="Hello, world!")
    w.pack()
    root.mainloop()
    return