# -*- coding: utf-8 -*-

from sql import AbstractPara, Teacher, Discipline, Gruppa, Session


abspara = AbstractPara(1, 1, 1)
teach = Teacher(u'Караваев', u'Сергей', u'Владимирович')
disc = Discipline(u'ТРПО')
grupp = Gruppa(u'П-329')

session = Session()

session.add(abspara)
session.add(teach)
session.add(disc)
session.add(grupp)

print abspara in session

session.commit()