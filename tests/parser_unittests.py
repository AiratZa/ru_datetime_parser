import unittest
import csv


def OurDateParserFunction(str):
    return ("2020-11-27")

class TestSum(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.expected = []
        self.result = []
        with open('temporal-thesaurus-analytical-corpora-test.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        firstline = True
        self.testsLength = len(data) - 1
        for row in data:
            if firstline:    #skip first line
                firstline = False
                continue
            self.expected.append(row[1])
            self.result.append(OurDateParserFunction(row[0]))

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def test_list_eq(self):
        for r, exp in zip(self.result, self.expected):
            with self.subTest(msg='Equal check'):
                self.assertEqual(r, exp)

if __name__ == '__main__':
    unittest.main()
