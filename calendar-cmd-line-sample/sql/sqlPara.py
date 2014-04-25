# -*- coding: utf-8 -*-
from sql import Para, AbstractPara, Session
import datetime
from excel_parser.dayparser import dayofweek
from mptparser.time_parser import timeparse

session = Session()

sqlabspara = session.query(AbstractPara).all()

for abspara in sqlabspara:
    #print timeparse(abspara.numberpara), abspara.numberpara, abspara.teacher.lastname, abspara.discipline.name
    b = dayofweek(abspara.dayofweek)
    now = datetime.date.today()

    a = datetime.date.weekday(now)
    if a == b and abspara.gruppa.name == u'П-329':
        paradate = datetime.date(2014, 04, 25)
        start, end = timeparse(abspara.numberpara)
        sqlpara = Para(abspara, paradate, start, end)
        session.add(sqlpara)

session.commit()