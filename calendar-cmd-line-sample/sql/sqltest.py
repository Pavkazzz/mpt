# -*- coding: utf-8 -*-

from sql import AbstractPara, Para, Teacher, Discipline, Gruppa, Session
import datetime
session = Session()

teach = Teacher(u'Караваев', u'Сергей', u'Владимирович')
session.add(teach)

gruppa = Gruppa(u'П-329')
session.add(gruppa)

disc = Discipline(u'ТРПО')
session.add(teach)

session.commit()

abspara = AbstractPara(teach, disc, gruppa)
session.add(abspara)
session.commit()

para = Para(abspara, datetime.date(2014, 04, 22), datetime.time(8, 30), datetime.time(10, 00))
session.add(para)
session.commit()
