import os
import sys

class TrickOrTreater:
    VampireValue = 3
    ZombieValue  = 4
    WitchValue = 5

    def __init__(self, count, value):
        self._count = count
        self._value = value

    def count(self):
        return self._count

    def totalValue(self):
        return (self._count * self._value)

    @staticmethod
    def createVampire(c):
        return TrickOrTreater(c, TrickOrTreater.VampireValue)
    
    @staticmethod
    def createZombie(c):
        return TrickOrTreater(c, TrickOrTreater.ZombieValue)

    @staticmethod
    def createWitch(c):
        return TrickOrTreater(c, TrickOrTreater.WitchValue)


class Halloween:
    def __init__(self, children, h):
        self._children = children
        self._houses = h

    def houses(self):
        return self._houses

    def totalChildren(self):
        return sum(map(lambda x: x.count(), self._children))
        
    def candyPerHouse(self):
        return sum(map(lambda x: x.totalValue(), self._children))
    
    def candyShare(self):
        return int((self.candyPerHouse() * self._houses) / float(self.totalChildren()))
    
    def __str__(self):
        return "%s"%(self.candyShare())


class LineProcessor:
    def __init__(self):
        self._vampireCache = {}
        self._zombieCache = {}
        self._witchCache = {}
        self._houseCache = {}

    def processLine(self, lineText):
        vs,zs,ws,hs = lineText.strip().split(",")
        children = []
        children.append(self.getVampire(vs.split(":")[1]))
        children.append(self.getZombie(zs.split(":")[1]))
        children.append(self.getWitch(ws.split(":")[1]))
        houses = self.getHouse(hs.split(":")[1])
        return Halloween(children, houses)
        
    def getVampire(self, rc):
        return self.getTrickOrTreater(TrickOrTreater.createVampire, self._vampireCache, rc)

    def getZombie(self, rc):
        return self.getTrickOrTreater(TrickOrTreater.createZombie, self._zombieCache, rc)

    def getWitch(self, rc):
        return self.getTrickOrTreater(TrickOrTreater.createWitch, self._witchCache, rc)

    def getTrickOrTreater(self, build, cache, value):
        sval = value.strip()
        if sval not in cache:
            cache[sval] = build(int(sval))
        return cache[sval]

    def getHouse(self, rh):
        srh = rh.strip()
        if srh not in self._houseCache:
            self._houseCache[srh] = int(srh)
        return self._houseCache[srh]


def process_file(f):
    processor = LineProcessor()
    for line in f:
        print processor.processLine(line)    

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as fd:
        process_file(fd)
