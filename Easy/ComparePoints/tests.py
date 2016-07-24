import unittest
import compare_points
from compare_points import Point

class TestPoint(unittest.TestCase):
    def test_parsingFromString(self):
        p = Point.fromStrings("1", "2")
        self.assertEqual(p.coordinates(), (1,2))

    def test_same(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        self.assertEqual(p1.relativePosition(p2), "here")
        self.assertEqual(p2.relativePosition(p1), "here")

    def test_north_south(self):
        p1 = Point(-1, 1)
        p2 = Point(-1, 2) 
        self.assertEqual(p1.relativePosition(p2), "S")
        self.assertEqual(p2.relativePosition(p1), "N")
        
    def test_east_west(self):
        p1 = Point(1, 2)
        p2 = Point(-1, 2)
        self.assertEqual(p1.relativePosition(p2), "E")
        self.assertEqual(p2.relativePosition(p1), "W")


class TestTextProcessing(unittest.TestCase):
    def test_process_lines(self):
        textLines = "1 2 1 2\n\n\n-1 2 -1 3\n\n\n"
        self.assertEqual(compare_points.process_lines(textLines), "here\nN")

