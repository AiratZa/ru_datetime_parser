import pandas as pd
import datetime


from ru_datetime_parser import RuDateTimeParser, covert_string_to_keys
from pattern_handlers.time_handlers import *

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
        if (i >= 4):
            return count_with_date_saved
    return count_with_date


if __name__ == '__main__':
    answers = []
    collapse_distance = 3
    current_datetime = datetime.datetime.now()

    start = WeekendHandler()
    weekend = DatesPeriodHandler()
    start.set_next(weekend).set_next
    
    text = input("Введите дату:  ")

    text_splitted = text.split()

    i = 0
    tokenized = covert_string_to_keys(text_splitted)
    while (i < len(tokenized)):
        count_another = 0
        while (i < len(tokenized) and tokenized[i] == '_'):
            count_another += 1
            i += 1
        if (count_another <= 3):
            while (i < len(tokenized)):
                len_wordcount_with_date = get_max_len_str_with_dates(tokenized[i:], collapse_distance)
                instance = RuDateTimeParser(' '.join(text_splitted[i : i + len_wordcount_with_date]))
                instance.set_converted_to_tokens(tokenized[i : i + len_wordcount_with_date])
                i += len_wordcount_with_date
                answers.append(instance)
                start.handle(instance)
                print(instance.get_converted_to_tokens())
                print(instance.get_dates())

    # month_day_ = DayMonthHandler()
    # dates_period_handler = DatesPeriodHandler()


    


    # # Клиент должен иметь возможность отправлять запрос любому обработчику, а не
    # # только первому в цепочке.
    # print("Chain: Monkey > Squirrel > Dog")
    # client_code(monkey)
    # print("\n")

    # print("Subchain: Squirrel > Dog")
    # client_code(squirrel)
    # print(result)
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


