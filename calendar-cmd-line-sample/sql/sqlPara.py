# -*- coding: utf-8 -*-
from sql import Para, AbstractPara, Session
import datetime
import xlrd
from excel_parser import dayparser, excel
from mptparser.time_parser import timeparse

session = Session()

sqlabspara = session.query(AbstractPara).all()

now = datetime.date.today()
if (int(datetime.datetime.strftime(now, '%W')) % 2) == 0:  # числитель
    print 'Числитель'
else:
    print 'Знаменатель'

for abspara in sqlabspara:

    paradate = now
    start, end = timeparse(abspara.numberpara)
    sqlpara = Para(abspara, paradate, start, end)
    session.add(sqlpara)


#session.commit()