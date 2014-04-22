# -*- coding: utf-8 -*-
from sql import AbstractPara, Para, Teacher, Discipline, Gruppa, Session
import datetime

abspara = AbstractPara(1, 1, 1)
teach = Teacher(u'Караваев', u'Сергей', u'Владимирович')
disc = Discipline(u'ТРПО')
grupp = Gruppa(u'П-329')
para = Para(datetime.date(2014, 04, 22), datetime.time(8, 30), datetime.time(10, 00))

session = Session()

session.add(abspara)
session.add(teach)
session.add(disc)
session.add(grupp)
session.add(para)

session.commit()

