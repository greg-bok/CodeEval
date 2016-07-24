import sys

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def coordinates(self):
        return (self._x, self._y)

    def compute_pointwise_difference_sign(self, p):
        return (cmp(self._x - p._x, 0), cmp(self._y - p._y, 0))

    def relativePosition(self, p1):
        d = self.compute_pointwise_difference_sign(p1)
        return {
            ( 0, 0) : "here",
            ( 1, 0) : "E",
            (-1, 0) : "W",
            ( 0, 1) : "N",
            ( 0,-1) : "S",
            ( 1, 1) : "NE",
            ( 1,-1) : "SE",
            (-1, 1) : "NW",
            (-1,-1) : "SW"
            }.get(d)

    @staticmethod
    def fromStrings(sx, sy):
        return Point(int(sx), int(sy))


def process_line(lineText):
    fields = lineText.split()
    p1 = Point.fromStrings(fields[0], fields[1])
    p2 = Point.fromStrings(fields[2], fields[3])
    return p2.relativePosition(p1)

    
def process_lines(test_cases):
    results = map(process_line, filter(lambda x: len(x.strip()) > 0, test_cases.splitlines()))
    return "\n".join(results) + "\n"

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as test_cases:
        print process_lines(test_cases)
        

