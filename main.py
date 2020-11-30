import pandas as pd
from ru_datetime_parser import RuDateTimeParser

if __name__ == '__main__':
    dataset = pd.read_csv('retropress/srcs.csv', delimiter=',').values.tolist()

    for row in dataset[:10]:
        inst = RuDateTimeParser(row[0])
        inst.parse_text()






































