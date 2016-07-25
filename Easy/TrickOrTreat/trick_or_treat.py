import os
import sys

class Halloween:
    vampireValue = 3
    zombieValue  = 4
    witchValue = 5

    def __init__(self, v, z, w, h):
        self._vampires = v
        self._zombies = z
        self._witches = w
        self._houses = h

    def vampires(self):
        return self._vampires

    def zombies(self):
        return self._zombies
    
    def witches(self):
        return self._witches

    def houses(self):
        return self._houses
        
    def candyShare(self):
        perHouseCandy = self._vampire * vampireValue
        perHouseCandy += self._zombie * zombieValue
        perHouseCandy += self._witch * witchValue
        return 0


class LineProcessor:
    parseMap = {"V" : "Vampires",
                "Z" : "Zombies",
                "W" : "Witches",
                "H" : "Houses" }

    def processLine(self, lineText):
        idx = 0
        vampires = 0
        zombies = 0
        witches = 0
        houses = 0
        vs,zs,ws,hs = lineText.strip().split(",")
        rvc = vs.split(":")[1]
        rzc = zs.split(":")[1]
        rwc = ws.split(":")[1]
        rhc = hs.split(":")[1]
        vampires = int(rvc)
        zombies = int(rzc)
        witches = int(rwc)
        houses = int(rhc)

        return Halloween(vampires, zombies, witches, houses)



def process_file(f):
    pass

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as fd:
        print process_file(fd)
