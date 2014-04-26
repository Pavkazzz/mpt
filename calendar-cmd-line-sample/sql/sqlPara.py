# -*- coding: utf-8 -*-
from sql import Para, AbstractPara, Session
import datetime

import xlrd
from excel_parser import dayparser, excel
from mptparser.time_parser import timeparse

session = Session()

sqlabspara = session.query(AbstractPara).all()

week = [u'понедельник', u'вторник', u'среда', u'четверг', u'пятница', u'суббота']

now = datetime.date.today()
if (int(datetime.datetime.strftime(now, '%W')) % 2) == 0:  # числитель
    print 'Числитель'
else:
    print 'Знаменатель'

print now.weekday()
for abspara in sqlabspara:
    for xday in xrange(0, 7):
        dateoffset = now + datetime.timedelta(days=xday)
        if dateoffset.weekday() == week.index(abspara.dayofweek):
            paradate = dateoffset
            start, end = timeparse(abspara.numberpara)
            sqlpara = Para(abspara, paradate, start, end)
            print sqlpara.abstractpara.dayofweek
            session.add(sqlpara)

#session.commit()