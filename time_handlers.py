from __future__ import annotations
from typing import Any

from abstract_handler import AbstractHandler

from dateutil.relativedelta import relativedelta, MO, TU, WE, TH, FR, SA, SU

import re
import datetime
from sets import *

"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""


class WeekendHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = 'W'
        if result := re.match(pattern, tokenized):
            # parser_instance.push_back_date_and_set_index_in_text(result)
            return 'weekend', 1, is_period
        else:
            return super().handle(tokenized, splitted_text)


class DatesPeriodHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        # print('hey', is_period)
        is_period = False
        pattern = 'f?(1)[ot]1(M|#)'
        if result := re.match(pattern, tokenized):
            return 'с 26 до 27 января/числа', 5, is_period
        return super().handle(tokenized, splitted_text)


class DaysMonthHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = '(([1, (1_)]?)+)(M|#)'
        i: int = 0
        if result := re.match(pattern, tokenized):
            day_nbr = 0
            month_id = 1
            result = result.group(0)
            print(f'{result=} {splitted_text=}')
            if result[i:].startswith('1_'):
                day_nbr = int(re.match(r'^\d+', splitted_text[0]).group(0))
                i += 2
            elif result[i] == '1':
                day_nbr = int(re.match(r'^\d+', splitted_text[0]).group(0))
                i += 1
            if splitted_text[i] in (*months['янв'], 'янв'):
                month_id = 1
            elif splitted_text[i] in (*months['фев'], 'фев'):
                month_id = 2
            elif splitted_text[i] in (*months['мар'], 'мар'):
                month_id = 3
            elif splitted_text[i] in (*months['апр'], 'апр'):
                month_id = 4
            elif splitted_text[i] in (*months['май'], 'май'):
                month_id = 5
            elif splitted_text[i] in (*months['июн'], 'июн'):
                month_id = 6
            elif splitted_text[i] in (*months['июл'], 'июл'):
                month_id = 7
            elif splitted_text[i] in (*months['авг'], 'авг'):
                month_id = 8
            elif splitted_text[i] in (*months['сен'], 'сен'):
                month_id = 9
            elif splitted_text[i] in (*months['окт'], 'окт'):
                month_id = 10
            elif splitted_text[i] in (*months['ноя'], 'ноя'):
                month_id = 11
            elif splitted_text[i] in (*months['дек'], 'дек'):
                month_id = 12
            return datetime.datetime(year=self._intial_time.year,
                                     month=month_id,
                                     day=day_nbr), len(result), False, is_period
        return super().handle(tokenized, splitted_text)


class RelativeDayHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        patterns = ['[2-7]', '1d']
        not_patterns = ['', '(i)?((0?[Ymwdhe]N?)+)([bl])?']
        for pattern, not_pattern in zip(patterns, not_patterns):
            if (result := re.match(pattern, tokenized)) and (not bool(re.match(not_pattern, tokenized)) if len(not_pattern) else True):
                if pattern == '1d' and (splitted_text[0] != '3'):
                    continue
                if result.group(0) == '3':
                    return datetime.timedelta(days=-1), len(result.group(0)), 0, is_period
                elif result.group(0) == '5':
                    return datetime.timedelta(days=1), len(result.group(0)), 0, is_period
                elif result.group(0) == '6':
                    return datetime.timedelta(days=2), len(result.group(0)), 0, is_period
                elif result.group(0) == '7':
                    return datetime.timedelta(days=3), len(result.group(0)), 0, is_period
                elif result.group(0) in ('2', '1d'):
                    return datetime.timedelta(days=-2), len(result.group(0)), 0, is_period
                else:
                    return datetime.timedelta(), len(result.group(0)), 0, is_period

        return super().handle(tokenized, splitted_text)


class TimeHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        # print(f'{is_period=}')
        is_period = False
        pattern = '([rvgd])?([fot])?(Q|H)?(h|(0)(h)?)((0)e?)?([rvgd])?'
        if result := re.match(pattern, tokenized):
            return '(в/с/до) (половину/четверть) час/9 (часов) (30 (минут)) (утра/дня/вечера/ночи)', 8, is_period
        return super().handle(tokenized, splitted_text)


def get_through_skipped_time(through, parse_pattern) -> relativedelta:
    if not through:
        return relativedelta()
    if 'Y' in parse_pattern:
        return relativedelta(years=1)
    elif 'm' in parse_pattern:
        return relativedelta(months=1)
    elif 'd' in parse_pattern:
        return relativedelta(days=1)
    elif 'w' in parse_pattern:
        return relativedelta(weeks=1)
    elif 'h' in parse_pattern:
        return relativedelta(hours=1)
    elif 'e' in parse_pattern:
        return relativedelta(minutes=1)
    else:
        return relativedelta()


class TimeSpanSkipHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        # print(f'{tokenized=}')
        is_period = False
        with_hm = False
        pattern = '^((l)?(((1)?[Ymwdhe]N?)+)(_)?([bl])?)'
        # print(f'\n\n{tokenized=}   |||   {splitted_text=}')
        if result := re.match(pattern, tokenized):
            result = result.groups()
            sign = 1
            if result[1] is None and result[-1] == 'b':
                sign = -1
            # print(result, f'{sign=}')
            parse_pattern = result[0]
            i = 0
            through = True if 'l' in parse_pattern else False
            start_delta = relativedelta() + get_through_skipped_time(through, parse_pattern)
            if parse_pattern[i] == 'l':
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
                        # print(f'{with_prefix_nbr=}')
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
                        # print(f'DAYS {days}')
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
                                 minutes=minutes * sign) + start_delta, len(parse_pattern), with_hm, is_period
        return super().handle(tokenized, splitted_text)


class NowHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = 'O'
        if result := re.match(pattern, tokenized):
            return datetime.timedelta(), len(result.group(0)), 1, is_period
        return super().handle(tokenized, splitted_text)


class DayOfWeekHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = 'f?([usxy])?(D)'
        day_of_week = None
        # print(day_of_week)
        if result := re.match(pattern, tokenized):
            result = result.group(0)
            if splitted_text[len(result) - 1] in week_days['пн']:
                day_of_week = MO
            elif splitted_text[len(result) - 1] in week_days['вт']:
                day_of_week = TU
            elif splitted_text[len(result) - 1] in week_days['ср']:
                day_of_week = WE
            elif splitted_text[len(result) - 1] in week_days['чт']:
                day_of_week = TH
            elif splitted_text[len(result) - 1] in week_days['пт']:
                day_of_week = FR
            elif splitted_text[len(result) - 1] in week_days['сб']:
                day_of_week = SA
            elif splitted_text[len(result) - 1] in week_days['вс']:
                day_of_week = SU
            if 'x' in result:
                return relativedelta(weekday=day_of_week), len(result), False, is_period

            return relativedelta(weekday=day_of_week), len(result), False, is_period
        return super().handle(tokenized, splitted_text)


class RelativeDateTimeHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        is_period = False
        pattern = 'f?([usxy])([Ymwdhe#])'
        if result := re.match(pattern, tokenized):
            relative: str = ''
            datetime_key: str = ''
            if 'u' in result.group(0):
                relative = 'current'
            elif 'x' in result.group(0):
                relative = 'tomorrow'
            if 'e' in result.group(0):
                datetime_key = 'minute'
            elif 'd' in result.group(0) or '#' in result.group(0):
                datetime_key = 'day'
            if relative == 'current' and datetime_key == 'minute':
                return datetime.timedelta(), len(result.group(0)), 1, is_period
            elif relative == 'current' and datetime_key == 'day':
                return datetime.timedelta(), len(result.group(0)), 0, is_period
            elif relative == 'tomorrow' and datetime_key == 'day':
                return datetime.timedelta(days=1), len(result.group(0)), 0, is_period
            return 'в/на] следующей/этой/предыдущей год/месяц/неделе/день', 7
        return super().handle(tokenized, splitted_text)


class PeriodKeywordsHandler(AbstractHandler):

    def __init__(self, initial_time):
        self._intial_time = initial_time

    def handle(self, tokenized: Any, splitted_text) -> tuple:
        pattern = 'op'
        if result := re.match(pattern, tokenized):
            is_period = True
            return datetime.timedelta(), 2, False, True
        return super().handle(tokenized, splitted_text)


def handle_time_patterns(splitted_text, tokenized, initial_time) -> list:
    weekend_handler = WeekendHandler(initial_time)
    dates_period = DatesPeriodHandler(initial_time)
    day_month = DaysMonthHandler(initial_time)
    time_recognizer = TimeHandler(initial_time)
    relative_day = RelativeDayHandler(initial_time)
    relative_datetime = RelativeDateTimeHandler(initial_time)
    now_handler = NowHandler(initial_time)
    period_keywords_handler = PeriodKeywordsHandler(initial_time)
    time_span_skip_handler = TimeSpanSkipHandler(initial_time)
    day_of_week_handler = DayOfWeekHandler(initial_time)

    start = now_handler
    start.set_next(period_keywords_handler) \
        .set_next(weekend_handler) \
        .set_next(dates_period) \
        .set_next(day_month) \
        .set_next(relative_day) \
        .set_next(time_span_skip_handler) \
        .set_next(relative_datetime) \
        .set_next(day_of_week_handler) \
        .set_next(time_recognizer)

    answer = []
    i: int = 0
    len_tokenized = len(tokenized)
    while i < len_tokenized:
        params = start.handle(tokenized[i:], splitted_text[i:])
        answer.append(params)
        i += params[1]
    return answer
