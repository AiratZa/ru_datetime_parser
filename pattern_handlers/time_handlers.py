from __future__ import annotations
from typing import Any
import re

import datetime

from .abstract_handler import AbstractHandler

from dateutil.relativedelta import relativedelta

# self.delta = {'days': 0, 'weeks': 0, 'hours': 0, 'minutes': 0}

"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""


class WeekendHandler(AbstractHandler):
    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = 'W'
        if result := re.match(pattern, tokenized):
            # parser_instance.push_back_date_and_set_index_in_text(result)
            return 'weekend', 1, is_period
        else:
            return super().handle(tokenized, splitted_text)


class DatesPeriodHandler(AbstractHandler):
    def handle(self, tokenized: Any, splitted_text) -> tuple:
        # print('hey', is_period)
        is_period = False
        pattern = 'f?(1)[ot]1(M|#)'
        if result := re.match(pattern, tokenized):
            return 'с 26 до 27 января/числа', 5, is_period
        return super().handle(tokenized, splitted_text)


class DaysMonthHandler(AbstractHandler):
    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = '((1?)+)(M|#)'
        if result := re.match(pattern, tokenized):
            return '24, 25, 26… и 27 января/числа', 4, is_period
        return super().handle(tokenized, splitted_text)


class RelativeDayHandler(AbstractHandler):
    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = '[2-6]'
        if result := re.match(pattern, tokenized):
            if result.group(0) == '3':
                return datetime.timedelta(days=-1), len(result.group(0)), 0, is_period
            return datetime.timedelta(), len(result.group(0)), 0, is_period
        return super().handle(tokenized, splitted_text)


class TimeHandler(AbstractHandler):
    def handle(self, tokenized: Any, splitted_text) -> tuple:
        # print(f'{is_period=}')
        is_period = False
        pattern = '([rvgd])?([fot])?(Q|H)?(h|(0)(h)?)((0)e?)?([rvgd])?'
        if result := re.match(pattern, tokenized):
            return '(в/с/до) (половину/четверть) час/9 (часов) (30 (минут)) (утра/дня/вечера/ночи)', 8, is_period
        return super().handle(tokenized, splitted_text)


class TimeSpanSkipHandler(AbstractHandler):
    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        with_hm = False
        pattern = '^((i)?(((1)?[Ymwdhe]N?)+)(_)?([bl])?)'
        # print(f'\n\n{tokenized=}   |||   {splitted_text=}')
        if result := re.match(pattern, tokenized):
            result = result.groups()
            sign = 1
            if result[1] is None and result[-1] == 'b':
                sign = -1
            # print(result, f'{sign=}')
            parse_pattern = result[0]
            i = 0
            if parse_pattern[i] == 'i':
                i += 1
            years: int = 0
            months: int = 0
            weeks: int = 0
            days: int = 0
            hours: int = 0
            minutes: int = 0

            while (i < len(parse_pattern)):
                # print(f'{days=} {hours=} {minutes=}')
                with_prefix_nbr = False
                if parse_pattern[i] == 'N':
                    i += 1
                elif parse_pattern[i] in '1Ymwdhe':
                    if parse_pattern[i] == '1':
                        with_prefix_nbr = True
                        i += 1
                    if not (i < len(parse_pattern)):
                        break
                    if parse_pattern[i] == 'Y':
                        years = int(splitted_text[i-1]) if with_prefix_nbr else 1
                    elif parse_pattern[i] == 'm':
                        months = int(splitted_text[i-1]) if with_prefix_nbr else 1
                    elif parse_pattern[i] == 'w':
                        weeks = int(splitted_text[i-1]) if with_prefix_nbr else 1
                    elif parse_pattern[i] == 'd':
                        days = int(splitted_text[i-1]) if with_prefix_nbr else 1
                    elif parse_pattern[i] == 'h':
                        hours = int(splitted_text[i-1]) if with_prefix_nbr else 1
                        with_hm = True
                    elif parse_pattern[i] == 'e':
                        minutes = int(splitted_text[i-1]) if with_prefix_nbr else 1
                        with_hm = True
                    i += 1
                else:
                    break
            return relativedelta(years=years * sign,
                                 months=months * sign,
                                 weeks=weeks * sign,
                                 days=days * sign,
                                 hours=hours * sign,
                                 minutes=minutes * sign), len(parse_pattern), with_hm, is_period

            # datetime.timedelta(years=years * sign, \
            #                    months=months * sign, \
            #                    weeks=weeks * sign, \
            #                    days=days * sign, \
            #                    hours=hours * sign, \
            #                    minutes=minutes * sign)
        return super().handle(tokenized, splitted_text)


class NowHandler(AbstractHandler):
    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = 'O'
        if result := re.match(pattern, tokenized):
            return datetime.timedelta(), len(result.group(0)), 1, is_period
        return super().handle(tokenized, splitted_text)


class RelativeDateTimeHandler(AbstractHandler):
    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = 'f?([usxy])([Ymwdhe#])'
        if result := re.match(pattern, tokenized):
            relative: str = ''
            datetime_key: str = ''
            if 'u' in result.group(0):
                relative = 'current'
            if 'e' in result.group(0):
                datetime_key = 'minute'
            elif 'd' in result.group(0) or '#' in result.group(0):
                datetime_key = 'day'
            if relative == 'current' and datetime_key == 'minute':
                return datetime.timedelta(), len(result.group(0)), 1, is_period
            elif relative == 'current' and datetime_key == 'day':
                return datetime.timedelta(), len(result.group(0)), 0, is_period
            return 'в/на] следующей/этой/предыдущей год/месяц/неделе/день', 7
        return super().handle(tokenized, splitted_text)


class PeriodKeywordsHandler(AbstractHandler):
    def handle(self, tokenized: Any, splitted_text) -> tuple:
        pattern = 'op'
        if result := re.match(pattern, tokenized):
            is_period = True
            return datetime.timedelta(), 2, False, True
        return super().handle(tokenized, splitted_text)


def handle_time_patterns(splitted_text, tokenized) -> list:
    weekend_handler = WeekendHandler()
    dates_period = DatesPeriodHandler()
    day_month = DaysMonthHandler()
    time_recognizer = TimeHandler()
    relative_day = RelativeDayHandler()
    relative_datetime = RelativeDateTimeHandler()
    now_handler = NowHandler()
    period_keywords_handler = PeriodKeywordsHandler()
    time_span_skip_handler = TimeSpanSkipHandler()

    start = now_handler
    start.set_next(period_keywords_handler) \
        .set_next(weekend_handler) \
        .set_next(dates_period) \
        .set_next(day_month) \
        .set_next(relative_day) \
        .set_next(time_span_skip_handler) \
        .set_next(relative_datetime) \
        .set_next(time_recognizer)

    answer = []
    i: int = 0
    len_tokenized = len(tokenized)
    while i < len_tokenized:
        params = start.handle(tokenized[i:], splitted_text[i:])
        answer.append(params)
        i += params[1]
    return answer
