import pandas as pd
import datetime
import re

from word2number import extractor as extr

from sets import *


def has_one_of_lemmas(splitted_word, key_values):
    for key in key_values:
        if splitted_word in (key, *key_values[key]):
            return True
    return False


def covert_string_to_keys(string_at_start):
    splitted_all = string_at_start.split()
    cur_index = 0
    answer = ''

    for splitted in splitted_all:
        if (has_one_of_lemmas(splitted, year_key)):
            answer += 'Y'
        elif (has_one_of_lemmas(splitted, months)):
            answer += 'M'
        elif (has_one_of_lemmas(splitted, weeks)):
            answer += 'D'
        elif (has_one_of_lemmas(splitted, back_time_keyword)):
            answer += 'b'
        elif (has_one_of_lemmas(splitted, forward_time_keyword)):
            answer += 'l'
        elif (has_one_of_lemmas(splitted, weekend)):
            answer += 'W'
        elif (has_one_of_lemmas(splitted, minute_keyword)):
            answer += 'e'
        elif (has_one_of_lemmas(splitted, hour_keyword)):
            answer += 'h'
        elif (has_one_of_lemmas(splitted, day_keyword)):
            answer += 'd'
        elif (has_one_of_lemmas(splitted, week_keyword)):
            answer += 'w'
        elif (has_one_of_lemmas(splitted, months_keyword)):
            answer += 'm'
        elif (has_one_of_lemmas(splitted, adj_back_time_keyword)):
            answer += 's'
        elif (has_one_of_lemmas(splitted, adj_current_time_keyword)):
            answer += 'u'
        elif (has_one_of_lemmas(splitted, adj_future_time_keyword)):
            answer += 'x'
        elif (has_one_of_lemmas(splitted, bb_day_keyword)):
            answer += '2'
        elif (has_one_of_lemmas(splitted, b_day_keyword)):
            answer += '3'
        elif (has_one_of_lemmas(splitted, today_day_keyword)):
            answer += '4'
        elif (has_one_of_lemmas(splitted, f_day_keyword)):
            answer += '5'
        elif (has_one_of_lemmas(splitted, ff_day_keyword)):
            answer += '6'
        elif (has_one_of_lemmas(splitted, morning_keyword)):
            answer += 'r'
        elif (has_one_of_lemmas(splitted, noon_keyword)):
            answer += 'n'
        elif (has_one_of_lemmas(splitted, evening_keyword)):
            answer += 'v'
        elif (has_one_of_lemmas(splitted, night_keyword)):
            answer += 'g'
        elif (has_one_of_lemmas(splitted, half_keyword)):
            answer += 'H'
        elif (has_one_of_lemmas(splitted, quater_keyword)):
            answer += 'Q'
        elif (re.match(r'^\d+', splitted)):
            answer += '1'
        elif (has_one_of_lemmas(splitted, from_keyword)):
            answer += 'f'
        elif (has_one_of_lemmas(splitted, to_keyword)):
            answer += 't'
        elif (has_one_of_lemmas(splitted, to_what_keyword)):
            answer += 'o'
        elif (has_one_of_lemmas(splitted, number_keyword)):
            answer += '#'
        elif splitted == 'и':
            answer += 'N'
        else:
            answer += '_'
        cur_index += 1

    return answer




# period_key_words = ['протяжении', 'с', 'по', '-', 'всю', 'за', 'до']


# def get_str_time_formatted(tmp_time, with_HM=True):
#     if (with_HM):
#         return current_datetime.strftime('%d-%m-%Y %H:%M')
#     return current_datetime.strftime('%d-%m-%Y')

# def create_timestamp_with_nulls_to_time_params(current_datetime, time_params):
#     tmp_time = current_datetime
#     for param in time_params:
#         if param == 'minute':
#             tmp_time = tmp_time - datetime.timedelta(minutes=current_datetime.minute)
#         elif param == 'hour':
#             tmp_time = tmp_time - datetime.timedelta(hours=current_datetime.hour)
#     return tmp_time


# def is_has_delta_sizes(row_splitted):
#     for r in row_splitted:
#         for i in delta_sizes:
#             for j in i[1]:
#                 if i[0] == 'days':
#                     continue
#                 if r == j:
#                     return True
#     return False

# def check_delta(row, params):
#     for i in params['row_splitted']:
#         for today_day in today_days:
#             if today_day in i:
#                 params['has_delta'] = True
#                 params['delta_count'] = 0
#                 params['delta_size'] = 'days'
#                 params['row_splitted'].remove(i)
#                 if not is_has_delta_sizes(params['row_splitted']):
#                     params['with_HM'] = False
#                 break


# def check_time_delta_size(row, params):
#     for i in delta_sizes:
#         for j in i[1]:
#             if j in row:
#                 params['delta_size'] = i[0]
#                 break




# def is_period(row, row_splitted):
#     for i in row_splitted:
#         for j in period_key_words:
#             if i == j:
#                 return True
#     return False

# def period_handler(row, row_splitted, current_datetime):
#     params = {'now_now': False,  
#             'now_flag': False, 'delta_size': '', 
#             'has_delta': False, 'delta_count': 0, 'with_HM': True, 'row_splitted':row_splitted}
#     check_now(row, params)
#     check_time_delta_size(row, params)
#     check_delta(row, params)

#     if params['delta_size'] == 'days':
#         if params['delta_count'] == 0:
#             first_datetime = current_datetime - datetime.timedelta(minutes=current_datetime.minute,hours=current_datetime.hour)
#             second_datetime = first_datetime + datetime.timedelta(days=1)
#             print(f"{row:55} - {first_datetime.strftime('%d-%m-%Y %H:%M')} |||| {second_datetime.strftime('%d-%m-%Y %H:%M')}")


# def non_period_handler(row, row_splitted, current_datetime):
#     params = {'now_now': False,  
#             'now_flag': False, 'delta_size': '', 
#             'has_delta': False, 'delta_count': 0, 'with_HM': True, 'row_splitted':row_splitted}
#     check_now(row, params)
#     if not params['now_now']:
#         check_time_delta_size(row, params)
#         check_delta(row, params)

#     if params['now_now'] or (params['now_flag'] and (params['delta_size'] in ('minutes', 'seconds'))):
#         print(f"{row:55} - {get_str_time_formatted(current_datetime, params['with_HM'])}")
#     elif params['delta_size'] and params['now_flag']:
#         if params['delta_size'] == 'days':
#             our_time = create_timestamp_with_nulls_to_time_params(current_datetime, ['minute', 'hour'])
#             print(f"{row:55} - {get_str_time_formatted(our_time, params['with_HM'])}")


if __name__ == '__main__':
    extractor = extr.NumberExtractor()
    text = input("Введите дату:  ")
    text = extractor.replace_groups(text.lower()) 
    result = covert_string_to_keys(text)
    print(result)
    # for i in months['янв']:
        # print(i)
    # dataset = pd.read_csv('../retropress/srcs.csv', delimiter=',').values.tolist()

    # current_datetime = datetime.datetime.now();
    # print(hours)

    # for row in dataset:
    #     row = str(row[0])
    #     # print(row)
    #     row_splitted = row.split()
    #     # print(row_splitted)
    #     is_period_flag = is_period(row, row_splitted)

    #     if is_period_flag:
    #         period_handler(row, row_splitted, current_datetime)
    #     else:
    #         non_period_handler(row, row_splitted, current_datetime)


