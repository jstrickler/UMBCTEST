#!/usr/bin/env python
#
import unittest
from unittest.mock import Mock

ham = Mock()  # <1>


# system under test
class Spam():
    def __init__(self, param):
        self._value = ham(param)  # <2>


# dependency to be mocked -- not used in test
# def ham(n):
#     pass

class TestSpam(unittest.TestCase):  # <3>

    def test_spam_calls_ham(self):
        _ = Spam(42)  # <4>
        ham.assert_called_once_with(42)  # <5>


if __name__ == '__main__':
    unittest.main()
