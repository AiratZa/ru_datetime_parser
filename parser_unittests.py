import unittest
import csv
from ru_datetime_parser import RuDateTimeParser
import datetime


class TestSum(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.expected = []
        self.result = []
        self.with_words = []
        with open('test_file.csv', newline='', encoding="utf8") as f:
            reader = csv.reader(f)
            data = list(reader)
        firstline = True
        self.testsLength = len(data) - 1
        for row in data[54:56]:
            if firstline:    #skip first line
                firstline = False
                continue
            self.expected.append(row[1])
            inst = RuDateTimeParser(row[0], initial_time=datetime.datetime(year=2020,
                                                                           month=11,
                                                                           day=27,
                                                                           hour=2,
                                                                           minute=30))
            answer = inst.parse_text()
            self.with_words.append(row[0])
            self.result.append(answer)

    # def tearDown(self):
    #     self.assertEqual([], self.verificationErrors)

    def test_list_eq(self):
        for r, exp, w_words in zip(self.result, self.expected, self.with_words):
            # print(w_words)
            with self.subTest(msg='Equal check'):
                self.assertEqual(r, exp, w_words)


if __name__ == '__main__':
    # unittest.main()

    inst = RuDateTimeParser('В эту среду, 23 ноября', )
    answer = inst.parse_text()

