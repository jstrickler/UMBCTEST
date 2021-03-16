#!/usr/bin/env python
import sys

# Test three functions from the random module:
import random
import unittest


class TestSequenceFunctions(unittest.TestCase):  # <1>
    @classmethod
    def setUpClass(cls):  # <2>
        print("Starting all tests")

    def setUp(self):  # <3>
        print("Hello!")
        self.seq = list(range(10))

    def testshuffle(self):  # <4>
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))  # <5>

    @unittest.skipIf(sys.platform == "win32", "Not implemented on Windows")
    def testchoice(self):
        element = random.choice(self.seq)
        self.assertIn(element, self.seq)  # <6>

    def testsample(self):
        self.assertRaises(ValueError, random.sample, self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertIn(element, self.seq)

    def tearDown(self):  # <7>
        print("Goodbye!")

    @classmethod
    def tearDownClass(cls):  # <8>
        print("Ending all tests")


if __name__ == '__main__':
    unittest.main()  # <9>
