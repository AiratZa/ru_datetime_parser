from __future__ import annotations
from typing import Any
import re

from .abstract_handler import AbstractHandler


"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""

class WeekendHandler(AbstractHandler):
    def handle(self, parser_instance: Any) -> str:
        parser_instance.skip_other_words()
        pattern = 'W'
        if (result := re.match(pattern, parser_instance.get_current_tokens())):
            parser_instance.push_back_date_and_set_index_in_text(result)
            return
        else:
            return super().handle(parser_instance)

class DatesPeriodHandler(AbstractHandler):
    def handle(self, parser_instance: Any) -> str:
        parser_instance.skip_other_words()
        pattern = 'f?(1)[ot]1(M|#)'
        if (result := re.match(pattern, parser_instance.get_current_tokens())):
            parser_instance.push_back_date_and_set_index_in_text(result)
            return
        return super().handle(parser_instance)


class DaysMonthHandler(AbstractHandler):
    def handle(self, parser_instance: Any) -> str:
        parser_instance.skip_other_words()
        pattern = '((1?)+)(M|#)'
        if (result := re.match(pattern, parser_instance.get_current_tokens())):
            parser_instance.push_back_date_and_set_index_in_text(result)
            return
        return super().handle(parser_instance)

class PassHandler(AbstractHandler):
    def handle(self, parser_instance: Any) -> str:
        raise Exception
        # while(parser_instance.get_current_tokens()):
        #     parser_instance.incr_current_token_index()


class RelativeDayHandler(AbstractHandler):
    def handle(self, parser_instance: Any) -> str:
        parser_instance.skip_other_words()
        pattern = '[2-6]'
        if (result := re.match(pattern, parser_instance.get_current_tokens())):
            parser_instance.push_back_date_and_set_index_in_text(result)
            return
        return super().handle(parser_instance)

class TimeRecognizerHandler(AbstractHandler):
    def handle(self, parser_instance: Any) -> str:
        parser_instance.skip_other_words()
        pattern = '([rvgd])?([fot])?(Q|H)?(h|(0)(h)?)((0)e?)?([rvgd])?'
        if (result := re.match(pattern, parser_instance.get_current_tokens())):
            parser_instance.push_back_date_and_set_index_in_text(result)
            return
        return super().handle(parser_instance)

class RelativeDateTimeHandler(AbstractHandler):
    def handle(self, parser_instance: Any) -> str:
        parser_instance.skip_other_words()
        pattern = 'f?([usxy])([Ymwdhe#])'
        if (result := re.match(pattern, parser_instance.get_current_tokens())):
            parser_instance.push_back_date_and_set_index_in_text(result)
            return
        return super().handle(parser_instance)


