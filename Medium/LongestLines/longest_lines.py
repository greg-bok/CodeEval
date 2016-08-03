import sys
import os


class TextLine:
    def __init__(self, text):
        self._text = text
        self._size = len(text)

    def __cmp__(self, other):
        return cmp(self._size, other._size)

    def __str__(self):
        return self._text


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
        self._buffer = self._buffer[-slice:]
    
    def items(self):
        items = self._buffer[:]
        items.reverse()
        return items


class LongestLines:
    def __init__(self, fileName):
        self._file = open(fileName, 'r')
        lineCount = int(self._file.next().rstrip())
        self._buffer = BoundedOrderedBuffer(lineCount)

    def run(self):
        with self._file as fd:
            for line in fd:
                self._buffer.add(TextLine(line.rstrip()))
        return self._buffer.items()
           
    
    
            

if __name__ == "__main__":
    fileName = sys.argv[1]
    main = LongestLines(fileName)
    result = main.run()
    for line in result:
        print line

        
    
    
