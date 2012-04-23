'''
S.T.E.V.E. Plugins
Additional commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code from various sources
'''

__all__ = []
with open("aplist.txt") as approved:
    for i, l in enumerate(approved):
        __all__.append(l[:-4])
        pass