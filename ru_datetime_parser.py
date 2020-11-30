import re
import datetime
from pattern_handlers.time_handlers import handle_time_patterns
from sets import *

from word2number import extractor
from typing import Optional


def replace_char_numbers_to_digits(initial_string: str) -> str:
    extractor_obj = extractor.NumberExtractor()
    return extractor_obj.replace_groups(initial_string)


def get_str_time_formatted(time_finish, with_hm=True):
    if with_hm:
        return time_finish.strftime('%Y-%m-%dT%H:%M')
    return time_finish.strftime('%Y-%m-%d')


def has_one_of_lemmas(splitted_word, key_values):
    for key in key_values:
        if splitted_word in (key, *key_values[key]):
            return True
    return False


class RuDateTimeParser:

    def __init__(self, string_at_start, initial_time=datetime.datetime.now(), max_collapse_distance=2):
        """Constructor"""
        self._is_period = False
        self._string_at_start = string_at_start
        self._parse_ready_str = replace_char_numbers_to_digits(string_at_start.lower())
        self._text_splitted = self._parse_ready_str.split()
        self._tokenized = self.covert_string_to_tokens()
        self._initial_time = initial_time
        self._max_collapse_distance = max_collapse_distance

    def parse_text(self):
        parsed = handle_time_patterns(self._text_splitted, self._tokenized)
        print(self._tokenized, '   ', self._text_splitted, '   ', end='')
        collapsed = self.collapse(parsed=parsed)
        print(collapsed)

    def collapse(self, parsed):
        i: int = 0
        len_p = len(parsed)
        delta_time: Optional[datetime.timedelta] = None
        has_initial_time = False
        with_hm = False
        while (i < len_p):
            count_non_time = 0
            while i < len_p and parsed[i][0] == '_':
                count_non_time += 1
                i += 1
            if count_non_time > self._max_collapse_distance:
                break
            if type(parsed[i][0]) is not datetime.timedelta:
                raise Exception
                # return 'BREAK'
            if not has_initial_time:
                delta_time = parsed[i][0]
                has_initial_time = True
            if parsed[i][2]:
                with_hm = True
            delta_time += parsed[i][0]
            i += 1

        if delta_time is None:
            return 'NONE'
        return get_str_time_formatted(self._initial_time + delta_time, with_hm=with_hm)

    def covert_string_to_tokens(self):
        cur_index = 0
        answer = ''

        for splitted in self._text_splitted:
            if has_one_of_lemmas(splitted, year_key):
                answer += 'Y'
            elif has_one_of_lemmas(splitted, months):
                answer += 'M'
            elif has_one_of_lemmas(splitted, weeks):
                answer += 'D'
            elif has_one_of_lemmas(splitted, back_time_keyword):
                answer += 'b'
            elif has_one_of_lemmas(splitted, forward_time_keyword):
                answer += 'l'
            elif has_one_of_lemmas(splitted, weekend):
                answer += 'W'
            elif has_one_of_lemmas(splitted, minute_keyword):
                answer += 'e'
            elif has_one_of_lemmas(splitted, hour_keyword):
                answer += 'h'
            elif has_one_of_lemmas(splitted, day_keyword):
                answer += 'd'
            elif has_one_of_lemmas(splitted, week_keyword):
                answer += 'w'
            elif has_one_of_lemmas(splitted, months_keyword):
                answer += 'm'
            elif has_one_of_lemmas(splitted, adj_back_time_keyword):
                answer += 's'
            elif has_one_of_lemmas(splitted, adj_current_time_keyword):
                answer += 'u'
            elif has_one_of_lemmas(splitted, adj_future_time_keyword):
                answer += 'x'
            elif has_one_of_lemmas(splitted, bb_day_keyword):
                answer += '2'
            elif has_one_of_lemmas(splitted, b_day_keyword):
                answer += '3'
            elif has_one_of_lemmas(splitted, today_day_keyword):
                answer += '4'
            elif has_one_of_lemmas(splitted, f_day_keyword):
                answer += '5'
            elif has_one_of_lemmas(splitted, ff_day_keyword):
                answer += '6'
            elif has_one_of_lemmas(splitted, morning_keyword):
                answer += 'r'
            elif has_one_of_lemmas(splitted, noon_keyword):
                answer += 'n'
            elif has_one_of_lemmas(splitted, evening_keyword):
                answer += 'v'
            elif has_one_of_lemmas(splitted, night_keyword):
                answer += 'g'
            elif has_one_of_lemmas(splitted, half_keyword):
                answer += 'H'
            elif has_one_of_lemmas(splitted, quater_keyword):
                answer += 'Q'
            elif re.match(r'^\d+', splitted):
                answer += '1'
            elif has_one_of_lemmas(splitted, from_keyword):
                answer += 'f'
            elif has_one_of_lemmas(splitted, to_keyword):
                answer += 't'
            elif has_one_of_lemmas(splitted, to_what_keyword):
                answer += 'o'
            elif has_one_of_lemmas(splitted, now_time_keyword):
                answer += 'O'
            elif has_one_of_lemmas(splitted, number_keyword):
                answer += '#'
            elif splitted == 'и':
                answer += 'N'
            else:
                answer += '_'
            cur_index += 1
        return answer