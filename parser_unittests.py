import unittest
import csv
from ru_datetime_parser import RuDateTimeParser
import datetime

# import codecs
# fileObj = codecs.open( "someFilePath", "r", "utf_8_sig", )

# def OurDateParserFunction(str):
#     return ("2020-11-27")

class TestSum(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.expected = []
        self.result = []
        with open('test_file.csv', newline='', encoding="utf8") as f:
            reader = csv.reader(f)
            data = list(reader)
        firstline = True
        self.testsLength = len(data) - 1
        for row in data[:10]:
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
            # answer = OurDateParserFunction(row[0])
            self.result.append(answer)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def test_list_eq(self):
        for r, exp in zip(self.result, self.expected):
            with self.subTest(msg='Equal check'):
                self.assertEqual(r, exp)


if __name__ == '__main__':
    unittest.main()


# import pandas as pd
# from ru_datetime_parser import RuDateTimeParser

# if __name__ == '__main__':
    # dataset = pd.read_csv('retropress/srcs.csv', delimiter=',').values.tolist()
    #
    # for row in dataset[:10]:
    #     inst = RuDateTimeParser(row[0])
    #     inst.parse_text()
