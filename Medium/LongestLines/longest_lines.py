import sys
import os


class BoundedOrderedBuffer:
    def __init__(self, maxSize):
        self._buffer = []
        self._size = 0
        self._maxSize = maxSize
        self._min = 0
        self._max = 0
        
    def add(self, item):        
        self._buffer.append(item)
        self._buffer.sort()
        slice = min(len(self._buffer), self._maxSize)
        self._buffer = self._buffer[:slice]
    
    def items(self):
        return self._buffer


class LongestLines:
    def __init__(self, fileName):
        self._file = open(fileName, 'r')
        self._lineCount = int(self._file.next().rstrip())

    def run(self):
        pass


if __name__ == "__main__":
    fileName = sys.argv[1]
    main = LongestLines(fileName)
    main.run()
    
