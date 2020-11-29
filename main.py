import pandas as pd
import datetime
from word2number import extractor as extr

from ru_datetime_parser import RuDateTimeParser, covert_string_to_keys
from pattern_handlers.time_handlers import *

extractor = extr.NumberExtractor()


def get_max_len_str_with_dates(text, collapse_distance):
    count_with_date = 0
    count_with_date_saved = count_with_date

    i = 0
    while (i < len(text)):
        if (text[i] != '_'):
            count_with_date += 1
            i += 1
        count_another = 0
        count_with_date_saved = count_with_date
        while (i < len(text) and text[i] == '_' and count_another <= collapse_distance):
            count_with_date += 1
            i += 1
        if (i > collapse_distance):
            return count_with_date_saved
    return count_with_date


if __name__ == '__main__':
    answers = []
    collapse_distance = 13

    # datetime(year, month, day, hour, minute, second, microsecond)
    # current_datetime = datetime.datetime.now()
    current_datetime = datetime.datetime(2020, 11, 27, 2, 30, 0, 0)

    start = WeekendHandler()
    dates_period = DatesPeriodHandler()
    day_month = DaysMonthHandler()
    pass_handle = PassHandler()
    time_recognizer = TimeRecognizerHandler()
    relative_day = RelativeDayHandler()
    relative_datetime = RelativeDateTimeHandler()

    start.set_next(dates_period).set_next(day_month)\
            .set_next(relative_day)\
            .set_next(relative_datetime)\
            .set_next(time_recognizer)\
            .set_next(pass_handle)
    
    # text = input("Введите дату:  ")
    # text_splitted = text.split()

    # i = 0
    # tokenized = covert_string_to_keys(text_splitted)
    # while (i < len(tokenized)):
    #     count_another = 0
    #     while (i < len(tokenized) and tokenized[i] == '_'):
    #         count_another += 1
    #         i += 1
    #     if (count_another <= 3):
    #         while (i < len(tokenized)):
    #             len_wordcount_with_date = get_max_len_str_with_dates(tokenized[i:], collapse_distance)
    #             instance = RuDateTimeParser(' '.join(text_splitted[i : i + len_wordcount_with_date]), current_datetime)
    #             instance.set_converted_to_tokens(tokenized[i : i + len_wordcount_with_date])
    #             i += len_wordcount_with_date
    #             answers.append(instance)
    #             start.handle(instance)
    #             print(instance.get_converted_to_tokens())
    #             print(instance.get_answer())

    dataset = pd.read_csv('retropress/srcs.csv', delimiter=',').values.tolist()

    for row in dataset:
        str_1 = extractor.replace_groups(row[0].lower())
        text_splitted = str_1.split()

        i = 0
        tokenized = covert_string_to_keys(text_splitted)
        len_tokenized = len(tokenized)
        while (i < len_tokenized):
            count_another = 0
            while (i < len_tokenized and tokenized[i] == '_'):
                count_another += 1
                i += 1
            if (count_another <= collapse_distance):
                while (i < len_tokenized):
                    len_wordcount_with_date = get_max_len_str_with_dates(tokenized[i:], collapse_distance)
                    print(row, 'None', tokenized[i:], 'hey', i)
                    instance = RuDateTimeParser(' '.join(text_splitted[i : i + len_wordcount_with_date]), current_datetime)
                    instance.set_converted_to_tokens(tokenized[i : i + len_wordcount_with_date])
                    i += len_wordcount_with_date
                    answers.append(instance)
                    print(instance.get_converted_to_tokens())
                    start.handle(instance)
                    instance.convert_to_answer()
                    print(text_splitted, '   ', instance.get_answer())






































