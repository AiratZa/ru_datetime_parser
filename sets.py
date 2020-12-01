import pymorphy2


morph = pymorphy2.MorphAnalyzer()

months = {
    'янв': tuple(i.word for i in morph.parse('январь')[0].lexeme),
    'фев': tuple(i.word for i in morph.parse('февраль')[0].lexeme),
    'мар': tuple(i.word for i in morph.parse('март')[0].lexeme),
    'апр': tuple(i.word for i in morph.parse('апрель')[0].lexeme),
    'июн': tuple(i.word for i in morph.parse('июнь')[0].lexeme),
    'июл': tuple(i.word for i in morph.parse('июль')[0].lexeme),
    'авг': tuple(i.word for i in morph.parse('август')[0].lexeme),
    'сен': tuple(i.word for i in morph.parse('сентябрь')[0].lexeme),
    'окт': tuple(i.word for i in morph.parse('октябрь')[0].lexeme),
    'ноя': tuple(i.word for i in morph.parse('ноябрь')[0].lexeme),
    'дек': tuple(i.word for i in morph.parse('декабрь')[0].lexeme),
}

weeks = {
    'пн': tuple(i.word for i in morph.parse('понедельник')[0].lexeme),
    'вт': tuple(i.word for i in morph.parse('вторник')[0].lexeme),
    'ср': tuple(i.word for i in morph.parse('среда')[0].lexeme),
    'чт': tuple(i.word for i in morph.parse('четверг')[0].lexeme),
    'пт': tuple(i.word for i in morph.parse('пятница')[0].lexeme),
    'сб': tuple(i.word for i in morph.parse('суббота')[0].lexeme),
    'вс': tuple(i.word for i in morph.parse('воскресенье')[0].lexeme),
}

back_time_keyword = {
    'назад': tuple(i.word for i in morph.parse('назад')[0].lexeme),
}

adj_back_time_keyword = {
    'прошлый': tuple(i.word for i in morph.parse('прошлый')[0].lexeme),
    'прошедший': tuple(i.word for i in morph.parse('прошедший')[0].lexeme),
    'предыдущий': tuple(i.word for i in morph.parse('предыдущий')[0].lexeme),
}

adj_current_time_keyword = {
    'этот': tuple(i.word for i in morph.parse('этот')[0].lexeme),
    'текущий': tuple(i.word for i in morph.parse('текущий')[0].lexeme),
    'нынешний': tuple(i.word for i in morph.parse('нынешний')[0].lexeme),
    'сего': tuple(i.word for i in morph.parse('сего')[0].lexeme),
    'настоящий': tuple(i.word for i in morph.parse('настоящий')[0].lexeme),
    'сегодняшний': tuple(i.word for i in morph.parse('сегодняшний')[0].lexeme),
    'сей': ('сей', ),
}

now_time_keyword = {
    'сейчас': ('сейчас', ),
}

adj_future_time_keyword = {
    'ближайший': tuple(i.word for i in morph.parse('ближайший')[0].lexeme),
    'грядущий': tuple(i.word for i in morph.parse('грядущий')[0].lexeme),
    'следующий': tuple(i.word for i in morph.parse('следующий')[0].lexeme),
    'будущий': tuple(i.word for i in morph.parse('будущий')[0].lexeme),
}

bb_day_keyword = {
    'позавчера': tuple(i.word for i in morph.parse('позавчера')[0].lexeme),
}

b_day_keyword = {
    'вчера': tuple(i.word for i in morph.parse('вчера')[0].lexeme),
    'накануне': tuple(i.word for i in morph.parse('накануне')[0].lexeme),
}

morning_keyword = {
    'утро': tuple(i.word for i in morph.parse('утро')[0].lexeme),
}

noon_keyword = {
    'полдень': tuple(i.word for i in morph.parse('полдень')[0].lexeme),
}

evening_keyword = {
    'вечер': tuple(i.word for i in morph.parse('вечер')[0].lexeme),
}

night_keyword = {
    'ночь': tuple(i.word for i in morph.parse('ночь')[0].lexeme),
}

half_keyword = {
    'половина': tuple(i.word for i in morph.parse('половина')[0].lexeme),
}

quater_keyword = {
    'четверть': tuple(i.word for i in morph.parse('четверть')[0].lexeme),
}

from_keyword = {
    'в': ('в', ),
    'с': ('с', ),
}

to_keyword = {
    'до': ('до', ),
    'по': ('по', ),
}

to_what_keyword = {
    'на': ('на', ),
}

number_keyword = {
    'число': tuple(i.word for i in morph.parse('число')[0].lexeme),
}

and_keyword = {
    'и': ('и', ),
}

number_tuple = tuple(str(i) for i in range(0, 10000))

today_day_keyword = {
    'сегодня': tuple(i.word for i in morph.parse('сегодня')[0].lexeme),
}

f_day_keyword = {
    'завтра': tuple(i.word for i in morph.parse('завтра')[0].lexeme),
}

ff_day_keyword = {
    'послезавтра': tuple(i.word for i in morph.parse('послезавтра')[0].lexeme),
}

weekend = {
    'выходной': tuple(i.word for i in morph.parse('выходной')[0].lexeme),
}

minute_keyword = {
    'мин': tuple(i.word for i in morph.parse('минута')[0].lexeme),
    'момент': tuple(i.word for i in morph.parse('момент')[0].lexeme),
}


second_keyword = {
    'сек': tuple(i.word for i in morph.parse('секунда')[0].lexeme),
}

hour_keyword = {
    'ч': tuple(i.word for i in morph.parse('час')[0].lexeme),
}

day_keyword = {
    'дн': tuple(i.word for i in morph.parse('день')[0].lexeme),
}

week_keyword = {
    'нд': tuple(i.word for i in morph.parse('неделя')[0].lexeme),
}

months_keyword = {
    'мес': tuple(i.word for i in morph.parse('месяц')[0].lexeme),
}

forward_time_keyword = {
    'спустя': tuple(i.word for i in morph.parse('спустя')[0].lexeme),
    'через': tuple(i.word for i in morph.parse('через')[0].lexeme),
}

year_key = {
    'год': tuple(i.word for i in morph.parse('год')[0].lexeme)
}

period_keyword = {
    'течение': ('течение', 'течении'),
    'протяжение': tuple(i.word for i in morph.parse('протяжение')[0].lexeme),
}










