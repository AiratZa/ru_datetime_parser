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
    'сей': ('сей', ),
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

# replaces = (
#     ('полчаса', '30 минут'),
#     ('полтора часа', '1 час 30 минут'),
#     ('с половиной часа', 'часа 30 минут'),
# )

# numbers = {
#     'один': 1,
#     'одна': 1,
#     'одну': 1,
#     'две': 2,
#     'два': 2,
#     'двое': 2,
#     'три': 3,
#     'трое': 3,
#     'четыре': 4,
#     'четверо': 4,
#     'пять': 5,
#     'пятеро': 5,
#     'шесть': 6,
#     'шестеро': 6,
#     'семь': 7,
#     'семеро': 7,
#     'восемь': 8,
#     'девять': 9,
#     'десять': 10,
#     'одиннадцать': 11,
#     'двенадцать': 12,
#     'тринадцать': 13,
#     'четырнадцать': 14,
#     'пятнадцать': 15,
#     'шестнадцать': 16,
#     'семнадцать': 17,
#     'восемнадцать': 18,
#     'девятнадцать': 19,
#     'двадцать': 20,
#     'тридцать': 30,
#     'сорок': 40,
#     'пятьдесят': 50,
#     'шестьдесят': 60,
#     'семьдесят': 70,
#     'восемьдесят': 80,
#     'девяносто': 90,
#     'сто': 100,
#     'двести': 200,
#     'триста': 300,
#     'четыреста': 400,
#     'пятьсот': 500,
# }

# dates = (
#     '%Y-%m-%d',
#     '%d.%m.%Y',
#     '%m/%d/%Y',
# )
# times = ('%H:%M', )



# from_now = {
#     'позавчера': -2,
#     'вчера': -1,
#     'сегодня': 0,
#     'завтра': 1,
#     'послезавтра': 2,
# }

# times_of_day = {
#     'утром': 9,
#     'днем': 15,
#     'вечером': 21,
#     'ночью': 3,
# }

# months = (
#     ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
#      'декабря'),
#     ('январе', 'феврале', 'марте', 'апреле', 'мае', 'июне', 'июле', 'августе', 'сентябре', 'октябре', 'ноябре',
#      'декабре'),
#     ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
#      'декабрь'),
# )

# weekdays = (
#     ('понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье'),
#     ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'),
#     ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'),
# )

# offset = (
#     (2, 'через'),
#     (1, 'следующей', 'следующий', 'следующую', 'следующее', 'следующем'),
#     (-1, 'перед', 'предыдущей', 'предыдущий', 'предыдущую', 'предыдущее', 'предыдущем'),
#     (-2, 'назад', 'за'),
# )

