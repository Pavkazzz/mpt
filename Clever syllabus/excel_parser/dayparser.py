# -*- coding: utf-8 -*-

week = [u'понедельник', u'вторник', u'среда', u'четверг', u'пятница', u'суббота']


def dayofweek(day):
    return week.index(day.lower())
