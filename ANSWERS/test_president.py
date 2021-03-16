#!/usr/bin/python
from datetime import date
import unittest
from president import President

class TestPresident(unittest.TestCase):

    def test_president_one_last_name_is_george(self):
        p = President(1)
        self.assertEqual(p.first_name, "George", "President 1's first name is not George")

    def test_date_fields_return_dates_or_none(self):
        for i in range(1,46):
            p = President(i)
            self.assertIsInstance(p.birth_date, date, "birth_date is not datetime.date object")
            self.assertIsInstance(p.death_date, (date, type(None)), "death_date is not datetime.date object or None")
            self.assertIsInstance(p.term_start_date, date, "term_start is not datetime.date object")
            self.assertIsInstance(p.term_end_date, (date, type(None)), "term_end is not datetime.date object or None")

    def test_invalid_term_raises_error(self):
        for invalid_term in -1, 0, 46, 1000:
            with self.assertRaises(ValueError):
                p = President(invalid_term)

    # add other tests here...


if __name__ == '__main__':
    unittest.main()
