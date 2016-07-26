import sys
import os


class BoundedOrderedBuffer:
    def __init__(self, maxSize):
        self._buffer = []
        
    def add(self, item):
        self._buffer.append(item)
        
    def items(self):
        return self._buffer

    def __eq__(self, other):
        return self._value == other._value

    def __ne__(self, other):
        return self._value != other._value


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
    
