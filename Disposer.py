#!/usr/bin/python

from Settings import Settings as S

class Disposer:
    def __init__(self):
        self.i=0
        self.curx=0
        self.cury=0

    def getNextPosition(self):
        self.curx = S.marginleft + (( self.i % S.nbxelt) * (S.spacex + S.imgwidth) ) 
        self.cury = S.margintop + (( self.i // S.nbxelt ) * (S.spacey + S.imgheight) )
	self.i += 1
        return self.curx, self.cury
    
    

if __name__ == '__main__':
    test = Disposer()
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    print("%s, %s" % test.getNextPosition())
    
