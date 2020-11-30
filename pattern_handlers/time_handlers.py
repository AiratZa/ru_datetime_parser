from __future__ import annotations
from typing import Any
import re

import datetime

from .abstract_handler import AbstractHandler

# self.delta = {'days': 0, 'weeks': 0, 'hours': 0, 'minutes': 0}

"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""


class WeekendHandler(AbstractHandler):
    def handle(self, tokenized: Any) -> tuple:
        pattern = 'W'
        if result := re.match(pattern, tokenized):
            # parser_instance.push_back_date_and_set_index_in_text(result)
            return 'weekend', 1
        else:
            return super().handle(tokenized)


class DatesPeriodHandler(AbstractHandler):
    def handle(self, tokenized: Any) -> tuple:
        pattern = 'f?(1)[ot]1(M|#)'
        if result := re.match(pattern, tokenized):
            return 'с 26 до 27 января/числа', 5
        return super().handle(tokenized)


class DaysMonthHandler(AbstractHandler):
    def handle(self, tokenized: Any) -> tuple:
        pattern = '((1?)+)(M|#)'
        if result := re.match(pattern, tokenized):
            return '24, 25, 26… и 27 января/числа', 4
        return super().handle(tokenized)


class RelativeDayHandler(AbstractHandler):
    def handle(self, tokenized: Any) -> tuple:
        pattern = '[2-6]'
        if result := re.match(pattern, tokenized):
            return datetime.timedelta(), len(result.group(0)), 0

            # return 'позавчера', 1
        return super().handle(tokenized)


class TimeHandler(AbstractHandler):
    def handle(self, tokenized: Any) -> tuple:
        pattern = '([rvgd])?([fot])?(Q|H)?(h|(0)(h)?)((0)e?)?([rvgd])?'
        if result := re.match(pattern, tokenized):
            return '(в/с/до) (половину/четверть) час/9 (часов) (30 (минут)) (утра/дня/вечера/ночи)', 8
        return super().handle(tokenized)


class NowHandler(AbstractHandler):
    def handle(self, tokenized: Any) -> tuple:
        pattern = 'O'
        if result := re.match(pattern, tokenized):
            return datetime.timedelta(), len(result.group(0)), 1
        return super().handle(tokenized)

class RelativeDateTimeHandler(AbstractHandler):
    def handle(self, tokenized: Any) -> tuple:
        pattern = 'f?([usxy])([Ymwdhe#])'
        if result := re.match(pattern, tokenized):
            relative: str = ''
            datetime_key: str = ''
            if 'u' in result.group(0):
                relative = 'current'
            if 'e' in result.group(0):
                datetime_key = 'minute'
            if relative == 'current' and datetime_key == 'minute':
                return datetime.timedelta(), len(result.group(0)), 1
            return 'в/на] следующей/этой/предыдущей год/месяц/неделе/день', 7
        return super().handle(tokenized)

def handle_time_patterns(splitted_text, tokenized) -> list:
    weekend_handler = WeekendHandler()
    dates_period = DatesPeriodHandler()
    day_month = DaysMonthHandler()
    time_recognizer = TimeHandler()
    relative_day = RelativeDayHandler()
    relative_datetime = RelativeDateTimeHandler()
    now_handler = NowHandler()

    start = now_handler
    start.set_next(weekend_handler).set_next(dates_period).set_next(day_month) \
        .set_next(relative_day) \
        .set_next(relative_datetime) \
        .set_next(time_recognizer)


    answer = []
    i: int = 0
    len_tokenized = len(tokenized)
    while i < len_tokenized:
        params = start.handle(tokenized[i:])
        answer.append(params)
        i += params[1]
    return answer
