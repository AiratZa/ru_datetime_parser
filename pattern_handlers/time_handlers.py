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
        pattern = 'W'
        if (result := re.match(pattern, parser_instance.get_current_tokens())):
            parser_instance.push_back_date_and_set_index_in_text(result)
            return True
        else:
            return super().handle(parser_instance)

# class SkipWordsHandler(AbstractHandler):
#     def handle(self, parser_instance: Any) -> str:
#         pattern = '_'
#         while (result := re.match(pattern, parser_instance.get_current_tokens())):
#             parser_instance.incr_current_token_index()
#         return super().handle(parser_instance)

class DatesPeriodHandler(AbstractHandler):
    def handle(self, parser_instance: Any) -> str:
        pattern = 'f?(0)[ot]0(M|#)'
        if (result := re.match(pattern, parser_instance.get_current_tokens())):
            parser_instance.push_back_date_and_set_index_in_text(result)
            return True
        return super().handle(parser_instance)

# class DayMonthHandler(AbstractHandler):
#     def handle(self, tokens: Any) -> str:
#         if result = re.match('W', tokens):
#           return True
#         else:
#             return super().handle(request)

# class DatesPeriodHandler(AbstractHandler):
#     def handle(self, tokens: Any) -> str:
#         if result = re.match('W', tokens):
#           return True
#         else:
#             return super().handle(request)
