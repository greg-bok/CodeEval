import unittest
from trick_or_treat import LineProcessor, Halloween, TrickOrTreater

class LineProcessorTests(unittest.TestCase):
    def setUp(self):
        self._lineText = "Vampires: 1, Zombies: 3,Witches:2,  Houses: 3\n"
        self._subjectUnderTest = LineProcessor().processLine(self._lineText)

    def test_parseHouses(self):
        self.assertEqual(self._subjectUnderTest.houses(), 3)
        
    def test_totalChildren(self):
        self.assertEqual(self._subjectUnderTest.totalChildren(), 6)

    def test_candyPerHouse(self):
        self.assertEqual(self._subjectUnderTest.candyPerHouse(), 25)


class HalloweenTests(unittest.TestCase):
    def test_candyShare(self):
        subjectUnderTest = Halloween([TrickOrTreater(2, 5)], 2)
        self.assertEqual(subjectUnderTest.candyShare(), 10)

    def test_roundsFractionalCandyShareDown(self):
        subjectUnderTest = Halloween([TrickOrTreater(2, 3), TrickOrTreater(1, 4)], 1)
        self.assertEqual(subjectUnderTest.candyShare(), 3)
