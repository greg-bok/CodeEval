import unittest
import trick_or_treat

class LineProcessorTests(unittest.TestCase):
    def setUp(self):
        self._lineText = "Vampires: 1, Zombies: 0,Witches:2,  Houses: 3\n"
        self._subjectUnderTest = trick_or_treat.LineProcessor()

    def test_parseVampires(self):
        self.assertEqual(self._subjectUnderTest.processLine(self._lineText).vampires(), 1)

    def test_parseZombies(self):
        self.assertEqual(self._subjectUnderTest.processLine(self._lineText).zombies(), 0)

    def test_parseWitches(self):
        self.assertEqual(self._subjectUnderTest.processLine(self._lineText).witches(), 2)

    def test_parseHouses(self):
        self.assertEqual(self._subjectUnderTest.processLine(self._lineText).houses(), 3)


class HalloweenTests(unittest.TestCase):
    def test_singleHouseCandyShare(self):
        self.assertEqual(0, 1)


