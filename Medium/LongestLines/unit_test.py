import unittest
import longest_lines

class TestItem:
    def __init__(self, value):
        self._value = value

    def size(self):
        return self._value
        
    def __str__(self):
        return "%i"%(self._value)


class TestBoundedOrderdBuffer(unittest.TestCase):
    def test_empty(self):
        subjectUnderTest = longest_lines.BoundedOrderedBuffer(1)
        self.assertEqual(subjectUnderTest.items(), [])
        
    def test_identicalMaxValues(self):
        subjectUnderTest = longest_lines.BoundedOrderedBuffer(2)
        item1 = TestItem(2)
        item2 = TestItem(1)
        item3 = TestItem(2)

        subjectUnderTest.add(item1)
        subjectUnderTest.add(item2)
        subjectUnderTets.add(item3)
        
        self.assertEqual(subjectUnderTest.items(), [item1, item3])

    def test_valuesSortedDescending(self):
        subjectUnderTest = longest_lines.BoundedOrderedBuffer(3)
        item1 = TestItem(2)
        item2 = TestItem(1)
        item3 = TestItem(3)
        item4 = TestItem(4)
        item5 = TestItem(3)
        item6 = TestItem(2)

        subjectUnderTest.add(item1)
        subjectUnderTest.add(item2)
        subjectUnderTest.add(item3)
        subjectUnderTest.add(item4)
        subjectUnderTest.add(item5)
        subjectUnderTest.add(item6)
        
        self.assertEqual(subjectUnderTest.items(), [item4, item3])

        

