from word2number import extractor as extr
import re
import datetime

from sets import *


extractor = extr.NumberExtractor()
 
def has_one_of_lemmas(splitted_word, key_values):
    for key in key_values:
        if splitted_word in (key, *key_values[key]):
            return True
    return False
def covert_string_to_keys(splitted_all):
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


class RuDateTimeParser():



    def __init__(self, string_at_start):
        """Constructor"""
        self._converted_to_tokens = ''
        self._is_period = False
        self._string_at_start = extractor.replace_groups(string_at_start.lower())
        self._splitted_all = self._string_at_start.split()
        self._current_token_index = 0
        self._dates = []
        self._splitted_with_tokens_indexes = self._string_at_start.split()





    def get_converted_to_tokens(self):
        return self._converted_to_tokens

    def set_converted_to_tokens(self, value):
        self._converted_to_tokens = value


    def get_current_tokens(self):
        return self._converted_to_tokens[self._current_token_index:]

    def incr_current_token_index(self):
        self._current_token_index += 1

    def push_back_date_and_set_index_in_text(self, result):
        result_len = len(result.group(0))
        for i in range(result_len):
            self._dates.append(self._splitted_all[self._current_token_index])
            self._splitted_with_tokens_indexes[self._current_token_index] = len(self._dates) - 1
            self.incr_current_token_index()

    def get_dates(self):
        return self._dates
